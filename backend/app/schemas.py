from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict


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


class CourseStructure(CourseOut):
    modules: list[ModuleOut] = []


# Teorija / Zadaci

class HintBase(BaseModel):
    sadrzaj: str
    redoslijed: int = 0


class HintOut(HintBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ProblemBase(BaseModel):
    tekst: str
    tip: str = "auto"
    tocan_odgovor: str = ""
    rjesenje: str = ""
    redoslijed: int = 0


class ProblemCreate(ProblemBase):
    course_id: int
    module_id: Optional[int] = None
    hints: list[str] = []


class ProblemUpdate(BaseModel):
    tekst: Optional[str] = None
    tip: Optional[str] = None
    tocan_odgovor: Optional[str] = None
    rjesenje: Optional[str] = None
    redoslijed: Optional[int] = None
    hints: Optional[list[str]] = None


class ProblemOut(ProblemBase):
    id: int
    course_id: int
    module_id: Optional[int] = None
    hints: list[HintOut] = []
    model_config = ConfigDict(from_attributes=True)


class TheoryItemBase(BaseModel):
    tip: str 
    sadrzaj: dict
    redoslijed: int = 0


class TheoryItemCreate(TheoryItemBase):
    course_id: int
    module_id: Optional[int] = None


class TheoryItemUpdate(BaseModel):
    tip: Optional[str] = None
    sadrzaj: Optional[dict] = None
    redoslijed: Optional[int] = None


class TheoryItemOut(TheoryItemBase):
    id: int
    course_id: int
    module_id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)



# Rjesavanje zadataka
class AnswerCheckRequest(BaseModel):
    odgovor: str


class AnswerCheckResponse(BaseModel):
    tocno: bool


class ProgressOut(BaseModel):
    kind: str
    item_id: int
    status: str
    broj_pokusaja: int
    model_config = ConfigDict(from_attributes=True)



# napredak
class AreaProgress(BaseModel):
    module_id: Optional[int] = None
    naziv: Optional[str] = None
    teorija_ukupno: int
    teorija_rijeseno: int
    zadaci_ukupno: int
    zadaci_rijeseno: int


class CourseProgressOut(BaseModel):
    course_id: int
    areas: list[AreaProgress]



class TheoryMarkRequest(BaseModel):
    tocno: bool = True  # False = "ne znam jos" / netocan odgovor -> ne oznacava se kao svladano