import { useEffect, useState } from "react";
import { api } from "../api/client";
import MathText from "./MathText";
import MathInput from "./MathInput";

const TYPE_LABELS = {
  flashcard: "Flash kartica",
  truefalse: "Točno / netočno",
  mcq: "Višestruki izbor",
  fillin: "Nadopuni rečenicu",
};

export default function TheoryEditor({ courseId, moduleId }) {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [mode, setMode] = useState(null);

  async function load() {
    setLoading(true);
    setItems(await api.listTheory(courseId, moduleId));
    setLoading(false);
  }
  useEffect(() => {
    load();
    setMode(null);
  }, [courseId, moduleId]);

  async function remove(id) {
    if (!window.confirm("Obrisati ovu stavku teorije?")) return;
    await api.deleteTheory(id);
    load();
  }

  const editing = mode && mode !== "new" ? items.find((it) => it.id === mode) : null;

  return (
    <div className="editor">
      {loading ? (
        <p className="empty">Učitavanje…</p>
      ) : items.length === 0 ? (
        <p className="empty">Još nema stavki teorije.</p>
      ) : (
        <ul className="content-list">
          {items.map((it) => (
            <li key={it.id} className="content-item">
              <div className="content-item-main">
                <TheoryPreview item={it} />
                <span className="badge badge-theory">{TYPE_LABELS[it.tip] || it.tip}</span>
              </div>
              <div className="item-actions">
                <button className="edit-mod" onClick={() => setMode(it.id)} title="Uredi">
                  ✎
                </button>
                <button className="del-mod" onClick={() => remove(it.id)} title="Obriši">
                  ✕
                </button>
              </div>
            </li>
          ))}
        </ul>
      )}

      {mode === null && (
        <button className="solid" onClick={() => setMode("new")}>
          + Nova stavka teorije
        </button>
      )}

      {mode === "new" && (
        <TheoryForm
          courseId={courseId}
          moduleId={moduleId}
          onSaved={() => {
            setMode(null);
            load();
          }}
          onCancel={() => setMode(null)}
        />
      )}

      {editing && (
        <TheoryForm
          courseId={courseId}
          moduleId={moduleId}
          existing={editing}
          onSaved={() => {
            setMode(null);
            load();
          }}
          onCancel={() => setMode(null)}
        />
      )}
    </div>
  );
}

