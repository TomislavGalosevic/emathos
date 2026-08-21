"""Teorija i Zadaci.

Oboje se vjesa na kolegij (course_id) i, ako kolegij ima podrucja
(trenutno samo Primijenjena matematika), na konkretno podrucje (module_id).
Za obicne kolegije module_id je uvijek NULL.

Citanje je javno (za ucenje); pisanje samo admin.
Provjera odgovora i pracenje napretka zahtijevaju prijavu (bilo koji korisnik).
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, selectinload

from ..database import get_db
from ..deps import require_admin, get_current_user
from ..checker import check_answer
from .. import models, schemas

router = APIRouter(prefix="/api", tags=["content"])


# ---------------------------------------------------------------------------
# Zadaci (Problem + Hint)
# ---------------------------------------------------------------------------
@router.get("/problems", response_model=list[schemas.ProblemOut])
def list_problems(
    course_id: int,
    module_id: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    q = (
        db.query(models.Problem)
        .options(selectinload(models.Problem.hints))
        .filter(models.Problem.course_id == course_id)
    )
    if module_id is not None:
        q = q.filter(models.Problem.module_id == module_id)
    else:
        q = q.filter(models.Problem.module_id.is_(None))
    return q.order_by(models.Problem.redoslijed).all()


@router.post("/problems", response_model=schemas.ProblemOut, status_code=201)
def create_problem(
    data: schemas.ProblemCreate,
    db: Session = Depends(get_db),
    _: models.User = Depends(require_admin),
):
    if not db.get(models.Course, data.course_id):
        raise HTTPException(status_code=404, detail="Kolegij ne postoji")
    if data.module_id is not None and not db.get(models.Module, data.module_id):
        raise HTTPException(status_code=404, detail="Podrucje ne postoji")

    payload = data.model_dump(exclude={"hints"})
    problem = models.Problem(**payload)
    for i, tekst in enumerate(data.hints):
        problem.hints.append(models.Hint(sadrzaj=tekst, redoslijed=i))
    db.add(problem)
    db.commit()
    db.refresh(problem)
    return problem


@router.patch("/problems/{problem_id}", response_model=schemas.ProblemOut)
def update_problem(
    problem_id: int,
    data: schemas.ProblemUpdate,
    db: Session = Depends(get_db),
    _: models.User = Depends(require_admin),
):
    problem = db.get(models.Problem, problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Zadatak ne postoji")

    changes = data.model_dump(exclude_unset=True, exclude={"hints"})
    for k, v in changes.items():
        setattr(problem, k, v)

    if data.hints is not None:
        problem.hints.clear()
        for i, tekst in enumerate(data.hints):
            problem.hints.append(models.Hint(sadrzaj=tekst, redoslijed=i))

    db.commit()
    db.refresh(problem)
    return problem


@router.delete("/problems/{problem_id}", status_code=204)
def delete_problem(
    problem_id: int,
    db: Session = Depends(get_db),
    _: models.User = Depends(require_admin),
):
    problem = db.get(models.Problem, problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Zadatak ne postoji")
    db.delete(problem)
    db.commit()


@router.post("/problems/{problem_id}/check", response_model=schemas.AnswerCheckResponse)
def check_problem_answer(
    problem_id: int,
    data: schemas.AnswerCheckRequest,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Provjerava korisnikov odgovor preko SymPy i azurira njegov napredak."""
    problem = db.get(models.Problem, problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Zadatak ne postoji")

    tocno = check_answer(data.odgovor, problem.tocan_odgovor)

    progress = (
        db.query(models.Progress)
        .filter(
            models.Progress.user_id == current_user.id,
            models.Progress.kind == "problem",
            models.Progress.item_id == problem_id,
        )
        .first()
    )
    if not progress:
        progress = models.Progress(
            user_id=current_user.id, kind="problem", item_id=problem_id, broj_pokusaja=0
        )
        db.add(progress)

    progress.broj_pokusaja += 1
    if tocno:
        progress.status = "solved"
    db.commit()

    return {"tocno": tocno}


# ---------------------------------------------------------------------------
# Teorija (TheoryItem)
# ---------------------------------------------------------------------------
@router.get("/theory", response_model=list[schemas.TheoryItemOut])
def list_theory(
    course_id: int,
    module_id: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    q = db.query(models.TheoryItem).filter(models.TheoryItem.course_id == course_id)
    if module_id is not None:
        q = q.filter(models.TheoryItem.module_id == module_id)
    else:
        q = q.filter(models.TheoryItem.module_id.is_(None))
    return q.order_by(models.TheoryItem.redoslijed).all()


@router.post("/theory", response_model=schemas.TheoryItemOut, status_code=201)
def create_theory(
    data: schemas.TheoryItemCreate,
    db: Session = Depends(get_db),
    _: models.User = Depends(require_admin),
):
    if not db.get(models.Course, data.course_id):
        raise HTTPException(status_code=404, detail="Kolegij ne postoji")
    if data.module_id is not None and not db.get(models.Module, data.module_id):
        raise HTTPException(status_code=404, detail="Podrucje ne postoji")

    item = models.TheoryItem(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.patch("/theory/{item_id}", response_model=schemas.TheoryItemOut)
def update_theory(
    item_id: int,
    data: schemas.TheoryItemUpdate,
    db: Session = Depends(get_db),
    _: models.User = Depends(require_admin),
):
    item = db.get(models.TheoryItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Stavka teorije ne postoji")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(item, k, v)
    db.commit()
    db.refresh(item)
    return item


@router.delete("/theory/{item_id}", status_code=204)
def delete_theory(
    item_id: int,
    db: Session = Depends(get_db),
    _: models.User = Depends(require_admin),
):
    item = db.get(models.TheoryItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Stavka teorije ne postoji")
    db.delete(item)
    db.commit()


@router.post("/theory/{item_id}/mark", response_model=schemas.ProgressOut)
def mark_theory_seen(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Oznaci da je korisnik svladao stavku teorije."""
    item = db.get(models.TheoryItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Stavka teorije ne postoji")

    progress = (
        db.query(models.Progress)
        .filter(
            models.Progress.user_id == current_user.id,
            models.Progress.kind == "theory",
            models.Progress.item_id == item_id,
        )
        .first()
    )
    if not progress:
        progress = models.Progress(
            user_id=current_user.id, kind="theory", item_id=item_id, broj_pokusaja=0
        )
        db.add(progress)
    progress.broj_pokusaja += 1
    progress.status = "solved"
    db.commit()
    db.refresh(progress)
    return progress


# ---------------------------------------------------------------------------
# Napredak (bilo koji ulogirani korisnik)
# ---------------------------------------------------------------------------
@router.get("/progress", response_model=list[schemas.ProgressOut])
def my_progress(
    kind: str | None = Query(default=None),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Napredak trenutnog korisnika. kind: 'problem' ili 'theory' (opcionalno filtrira)."""
    q = db.query(models.Progress).filter(models.Progress.user_id == current_user.id)
    if kind:
        q = q.filter(models.Progress.kind == kind)
    return q.all()