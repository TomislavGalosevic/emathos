import { useEffect, useState } from "react";
import { api } from "../api/client";
import MathText from "./MathText";
import MathInput from "./MathInput";

export default function ProblemsEditor({ courseId, moduleId }) {
  const [problems, setProblems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [open, setOpen] = useState(false);

  async function load() {
    setLoading(true);
    setProblems(await api.listProblems(courseId, moduleId));
    setLoading(false);
  }
  useEffect(() => {
    load();
    setOpen(false);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [courseId, moduleId]);

  async function remove(id) {
    if (!window.confirm("Obrisati ovaj zadatak?")) return;
    await api.deleteProblem(id);
    load();
  }

  return (
    <div className="editor">
      {loading ? (
        <p className="empty">Učitavanje…</p>
      ) : problems.length === 0 ? (
        <p className="empty">Još nema zadataka.</p>
      ) : (
        <ul className="content-list">
          {problems.map((p) => (
            <li key={p.id} className="content-item">
              <div className="content-item-main">
                <MathText text={p.tekst} />
              </div>
              {p.hints.length > 0 && (
                <div className="content-item-sub">
                  {p.hints.length} hint{p.hints.length > 1 ? "ova" : ""}
                </div>
              )}
              <button className="del-mod" onClick={() => remove(p.id)} title="Obriši">
                ✕
              </button>
            </li>
          ))}
        </ul>
      )}

      {!open ? (
        <button className="solid" onClick={() => setOpen(true)}>
          + Novi zadatak
        </button>
      ) : (
        <NewProblemForm
          courseId={courseId}
          moduleId={moduleId}
          onSaved={() => {
            setOpen(false);
            load();
          }}
          onCancel={() => setOpen(false)}
        />
      )}
    </div>
  );
}

function NewProblemForm({ courseId, moduleId, onSaved, onCancel }) {
  const [tekst, setTekst] = useState("");
  const [tocanOdgovor, setTocanOdgovor] = useState("");
  const [rjesenje, setRjesenje] = useState("");
  const [hints, setHints] = useState([""]);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");

  function setHint(i, val) {
    setHints((h) => h.map((x, idx) => (idx === i ? val : x)));
  }
  function addHint() {
    setHints((h) => [...h, ""]);
  }
  function removeHint(i) {
    setHints((h) => h.filter((_, idx) => idx !== i));
  }

  async function save() {
    if (!tekst.trim()) {
      setError("Unesi tekst zadatka.");
      return;
    }
    if (!tocanOdgovor.trim()) {
      setError("Unesi točan odgovor.");
      return;
    }
    setSaving(true);
    setError("");
    try {
      await api.createProblem({
        course_id: courseId,
        module_id: moduleId,
        tekst,
        tip: "auto",
        tocan_odgovor: tocanOdgovor,
        rjesenje,
        hints: hints.map((h) => h.trim()).filter(Boolean),
      });
      onSaved();
    } catch (e) {
      setError(e.message);
    } finally {
      setSaving(false);
    }
  }

  return (
    <div className="new-form">
      <label>Tekst zadatka (LaTeX: $...$ za formule)</label>
      <MathInput value={tekst} onChange={setTekst} placeholder="npr. Izracunajte $\lim_{n\to\infty} \frac{2n+1}{n}$." rows={3} />

      <label>Točan odgovor</label>
      <input
        value={tocanOdgovor}
        onChange={(e) => setTocanOdgovor(e.target.value)}
        placeholder="npr. 2  ili  2x+3  ili matrica [[1,0],[0,1]]"
      />

      <label>Rješenje (prikazuje se na kraju)</label>
      <MathInput value={rjesenje} onChange={setRjesenje} placeholder="Puno rješenje s postupkom…" rows={3} />

      <label>Hintovi (redoslijedom)</label>
      {hints.map((h, i) => (
        <div className="hint-row" key={i}>
          <input
            value={h}
            onChange={(e) => setHint(i, e.target.value)}
            placeholder={`Hint ${i + 1}`}
          />
          {hints.length > 1 && (
            <button className="del-mod" onClick={() => removeHint(i)} title="Ukloni">
              ✕
            </button>
          )}
        </div>
      ))}
      <button className="ghost" onClick={addHint} style={{ marginBottom: "1rem" }}>
        + hint
      </button>

      {error && <p className="error">{error}</p>}
      <div className="form-actions">
        <button className="solid" onClick={save} disabled={saving}>
          {saving ? "Spremanje…" : "Spremi zadatak"}
        </button>
        <button className="ghost" onClick={onCancel}>
          Odustani
        </button>
      </div>
    </div>
  );
}