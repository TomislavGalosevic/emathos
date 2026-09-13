import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api/client";
import { useAuth } from "../auth/AuthContext";
import StudyTheory from "../components/StudyTheory";
import SolveProblems from "../components/SolveProblems";

const YEARS = [
  { n: 1, rimski: "I", rijec: "Prva godina" },
  { n: 2, rimski: "II", rijec: "Druga godina" },
  { n: 3, rimski: "III", rijec: "Treća godina" },
];

const NO_THEORY_COURSES = [
  "Primijenjena matematika za racunalnu znanost",
  "Primjena diferencijalnog i integralnog racuna",
];

function aggregatePercent(areas) {
  const total = areas.reduce((s, a) => s + a.teorija_ukupno + a.zadaci_ukupno, 0);
  const solved = areas.reduce((s, a) => s + a.teorija_rijeseno + a.zadaci_rijeseno, 0);
  if (total === 0) return null;
  return Math.round((solved / total) * 100);
}

export default function LearnPage() {
  const { user, logout } = useAuth();
  const [view, setView] = useState("years");
  const [year, setYear] = useState(null);
  const [courses, setCourses] = useState([]);
  const [courseProgress, setCourseProgress] = useState({});
  const [selected, setSelected] = useState(null);
  const [areaProgress, setAreaProgress] = useState(null);
  const [section, setSection] = useState(null);

  useEffect(() => {
    api.listCourses().then(setCourses);
  }, []);

  function openYear(y) {
    setYear(y);
    setView("subjects");
    const yearCourses = courses.filter((c) => c.godina === y);
    Promise.all(
      yearCourses.map((c) =>
        api
          .courseProgress(c.id)
          .then((r) => [c.id, aggregatePercent(r.areas)])
          .catch(() => [c.id, null])
      )
    ).then((pairs) => {
      setCourseProgress((prev) => ({ ...prev, ...Object.fromEntries(pairs) }));
    });
  }

  function refreshAreaProgress() {
    if (selected) {
      api.courseProgress(selected.id).then((r) => setAreaProgress(r.areas));
    }
  }

  async function openCourse(id) {
    const tree = await api.courseTree(id);
    setSelected(tree);
    setSection(null);
    setView("course");
    api.courseProgress(id).then((r) => setAreaProgress(r.areas));
  }

  const coursesInYear = courses.filter((c) => c.godina === year);
  const areas =
    selected && selected.modules.length > 0
      ? selected.modules
      : [{ id: null, naziv: null }];
  const hideTheory = selected && NO_THEORY_COURSES.includes(selected.naziv);

  function findAreaProgress(moduleId) {
    return areaProgress?.find((a) => a.module_id === moduleId) || null;
  }

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
              {coursesInYear.map((c, i) => {
                const pct = courseProgress[c.id];
                return (
                  <div className="hex-wrap pop" style={{ "--d": `${i * 60}ms` }} key={c.id}>
                    <button className="hex" onClick={() => openCourse(c.id)}>
                      <span className="hex-inner">
                        <span className="hex-title">{c.naziv}</span>
                        {pct !== null && pct !== undefined && (
                          <span className="hex-progress">
                            <span className="hex-progress-bar">
                              <span className="hex-progress-fill" style={{ width: `${pct}%` }} />
                            </span>
                            <span className="hex-progress-label">{pct}%</span>
                          </span>
                        )}
                      </span>
                    </button>
                  </div>
                );
              })}
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

            {areas.map((area) => {
              const ap = findAreaProgress(area.id);
              return (
                <div className="area" key={area.id ?? "root"}>
                  {area.naziv && <h2 className="area-title">{area.naziv}</h2>}
                  <div className="section-cards">
                    {!hideTheory && (
                      <SectionCard
                        label="Teorija"
                        desc={
                          ap
                            ? `${ap.teorija_rijeseno}/${ap.teorija_ukupno} svladano`
                            : "Uči kroz kartice i pitanja"
                        }
                        active={section?.kind === "teorija" && section?.moduleId === area.id}
                        onClick={() => setSection({ kind: "teorija", moduleId: area.id })}
                      />
                    )}
                    <SectionCard
                      label="Zadaci"
                      desc={
                        ap
                          ? `${ap.zadaci_rijeseno}/${ap.zadaci_ukupno} riješeno`
                          : "Riješi zadatke uz hintove"
                      }
                      active={section?.kind === "zadaci" && section?.moduleId === area.id}
                      onClick={() => setSection({ kind: "zadaci", moduleId: area.id })}
                    />
                  </div>
                </div>
              );
            })}

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
                    onProgressChange={refreshAreaProgress}
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