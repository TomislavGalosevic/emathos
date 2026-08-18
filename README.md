# e-Mathos

Web aplikacija za praćenje i učenje matematičkih kolegija.
Backend: FastAPI + SQLAlchemy + SQLite + SymPy. Frontend: React + Vite.

## Struktura sadržaja
Kolegij → Modul → Cjelina → (Teorija / Zadaci)
Običan kolegij ima jedan modul ("Osnovno"); "Primijenjena matematika"
ima tri modula. Frontend može preskočiti odabir modula kad ga je samo jedan.

## Pokretanje — backend
```
cd backend
python -m venv venv && source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
cp .env.example .env        # po želji promijeni SECRET_KEY / admin lozinku
python -m app.seed          # kreira admina + popis kolegija
uvicorn app.main:app --reload
```
API: http://localhost:8000  ·  Swagger dokumentacija: http://localhost:8000/docs
Test admin: **admin / admin123**

## Pokretanje — frontend
```
cd frontend
cp .env.example .env
npm install
npm run dev
```
Aplikacija: http://localhost:5173  ·  Admin sučelje: /admin

## Što je gotovo (kostur)
- Auth s JWT-om i rolama user/admin (register, login, me)
- Zaštita ruta: pisanje sadržaja smije samo admin (403 za usera, 401 za anon)
- CRUD za Kolegije, Module, Cjeline + /tree endpoint (ugniježđeno stablo)
- Seed s tvojim popisom kolegija (1.–3. godina)
- Frontend: AuthContext, login, zaštićena admin stranica s prikazom stabla
  i formama za dodavanje kolegija/cjelina

## Sljedeći koraci (redoslijed)
1. KaTeX render + Quill unos formula
2. Model + CRUD za teoriju (flashcard, T/N, MCQ, multi, fillin, match, order)
3. Zadaci + provjera odgovora (broj u rečenicu + SymPy za izraze) + hintovi
4. Praćenje napretka korisnika
5. Dizajn i deploy (Render + Vercel)
