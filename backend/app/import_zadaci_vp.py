"""
Import zadataka za kolegij "Vektorski prostori".
Pokretanje: python -m app.import_zadaci_vp
"""

import json
from .database import Base, engine, SessionLocal
from . import models

COURSE_NAME = "Vektorski prostori"

def multi(fields):
    return json.dumps(fields, ensure_ascii=False)

def matrix(m):
    return json.dumps({"matrix": m}, ensure_ascii=False)

def choice(answer, options):
    return json.dumps({"answer": answer, "options": options}, ensure_ascii=False)

VP   = ["jest vektorski prostor", "nije vektorski prostor"]
PS   = ["jest potprostor", "nije potprostor"]
DN   = ["jest", "nije"]
MONO = ["jest monomorfizam", "nije monomorfizam"]
EPI  = ["jest epimorfizam", "nije epimorfizam"]
IZO  = ["jest izomorfizam", "nije izomorfizam"]
DIR  = ["jest direktna", "nije direktna"]

ZADACI = [
    {
        "tekst": r"Je li skup $V_1=\{(x_1,x_2,x_3,x_4)\in\mathbb{R}^4: x_1+x_2=2,\;x_4=5\}$ realni vektorski prostor?",
        "tip": "choice",
        "tocan_odgovor": choice("nije vektorski prostor", VP),
        "rjesenje": r"nije vektorski prostor",
        "hints": [r"Provjeri sadrži li $V_1$ nul-vektor: $(0,0,0,0)\notin V_1$ jer $0+0\neq 2$."]
    },
    {
        "tekst": r"Je li skup $V_2=\{(x_1,x_2,x_3,x_4)\in\mathbb{R}^4: x_1+x_2=x_3,\;x_2+x_3=x_4\}$ realni vektorski prostor? Odredite dimenziju.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "V₂ je:", "answer": "jest vektorski prostor", "type": "choice", "options": VP},
            {"label": "dim V₂ =", "answer": "2"}
        ]),
        "rjesenje": r"jest vektorski prostor, $\dim V_2=2$",
        "hints": [r"Uvjeti su homogeni $\Rightarrow$ nul-vektor je u $V_2$, zatvoren je na zbrajanje i množenje skalarom.", r"Slobodne varijable: $x_1$ i $x_2$. Ostale su određene uvjetima."]
    },
    {
        "tekst": r"Dan je skup $V=\{(x_1,x_2,x_3)\in\mathbb{R}^3: x_3=-x_1\}$. Je li $V$ realni vektorski prostor? Odredite dimenziju.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "V je:", "answer": "jest vektorski prostor", "type": "choice", "options": VP},
            {"label": "dim V =", "answer": "2"}
        ]),
        "rjesenje": r"jest vektorski prostor, $\dim V=2$; baza $e=\{(1,0,-1),(0,1,0)\}$",
        "hints": [r"Homogeni uvjet: nul-vektor je u $V$, zatvoren na zbrajanje i množenje.", r"Parametrizacija: $(x_1,x_2,-x_1)$ s parametrima $x_1,x_2$ $\Rightarrow\dim=2$."]
    },
    {
        "tekst": r"Neka je $V$ dvodimenzionalan realni vektorski prostor i $\mathbb{C}^2$ realni vektorski prostor dimenzije $4$. Kolika je dimenzija prostora linearnih operatora $L(V,\mathbb{C}^2)$?",
        "tip": "auto",
        "tocan_odgovor": "8",
        "rjesenje": r"$\dim L(V,\mathbb{C}^2)=\dim_\mathbb{R}(V)\cdot\dim_\mathbb{R}(\mathbb{C}^2)=2\cdot 4=8$",
        "hints": [r"$\dim L(V,W)=\dim V\cdot\dim W$ za realne vektorske prostore."]
    },
    {
        "tekst": r"Linearan operator $A:V\to\mathbb{C}^2$ definiran je s $A(x_1,x_2,x_3)=(x_2,\;ix_1+x_3)$, gdje je $V=\{x_3=-x_1\}$. Odredite rang i defekt operatora $A$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "rang(A) =", "answer": "2"},
            {"label": "defekt(A) =", "answer": "0"}
        ]),
        "rjesenje": r"$\operatorname{rang}(A)=2$, $\operatorname{defekt}(A)=0$",
        "hints": [r"Na vektorima baze: $Ae_1=A(1,0,-1)=(0,i+(-1))=(0,i-1)$ i $Ae_2=A(0,1,0)=(1,0)$ — lin. neovisni.", r"$\ker A=\{0\}$ jer $A(x_1,x_2,-x_1)=(x_2,ix_1-x_1)=(0,0)\Rightarrow x_2=0$ i $x_1(i-1)=0\Rightarrow x_1=0$."]
    },
    {
        "tekst": r"Linearan operator $A:V\to\mathbb{C}^2$, $V=\{x_3=-x_1\}$, $A(x_1,x_2,x_3)=(x_2,\;ix_1+x_3)$. Je li $A$ monomorfizam, epimorfizam, izomorfizam?",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "A je monomorfizam:", "answer": "jest monomorfizam", "type": "choice", "options": MONO},
            {"label": "A je epimorfizam:", "answer": "nije epimorfizam", "type": "choice", "options": EPI},
            {"label": "A je izomorfizam:", "answer": "nije izomorfizam", "type": "choice", "options": IZO}
        ]),
        "rjesenje": r"monomorfizam; nije epimorfizam; nije izomorfizam",
        "hints": [r"$\ker A=\{0\}\Rightarrow$ monomorfizam.", r"$\operatorname{rang}=2<4=\dim_\mathbb{R}(\mathbb{C}^2)\Rightarrow$ nije epimorfizam."]
    },
    {
        "tekst": r"U $\mathbb{R}^3$ dan je potprostor $M$ razapet skupom $S_M=\{(1,0,1),(2,1,3),(4,1,5)\}$. Je li $S_M$ baza od $M$?",
        "tip": "choice",
        "tocan_odgovor": choice("nije", ["jest", "nije"]),
        "rjesenje": r"nije — skup je linearno zavisan ($\det=0$)",
        "hints": [r"Svedite vektore na redčanu formu ili izračunajte determinantu matrice $3\times 3$ — iznosi $0$."]
    },
    {
        "tekst": r"U $\mathbb{R}^3$ zadani su $M=\operatorname{sp}\{(1,0,1),(2,1,3),(4,1,5)\}$ i $N=\{x_1-2x_2+x_3=0,\;-3x_1-x_2+4x_3=0\}$. Kolika je $\dim(M+N)$?",
        "tip": "auto",
        "tocan_odgovor": "3",
        "rjesenje": r"$\dim(M+N)=3$",
        "hints": [r"$\dim M=2$ (S_M linearno zavisan, rang=2). $\dim N=1$ (homogeni sustav ranga 2).", r"Grassmannova formula: $\dim(M\cap N)=2+1-3=0$, pa $\dim(M+N)=3$."]
    },
    {
        "tekst": r"Za $M$ i $N$ iz prethodnog zadatka — je li suma $M+N$ direktna?",
        "tip": "choice",
        "tocan_odgovor": choice("jest direktna", DIR),
        "rjesenje": r"jest direktna ($\dim(M\cap N)=0$)",
        "hints": [r"Suma je direktna $\Leftrightarrow M\cap N=\{0\}$.", r"$\dim(M\cap N)=\dim M+\dim N-\dim(M+N)=2+1-3=0$."]
    },
    {
        "tekst": r"Linearan operator $A\in L(\mathbb{R}^3,\mathbb{C})$ zadan je s $Ae_1=2f_1-2f_2$, $Ae_2=f_2$, $Ae_3=3f_1+f_2$, "
                 r"gdje je $e$ kanonska baza $\mathbb{R}^3$, a $f=\{2,\,i\}$ realna baza od $\mathbb{C}$. "
                 r"Odredite matricu $[A]_f^e$.",
        "tip": "matrix",
        "tocan_odgovor": matrix([[2,0,3],[-2,1,1]]),
        "rjesenje": r"$[A]_f^e=\begin{pmatrix}2&0&3\\-2&1&1\end{pmatrix}$",
        "hints": [r"Stupci su koordinate $Ae_j$ u bazi $f$: $Ae_1=2f_1-2f_2\to[2,-2]^T$, $Ae_2=f_2\to[0,1]^T$, $Ae_3=3f_1+f_2\to[3,1]^T$."]
    },
    {
        "tekst": r"Za operator $A$ iz prethodnog zadatka i novu bazu $f'=\{4,\;2-i\}$ od $\mathbb{C}$, odredite matricu $[A]_{f'}^e$.",
        "tip": "matrix",
        "tocan_odgovor": matrix([[0, 0.5, 2],[2, -1, -1]]),
        "rjesenje": r"$[A]_{f'}^e=\begin{pmatrix}0&\tfrac{1}{2}&2\\2&-1&-1\end{pmatrix}$",
        "hints": [r"$[A]_{f'}^e = I(f',f)\cdot[A]_f^e$ gdje $I(f',f)=[I(f,f')]^{-1}$.", r"Izrazite $f_1=2$ i $f_2=i$ u bazi $f'$: $f_1=\frac{1}{2}f'_1+0\cdot f'_2$, $f_2=\frac{1}{2}f'_1-f'_2$."]
    },
    {
        "tekst": r"Za operator $A$ i baze $f'=\{4,\;2-i\}$, $e'=\{(1,2,1),(0,2,-1),(3,0,1)\}$, odredite $[A]_{f'}^{e'}$.",
        "tip": "matrix",
        "tocan_odgovor": matrix([[-1.5, 2.5, -2],[2, -2, 7]]),
        "rjesenje": r"$[A]_{f'}^{e'}=\begin{pmatrix}-\tfrac{3}{2}&\tfrac{5}{2}&-2\\2&-2&7\end{pmatrix}$",
        "hints": [r"$[A]_{f'}^{e'} = I(f',f)\cdot[A]_f^e\cdot I(e,e')$ gdje $I(e,e')$ ima stupce = prikaz $e'_j$ u $e$."]
    },
    {
        "tekst": r"Linearan operator $A\in L(\mathbb{R}^3,\mathbb{C})$ zadan je s $Ae_1=f_1+2f_2$, $Ae_2=-f_1$, $Ae_3=3f_1-f_2$, "
                 r"gdje je $e$ kanonska baza $\mathbb{R}^3$, $f=\{1,\;2i\}$ realna baza od $\mathbb{C}$. "
                 r"Odredite $[A]_f^e$.",
        "tip": "matrix",
        "tocan_odgovor": matrix([[1,-1,3],[2,0,-1]]),
        "rjesenje": r"$[A]_f^e=\begin{pmatrix}1&-1&3\\2&0&-1\end{pmatrix}$",
        "hints": [r"Stupci = koordinate $Ae_j$ u $f=\{1,2i\}$: $Ae_1=1+4i=[1,2]^T$, $Ae_2=-1=[-1,0]^T$, $Ae_3=3-2i=[3,-1]^T$."]
    },
    {
        "tekst": r"Za $A$ iz prethodnog zadatka i $f'=\{2,\;1+i\}$, $e'=\{(1,2,3),(0,1,1),(-1,0,2)\}$, odredite $[A]_{f'}^{e'}$.",
        "tip": "matrix",
        "tocan_odgovor": matrix([[5, 2, 6.5],[-2, -2, -8]]),
        "rjesenje": r"$[A]_{f'}^{e'}=\begin{pmatrix}5&2&\tfrac{13}{2}\\-2&-2&-8\end{pmatrix}$",
        "hints": [r"$[A]_{f'}^{e'} = I(f',f)\cdot[A]_f^e\cdot I(e,e')$."]
    },
    {
        "tekst": r"Za $A$ iz prethodnog zadatka i $f=\{1,\;2i\}$, $e'=\{(1,2,3),(0,1,1),(-1,0,2)\}$, odredite $[A]_f^{e'}$.",
        "tip": "matrix",
        "tocan_odgovor": matrix([[8, 2, 5],[-1, -1, -4]]),
        "rjesenje": r"$[A]_f^{e'}=\begin{pmatrix}8&2&5\\-1&-1&-4\end{pmatrix}$",
        "hints": [r"$[A]_f^{e'} = [A]_f^e\cdot I(e,e')$ gdje $I(e,e')$ ima stupce = koordinate $e'_j$ u $e$."]
    },
    {
        "tekst": r"Linearan operator $A\in L(\mathbb{R}^3,\mathbb{C})$ ima matricu $[A]_f^e=\begin{pmatrix}2&-1&3\\1&4&-2\end{pmatrix}$ "
                 r"u kanonskim bazama $e$ i $f=\{1,i\}$. Za $f'=\{2-i,\,-i\}$ i $e'=\{(0,1,2),(3,2,1),(-1,1,2)\}$ odredite $[A]_{f'}^e$.",
        "tip": "matrix",
        "tocan_odgovor": matrix([[2,-1,3],[-4,3,-5]]),
        "rjesenje": r"$[A]_{f'}^e=\begin{pmatrix}2&-1&3\\-4&3&-5\end{pmatrix}$",
        "hints": [r"$[A]_{f'}^e = I(f',f)\cdot[A]_f^e$."]
    },
    {
        "tekst": r"Za $A$ iz prethodnog zadatka, $f'=\{2-i,\,-i\}$ i $e'=\{(0,1,2),(3,2,1),(-1,1,2)\}$, odredite $[A]_{f'}^{e'}$.",
        "tip": "matrix",
        "tocan_odgovor": matrix([[7,13,3],[-13,-25,-7]]),
        "rjesenje": r"$[A]_{f'}^{e'}=\begin{pmatrix}7&13&3\\-13&-25&-7\end{pmatrix}$",
        "hints": [r"$[A]_{f'}^{e'}= I(f',f)\cdot[A]_f^e\cdot I(e,e')$."]
    },
    {
        "tekst": r"Neka je $e=\{1,\;5-x,\;2+x-2x^2\}$ baza prostora $P_2(\mathbb{R})$ i $e'$ dualna baza. "
                 r"Izračunajte $e_1'(2x^2)$, $e_2'(2x^2)$ i $e_3'(2x^2)$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "e₁'(2x²) =", "answer": "7"},
            {"label": "e₂'(2x²) =", "answer": "-1"},
            {"label": "e₃'(2x²) =", "answer": "-1"}
        ]),
        "rjesenje": r"$e_1'(2x^2)=7$, $e_2'(2x^2)=-1$, $e_3'(2x^2)=-1$",
        "hints": [r"Prikažite $2x^2=a\cdot 1+b\cdot(5-x)+c\cdot(2+x-2x^2)$.", r"Uspoređivanjem koeficijenata uz $x^2,x,1$ dobijete sustav za $a,b,c$."]
    },
    {
        "tekst": r"Neka je $e=\{1,\;2+x,\;1-x+3x^2\}$ baza $P_2(\mathbb{R})$ i $e'$ dualna baza. "
                 r"Za polinom $p(x)=ax^2+bx+c$ odredite opće formule $e_1'(p)$, $e_2'(p)$, $e_3'(p)$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "e₁'(p) =", "answer": "c+b"},
            {"label": "e₂'(p) =", "answer": "-b-a/3"},
            {"label": "e₃'(p) =", "answer": "a/3"}
        ]),
        "rjesenje": r"$e_1'(p)=c+b$, $e_2'(p)=-b-\tfrac{a}{3}$, $e_3'(p)=\tfrac{a}{3}$",
        "hints": [r"Uvjet dualne baze: $e_i'(e_j)=\delta_{ij}$.", r"Prikažite $p=\alpha e_1+\beta e_2+\gamma e_3$ i riješite sustav."]
    },
    {
        "tekst": r"Odredite Jordanovu formu operatora $A$ zadanog matricom "
                 r"$A=\begin{pmatrix}0&0&0&1\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}$.",
        "tip": "matrix",
        "tocan_odgovor": matrix([[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
        "rjesenje": r"$J=\begin{pmatrix}0&1&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}$",
        "hints": [r"Jedina s.v. je $\lambda=0$, algebarska kratnost $4$.", r"$\operatorname{defekt}(A-0\cdot I)=\operatorname{defekt}(A)=3\Rightarrow$ postoje $3$ Jordanova bloka za $\lambda=0$."]
    },
    {
        "tekst": r"Za matricu $A$ iz prethodnog zadatka izračunajte $\cos(A)$ u Jordanovoj bazi.",
        "tip": "auto",
        "tocan_odgovor": "I",
        "rjesenje": r"$\cos(A)=I$ (jedinična matrica)",
        "hints": [r"$J^2=0$, pa $\cos(J)=I-\frac{J^2}{2!}+\ldots=I$.", r"$\cos(J)=I$ jer sve potencije $J^k=0$ za $k\ge 2$."]
    },
    {
        "tekst": r"Ako je na $C_{[0,1]}$ zadan skalarni produkt $(f|g)=\int_0^1 f(x)g(x)\,\mathrm{d}x$, "
                 r"odredite $\lambda\in\mathbb{R}$ takav da su $f_1(x)=x^2$ i $f_2(x)=\lambda-2x$ ortogonalni.",
        "tip": "auto",
        "tocan_odgovor": "3/2",
        "rjesenje": r"$\lambda=\dfrac{3}{2}$",
        "hints": [r"Uvjet ortogonalnosti: $\int_0^1 x^2(\lambda-2x)\,\mathrm{d}x=0$.", r"$\frac{\lambda}{3}-\frac{1}{2}=0\Rightarrow\lambda=\frac{3}{2}$."]
    },
    {
        "tekst": r"Odredite $\sqrt{A}$ u polaznoj bazi za operator $A\in L(\mathbb{C}^3)$ zadan matricom "
                 r"$A=\begin{pmatrix}4&-2&2\\6&-3&4\\3&-2&3\end{pmatrix}$.",
        "tip": "matrix",
        "tocan_odgovor": matrix([[2,-1,1],[3,-2,2],[2,-1,1]]),
        "rjesenje": r"$\sqrt{A}=\begin{pmatrix}2&-1&1\\3&-2&2\\2&-1&1\end{pmatrix}$",
        "hints": [r"Nađite Jordanovu formu $J$ i matricu prijelaza $P$ ($A=PJP^{-1}$).", r"$\sqrt{A}=P\cdot\sqrt{J}\cdot P^{-1}$."]
    },
]


def run():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        course = db.query(models.Course).filter(models.Course.naziv == COURSE_NAME).first()
        if not course:
            print(f"Kolegij '{COURSE_NAME}' ne postoji. Pokreni seed.")
            return
        existing = db.query(models.Problem).filter(
            models.Problem.course_id == course.id,
            models.Problem.module_id.is_(None),
        ).all()
        for p in existing:
            db.delete(p)
        db.flush()
        for i, z in enumerate(ZADACI):
            problem = models.Problem(
                course_id=course.id, module_id=None,
                tekst=z["tekst"], tip=z["tip"],
                tocan_odgovor=z["tocan_odgovor"],
                rjesenje=z["rjesenje"], redoslijed=i,
            )
            for j, h in enumerate(z.get("hints", [])):
                problem.hints.append(models.Hint(sadrzaj=h, redoslijed=j))
            db.add(problem)
        db.commit()
        print(f"Umetnuto {len(ZADACI)} zadataka za '{COURSE_NAME}'.")
        tips = {}
        for z in ZADACI:
            tips[z["tip"]] = tips.get(z["tip"], 0) + 1
        for t, c in sorted(tips.items()):
            print(f"  {t}: {c}")
    except Exception:
        import traceback; traceback.print_exc()
    finally:
        db.close()


if __name__ == "__main__":
    run()