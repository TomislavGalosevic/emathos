from .database import SessionLocal
from . import models

def run():
    db = SessionLocal()
    valid_ids = set(p.id for p in db.query(models.Problem).all())
    orphans = db.query(models.Progress).filter(
        models.Progress.kind == "problem",
        ~models.Progress.item_id.in_(valid_ids)
    ).all()
    print(f"Brisem {len(orphans)} orphan zapisa")
    for o in orphans:
        db.delete(o)
    db.commit()
    db.close()

if __name__ == "__main__":
    run()