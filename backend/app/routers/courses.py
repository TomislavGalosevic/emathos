from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..deps import require_admin
from .. import models, schemas

router = APIRouter(prefix="/api/courses", tags=["courses"])


@router.get("", response_model=list[schemas.CourseOut])
def list_courses(db: Session = Depends(get_db)):
    return (
        db.query(models.Course)
        .order_by(models.Course.godina, models.Course.redoslijed)
        .all()
    )


@router.get("/{course_id}", response_model=schemas.CourseStructure)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.get(models.Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Kolegij ne postoji")
    return course


# Alias radi kompatibilnosti s frontendom (courseTree).
@router.get("/{course_id}/tree", response_model=schemas.CourseStructure)
def get_course_tree(course_id: int, db: Session = Depends(get_db)):
    course = db.get(models.Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Kolegij ne postoji")
    return course


@router.post("", response_model=schemas.CourseOut, status_code=201)
def create_course(
    data: schemas.CourseCreate,
    db: Session = Depends(get_db),
    _: models.User = Depends(require_admin),
):
    # Obican kolegij nema module; Teorija/Zadaci su fiksni u sucelju.
    course = models.Course(**data.model_dump())
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


@router.patch("/{course_id}", response_model=schemas.CourseOut)
def update_course(
    course_id: int,
    data: schemas.CourseUpdate,
    db: Session = Depends(get_db),
    _: models.User = Depends(require_admin),
):
    course = db.get(models.Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Kolegij ne postoji")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(course, k, v)
    db.commit()
    db.refresh(course)
    return course


@router.delete("/{course_id}", status_code=204)
def delete_course(
    course_id: int,
    db: Session = Depends(get_db),
    _: models.User = Depends(require_admin),
):
    course = db.get(models.Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Kolegij ne postoji")
    db.delete(course)
    db.commit()