import { useEffect, useState } from "react";
import { api } from "../api/client";
import MathText from "./MathText";

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function normalize(s) {
  return (s || "").replace(/\s+/g, "").toLowerCase().replace(/,/g, ".").trim();
}

export default function SolveProblems({ courseId, moduleId }) {
  const [problems, setProblems] = useState([]);
  const [solvedIds, setSolvedIds] = useState(new Set());
  const [sessionSolvedIds, setSessionSolvedIds] = useState(new Set());
  const [loading, setLoading] = useState(true);
  const [idx, setIdx] = useState(0);
  const [hideSolved, setHideSolved] = useState(false);

  useEffect(() => {
    setLoading(true);
    setIdx(0);
    Promise.all([api.listProblems(courseId, moduleId), api.myProgress("problem")]).then(
      ([probs, progress]) => {
        setProblems(shuffle(probs));
        setSolvedIds(new Set(progress.filter((p) => p.status === "solved").map((p) => p.item_id)));
        setLoading(false);
      }
    );
  }, [courseId, moduleId]);

  function markSolved(problemId) {
    setSolvedIds((prev) => new Set(prev).add(problemId));
    if (hideSolved) setSessionSolvedIds((prev) => new Set(prev).add(problemId));
  }

  function toggleHideSolved(checked) {
    setHideSolved(checked);
    if (checked) setSessionSolvedIds(new Set());
    setIdx(0);
  }

  if (loading) return <p className="empty">Učitavanje…</p>;
  if (problems.length === 0) return <p className="empty">Za ovo područje još nema zadataka.</p>;

  const activeSolved = hideSolved ? sessionSolvedIds : solvedIds;
  const visible = hideSolved ? problems.filter((p) => !sessionSolvedIds.has(p.id)) : problems;

  if (visible.length === 0) {
    return (
      <div className="study">
        <p className="empty">Svi zadaci su riješeni. 🎉</p>
        <label className="hide-toggle">
          <input type="checkbox" checked={hideSolved} onChange={(e) => toggleHideSolved(e.target.checked)} />
          Sakrij riješeno
        </label>
      </div>
    );
  }

  const safeIdx = idx % visible.length;
  const problem = visible[safeIdx];
  const solvedInList = problems.filter((p) => activeSolved.has(p.id)).length;

  return (
    <div className="study">
      <div className="study-progress">
        <span>Pitanje {safeIdx + 1}/{visible.length}</span>
        <span className="live-solved">Riješeno: {solvedInList}/{problems.length}</span>
        <label className="hide-toggle">
          <input type="checkbox" checked={hideSolved} onChange={(e) => toggleHideSolved(e.target.checked)} />
          Sakrij riješeno
        </label>
      </div>

      {problem.tip === "multi" ? (
        <MultiProblemCard key={problem.id} problem={problem} solved={activeSolved.has(problem.id)} onSolved={() => markSolved(problem.id)} />
      ) : (
        <ProblemCard key={problem.id} problem={problem} solved={activeSolved.has(problem.id)} onSolved={() => markSolved(problem.id)} />
      )}

      <div className="study-nav">
        <button className="ghost" onClick={() => setIdx((i) => (i - 1 + visible.length) % visible.length)}>← Prethodni</button>
        <button className="ghost" onClick={() => setIdx((i) => (i + 1) % visible.length)}>Sljedeći →</button>
      </div>
    </div>
  );
}

