import { createContext, useContext, useEffect, useRef, useState, useCallback } from "react";
import { api } from "../api/client";

const AuthContext = createContext(null);
const IDLE_LIMIT = 10 * 60 * 1000; // 10 minuta neaktivnosti

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  const logout = useCallback((reason) => {
    localStorage.removeItem("token");
    localStorage.removeItem("lastActivity");
    if (reason === "idle") localStorage.setItem("idleLogout", "1");
    setUser(null);
  }, []);

  // Pocetno ucitavanje: ako je token istekao ILI je proslo >10 min neaktivnosti -> odjava
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      setLoading(false);
      return;
    }
    const last = Number(localStorage.getItem("lastActivity") || 0);
    if (last && Date.now() - last > IDLE_LIMIT) {
      logout("idle");
      setLoading(false);
      return;
    }
    api
      .me()
      .then((u) => {
        setUser(u);
        localStorage.setItem("lastActivity", String(Date.now()));
      })
      .catch(() => logout())
      .finally(() => setLoading(false));
  }, [logout]);

  // Pracenje aktivnosti dok je korisnik prijavljen
  const lastBump = useRef(0);
  useEffect(() => {
    if (!user) return;

    const bump = () => {
      const now = Date.now();
      if (now - lastBump.current > 5000) {
        lastBump.current = now;
        localStorage.setItem("lastActivity", String(now));
      }
    };
    bump();

    const events = ["mousemove", "mousedown", "keydown", "scroll", "touchstart", "click"];
    events.forEach((e) => window.addEventListener(e, bump, { passive: true }));

    const iv = setInterval(() => {
      const last = Number(localStorage.getItem("lastActivity") || 0);
      if (Date.now() - last > IDLE_LIMIT) logout("idle");
    }, 15000); // provjera svakih 15 s

    return () => {
      events.forEach((e) => window.removeEventListener(e, bump));
      clearInterval(iv);
    };
  }, [user, logout]);

  async function login(username, password) {
    const data = await api.login(username, password);
    localStorage.setItem("token", data.access_token);
    localStorage.setItem("lastActivity", String(Date.now()));
    localStorage.removeItem("idleLogout");
    setUser(data.user);
    return data.user;
  }

  const value = { user, loading, login, logout, isAdmin: user?.role === "admin" };
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  return useContext(AuthContext);
}