

from .database import Base, engine, SessionLocal
from .config import settings
from .security import hash_password
from . import models

# kolegiji
COURSES = [
    (1, "Diferencijalni racun", []),
    (1, "Integralni racun", []),
    (1, "Linearna algebra I", []),
    (1, "Linearna algebra II", []),
    (
        2,
        "Primijenjena matematika za racunalnu znanost",
        ["Teorija brojeva i kombinatorika", "Vjerojatnost", "Funkcije vise varijabli"],
    ),
    (2, "Primjena diferencijalnog i integralnog racuna", []),
    (2, "Vektorski prostori", []),
    (3, "Numericka matematika", []),
    (3, "Obicne diferencijalne jednadzbe", []),
]


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        admin = (
            db.query(models.User)
            .filter(models.User.username == settings.admin_username)
            .first()
        )
        if not admin:
            db.add(models.User(
                username=settings.admin_username,
                email=settings.admin_email,
                password_hash=hash_password(settings.admin_password),
                role="admin",
            ))
            print(f"[+] Admin: {settings.admin_username} / {settings.admin_password}")
        else:
            print("[=] Admin vec postoji.")

        for redoslijed, (godina, naziv, podrucja) in enumerate(COURSES):
            if db.query(models.Course).filter(models.Course.naziv == naziv).first():
                print(f"[=] Vec postoji: {naziv}")
                continue
            course = models.Course(naziv=naziv, godina=godina, redoslijed=redoslijed)
            db.add(course)
            db.flush()
            for i, p in enumerate(podrucja):
                db.add(models.Module(course_id=course.id, naziv=p, redoslijed=i))
            oznaka = f"{len(podrucja)} podrucja" if podrucja else "bez podrucja"
            print(f"[+] Kolegij: {naziv} ({oznaka})")

        db.commit()
        print("\nGotovo.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()