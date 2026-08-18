const BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";

function getToken() {
  return localStorage.getItem("token");
}

async function request(path, { method = "GET", body, form, auth = true } = {}) {
  const headers = {};
  if (auth && getToken()) headers["Authorization"] = `Bearer ${getToken()}`;

  let payload;
  if (form) {
    payload = new URLSearchParams(form).toString();
    headers["Content-Type"] = "application/x-www-form-urlencoded";
  } else if (body !== undefined) {
    payload = JSON.stringify(body);
    headers["Content-Type"] = "application/json";
  }

  const res = await fetch(`${BASE}${path}`, { method, headers, body: payload });

  if (!res.ok) {
    let detail = `Greska ${res.status}`;
    try {
      detail = (await res.json()).detail || detail;
    } catch (_) {}
    throw new Error(detail);
  }
  if (res.status === 204) return null;
  return res.json();
}

export const api = {
  // auth
  login: (username, password) =>
    request("/api/auth/login", { method: "POST", form: { username, password }, auth: false }),
  register: (username, email, password) =>
    request("/api/auth/register", { method: "POST", body: { username, email, password }, auth: false }),
  me: () => request("/api/auth/me"),

  // courses
  listCourses: () => request("/api/courses", { auth: false }),
  courseTree: (id) => request(`/api/courses/${id}/tree`, { auth: false }),
  createCourse: (data) => request("/api/courses", { method: "POST", body: data }),
  deleteCourse: (id) => request(`/api/courses/${id}`, { method: "DELETE" }),
};