function TheoryPreview({ item }) {
  const s = item.sadrzaj;
  if (item.tip === "flashcard") {
    return (
      <span>
        <MathText text={s.pitanje} /> <span className="arrow">→</span> <MathText text={s.odgovor} />
      </span>
    );
  }
  if (item.tip === "truefalse") {
    return (
      <span>
        <MathText text={s.tvrdnja} /> <em className="hint-inline">({s.tocno ? "točno" : "netočno"})</em>
      </span>
    );
  }
  if (item.tip === "mcq") {
    return (
      <span>
        <MathText text={s.pitanje} />{" "}
        <em className="hint-inline">({s.opcije?.length || 0} opcije, točna #{(s.tocna ?? 0) + 1})</em>
      </span>
    );
  }
  if (item.tip === "fillin") {
    return <MathText text={(s.tekst || "").replace("___", `[${s.odgovor}]`)} />;
  }
  return <span>{JSON.stringify(s)}</span>;
}

function TheoryForm({ courseId, moduleId, existing, onSaved, onCancel }) {
  const isEdit = !!existing;
  const [tip, setTip] = useState(existing?.tip || "flashcard");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");

  const s = existing?.sadrzaj || {};

  // flashcard
  const [pitanje, setPitanje] = useState(s.pitanje && existing?.tip === "flashcard" ? s.pitanje : "");
  const [odgovor, setOdgovor] = useState(s.odgovor && existing?.tip === "flashcard" ? s.odgovor : "");
  // truefalse
  const [tvrdnja, setTvrdnja] = useState(existing?.tip === "truefalse" ? s.tvrdnja || "" : "");
  const [tocno, setTocno] = useState(existing?.tip === "truefalse" ? !!s.tocno : true);
  // mcq
  const [mcqPitanje, setMcqPitanje] = useState(existing?.tip === "mcq" ? s.pitanje || "" : "");
  const [opcije, setOpcije] = useState(existing?.tip === "mcq" && s.opcije?.length ? s.opcije : ["", ""]);
  const [tocnaIdx, setTocnaIdx] = useState(existing?.tip === "mcq" ? s.tocna || 0 : 0);
  // fillin
  const [fillinTekst, setFillinTekst] = useState(existing?.tip === "fillin" ? s.tekst || "" : "");
  const [fillinOdgovor, setFillinOdgovor] = useState(existing?.tip === "fillin" ? s.odgovor || "" : "");

  function setOpcija(i, val) {
    setOpcije((o) => o.map((x, idx) => (idx === i ? val : x)));
  }
  function addOpcija() {
    setOpcije((o) => [...o, ""]);
  }
  function removeOpcija(i) {
    setOpcije((o) => o.filter((_, idx) => idx !== i));
    setTocnaIdx((t) => (t === i ? 0 : t > i ? t - 1 : t));
  }

  async function save() {
    setError("");
    let sadrzaj;

    if (tip === "flashcard") {
      if (!pitanje.trim() || !odgovor.trim()) {
        setError("Unesi pitanje i odgovor.");
        return;
      }
      sadrzaj = { pitanje, odgovor };
    } else if (tip === "truefalse") {
      if (!tvrdnja.trim()) {
        setError("Unesi tvrdnju.");
        return;
      }
      sadrzaj = { tvrdnja, tocno };
    } else if (tip === "mcq") {
      const cisteOpcije = opcije.map((o) => o.trim()).filter(Boolean);
      if (!mcqPitanje.trim() || cisteOpcije.length < 2) {
        setError("Unesi pitanje i barem 2 opcije.");
        return;
      }
      sadrzaj = { pitanje: mcqPitanje, opcije: cisteOpcije, tocna: tocnaIdx };
    } else if (tip === "fillin") {
      if (!fillinTekst.includes("___")) {
        setError("Tekst mora sadržavati ___ na mjestu praznine.");
        return;
      }
      if (!fillinOdgovor.trim()) {
        setError("Unesi točan odgovor za prazninu.");
        return;
      }
      sadrzaj = { tekst: fillinTekst, odgovor: fillinOdgovor };
    }

    setSaving(true);
    try {
      if (isEdit) {
        await api.updateTheory(existing.id, { tip, sadrzaj });
      } else {
        await api.createTheory({ course_id: courseId, module_id: moduleId, tip, sadrzaj });
      }
      onSaved();
    } catch (e) {
      setError(e.message);
    } finally {
      setSaving(false);
    }
  }

  return (
    <div className="new-form">
      {isEdit && <p className="edit-label">Uređivanje stavke</p>}

      <label>Tip stavke</label>
      <select value={tip} onChange={(e) => setTip(e.target.value)} disabled={isEdit}>
        <option value="flashcard">Flash kartica</option>
        <option value="truefalse">Točno / netočno</option>
        <option value="mcq">Višestruki izbor</option>
        <option value="fillin">Nadopuni rečenicu</option>
      </select>
      {isEdit && <p className="hint" style={{ marginTop: ".3rem" }}>Tip se ne može mijenjati — obriši i dodaj novu ako trebaš drugi tip.</p>}

      {tip === "flashcard" && (
        <>
          <label>Pitanje</label>
          <MathInput value={pitanje} onChange={setPitanje} placeholder="npr. Definicija limesa niza?" rows={2} />
          <label>Odgovor</label>
          <MathInput value={odgovor} onChange={setOdgovor} placeholder="npr. Niz $a_n \to L$ ako..." rows={3} />
        </>
      )}

      {tip === "truefalse" && (
        <>
          <label>Tvrdnja</label>
          <MathInput value={tvrdnja} onChange={setTvrdnja} placeholder="npr. Svaki konvergentan niz je omeđen." rows={2} />
          <label>Tvrdnja je</label>
          <select value={tocno ? "1" : "0"} onChange={(e) => setTocno(e.target.value === "1")}>
            <option value="1">Točna</option>
            <option value="0">Netočna</option>
          </select>
        </>
      )}

      {tip === "mcq" && (
        <>
          <label>Pitanje</label>
          <MathInput value={mcqPitanje} onChange={setMcqPitanje} placeholder="npr. Koji je red konvergentan?" rows={2} />
          <label>Opcije (označi točnu)</label>
          {opcije.map((o, i) => (
            <div className="hint-row" key={i}>
              <input
                type="radio"
                name="tocna-opcija"
                checked={tocnaIdx === i}
                onChange={() => setTocnaIdx(i)}
                style={{ width: "auto" }}
              />
              <input value={o} onChange={(e) => setOpcija(i, e.target.value)} placeholder={`Opcija ${i + 1}`} />
              {opcije.length > 2 && (
                <button className="del-mod" onClick={() => removeOpcija(i)} title="Ukloni">
                  ✕
                </button>
              )}
            </div>
          ))}
          <button className="ghost" onClick={addOpcija} style={{ marginTop: ".4rem", marginBottom: "1rem" }}>
            + opcija
          </button>
        </>
      )}

      {tip === "fillin" && (
        <>
          <label>Rečenica (koristi ___ za prazninu)</label>
          <MathInput
            value={fillinTekst}
            onChange={setFillinTekst}
            placeholder="npr. Derivacija funkcije $x^2$ je ___."
            rows={2}
          />
          <label>Točan odgovor za prazninu</label>
          <input value={fillinOdgovor} onChange={(e) => setFillinOdgovor(e.target.value)} placeholder="npr. 2x" />
        </>
      )}

      {error && <p className="error">{error}</p>}
      <div className="form-actions">
        <button className="solid" onClick={save} disabled={saving}>
          {saving ? "Spremanje…" : isEdit ? "Spremi izmjene" : "Spremi"}
        </button>
        <button className="ghost" onClick={onCancel}>
          Odustani
        </button>
      </div>
    </div>
  );
}