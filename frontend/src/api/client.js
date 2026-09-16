const isLocal = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1";
const BASE = (import.meta.env.VITE_API_URL || (isLocal ? "http://localhost:8000" : "https://emathos.onrender.com")).replace(/\/$/, "");

function getToken() {
  return sessionStorage.getItem("token");
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

function qs(params) {
  const usp = new URLSearchParams();
  Object.entries(params).forEach(([k, v]) => {
    if (v !== null && v !== undefined) usp.set(k, v);
  });
  const s = usp.toString();
  return s ? `?${s}` : "";
}

export const api = {
  login: (username, password) =>
    request("/api/auth/login", { method: "POST", form: { username, password }, auth: false }),
  register: (username, email, password) =>
    request("/api/auth/register", { method: "POST", body: { username, email, password }, auth: false }),
  me: () => request("/api/auth/me"),

  listCourses: () => request("/api/courses", { auth: false }),
  courseTree: (id) => request(`/api/courses/${id}/tree`, { auth: false }),
  createCourse: (data) => request("/api/courses", { method: "POST", body: data }),
  deleteCourse: (id) => request(`/api/courses/${id}`, { method: "DELETE" }),

  listProblems: (courseId, moduleId) =>
    request(`/api/problems${qs({ course_id: courseId, module_id: moduleId })}`, { auth: false }),
  createProblem: (data) => request("/api/problems", { method: "POST", body: data }),
  updateProblem: (id, data) => request(`/api/problems/${id}`, { method: "PATCH", body: data }),
  deleteProblem: (id) => request(`/api/problems/${id}`, { method: "DELETE" }),
  checkProblem: (id, odgovor) =>
    request(`/api/problems/${id}/check`, { method: "POST", body: { odgovor } }),
  markProblemSeen: (id) =>
    request(`/api/problems/${id}/seen`, { method: "POST" }),

  listTheory: (courseId, moduleId) =>
    request(`/api/theory${qs({ course_id: courseId, module_id: moduleId })}`, { auth: false }),
  createTheory: (data) => request("/api/theory", { method: "POST", body: data }),
  updateTheory: (id, data) => request(`/api/theory/${id}`, { method: "PATCH", body: data }),
  deleteTheory: (id) => request(`/api/theory/${id}`, { method: "DELETE" }),
  markTheorySeen: (id, tocno = true) =>
    request(`/api/theory/${id}/mark`, { method: "POST", body: { tocno } }),

  myProgress: (kind) => request(`/api/progress${qs({ kind })}`),
  courseProgress: (courseId) => request(`/api/courses/${courseId}/progress`),
};