import { useEffect, useState } from "react";
import { api } from "../api/client";
import MathText from "./MathText";

export default function SolveProblems({ courseId, moduleId }) {
  const [problems, setProblems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [idx, setIdx] = useState(0);

  useEffect(() => {
    setLoading(true);
    setIdx(0);
    api.listProblems(courseId, moduleId).then((d) => {
      setProblems(d);
      setLoading(false);
    });
  }, [courseId, moduleId]);

  if (loading) return <p className="empty">Učitavanje…</p>;
  if (problems.length === 0) return <p className="empty">Za ovo područje još nema zadataka.</p>;

  const problem = problems[idx];

  return (
    <div className="study">
      <div className="study-progress">
        {idx + 1} / {problems.length}
      </div>
      <ProblemCard key={problem.id} problem={problem} />
      <div className="study-nav">
        <button className="ghost" onClick={() => setIdx((i) => (i - 1 + problems.length) % problems.length)}>
          ← Prethodni
        </button>
        <button className="ghost" onClick={() => setIdx((i) => (i + 1) % problems.length)}>
          Sljedeći →
        </button>
      </div>
    </div>
  );
}

function ProblemCard({ problem }) {
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
    } catch (e) {
      setResult(null);
    } finally {
      setChecking(false);
    }
  }

  return (
    <div className="study-card">
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