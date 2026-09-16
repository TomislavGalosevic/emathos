# e-Mathos

Web aplikacija za učenje sveučilišnih matematičkih kolegija — teorija, flash kartice i zadaci s automatskom provjerom odgovora.

**Live demo:** [emathos-1.onrender.com](https://emathos-1.onrender.com)

---

## Tehnologije

| Sloj | Tehnologija |
|------|------------|
| Backend | FastAPI, SQLAlchemy, SQLite |
| Frontend | React, Vite, KaTeX |
| Provjera odgovora | SymPy |
| Autentikacija | JWT (python-jose) |
| Deployment | Render (backend + frontend) |

---

## Lokalno pokretanje

### Preduvjeti
- Python 3.11+
- Node.js 18+

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
python -m app.seed             # kreira bazu, kolegije i uvozi sav sadržaj
uvicorn app.main:app --reload
```

Backend dostupan na `http://localhost:8000`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend dostupan na `http://localhost:5173`.

---

## Inicijalno punjenje baze

`python -m app.seed` radi sve odjednom:

1. Kreira tablice u bazi
2. Dodaje admin korisnika
3. Uvozi sve kolegije
4. Uvozi teoriju (7 kolegija)
5. Uvozi zadatke (11 kolegija)

**Admin kredencijali:** `admin` / `admin123`

---

## Kolegiji i sadržaj

| Kolegij | Teorija | Zadaci |
|---------|---------|--------|
| Diferencijalni račun | ✓ | ✓ |
| Integralni račun | ✓ | ✓ |
| Linearna algebra I | ✓ | ✓ |
| Linearna algebra II | ✓ | ✓ |
| Vektorski prostori | ✓ | ✓ |
| Obične diferencijalne jednadžbe | ✓ | ✓ |
| Numerička matematika | ✓ | ✓ |
| Primijenjena matematika — Teorija brojeva i kombinatorika | — | ✓ |
| Primijenjena matematika — Vjerojatnost | — | ✓ |
| Primijenjena matematika — Funkcije više varijabli | — | ✓ |
| Primjena diferencijalnog i integralnog računa | — | ✓ |

---

## Tipovi zadataka

| Tip | Opis |
|-----|------|
| `auto` | Jedan unos, provjera via SymPy (podržava razlomke, `e^x`, `ln`, decimalne zareze…) |
| `multi` | Više labelled polja, svako SymPy-provjereno |
| `matrix` | Odabir dimenzija + grid unos za matrice |
| `choice` | Klik na jednu od ponuđenih opcija |
| `point` | Koordinatni unos `T( x , y )` |

---

## Struktura projekta

```
emathos/
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI app, CORS, routeri
│   │   ├── models.py             # SQLAlchemy modeli
│   │   ├── schemas.py            # Pydantic sheme
│   │   ├── checker.py            # SymPy provjera odgovora
│   │   ├── seed.py               # Inicijalno punjenje baze
│   │   ├── routers/
│   │   │   ├── auth.py
│   │   │   ├── courses.py
│   │   │   └── content.py
│   │   ├── import_theory_*.py    # Uvoz teorijskog sadržaja
│   │   └── import_zadaci_*.py    # Uvoz zadataka
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── api/client.js         # API klijent
│   │   ├── auth/AuthContext.jsx  # Auth (sessionStorage)
│   │   ├── components/           # SolveProblems, TheoryViewer…
│   │   └── pages/
│   └── vite.config.js
├── render.yaml                   # Render deployment config
└── README.md
```

---

## Deployment (Render)

Backend (`emathos`) i frontend (`emathos-1`) deployjaju se automatski pri svakom pushu na `main`.

| | Backend | Frontend |
|-|---------|----------|
| Runtime | Python 3 | Static |
| Build | `pip install -r backend/requirements.txt && cd backend && python -m app.seed` |  `npm run build` |
| Start | `uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT` | — |

**Environment varijable (backend):**

| Varijabla | Opis |
|-----------|------|
| `SECRET_KEY` | JWT tajni ključ (auto-generiraj u Renderu) |
| `ADMIN_USERNAME` | Admin korisničko ime (default: `admin`) |
| `ADMIN_PASSWORD` | Admin lozinka (default: `admin123`) |

---

## Napomene

- Sesija traje dok je browser tab otvoren; zatvaranjem taba/prozora korisnik se automatski odjavljuje (sessionStorage)
- SymPy checker prihvaća različite notacije: `e^x` = `exp(x)`, `ln(x)` = `log(x)`, decimalne zareze (`3,14`), mjerne jedinice na kraju (`83.97 min`), `y=...` prefiks
- SQLite baza se recreira pri svakom Render deploymentu — svi podaci dolaze iz seed skripti
