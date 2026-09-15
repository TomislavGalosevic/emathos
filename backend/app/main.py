from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import auth, courses, content

Base.metadata.create_all(bind=engine)

app = FastAPI(title="e-Mathos API", version="0.3.0")

# Popis dozvoljenih domena (ispravljen sintaksni zarez i dodani lokalni portovi)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "https://emathos-frontend.onrender.com",
    "https://emathos-1.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=r"https://.*\.onrender\.com",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(content.router)


@app.get("/api/health")
def health():
    return {"status": "ok"}