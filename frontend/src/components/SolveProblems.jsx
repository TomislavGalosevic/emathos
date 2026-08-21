import { useEffect, useState } from "react";
import { api } from "../api/client";
import MathText from "./MathText";

export default function SolveProblems({ courseId, moduleId }) {
  const [problems, setProblems] = useState([]);
  const [solvedIds, setSolvedIds] = useState(new Set());
  const [loading, setLoading] = useState(true);
  const [idx, setIdx] = useState(0);
  const [hideSolved, setHideSolved] = useState(false);

  useEffect(() => {
    setLoading(true);
    setIdx(0);
    Promise.all([api.listProblems(courseId, moduleId), api.myProgress("problem")]).then(
      ([probs, progress]) => {
        setProblems(probs);
        setSolvedIds(new Set(progress.filter((p) => p.status === "solved").map((p) => p.item_id)));
        setLoading(false);
      }
    );
  }, [courseId, moduleId]);

  function markSolved(problemId) {
    setSolvedIds((prev) => new Set(prev).add(problemId));
  }

  if (loading) return <p className="empty">Učitavanje…</p>;
  if (problems.length === 0) return <p className="empty">Za ovo područje još nema zadataka.</p>;

  const visible = hideSolved ? problems.filter((p) => !solvedIds.has(p.id)) : problems;

  if (visible.length === 0) {
    return (
      <div className="study">
        <p className="empty">Svi zadaci su riješeni. 🎉</p>
        <label className="hide-toggle">
          <input type="checkbox" checked={hideSolved} onChange={(e) => setHideSolved(e.target.checked)} />
          Sakrij riješeno
        </label>
      </div>
    );
  }

  const safeIdx = idx % visible.length;
  const problem = visible[safeIdx];

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
      <ProblemCard
        key={problem.id}
        problem={problem}
        solved={solvedIds.has(problem.id)}
        onSolved={() => markSolved(problem.id)}
      />
      <div className="study-nav">
        <button className="ghost" onClick={() => setIdx((i) => (i - 1 + visible.length) % visible.length)}>
          ← Prethodni
        </button>
        <button className="ghost" onClick={() => setIdx((i) => (i + 1) % visible.length)}>
          Sljedeći →
        </button>
      </div>
    </div>
  );
}

function ProblemCard({ problem, solved, onSolved }) {
  const [answer, setAnswer] = useState("");
  const [result, setResult] = useState(null); // null | true | false
  const [checking, setChecking] = useState(false);
  const [hintsShown, setHintsShown] = useState(0);
  const [showSolution, setShowSolution] = useState(false);

  async function check() {
    if (!answer.trim()) return;
    setChecking(true);
    try {
      const r = await api.checkProblem(problem.id, answer);
      setResult(r.tocno);
      if (r.tocno) onSolved();
    } catch (e) {
      setResult(null);
    } finally {
      setChecking(false);
    }
  }

  return (
    <div className="study-card">
      {solved && <span className="solved-badge">✓ Riješeno</span>}
      <p className="study-prompt">
        <MathText text={problem.tekst} />
      </p>

      <div className="solve-row">
        <input
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
          placeholder="Tvoj odgovor…"
          onKeyDown={(e) => e.key === "Enter" && check()}
        />
        <button className="solid" onClick={check} disabled={checking || !answer.trim()}>
          {checking ? "Provjera…" : "Provjeri"}
        </button>
      </div>

      {result !== null && (
        <p className={"feedback " + (result ? "feedback-ok" : "feedback-bad")}>
          {result ? "Točno! 🎉" : "Netočno, pokušaj ponovno ili zatraži hint."}
        </p>
      )}

      {problem.hints.length > 0 && !result && (
        <div className="hints-block">
          {problem.hints.slice(0, hintsShown).map((h) => (
            <p key={h.id} className="hint-reveal">
              💡 <MathText text={h.sadrzaj} />
            </p>
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
            <button className="ghost" onClick={() => setShowSolution(true)}>
              Prikaži rješenje
            </button>
          ) : (
            <div className="solution-text">
              <strong>Rješenje:</strong> <MathText text={problem.rjesenje} />
            </div>
          )}
        </div>
      )}
    </div>
  );
}