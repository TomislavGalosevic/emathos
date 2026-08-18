from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    JSON,
    DateTime,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import relationship

from .database import Base


# ---------------------------------------------------------------------------
# Korisnici
# ---------------------------------------------------------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default="user", nullable=False)  # "user" | "admin"
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    progress = relationship("Progress", back_populates="user", cascade="all, delete-orphan")


# ---------------------------------------------------------------------------
# Sadrzaj
#   Obican kolegij:            Kolegij -> (Teorija, Zadaci)
#   Primijenjena matematika:   Kolegij -> 3 podrucja (Module) -> (Teorija, Zadaci)
#
# "Teorija" i "Zadaci" nisu zasebne tablice nego dva tipa sadrzaja:
#   Teorija = TheoryItem zapisi, Zadaci = Problem zapisi.
# Sadrzaj se vjesa na kolegij (module_id = NULL) ili na podrucje (module_id).
# ---------------------------------------------------------------------------
class Course(Base):
    """Kolegij, npr. 'Realna analiza'."""

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    naziv = Column(String, nullable=False)
    opis = Column(Text, default="")
    godina = Column(Integer, default=1)  # godina studija (1/2/3)
    redoslijed = Column(Integer, default=0)

    modules = relationship(
        "Module",
        back_populates="course",
        cascade="all, delete-orphan",
        order_by="Module.redoslijed",
    )


class Module(Base):
    """Podrucje unutar kolegija. Koristi se SAMO za Primijenjenu matematiku
    (Teorija brojeva i kombinatorika, Vjerojatnost, Funkcije vise varijabli).
    Obicni kolegiji nemaju module."""

    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    naziv = Column(String, nullable=False)
    redoslijed = Column(Integer, default=0)

    course = relationship("Course", back_populates="modules")


class TheoryItem(Base):
    """Stavka teorije (flashcard, T/N, MCQ, nadopuni, ...).

    Vjesa se na kolegij (module_id=NULL) ili na podrucje Primijenjene (module_id).
    """

    __tablename__ = "theory_items"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    module_id = Column(Integer, ForeignKey("modules.id", ondelete="CASCADE"), nullable=True)
    tip = Column(String, nullable=False)
    sadrzaj = Column(JSON, nullable=False)
    redoslijed = Column(Integer, default=0)


class Problem(Base):
    """Zadatak. tip: 'auto' (SymPy/broj provjera) ili 'self' (samoprocjena).

    Vjesa se na kolegij (module_id=NULL) ili na podrucje Primijenjene (module_id).
    """

    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    module_id = Column(Integer, ForeignKey("modules.id", ondelete="CASCADE"), nullable=True)
    tekst = Column(Text, nullable=False)
    tip = Column(String, default="auto", nullable=False)
    tocan_odgovor = Column(Text, default="")
    rjesenje = Column(Text, default="")
    redoslijed = Column(Integer, default=0)

    hints = relationship(
        "Hint",
        back_populates="problem",
        cascade="all, delete-orphan",
        order_by="Hint.redoslijed",
    )


class Hint(Base):
    __tablename__ = "hints"

    id = Column(Integer, primary_key=True, index=True)
    problem_id = Column(Integer, ForeignKey("problems.id", ondelete="CASCADE"), nullable=False)
    redoslijed = Column(Integer, default=0)
    sadrzaj = Column(Text, nullable=False)

    problem = relationship("Problem", back_populates="hints")


# ---------------------------------------------------------------------------
# Pracenje napretka
# ---------------------------------------------------------------------------
class Progress(Base):
    __tablename__ = "progress"
    __table_args__ = (
        UniqueConstraint("user_id", "kind", "item_id", name="uq_progress_item"),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    kind = Column(String, nullable=False)  # "theory" | "problem"
    item_id = Column(Integer, nullable=False)
    status = Column(String, default="in_progress")
    broj_pokusaja = Column(Integer, default=0)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="progress")