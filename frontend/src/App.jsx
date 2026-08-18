import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider, useAuth } from "./auth/AuthContext";
import LoginPage from "./pages/LoginPage";
import AdminCoursesPage from "./pages/AdminCoursesPage";

function AdminRoute({ children }) {
  const { user, loading, isAdmin } = useAuth();
  if (loading) return <p style={{ padding: 24 }}>Ucitavanje...</p>;
  if (!user) return <Navigate to="/login" replace />;
  if (!isAdmin) return <Navigate to="/" replace />;
  return children;
}

function Home() {
  const { user, loading } = useAuth();
  if (loading) return null;
  // Admina vodimo ravno na ploču
  if (user?.role === "admin") return <Navigate to="/admin" replace />;
  return (
    <div className="app">
      <div className="glow glow-a" />
      <div className="glow glow-b" />
      <div className="stage">
        <p className="eyebrow">Dobrodošao</p>
        <h1 className="title">e‑Mathos</h1>
        <p className="empty">
          {user ? `Prijavljen kao ${user.username}. ` : ""}
          Ovdje će ići učenje kolegija.
        </p>
        {!user && (
          <a href="/login">
            <button className="solid" style={{ marginTop: "1rem" }}>
              Prijava
            </button>
          </a>
        )}
      </div>
    </div>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<LoginPage />} />
          <Route
            path="/admin"
            element={
              <AdminRoute>
                <AdminCoursesPage />
              </AdminRoute>
            }
          />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}