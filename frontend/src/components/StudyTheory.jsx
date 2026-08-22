import { useEffect, useState } from "react";
import { api } from "../api/client";
import MathText from "./MathText";

const TYPE_OPTIONS = [
  { key: "flashcard", label: "Flash kartice" },
  { key: "truefalse", label: "Točno / netočno" },
  { key: "mcq", label: "Višestruki izbor" },
  { key: "fillin", label: "Nadopuni rečenicu" },
];

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export default function StudyTheory({ courseId, moduleId }) {
  const [allItems, setAllItems] = useState([]);
  const [solvedIds, setSolvedIds] = useState(new Set()); // stvarni (trajni) napredak
  const [sessionSolvedIds, setSessionSolvedIds] = useState(new Set()); // brojac za "novi krug"
  const [loading, setLoading] = useState(true);

  const [phase, setPhase] = useState("select"); // "select" | "study"
  const [selectedType, setSelectedType] = useState(TYPE_OPTIONS[0].key);
  const [resetRound, setResetRound] = useState(false); // "Sakrij rijeseno" -> zapravo "novi krug"

  const [queue, setQueue] = useState([]);
  const [idx, setIdx] = useState(0);

  useEffect(() => {
    setLoading(true);
    setPhase("select");
    Promise.all([api.listTheory(courseId, moduleId), api.myProgress("theory")]).then(
      ([theoryItems, progress]) => {
        setAllItems(theoryItems);
        setSolvedIds(new Set(progress.filter((p) => p.status === "solved").map((p) => p.item_id)));
        setLoading(false);
      }
    );
  }, [courseId, moduleId]);

  function markSolved(itemId, tocno) {
    api.markTheorySeen(itemId, tocno).catch(() => {});
    if (tocno) {
      setSolvedIds((prev) => new Set(prev).add(itemId));
      if (resetRound) setSessionSolvedIds((prev) => new Set(prev).add(itemId));
    }
  }

  function itemsOfType(type) {
    return allItems.filter((it) => it.tip === type);
  }

  function toggleResetRound(checked) {
    setResetRound(checked);
    if (checked) setSessionSolvedIds(new Set());
  }

  function startStudy() {
    if (resetRound) setSessionSolvedIds(new Set());
    setQueue(shuffle(itemsOfType(selectedType)));
    setIdx(0);
    setPhase("study");
  }

  if (loading) return <p className="empty">Učitavanje…</p>;
  if (allItems.length === 0) return <p className="empty">Za ovo područje još nema teorije.</p>;

  const activeSolved = resetRound ? sessionSolvedIds : solvedIds;

  if (phase === "select") {
    return (
      <div className="type-select">
        <p className="type-select-label">Odaberi tip pitanja</p>
        <div className="type-grid">
          {TYPE_OPTIONS.map((opt) => {
            const items = itemsOfType(opt.key);
            const solvedCount = items.filter((it) => activeSolved.has(it.id)).length;
            if (items.length === 0) return null;
            return (
              <button
                key={opt.key}
                className={"type-opt" + (selectedType === opt.key ? " active" : "")}
                onClick={() => setSelectedType(opt.key)}
              >
                <span className="type-opt-label">{opt.label}</span>
                <span className="type-opt-count">
                  {solvedCount}/{items.length} riješeno
                </span>
              </button>
            );
          })}
        </div>

        <label className="hide-toggle hide-toggle-standalone">
          <input
            type="checkbox"
            checked={resetRound}
            onChange={(e) => toggleResetRound(e.target.checked)}
          />
          Sakrij riješeno
        </label>

        <button className="solid" onClick={startStudy}>
          Počni
        </button>
      </div>
    );
  }

  // phase === "study"
  if (queue.length === 0) {
    return (
      <div className="study">
        <p className="empty">Nema pitanja za odabrani tip.</p>
        <button className="ghost" onClick={() => setPhase("select")}>
          ← Promijeni postavke
        </button>
      </div>
    );
  }

  const safeIdx = idx % queue.length;
  const item = queue[safeIdx];
  const solvedInQueue = queue.filter((it) => activeSolved.has(it.id)).length;

  function next() {
    setIdx((i) => (i + 1) % queue.length);
  }
  function prev() {
    setIdx((i) => (i - 1 + queue.length) % queue.length);
  }

  return (
    <div className="study">
      <div className="study-progress">
        <span>
          Pitanje {safeIdx + 1}/{queue.length}
        </span>
        <span className="live-solved">Riješeno: {solvedInQueue}/{queue.length}</span>
      </div>
      <StudyItem key={item.id} item={item} solved={activeSolved.has(item.id)} onMark={markSolved} onDone={next} />
      <div className="study-nav">
        <button className="ghost" onClick={prev}>
          ← Prethodno
        </button>
        <button className="ghost" onClick={() => setPhase("select")}>
          Promijeni tip
        </button>
        <button className="ghost" onClick={next}>
          Sljedeće →
        </button>
      </div>
    </div>
  );
}

function SolvedBadge() {
  return <span className="solved-badge">✓ Riješeno</span>;
}

function StudyItem({ item, solved, onMark, onDone }) {
  if (item.tip === "flashcard") return <FlashcardItem item={item} solved={solved} onMark={onMark} onDone={onDone} />;
  if (item.tip === "truefalse") return <TrueFalseItem item={item} solved={solved} onMark={onMark} onDone={onDone} />;
  if (item.tip === "mcq") return <McqItem item={item} solved={solved} onMark={onMark} onDone={onDone} />;
  if (item.tip === "fillin") return <FillinItem item={item} solved={solved} onMark={onMark} onDone={onDone} />;
  return null;
}

