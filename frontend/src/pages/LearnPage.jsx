import { useEffect, useState } from "react";
import { api } from "../api/client";
import { useAuth } from "../auth/AuthContext";
import StudyTheory from "../components/StudyTheory";
import SolveProblems from "../components/SolveProblems";

const YEARS = [
  { n: 1, rimski: "I", rijec: "Prva godina" },
  { n: 2, rimski: "II", rijec: "Druga godina" },
  { n: 3, rimski: "III", rijec: "Treća godina" },
];

export default function LearnPage() {
  const { user, logout } = useAuth();
  const [view, setView] = useState("years");
  const [year, setYear] = useState(null);
  const [courses, setCourses] = useState([]);
  const [selected, setSelected] = useState(null);
  const [section, setSection] = useState(null);

  useEffect(() => {
    api.listCourses().then(setCourses);
  }, []);

  function openYear(y) {
    setYear(y);
    setView("subjects");
  }
  async function openCourse(id) {
    setSelected(await api.courseTree(id));
    setSection(null);
    setView("course");
  }

  const coursesInYear = courses.filter((c) => c.godina === year);
  const areas =
    selected && selected.modules.length > 0
      ? selected.modules
      : [{ id: null, naziv: null }];

  return (
    <div className="app">
      <div className="glow glow-a" />
      <div className="glow glow-b" />

      <header className="topbar">
        <span className="brand">
          <img className="logo" src="/logo.png" alt="" />
          e‑Mathos
        </span>
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
            <p className="eyebrow">Učenje</p>
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
                </div>
              ))}
              {coursesInYear.length === 0 && (
                <p className="empty">Za ovu godinu još nema kolegija.</p>
              )}
            </div>
          </section>
        )}

        {view === "course" && selected && (
          <section className="fade">
            <button className="back" onClick={() => setView("subjects")}>
              ← {YEARS.find((y) => y.n === year)?.rijec}
            </button>
            <h1 className="title">{selected.naziv}</h1>

            {areas.map((area) => (
              <div className="area" key={area.id ?? "root"}>
                {area.naziv && <h2 className="area-title">{area.naziv}</h2>}
                <div className="section-cards">
                  <SectionCard
                    label="Teorija"
                    desc="Uči kroz kartice i pitanja"
                    active={section?.kind === "teorija" && section?.moduleId === area.id}
                    onClick={() =>
                      setSection({ kind: "teorija", moduleId: area.id })
                    }
                  />
                  <SectionCard
                    label="Zadaci"
                    desc="Riješi zadatke uz hintove"
                    active={section?.kind === "zadaci" && section?.moduleId === area.id}
                    onClick={() =>
                      setSection({ kind: "zadaci", moduleId: area.id })
                    }
                  />
                </div>
              </div>
            ))}

            {section && (
              <div className="section-detail">
                {section.kind === "teorija" ? (
                  <StudyTheory
                    key={`t-${selected.id}-${section.moduleId}`}
                    courseId={selected.id}
                    moduleId={section.moduleId}
                  />
                ) : (
                  <SolveProblems
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