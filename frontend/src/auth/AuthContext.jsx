// @refresh reset
import { createContext, useContext, useEffect, useState, useCallback } from "react";
import { api } from "../api/client";

const AuthContext = createContext(null);

// sessionStorage — briše se kada korisnik zatvori tab/prozor (za razliku od localStorage)
const storage = sessionStorage;

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  const logout = useCallback(() => {
    storage.removeItem("token");
    setUser(null);
  }, []);

  // Pocetno ucitavanje: token postoji samo dok je tab otvoren
  useEffect(() => {
    const token = storage.getItem("token");
    if (!token) {
      setLoading(false);
      return;
    }
    api
      .me()
      .then((u) => setUser(u))
      .catch(() => logout())
      .finally(() => setLoading(false));
  }, [logout]);

  async function login(username, password) {
    const data = await api.login(username, password);
    storage.setItem("token", data.access_token);
    setUser(data.user);
    return data.user;
  }

  const value = { user, loading, login, logout, isAdmin: user?.role === "admin" };
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  return useContext(AuthContext);
}