function tintClass(result) {
  if (result === true) return " card-correct";
  if (result === false) return " card-wrong";
  return "";
}

function FlashcardItem({ item, solved, onMark, onDone }) {
  const [flipped, setFlipped] = useState(false);
  const [result, setResult] = useState(null); // null | true | false

  function assess(knowsIt) {
    setResult(knowsIt);
    onMark(item.id, knowsIt);
  }

  return (
    <div className={"study-card flashcard-wrap" + tintClass(result)}>
      {solved && <SolvedBadge />}
      <div className="flashcard-scene" onClick={() => !result && setFlipped((f) => !f)}>
        <div className={"flashcard-3d" + (flipped ? " is-flipped" : "")}>
          <div className="flashcard-face flashcard-front">
            <MathText text={item.sadrzaj.pitanje} />
            <span className="flashcard-hint">(klikni za odgovor)</span>
          </div>
          <div className="flashcard-face flashcard-back">
            <MathText text={item.sadrzaj.odgovor} />
          </div>
        </div>
      </div>
      {flipped && result === null && (
        <div className="self-assess">
          <button className="ghost" onClick={() => assess(false)}>
            Ne znam još
          </button>
          <button className="solid" onClick={() => assess(true)}>
            Znam
          </button>
        </div>
      )}
      {result !== null && (
        <button className="solid" onClick={onDone}>
          Dalje
        </button>
      )}
    </div>
  );
}

function TrueFalseItem({ item, solved, onMark, onDone }) {
  const [answered, setAnswered] = useState(null);
  const correct = item.sadrzaj.tocno;
  const preShow = solved && answered === null;

  function answer(val) {
    setAnswered(val);
    onMark(item.id, val === correct);
  }

  const result = answered === null ? null : answered === correct;

  function btnClass(val) {
    let cls = "tf-btn";
    if (answered === val) cls += val === correct ? " tf-correct" : " tf-wrong";
    else if (preShow && val === correct) cls += " tf-correct";
    return cls;
  }

  return (
    <div className={"study-card" + tintClass(result)}>
      {solved && <SolvedBadge />}
      <p className="study-prompt">
        <MathText text={item.sadrzaj.tvrdnja} />
      </p>
      <div className="tf-buttons">
        <button className={btnClass(true)} disabled={answered !== null} onClick={() => answer(true)}>
          Točno
        </button>
        <button className={btnClass(false)} disabled={answered !== null} onClick={() => answer(false)}>
          Netočno
        </button>
      </div>
      {answered !== null && (
        <>
          <p className={"feedback " + (result ? "feedback-ok" : "feedback-bad")}>
            {result ? "Točno!" : `Netočno — tvrdnja je ${correct ? "točna" : "netočna"}.`}
          </p>
          <button className="solid" onClick={onDone}>
            Dalje
          </button>
        </>
      )}
    </div>
  );
}

function McqItem({ item, solved, onMark, onDone }) {
  const [selected, setSelected] = useState(null);
  const correctIdx = item.sadrzaj.tocna;
  const preShow = solved && selected === null;

  function choose(i) {
    if (selected !== null) return;
    setSelected(i);
    onMark(item.id, i === correctIdx);
  }

  const result = selected === null ? null : selected === correctIdx;

  return (
    <div className={"study-card" + tintClass(result)}>
      {solved && <SolvedBadge />}
      <p className="study-prompt">
        <MathText text={item.sadrzaj.pitanje} />
      </p>
      <div className="mcq-options">
        {item.sadrzaj.opcije.map((op, i) => {
          let cls = "mcq-opt";
          if (selected !== null) {
            if (i === correctIdx) cls += " mcq-correct";
            else if (i === selected) cls += " mcq-wrong";
          } else if (preShow && i === correctIdx) {
            cls += " mcq-correct";
          }
          return (
            <button key={i} className={cls} disabled={selected !== null} onClick={() => choose(i)}>
              <MathText text={op} />
            </button>
          );
        })}
      </div>
      {selected !== null && (
        <button className="solid" onClick={onDone}>
          Dalje
        </button>
      )}
    </div>
  );
}

function FillinItem({ item, solved, onMark, onDone }) {
  const [value, setValue] = useState(() => (solved ? item.sadrzaj.odgovor : ""));
  const [checked, setChecked] = useState(false);

  function normalize(s) {
    return s.trim().toLowerCase().replace(/\s+/g, "");
  }

  const isCorrect = normalize(value) === normalize(item.sadrzaj.odgovor);
  const preShow = solved && !checked;

  function check() {
    setChecked(true);
    onMark(item.id, isCorrect);
  }

  const [before, after] = item.sadrzaj.tekst.split("___");
  const result = checked ? isCorrect : null;

  return (
    <div className={"study-card" + tintClass(result)}>
      {solved && <SolvedBadge />}
      <p className="study-prompt fillin-prompt">
        <MathText text={before} />
        <input
          className={"fillin-input" + (preShow ? " prefilled-correct" : "")}
          value={value}
          onChange={(e) => setValue(e.target.value)}
          disabled={checked}
          placeholder="?"
        />
        <MathText text={after} />
      </p>
      {!checked ? (
        <button className="solid" onClick={check} disabled={!value.trim()}>
          Provjeri
        </button>
      ) : (
        <>
          <p className={"feedback " + (isCorrect ? "feedback-ok" : "feedback-bad")}>
            {isCorrect ? "Točno!" : (
              <>
                Netočno — točan odgovor: <MathText text={item.sadrzaj.odgovor} />
              </>
            )}
          </p>
          <button className="solid" onClick={onDone}>
            Dalje
          </button>
        </>
      )}
    </div>
  );
}