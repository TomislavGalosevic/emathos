import { BrowserRouter, Routes, Route, Navigate, Link } from "react-router-dom";
import { AuthProvider, useAuth } from "./auth/AuthContext";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import AdminCoursesPage from "./pages/AdminCoursesPage";
import LearnPage from "./pages/LearnPage";

function AdminRoute({ children }) {
  const { user, loading, isAdmin } = useAuth();
  if (loading) return <p style={{ padding: 24 }}>Ucitavanje...</p>;
  if (!user) return <Navigate to="/login" replace />;
  if (!isAdmin) return <Navigate to="/" replace />;
  return children;
}

function UserRoute({ children }) {
  const { user, loading } = useAuth();
  if (loading) return <p style={{ padding: 24 }}>Ucitavanje...</p>;
  if (!user) return <Navigate to="/login" replace />;
  return children;
}

function Home() {
  const { user, loading, isAdmin } = useAuth();
  if (loading) return null;
  if (user) return <Navigate to={isAdmin ? "/admin" : "/uci"} replace />;
  return (
    <div className="app">
      <div className="glow glow-a" />
      <div className="glow glow-b" />
      <div className="hero">
        <img className="hero-logo" src="/logo.png" alt="" />
        <p className="eyebrow">Dobrodošao</p>
        <h1 className="hero-title">e‑Mathos</h1>
        <div className="hero-actions">
          <Link to="/login">
            <button className="solid big-btn">Prijava</button>
          </Link>
          <Link to="/register">
            <button className="ghost big-btn">Registracija</button>
          </Link>
        </div>
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
          <Route path="/register" element={<RegisterPage />} />
          <Route
            path="/admin"
            element={
              <AdminRoute>
                <AdminCoursesPage />
              </AdminRoute>
            }
          />
          <Route
            path="/uci"
            element={
              <UserRoute>
                <LearnPage />
              </UserRoute>
            }
          />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}