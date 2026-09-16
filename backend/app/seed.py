"""Pocetno punjenje baze: admin + popis kolegija.

Pokretanje (iz mape backend/):  python -m app.seed
Idempotentno: ne duplira kolegije koji vec postoje.

Struktura:
  - obicni kolegiji nemaju module (Teorija/Zadaci su fiksni u sucelju)
  - Primijenjena matematika ima 3 fiksna podrucja (module)
"""

from .database import Base, engine, SessionLocal
from .config import settings
from .security import hash_password
from . import models

# (godina, naziv, [podrucja]) — podrucja SAMO za Primijenjenu
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

    print("\n--- Teorija ---")
    from .import_theory_dif_racun        import run as run_th_dif;  run_th_dif()
    from .import_theory_int_racun        import run as run_th_int;  run_th_int()
    from .import_theory_lin_alg_1        import run as run_th_la1;  run_th_la1()
    from .import_theory_lin_alg_2        import run as run_th_la2;  run_th_la2()
    from .import_theory_vektorski_prostori import run as run_th_vp; run_th_vp()
    from .import_theory_numericka        import run as run_th_num;  run_th_num()
    from .import_theory_odj              import run as run_th_odj;  run_th_odj()

    print("\n--- Zadaci ---")
    from .import_zadaci_diff       import run as run_zd_diff;  run_zd_diff()
    from .import_zadaci_int        import run as run_zd_int;   run_zd_int()
    from .import_zadaci_la1        import run as run_zd_la1;   run_zd_la1()
    from .import_zadaci_la2        import run as run_zd_la2;   run_zd_la2()
    from .import_zadaci_tbik       import run as run_zd_tbik;  run_zd_tbik()
    from .import_zadaci_vjerojatnost import run as run_zd_vj;  run_zd_vj()
    from .import_zadaci_fvv        import run as run_zd_fvv;   run_zd_fvv()
    from .import_zadaci_numericka  import run as run_zd_num;   run_zd_num()
    from .import_zadaci_odj        import run as run_zd_odj;   run_zd_odj()
    from .import_zadaci_pdir       import run as run_zd_pdir;  run_zd_pdir()
    from .import_zadaci_vp         import run as run_zd_vp;    run_zd_vp()

    print("\nSve gotovo.")