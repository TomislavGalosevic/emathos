import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { api } from "../api/client";
import { useAuth } from "../auth/AuthContext";

export default function RegisterPage() {
  const navigate = useNavigate();
  const { login } = useAuth();
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [saving, setSaving] = useState(false);

  async function handleSubmit() {
    setError("");
    if (!username.trim() || !email.trim() || password.length < 6) {
      setError("Ispuni sva polja (lozinka barem 6 znakova).");
      return;
    }
    setSaving(true);
    try {
      await api.register(username, email, password);
      await login(username, password);
      navigate("/uci");
    } catch (e) {
      setError(e.message);
    } finally {
      setSaving(false);
    }
  }

  return (
    <div className="login-wrap">
      <Link to="/" className="back-link">← Natrag na početnu</Link>
      <div className="card">
        <h2>Registracija</h2>
        <label>Korisnicko ime</label>
        <input value={username} onChange={(e) => setUsername(e.target.value)} />
        <label>Email</label>
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <label>Lozinka</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
        />
        {error && <p className="error">{error}</p>}
        <button onClick={handleSubmit} disabled={saving}>
          {saving ? "Stvaranje računa…" : "Registriraj se"}
        </button>
        <p className="hint">
          Već imaš račun? <Link to="/login">Prijavi se</Link>
        </p>
      </div>
    </div>
  );
}