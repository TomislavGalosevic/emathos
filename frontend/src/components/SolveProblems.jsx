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

function parseCell(s) {
  s = (s || "").replace(",", ".").trim();
  if (!s) return NaN;
  const m = s.match(/^(-?\d*\.?\d+)\s*\/\s*(-?\d*\.?\d+)$/);
  if (m) return parseFloat(m[1]) / parseFloat(m[2]);
  return parseFloat(s);
}

export default function SolveProblems({ courseId, moduleId, onProgressChange }) {
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
        const problemIds = new Set(probs.map((p) => p.id));
        setSolvedIds(new Set(
          progress
            .filter((p) => p.status === "solved" && problemIds.has(p.item_id))
            .map((p) => p.item_id)
        ));
        setLoading(false);
      }
    );
  }, [courseId, moduleId]);

  function markSolved(problemId) {
    setSolvedIds((prev) => new Set(prev).add(problemId));
    if (hideSolved) setSessionSolvedIds((prev) => new Set(prev).add(problemId));
    if (onProgressChange) onProgressChange();
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

      {problem.tip === "matrix" ? (
        <MatrixProblemCard key={problem.id} problem={problem} solved={activeSolved.has(problem.id)} onSolved={() => markSolved(problem.id)} />
      ) : problem.tip === "multi" ? (
        <MultiProblemCard key={problem.id} problem={problem} solved={activeSolved.has(problem.id)} onSolved={() => markSolved(problem.id)} />
      ) : problem.tip === "choice" ? (
        <ChoiceProblemCard key={problem.id} problem={problem} solved={activeSolved.has(problem.id)} onSolved={() => markSolved(problem.id)} />
      ) : problem.tip === "point" ? (
        <PointProblemCard key={problem.id} problem={problem} solved={activeSolved.has(problem.id)} onSolved={() => markSolved(problem.id)} />
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

function ProblemCard({ problem, solved, onSolved }) {
  const [answer, setAnswer] = useState("");
  const [result, setResult] = useState(null);
  const [checking, setChecking] = useState(false);
  const [hintsShown, setHintsShown] = useState(0);
  const [showSolution, setShowSolution] = useState(false);
  const [locked, setLocked] = useState(false);

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
  }

  const inputDisabled = locked || checking;

  return (
    <div className="study-card">
      {solved && <span className="solved-badge">✓ Riješeno</span>}
      <p className="study-prompt"><MathText text={problem.tekst} /></p>

      <div className="solve-row">
        <input value={answer} onChange={(e) => setAnswer(e.target.value)}
          placeholder={locked ? "Rješenje je prikazano" : "Tvoj odgovor…"}
          onKeyDown={(e) => e.key === "Enter" && check()} disabled={inputDisabled} />
        <button className="solid" onClick={check} disabled={inputDisabled || !answer.trim()}>
          {checking ? "Provjera…" : "Provjeri"}
        </button>
      </div>

      {result === true && <p className="feedback feedback-ok">Točno! 🎉</p>}
      {result === false && !locked && <p className="feedback feedback-bad">Netočno.</p>}

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

function MultiProblemCard({ problem, solved, onSolved }) {
  let fields = [];
  try { fields = JSON.parse(problem.tocan_odgovor); } catch { fields = []; }

  const [answers, setAnswers] = useState(() =>
    fields.map(f =>
      f.type === "matrix"
        ? { rows: 2, cols: 2, cells: Array.from({ length: 5 }, () => Array(5).fill("")) }
        : ""
    )
  );
  const [checked, setChecked]       = useState(false);
  const [results, setResults]       = useState([]);
  const [dimErrors, setDimErrors]   = useState([]);
  const [showSolution, setShowSolution] = useState(false);
  const [locked, setLocked]         = useState(false);
  const [hintsShown, setHintsShown] = useState(0);

  function setTextAnswer(i, val) {
    setAnswers(prev => { const n = [...prev]; n[i] = val; return n; });
  }
  function setMatrixDim(i, key, val) {
    setAnswers(prev => { const n = [...prev]; n[i] = { ...n[i], [key]: +val }; return n; });
  }
  function setMatrixCell(i, r, c, val) {
    setAnswers(prev => {
      const n = [...prev];
      const cells = n[i].cells.map(row => [...row]);
      cells[r][c] = val;
      n[i] = { ...n[i], cells };
      return n;
    });
  }

  function checkField(f, ans) {
    if (f.type === "choice") return normalize(ans) === normalize(f.answer);
    if (f.type === "matrix") {
      try {
        const exp = JSON.parse(f.answer);
        const er = exp.length, ec = exp[0].length;
        if (ans.rows !== er || ans.cols !== ec) return null;
        for (let r = 0; r < er; r++)
          for (let c = 0; c < ec; c++) {
            const uv = parseCell(ans.cells[r][c]);
            const ev = parseCell(String(exp[r][c]));
            if (isNaN(uv) || Math.abs(uv - ev) >= 0.01) return false;
          }
        return true;
      } catch { return false; }
    }
    return normalize(ans) === normalize(f.answer);
  }

  function checkAll() {
    const res = fields.map((f, i) => checkField(f, answers[i]));
    const dims = res.map(r => r === null);
    setResults(res.map(r => r === null ? false : r));
    setDimErrors(dims);
    setChecked(true);
    if (res.every(r => r === true)) {
      setLocked(true);
      api.markProblemSeen(problem.id).catch(() => {});
      onSolved();
    }
  }

  function revealSolution() {
    setShowSolution(true);
    setLocked(true);
    setChecked(false);
    setAnswers(fields.map(f => {
      if (f.type === "matrix") {
        try {
          const exp = JSON.parse(f.answer);
          return { rows: exp.length, cols: exp[0].length, cells: exp.map(row => row.map(String)) };
        } catch { return { rows: 2, cols: 2, cells: Array.from({length:5},()=>Array(5).fill("")) }; }
      }
      return f.answer;
    }));
  }

  return (
    <div className="study-card">
      {solved && <span className="solved-badge">✓ Riješeno</span>}
      <p className="study-prompt"><MathText text={problem.tekst} /></p>

      <div className="multi-fields">
        {fields.map((f, i) => {
          const res = results[i];
          const dimErr = dimErrors[i];

          if (f.type === "choice") {
            const opts = f.options || [];
            return (
              <div key={i} className="multi-field multi-field-choice">
                <label><MathText text={f.label} /></label>
                <div className="choice-options">
                  {opts.map(opt => {
                    const isSel = answers[i] === opt;
                    let cls = "choice-btn";
                    if (isSel && checked && locked && res === true)   cls += " choice-correct";
                    else if (isSel && checked && res === false)       cls += " choice-wrong";
                    else if (isSel)                                   cls += " choice-selected";
                    return (
                      <button key={opt} className={cls}
                        onClick={() => !locked && setTextAnswer(i, opt)}
                        disabled={locked}>
                        {opt}
                      </button>
                    );
                  })}
                </div>
                {checked && !locked && res === true  && <span className="field-ok">✓</span>}
                {checked && !locked && res === false && (
                  <><span className="field-bad">✗</span>
                    <span className="field-correct">Točno: <MathText text={f.answer} /></span></>
                )}
                {showSolution && <span className="field-ok">✓</span>}
              </div>
            );
          }

          if (f.type === "matrix") {
            const state = answers[i];
            return (
              <div key={i} className="multi-field multi-field-matrix">
                <label><MathText text={f.label} /></label>
                <div className="matrix-size" style={{ marginBottom: "6px" }}>
                  <span>Dim:</span>
                  <select value={state.rows} disabled={locked}
                    onChange={e => setMatrixDim(i, "rows", e.target.value)}>
                    {[1,2,3,4,5].map(n => <option key={n} value={n}>{n}</option>)}
                  </select>
                  <span>×</span>
                  <select value={state.cols} disabled={locked}
                    onChange={e => setMatrixDim(i, "cols", e.target.value)}>
                    {[1,2,3,4,5].map(n => <option key={n} value={n}>{n}</option>)}
                  </select>
                </div>
                <div className="matrix-grid" style={{ gridTemplateColumns: `repeat(${state.cols}, 60px)` }}>
                  {Array.from({ length: state.rows }).map((_, r) =>
                    Array.from({ length: state.cols }).map((_, c) => (
                      <input key={`${r}-${c}`}
                        value={state.cells[r]?.[c] || ""}
                        onChange={e => setMatrixCell(i, r, c, e.target.value)}
                        disabled={locked}
                        className={
                          checked && cellOk(results[i], r, c) === true  ? "cell-ok"  :
                          checked && cellOk(results[i], r, c) === false ? "cell-bad" : ""
                        }
                      />
                    ))
                  )}
                </div>
                {dimErr    && <p className="feedback feedback-bad" style={{marginTop:"4px"}}>Dimenzije nisu ispravne.</p>}
                {checked && !locked && !dimErr && res === true  && <span className="field-ok">✓</span>}
                {checked && !locked && !dimErr && res === false && <span className="field-bad">✗</span>}
                {showSolution && <span className="field-ok">✓</span>}
              </div>
            );
          }

          return (
            <div key={i} className="multi-field">
              <label><MathText text={f.label} /></label>
              <input
                value={showSolution ? f.answer : answers[i]}
                onChange={e => setTextAnswer(i, e.target.value)}
                disabled={locked}
                placeholder="..."
                onKeyDown={e => e.key === "Enter" && !locked && checkAll()}
              />
              {checked && !locked && res === true  && <span className="field-ok">✓</span>}
              {checked && !locked && res === false && (
                <><span className="field-bad">✗</span>
                  <span className="field-correct">Točno: <MathText text={f.answer} /></span></>
              )}
              {showSolution && <span className="field-ok">✓</span>}
            </div>
          );
        })}
      </div>

      {!locked && (
        <div className="solve-row">
          <button className="solid" onClick={checkAll}>Provjeri</button>
        </div>
      )}

      {checked && locked  && <p className="feedback feedback-ok">Sve točno! 🎉</p>}
      {checked && !locked && !results.every(Boolean) && (
        <p className="feedback feedback-bad">Nisu svi odgovori točni.</p>
      )}

      {problem.hints.length > 0 && !locked && (
        <div className="hints-block">
          {problem.hints.slice(0, hintsShown).map((h) => (
            <p key={h.id} className="hint-reveal">💡 <MathText text={h.sadrzaj} /></p>
          ))}
          {hintsShown < problem.hints.length && (
            <button className="ghost" onClick={() => setHintsShown(n => n + 1)}>
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

function cellOk(fieldResult, r, c) { return undefined; }

function ChoiceProblemCard({ problem, solved, onSolved }) {
  let options = [];
  try { options = JSON.parse(problem.tocan_odgovor).options; } catch { options = []; }

  const [selected, setSelected] = useState(null);
  const [result, setResult] = useState(null); 
  const [hintsShown, setHintsShown] = useState(0);
  const [showSolution, setShowSolution] = useState(false);
  const locked = result === true || showSolution;

  async function handleSelect(opt) {
    if (locked) return;
    setSelected(opt);
    try {
      const r = await api.checkProblem(problem.id, opt);
      setResult(r.tocno);
      if (r.tocno) onSolved();
    } catch { setResult(false); }
  }

  function revealSolution() {
    setShowSolution(true);
  }

  return (
    <div className="study-card">
      {solved && <span className="solved-badge">✓ Riješeno</span>}
      <p className="study-prompt"><MathText text={problem.tekst} /></p>

      <div className="choice-options">
        {options.map((opt) => {
          const isSelected = selected === opt;
          let cls = "choice-btn";
          if (isSelected && result === true)  cls += " choice-correct";
          else if (isSelected && result === false) cls += " choice-wrong";
          else if (isSelected) cls += " choice-selected";
          return (
            <button key={opt} className={cls} onClick={() => handleSelect(opt)} disabled={locked}>
              {opt}
            </button>
          );
        })}
      </div>

      {result === true  && <p className="feedback feedback-ok">Točno! 🎉</p>}
      {result === false && !locked && <p className="feedback feedback-bad">Netočno.</p>}

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
          {!showSolution && !result ? (
            <button className="ghost" onClick={revealSolution}>Prikaži rješenje</button>
          ) : showSolution ? (
            <div className="solution-text"><strong>Rješenje:</strong> <MathText text={problem.rjesenje} /></div>
          ) : null}
        </div>
      )}
    </div>
  );
}

function PointProblemCard({ problem, solved, onSolved }) {
  const [xVal, setXVal] = useState("");
  const [yVal, setYVal] = useState("");
  const [result, setResult]     = useState(null);
  const [locked, setLocked]     = useState(false);
  const [hintsShown, setHintsShown] = useState(0);
  const [showSolution, setShowSolution] = useState(false);

  async function handleCheck() {
    if (locked || (!xVal.trim() && !yVal.trim())) return;
    const combined = `(${xVal.trim()}, ${yVal.trim()})`;
    try {
      const r = await api.checkProblem(problem.id, combined);
      setResult(r.tocno);
      if (r.tocno) { setLocked(true); onSolved(); }
    } catch { setResult(false); }
  }

  function revealSolution() {
    setShowSolution(true);
    setLocked(true);
    setResult(null);
    try {
      const s = problem.tocan_odgovor.replace(/^[Tt]?\s*\(/, "").replace(/\)\s*$/, "");
      const parts = s.split(",");
      if (parts.length === 2) { setXVal(parts[0].trim()); setYVal(parts[1].trim()); }
    } catch {}
  }

  const inputCls = `point-coord-input${result === true ? " cell-ok" : result === false ? " cell-bad" : ""}`;

  return (
    <div className="study-card">
      {solved && <span className="solved-badge">✓ Riješeno</span>}
      <p className="study-prompt"><MathText text={problem.tekst} /></p>

      <div className="point-input-wrapper">
        <span className="point-T">T</span>
        <span className="point-paren">(</span>
        <input className={inputCls} value={xVal} onChange={e => setXVal(e.target.value)}
          disabled={locked} placeholder="x" onKeyDown={e => e.key === "Enter" && handleCheck()} />
        <span className="point-comma">,</span>
        <input className={inputCls} value={yVal} onChange={e => setYVal(e.target.value)}
          disabled={locked} placeholder="y" onKeyDown={e => e.key === "Enter" && handleCheck()} />
        <span className="point-paren">)</span>
        {!locked && <button className="solid" onClick={handleCheck}>Provjeri</button>}
      </div>

      {result === true  && <p className="feedback feedback-ok">Točno! 🎉</p>}
      {result === false && <p className="feedback feedback-bad">Netočno.</p>}

      {problem.hints.length > 0 && !locked && (
        <div className="hints-block">
          {problem.hints.slice(0, hintsShown).map(h => (
            <p key={h.id} className="hint-reveal">💡 <MathText text={h.sadrzaj} /></p>
          ))}
          {hintsShown < problem.hints.length && (
            <button className="ghost" onClick={() => setHintsShown(n => n + 1)}>
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
      {showSolution && problem.rjesenje && (
        <div className="solution-text"><strong>Rješenje:</strong> <MathText text={problem.rjesenje} /></div>
      )}
    </div>
  );
}

function MatrixProblemCard({ problem, solved, onSolved }) {
  let expected = { matrix: [[]] };
  try { expected = JSON.parse(problem.tocan_odgovor); } catch {}

  const [rows, setRows] = useState(2);
  const [cols, setCols] = useState(2);
  const [cells, setCells] = useState(() => Array.from({ length: 5 }, () => Array.from({ length: 5 }, () => "")));
  const [checked, setChecked] = useState(false);
  const [cellResults, setCellResults] = useState([]);
  const [showSolution, setShowSolution] = useState(false);
  const [locked, setLocked] = useState(false);
  const [hintsShown, setHintsShown] = useState(0);
  const [dimError, setDimError] = useState(false);

  function updateCell(r, c, val) {
    setCells(prev => {
      const next = prev.map(row => [...row]);
      next[r][c] = val;
      return next;
    });
  }

  function checkMatrix() {
    const exp = expected.matrix;
    const expRows = exp.length;
    const expCols = exp[0].length;

    if (rows !== expRows || cols !== expCols) {
      setDimError(true);
      setCellResults([]);
      setChecked(true);
      return;
    }

    setDimError(false);
    const results = [];
    let allOk = true;
    for (let r = 0; r < rows; r++) {
      results[r] = [];
      for (let c = 0; c < cols; c++) {
        const userVal = parseCell(cells[r][c]);
        const expVal = parseCell(String(exp[r][c]));
        const ok = !isNaN(userVal) && Math.abs(userVal - expVal) < 0.01;
        results[r][c] = ok;
        if (!ok) allOk = false;
      }
    }
    setCellResults(results);
    setChecked(true);

    if (allOk) {
      setLocked(true);
      api.markProblemSeen(problem.id).catch(() => {});
      onSolved();
    }
  }

  function revealSolution() {
    setShowSolution(true);
    setLocked(true);
    setDimError(false);
    const exp = expected.matrix;
    setRows(exp.length);
    setCols(exp[0].length);
    setCells(exp.map(row => row.map(v => String(v))));
  }

  return (
    <div className="study-card">
      {solved && <span className="solved-badge">✓ Riješeno</span>}
      <p className="study-prompt"><MathText text={problem.tekst} /></p>

      <div className="matrix-size">
        <span>Dimenzije:</span>
        <select value={rows} onChange={e => { setRows(+e.target.value); setChecked(false); setDimError(false); }} disabled={locked}>
          {[1,2,3,4,5].map(n => <option key={n} value={n}>{n}</option>)}
        </select>
        <span>×</span>
        <select value={cols} onChange={e => { setCols(+e.target.value); setChecked(false); setDimError(false); }} disabled={locked}>
          {[1,2,3,4,5].map(n => <option key={n} value={n}>{n}</option>)}
        </select>
      </div>

      <div className="matrix-grid" style={{ gridTemplateColumns: `repeat(${cols}, 60px)` }}>
        {Array.from({ length: rows }).map((_, r) =>
          Array.from({ length: cols }).map((_, c) => (
            <input
              key={`${r}-${c}`}
              value={cells[r]?.[c] || ""}
              onChange={e => updateCell(r, c, e.target.value)}
              disabled={locked}
              className={checked && cellResults[r]?.[c] === true ? "cell-ok" : checked && cellResults[r]?.[c] === false ? "cell-bad" : ""}
            />
          ))
        )}
      </div>

      {dimError && <p className="feedback feedback-bad">Dimenzije matrice nisu ispravne.</p>}
      {checked && locked && <p className="feedback feedback-ok">Točno! 🎉</p>}
      {checked && !locked && !dimError && cellResults.length > 0 && !cellResults.flat().every(Boolean) && (
        <p className="feedback feedback-bad">Neke vrijednosti nisu točne.</p>
      )}

      {!locked && (
        <div className="solve-row">
          <button className="solid" onClick={checkMatrix}>Provjeri</button>
        </div>
      )}

      {problem.hints.length > 0 && !locked && (
        <div className="hints-block">
          {problem.hints.slice(0, hintsShown).map((h) => (
            <p key={h.id} className="hint-reveal">💡 <MathText text={h.sadrzaj} /></p>
          ))}
          {hintsShown < problem.hints.length && (
            <button className="ghost" onClick={() => setHintsShown(n => n + 1)}>
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