/* ---- SINGLE ANSWER ---- */
function ProblemCard({ problem, solved, onSolved }) {
  const [answer, setAnswer] = useState("");
  const [result, setResult] = useState(null);
  const [checking, setChecking] = useState(false);
  const [hintsShown, setHintsShown] = useState(0);
  const [showSolution, setShowSolution] = useState(false);
  const [locked, setLocked] = useState(false);

  const isSelf = problem.tip === "self";

  async function check() {
    if (!answer.trim() || locked) return;
    setChecking(true);
    try {
      const r = await api.checkProblem(problem.id, answer);
      setResult(r.tocno);
      if (r.tocno) { onSolved(); setLocked(true); }
    } catch (e) { setResult(null); }
    finally { setChecking(false); }
  }

  function revealSolution() {
    setShowSolution(true);
    setLocked(true);
    setResult(null);
    api.markProblemSeen(problem.id).catch(() => {});
    onSolved();
  }

  const inputDisabled = locked || checking;

  return (
    <div className="study-card">
      {solved && <span className="solved-badge">✓ Riješeno</span>}
      <p className="study-prompt"><MathText text={problem.tekst} /></p>

      {!isSelf && (
        <div className="solve-row">
          <input value={answer} onChange={(e) => setAnswer(e.target.value)}
            placeholder={locked ? "Rješenje je prikazano" : "Tvoj odgovor…"}
            onKeyDown={(e) => e.key === "Enter" && check()} disabled={inputDisabled} />
          <button className="solid" onClick={check} disabled={inputDisabled || !answer.trim()}>
            {checking ? "Provjera…" : "Provjeri"}
          </button>
        </div>
      )}

      {result === true && <p className="feedback feedback-ok">Točno! 🎉</p>}
      {result === false && !locked && <p className="feedback feedback-bad">Netočno, pokušaj ponovno ili zatraži hint.</p>}

      {problem.hints.length > 0 && !locked && result !== true && (
        <div className="hints-block">
          {problem.hints.slice(0, hintsShown).map((h) => (
            <p key={h.id} className="hint-reveal">💡 <MathText text={h.sadrzaj} /></p>
          ))}
          {hintsShown < problem.hints.length && (
            <button className="ghost" onClick={() => setHintsShown((n) => n + 1)}>
              Pokaži hint ({hintsShown + 1}/{problem.hints.length})
            </button>
          )}
        </div>
      )}

      {problem.rjesenje && (
        <div className="solution-block">
          {!showSolution ? (
            <button className="ghost" onClick={revealSolution}>Prikaži rješenje</button>
          ) : (
            <div className="solution-text"><strong>Rješenje:</strong> <MathText text={problem.rjesenje} /></div>
          )}
        </div>
      )}
    </div>
  );
}

/* ---- MULTI ANSWER ---- */
function MultiProblemCard({ problem, solved, onSolved }) {
  let fields = [];
  try { fields = JSON.parse(problem.tocan_odgovor); } catch { fields = []; }

  const [answers, setAnswers] = useState(() => fields.map(() => ""));
  const [checked, setChecked] = useState(false);
  const [results, setResults] = useState([]);
  const [showSolution, setShowSolution] = useState(false);
  const [locked, setLocked] = useState(false);
  const [hintsShown, setHintsShown] = useState(0);

  function updateAnswer(i, val) {
    setAnswers((prev) => { const next = [...prev]; next[i] = val; return next; });
  }

  function checkAll() {
    const res = fields.map((f, i) => normalize(answers[i]) === normalize(f.answer));
    setResults(res);
    setChecked(true);
    if (res.every(Boolean)) {
      setLocked(true);
      api.markProblemSeen(problem.id).catch(() => {});
      onSolved();
    }
  }

  function revealSolution() {
    setShowSolution(true);
    setLocked(true);
    setChecked(false);
    api.markProblemSeen(problem.id).catch(() => {});
    onSolved();
  }

  return (
    <div className="study-card">
      {solved && <span className="solved-badge">✓ Riješeno</span>}
      <p className="study-prompt"><MathText text={problem.tekst} /></p>

      <div className="multi-fields">
        {fields.map((f, i) => (
          <div key={i} className="multi-field">
            <label><MathText text={f.label} /></label>
            <input
              value={showSolution ? f.answer : answers[i]}
              onChange={(e) => updateAnswer(i, e.target.value)}
              disabled={locked}
              placeholder="..."
              onKeyDown={(e) => e.key === "Enter" && !locked && checkAll()}
            />
            {checked && !locked && results[i] === true && <span className="field-ok">✓</span>}
            {checked && !locked && results[i] === false && (
              <>
                <span className="field-bad">✗</span>
                <span className="field-correct">Točno: <MathText text={f.answer} /></span>
              </>
            )}
            {showSolution && <span className="field-ok">✓</span>}
          </div>
        ))}
      </div>

      {!locked && (
        <div className="solve-row">
          <button className="solid" onClick={checkAll}>Provjeri</button>
        </div>
      )}

      {checked && !locked && results.every(Boolean) && (
        <p className="feedback feedback-ok">Sve točno! 🎉</p>
      )}
      {checked && !locked && !results.every(Boolean) && (
        <p className="feedback feedback-bad">Nisu svi odgovori točni.</p>
      )}

      {problem.hints.length > 0 && !locked && (
        <div className="hints-block">
          {problem.hints.slice(0, hintsShown).map((h) => (
            <p key={h.id} className="hint-reveal">💡 <MathText text={h.sadrzaj} /></p>
          ))}
          {hintsShown < problem.hints.length && (
            <button className="ghost" onClick={() => setHintsShown((n) => n + 1)}>
              Pokaži hint ({hintsShown + 1}/{problem.hints.length})
            </button>
          )}
        </div>
      )}

      {problem.rjesenje && !locked && (
        <div className="solution-block">
          <button className="ghost" onClick={revealSolution}>Prikaži rješenje</button>
        </div>
      )}
    </div>
  );
}