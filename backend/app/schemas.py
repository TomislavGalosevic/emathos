from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict


# ---------------------------------------------------------------------------
# Auth / User
# ---------------------------------------------------------------------------
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut


class LoginRequest(BaseModel):
    username: str
    password: str


# ---------------------------------------------------------------------------
# Course / Module
# ---------------------------------------------------------------------------
class CourseBase(BaseModel):
    naziv: str
    opis: str = ""
    godina: int = 1
    redoslijed: int = 0


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    naziv: Optional[str] = None
    opis: Optional[str] = None
    godina: Optional[int] = None
    redoslijed: Optional[int] = None


class CourseOut(CourseBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ModuleOut(BaseModel):
    id: int
    course_id: int
    naziv: str
    redoslijed: int = 0
    model_config = ConfigDict(from_attributes=True)


# Struktura kolegija: kolegij + eventualna podrucja (moduli).
# Obican kolegij ima modules = []. Primijenjena ima 3 podrucja.
class CourseStructure(CourseOut):
    modules: list[ModuleOut] = []