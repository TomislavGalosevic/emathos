import { useEffect, useState } from "react";
import { api } from "../api/client";
import MathText from "./MathText";

export default function StudyTheory({ courseId, moduleId }) {
  const [items, setItems] = useState([]);
  const [solvedIds, setSolvedIds] = useState(new Set());
  const [loading, setLoading] = useState(true);
  const [idx, setIdx] = useState(0);
  const [hideSolved, setHideSolved] = useState(false);

  useEffect(() => {
    setLoading(true);
    setIdx(0);
    Promise.all([api.listTheory(courseId, moduleId), api.myProgress("theory")]).then(
      ([theoryItems, progress]) => {
        setItems(theoryItems);
        setSolvedIds(new Set(progress.filter((p) => p.status === "solved").map((p) => p.item_id)));
        setLoading(false);
      }
    );
  }, [courseId, moduleId]);

  function markSolved(itemId, tocno) {
    api.markTheorySeen(itemId, tocno).catch(() => {});
    if (tocno) {
      setSolvedIds((prev) => new Set(prev).add(itemId));
    }
  }

  if (loading) return <p className="empty">Učitavanje…</p>;
  if (items.length === 0) return <p className="empty">Za ovo područje još nema teorije.</p>;

  const visible = hideSolved ? items.filter((it) => !solvedIds.has(it.id)) : items;

  if (visible.length === 0) {
    return (
      <div className="study">
        <p className="empty">Sve stavke su svladane. 🎉</p>
        <label className="hide-toggle">
          <input type="checkbox" checked={hideSolved} onChange={(e) => setHideSolved(e.target.checked)} />
          Sakrij riješeno
        </label>
      </div>
    );
  }

  const safeIdx = idx % visible.length;
  const item = visible[safeIdx];

  function next() {
    setIdx((i) => (i + 1) % visible.length);
  }
  function prev() {
    setIdx((i) => (i - 1 + visible.length) % visible.length);
  }

  return (
    <div className="study">
      <div className="study-progress">
        {safeIdx + 1} / {visible.length}
        <label className="hide-toggle">
          <input
            type="checkbox"
            checked={hideSolved}
            onChange={(e) => {
              setHideSolved(e.target.checked);
              setIdx(0);
            }}
          />
          Sakrij riješeno
        </label>
      </div>
      <StudyItem key={item.id} item={item} solved={solvedIds.has(item.id)} onMark={markSolved} onDone={next} />
      <div className="study-nav">
        <button className="ghost" onClick={prev}>
          ← Prethodno
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

function FlashcardItem({ item, solved, onMark, onDone }) {
  const [flipped, setFlipped] = useState(false);
  return (
    <div className="study-card flashcard-wrap">
      {solved && <SolvedBadge />}
      <div className="flashcard-scene" onClick={() => setFlipped((f) => !f)}>
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
      {flipped && (
        <div className="self-assess">
          <button
            className="ghost"
            onClick={() => {
              onMark(item.id, false);
              onDone();
            }}
          >
            Ne znam još
          </button>
          <button
            className="solid"
            onClick={() => {
              onMark(item.id, true);
              onDone();
            }}
          >
            Znam
          </button>
        </div>
      )}
    </div>
  );
}

function TrueFalseItem({ item, solved, onMark, onDone }) {
  const [answered, setAnswered] = useState(null);

  const correct = item.sadrzaj.tocno;
  function answer(val) {
    setAnswered(val);
    onMark(item.id, val === correct);
  }

  return (
    <div className="study-card">
      {solved && <SolvedBadge />}
      <p className="study-prompt">
        <MathText text={item.sadrzaj.tvrdnja} />
      </p>
      <div className="tf-buttons">
        <button
          className={"tf-btn" + (answered === true ? (correct ? " tf-correct" : " tf-wrong") : "")}
          disabled={answered !== null}
          onClick={() => answer(true)}
        >
          Točno
        </button>
        <button
          className={"tf-btn" + (answered === false ? (!correct ? " tf-correct" : " tf-wrong") : "")}
          disabled={answered !== null}
          onClick={() => answer(false)}
        >
          Netočno
        </button>
      </div>
      {answered !== null && (
        <>
          <p className={"feedback " + (answered === correct ? "feedback-ok" : "feedback-bad")}>
            {answered === correct ? "Točno!" : `Netočno — tvrdnja je ${correct ? "točna" : "netočna"}.`}
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

  function choose(i) {
    if (selected !== null) return;
    setSelected(i);
    onMark(item.id, i === correctIdx);
  }

  return (
    <div className="study-card">
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
  const [value, setValue] = useState("");
  const [checked, setChecked] = useState(false);

  function normalize(s) {
    return s.trim().toLowerCase().replace(/\s+/g, "");
  }

  const isCorrect = normalize(value) === normalize(item.sadrzaj.odgovor);

  function check() {
    setChecked(true);
    onMark(item.id, isCorrect);
  }

  const [before, after] = item.sadrzaj.tekst.split("___");

  return (
    <div className="study-card">
      {solved && <SolvedBadge />}
      <p className="study-prompt fillin-prompt">
        <MathText text={before} />
        <input
          className="fillin-input"
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