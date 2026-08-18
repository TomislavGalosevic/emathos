import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../auth/AuthContext";

export default function LoginPage() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [info, setInfo] = useState("");

  useEffect(() => {
    if (localStorage.getItem("idleLogout")) {
      setInfo("Odjavljeni ste zbog neaktivnosti (10 min). Prijavite se ponovno.");
      localStorage.removeItem("idleLogout");
    }
  }, []);

  async function handleSubmit() {
    setError("");
    try {
      const user = await login(username, password);
      navigate(user.role === "admin" ? "/admin" : "/");
    } catch (e) {
      setError(e.message);
    }
  }

  return (
    <div className="card" style={{ maxWidth: 360, margin: "4rem auto" }}>
      <h2>Prijava</h2>
      {info && <p className="info">{info}</p>}
      <label>Korisnicko ime</label>
      <input value={username} onChange={(e) => setUsername(e.target.value)} />
      <label>Lozinka</label>
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
      />
      {error && <p className="error">{error}</p>}
      <button onClick={handleSubmit}>Prijavi se</button>
      <p className="hint">Test admin: admin / admin123</p>
    </div>
  );
}