import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api/client";
import { useAuth } from "../auth/AuthContext";
import ProblemsEditor from "../components/ProblemsEditor";
import TheoryEditor from "../components/TheoryEditor";

const YEARS = [
  { n: 1, rimski: "I", rijec: "Prva godina" },
  { n: 2, rimski: "II", rijec: "Druga godina" },
  { n: 3, rimski: "III", rijec: "Treća godina" },
];

// Ovi kolegiji nemaju teoriju (samo zadaci)
const NO_THEORY_COURSES = [
  "Primijenjena matematika za racunalnu znanost",
  "Primjena diferencijalnog i integralnog racuna",
];

export default function AdminCoursesPage() {
  const { user, logout } = useAuth();
  const [view, setView] = useState("years");
  const [year, setYear] = useState(null);
  const [courses, setCourses] = useState([]);
  const [selected, setSelected] = useState(null);
  const [newCourseName, setNewCourseName] = useState("");
  const [section, setSection] = useState(null);

  async function loadCourses() {
    setCourses(await api.listCourses());
  }
  useEffect(() => {
    loadCourses();
  }, []);

  function openYear(y) {
    setYear(y);
    setView("subjects");
  }
  async function openCourse(id) {
    setSelected(await api.courseTree(id));
    setSection(null);
    setView("editor");
  }

  async function addCourse() {
    if (!newCourseName.trim()) return;
    await api.createCourse({ naziv: newCourseName, godina: year });
    setNewCourseName("");
    loadCourses();
  }
  async function removeCourse(id, naziv, e) {
    e.stopPropagation();
    if (!window.confirm(`Obrisati kolegij "${naziv}" sa svime unutra?`)) return;
    await api.deleteCourse(id);
    loadCourses();
  }

  const coursesInYear = courses.filter((c) => c.godina === year);
  const areas =
    selected && selected.modules.length > 0
      ? selected.modules
      : [{ id: null, naziv: null }];
  const hideTheory = selected && NO_THEORY_COURSES.includes(selected.naziv);

  return (
    <div className="app">
      <div className="glow glow-a" />
      <div className="glow glow-b" />

      <header className="topbar">
        <Link to="/" className="brand">
          <img className="logo" src="/logo.png" alt="" />
          e‑Mathos
        </Link>
        <span className="who">
          {user?.username}
          <button className="ghost" onClick={logout}>
            Odjava
          </button>
        </span>
      </header>

      <main className="stage">
        {view === "years" && (
          <section className="fade">
            <p className="eyebrow">Administracija sadržaja</p>
            <h1 className="title">Odaberi godinu studija</h1>
            <div className="hex-grid years">
              {YEARS.map((y, i) => (
                <div className="hex-wrap pop" style={{ "--d": `${i * 70}ms` }} key={y.n}>
                  <button className="hex big" onClick={() => openYear(y.n)}>
                    <span className="hex-inner">
                      <span className="hex-num">{y.rimski}</span>
                      <span className="hex-label">{y.rijec}</span>
                    </span>
                  </button>
                </div>
              ))}
            </div>
          </section>
        )}

        {view === "subjects" && (
          <section className="fade">
            <button className="back" onClick={() => setView("years")}>
              ← Godine
            </button>
            <h1 className="title">{YEARS.find((y) => y.n === year)?.rijec}</h1>

            <div className="hex-grid">
              {coursesInYear.map((c, i) => (
                <div className="hex-wrap pop" style={{ "--d": `${i * 60}ms` }} key={c.id}>
                  <button className="hex" onClick={() => openCourse(c.id)}>
                    <span className="hex-inner">
                      <span className="hex-title">{c.naziv}</span>
                    </span>
                  </button>
                  <button
                    className="del"
                    title="Obriši kolegij"
                    onClick={(e) => removeCourse(c.id, c.naziv, e)}
                  >
                    ✕
                  </button>
                </div>
              ))}
              {coursesInYear.length === 0 && (
                <p className="empty">Nema kolegija u ovoj godini — dodaj prvi ispod.</p>
              )}
            </div>

            <div className="add-row">
              <input
                placeholder="Naziv novog kolegija"
                value={newCourseName}
                onChange={(e) => setNewCourseName(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && addCourse()}
              />
              <button className="solid" onClick={addCourse}>
                Dodaj kolegij
              </button>
            </div>
          </section>
        )}

        {view === "editor" && selected && (
          <section className="fade">
            <button className="back" onClick={() => setView("subjects")}>
              ← {YEARS.find((y) => y.n === year)?.rijec}
            </button>
            <h1 className="title">{selected.naziv}</h1>

            {areas.map((area) => (
              <div className="area" key={area.id ?? "root"}>
                {area.naziv && <h2 className="area-title">{area.naziv}</h2>}
                <div className="section-cards">
                  {!hideTheory && (
                    <SectionCard
                      label="Teorija"
                      desc="Flash kartice, T/N, MCQ, nadopuni…"
                      active={section?.kind === "teorija" && section?.moduleId === area.id}
                      onClick={() =>
                        setSection({ kind: "teorija", moduleId: area.id, moduleName: area.naziv })
                      }
                    />
                  )}
                  <SectionCard
                    label="Zadaci"
                    desc="Zadaci s hintovima i rješenjem"
                    active={section?.kind === "zadaci" && section?.moduleId === area.id}
                    onClick={() =>
                      setSection({ kind: "zadaci", moduleId: area.id, moduleName: area.naziv })
                    }
                  />
                </div>
              </div>
            ))}

            {section && (
              <div className="section-detail">
                <strong>
                  {section.kind === "teorija" ? "Teorija" : "Zadaci"}
                  {section.moduleName ? ` · ${section.moduleName}` : ""}
                </strong>
                {section.kind === "teorija" ? (
                  <TheoryEditor
                    key={`t-${selected.id}-${section.moduleId}`}
                    courseId={selected.id}
                    moduleId={section.moduleId}
                  />
                ) : (
                  <ProblemsEditor
                    key={`p-${selected.id}-${section.moduleId}`}
                    courseId={selected.id}
                    moduleId={section.moduleId}
                  />
                )}
              </div>
            )}
          </section>
        )}
      </main>
    </div>
  );
}

function SectionCard({ label, desc, active, onClick }) {
  return (
    <button className={"section-card" + (active ? " active" : "")} onClick={onClick}>
      <span className="section-label">{label}</span>
      <span className="section-desc">{desc}</span>
    </button>
  );
}