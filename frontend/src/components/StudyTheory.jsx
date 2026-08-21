import { useEffect, useState } from "react";
import { api } from "../api/client";
import MathText from "./MathText";

export default function StudyTheory({ courseId, moduleId }) {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [idx, setIdx] = useState(0);

  useEffect(() => {
    setLoading(true);
    setIdx(0);
    api.listTheory(courseId, moduleId).then((d) => {
      setItems(d);
      setLoading(false);
    });
  }, [courseId, moduleId]);

  if (loading) return <p className="empty">Učitavanje…</p>;
  if (items.length === 0) return <p className="empty">Za ovo područje još nema teorije.</p>;

  const item = items[idx];

  function next() {
    setIdx((i) => (i + 1) % items.length);
  }
  function prev() {
    setIdx((i) => (i - 1 + items.length) % items.length);
  }

  return (
    <div className="study">
      <div className="study-progress">
        {idx + 1} / {items.length}
      </div>
      <StudyItem key={item.id} item={item} onDone={next} />
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

function StudyItem({ item, onDone }) {
  if (item.tip === "flashcard") return <FlashcardItem item={item} onDone={onDone} />;
  if (item.tip === "truefalse") return <TrueFalseItem item={item} onDone={onDone} />;
  if (item.tip === "mcq") return <McqItem item={item} onDone={onDone} />;
  if (item.tip === "fillin") return <FillinItem item={item} onDone={onDone} />;
  return null;
}

function mark(itemId) {
  api.markTheorySeen(itemId).catch(() => {});
}

function FlashcardItem({ item, onDone }) {
  const [flipped, setFlipped] = useState(false);
  return (
    <div className="study-card flashcard-wrap">
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
        <button
          className="solid"
          onClick={() => {
            mark(item.id);
            onDone();
          }}
        >
          Dalje
        </button>
      )}
    </div>
  );
}

function TrueFalseItem({ item, onDone }) {
  const [answered, setAnswered] = useState(null);

  function answer(val) {
    setAnswered(val);
    mark(item.id);
  }

  const correct = item.sadrzaj.tocno;
  return (
    <div className="study-card">
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

function McqItem({ item, onDone }) {
  const [selected, setSelected] = useState(null);

  function choose(i) {
    if (selected !== null) return;
    setSelected(i);
    mark(item.id);
  }

  const correctIdx = item.sadrzaj.tocna;
  return (
    <div className="study-card">
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

function FillinItem({ item, onDone }) {
  const [value, setValue] = useState("");
  const [checked, setChecked] = useState(false);

  function normalize(s) {
    return s.trim().toLowerCase().replace(/\s+/g, "");
  }

  function check() {
    setChecked(true);
    mark(item.id);
  }

  const isCorrect = normalize(value) === normalize(item.sadrzaj.odgovor);
  const [before, after] = item.sadrzaj.tekst.split("___");

  return (
    <div className="study-card">
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