"""
Import zadataka za kolegij "Linearna algebra I".
Pokretanje: python -m app.import_zadaci_la1
"""

import json
from .database import Base, engine, SessionLocal
from . import models

COURSE_NAME = "Linearna algebra I"

def multi(fields):
    return json.dumps(fields, ensure_ascii=False)

def matrix(m):
    return json.dumps({"matrix": m}, ensure_ascii=False)

ZADACI = [
    {
        "tekst": r"Dan je trokut $\triangle ABC$. Neka je $E$ točka na dužini $AB$ za koju vrijedi $\boldsymbol{AE}=\tfrac{1}{3}\boldsymbol{AB}$, a $F$ točka na dužini $BC$ za koju vrijedi $\boldsymbol{BF}=\tfrac{2}{3}\boldsymbol{BC}$. Odredite $\lambda\in\mathbb{R}$ za koji vrijedi: $$\boldsymbol{EF}=\lambda\,\boldsymbol{AC}$$",
        "tip": "auto",
        "tocan_odgovor": "2/3",
        "rjesenje": "2/3",
        "hints": [r"Izrazite $\boldsymbol{EF}$ preko lanca: $\boldsymbol{EF}=\boldsymbol{EA}+\boldsymbol{AB}+\boldsymbol{BF}$."]
    },
    {
        "tekst": r"Zadani su vektori $\boldsymbol{a}=\boldsymbol{i}+2\boldsymbol{j}-2\boldsymbol{k}$ i $\boldsymbol{b}=-4\boldsymbol{i}+\boldsymbol{j}+5\boldsymbol{k}$. Za koju normu $\|\cdot\|$, ukoliko takva postoji, vrijedi $\|\boldsymbol{a}\|=\tfrac{1}{2}\|\boldsymbol{b}\|$?",
        "tip": "auto",
        "tocan_odgovor": "ne postoji",
        "rjesenje": "ne postoji",
        "hints": [r"Iz homogenosti norme: $\|2\boldsymbol{a}\|=\|\boldsymbol{b}\|$. Usporedite komponente $2\boldsymbol{a}$ i $\boldsymbol{b}$."]
    },
    {
        "tekst": r"Vektor $\boldsymbol{a}$ okomit je na vektor $-2\boldsymbol{a}+\boldsymbol{b}$, a vektor $2\boldsymbol{a}-\boldsymbol{b}$ okomit je na vektor $3\boldsymbol{a}+\boldsymbol{b}$. Odredite kut između vektora $\boldsymbol{a}$ i $\boldsymbol{b}$ (u stupnjevima).",
        "tip": "auto",
        "tocan_odgovor": "45",
        "rjesenje": "45",
        "hints": [r"Postavite $\boldsymbol{a}\cdot(-2\boldsymbol{a}+\boldsymbol{b})=0$ i $(2\boldsymbol{a}-\boldsymbol{b})\cdot(3\boldsymbol{a}+\boldsymbol{b})=0$.", r"Izrazite $\boldsymbol{a}\cdot\boldsymbol{b}$ i $\|\boldsymbol{b}\|^2$ preko $\|\boldsymbol{a}\|^2$."]
    },
    {
        "tekst": r"Čine li vektori $\boldsymbol{a}=2\boldsymbol{i}-2\boldsymbol{j}+\boldsymbol{k}$, $\boldsymbol{b}=-3\boldsymbol{i}-3\boldsymbol{k}$ i $\boldsymbol{c}=\boldsymbol{i}-\boldsymbol{j}$ bazu u $X_0(E)$? Odgovorite s 'da' ili 'ne'.",
        "tip": "auto",
        "tocan_odgovor": "da",
        "rjesenje": "da",
        "hints": [r"Izračunajte determinantu matrice čiji su stupci vektori $\boldsymbol{a},\boldsymbol{b},\boldsymbol{c}$. Ako je $\det\neq 0$, čine bazu."]
    },
    {
        "tekst": r"Gram-Schmidtovim postupkom iz vektora $\boldsymbol{a}=2\boldsymbol{i}-2\boldsymbol{j}+\boldsymbol{k}$, $\boldsymbol{b}=-3\boldsymbol{i}-3\boldsymbol{k}$, $\boldsymbol{c}=\boldsymbol{i}-\boldsymbol{j}$ sagrađena je ortonormirana baza $(\boldsymbol{u},\boldsymbol{v},\boldsymbol{w})$. Vektor $\boldsymbol{d}=3\boldsymbol{i}-6\boldsymbol{j}+3\boldsymbol{k}$ prikažite u toj bazi:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "$\\boldsymbol{d}\\cdot\\boldsymbol{u}$ =", "answer": "7"},
            {"label": "$\\boldsymbol{d}\\cdot\\boldsymbol{v}$ =", "answer": "sqrt(2)"},
            {"label": "$\\boldsymbol{d}\\cdot\\boldsymbol{w}$ =", "answer": "-3*sqrt(2)/2"}
        ]),
        "rjesenje": multi([
            {"label": "$\\boldsymbol{d}\\cdot\\boldsymbol{u}$ =", "answer": "7"},
            {"label": "$\\boldsymbol{d}\\cdot\\boldsymbol{v}$ =", "answer": "sqrt(2)"},
            {"label": "$\\boldsymbol{d}\\cdot\\boldsymbol{w}$ =", "answer": "-3*sqrt(2)/2"}
        ]),
        "hints": [r"Koeficijente dobivate skalarnim umnošcima $\boldsymbol{d}\cdot\boldsymbol{u}$, $\boldsymbol{d}\cdot\boldsymbol{v}$, $\boldsymbol{d}\cdot\boldsymbol{w}$.", r"Prvo provedite Gram-Schmidtov postupak da dobijete $\boldsymbol{u},\boldsymbol{v},\boldsymbol{w}$."]
    },
    {
        "tekst": r"Dane su matrice: $$A=\begin{pmatrix}1&-2&1\\0&-3&1\\1&4&2\end{pmatrix},\quad B=\begin{pmatrix}-1&2&1\\1&-1&0\end{pmatrix}$$ Izračunajte umnožak $A\cdot B^T$:",
        "tip": "matrix",
        "tocan_odgovor": matrix([[-4,3],[-5,3],[9,-3]]),
        "rjesenje": matrix([[-4,3],[-5,3],[9,-3]]),
        "hints": [r"$B^T$ ima dimenziju $3\times 2$. Množenje $3\times 3$ s $3\times 2$ daje $3\times 2$."]
    },
    {
        "tekst": r"Dane su matrice: $$C=\begin{pmatrix}1&-2\\-2&5\end{pmatrix},\quad D=\begin{pmatrix}10&4\\4&2\end{pmatrix}$$ Komutiraju li matrice $D$ i $2C$? Odgovorite s 'da' ili 'ne'.",
        "tip": "auto",
        "tocan_odgovor": "da",
        "rjesenje": "da",
        "hints": [r"Izračunajte $2C$, pa oba umnoška $(2C)\cdot D$ i $D\cdot(2C)$. Ako su jednaki, komutiraju."]
    },
    {
        "tekst": r"Neka je $E$ točka na stranici $AD$ i $F$ točka na dijagonali $AC$ paralelograma $ABCD$. Ako je $\boldsymbol{AE}=\tfrac{1}{4}\boldsymbol{AD}$ i $\boldsymbol{AF}=\tfrac{1}{5}\boldsymbol{AC}$, odredite $\lambda\in\mathbb{R}$ za koji je: $$\boldsymbol{EF}=\lambda\,\boldsymbol{EB}$$",
        "tip": "auto",
        "tocan_odgovor": "1/5",
        "rjesenje": "1/5",
        "hints": [r"Izrazite $\boldsymbol{EF}$ i $\boldsymbol{EB}$ preko $\boldsymbol{a}=\boldsymbol{AB}$ i $\boldsymbol{b}=\boldsymbol{AD}$.", r"$\boldsymbol{EF}=\tfrac{1}{5}\boldsymbol{a}-\tfrac{1}{20}\boldsymbol{b}$, $\boldsymbol{EB}=\boldsymbol{a}-\tfrac{1}{4}\boldsymbol{b}$."]
    },
    {
        "tekst": r"Dani su vektori $\boldsymbol{a}=\boldsymbol{i}+\boldsymbol{j}+\boldsymbol{k}$, $\boldsymbol{b}=\boldsymbol{i}+\boldsymbol{j}$, $\boldsymbol{c}=\boldsymbol{i}-\boldsymbol{j}+3\boldsymbol{k}$. Odredite vektor $\boldsymbol{x}$ okomit na $\boldsymbol{b}$ i $\boldsymbol{c}$ za koji vrijedi $\boldsymbol{a}\cdot\boldsymbol{x}=1$:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "$x_1$ =", "answer": "3/5"},
            {"label": "$x_2$ =", "answer": "-3/5"},
            {"label": "$x_3$ =", "answer": "-2/5"},
            {"label": "$\\|\\boldsymbol{x}\\|_1$ =", "answer": "8/5"},
            {"label": "$\\|\\boldsymbol{x}\\|_\\infty$ =", "answer": "3/5"}
        ]),
        "rjesenje": multi([
            {"label": "$x_1$ =", "answer": "3/5"},
            {"label": "$x_2$ =", "answer": "-3/5"},
            {"label": "$x_3$ =", "answer": "-2/5"},
            {"label": "$\\|\\boldsymbol{x}\\|_1$ =", "answer": "8/5"},
            {"label": "$\\|\\boldsymbol{x}\\|_\\infty$ =", "answer": "3/5"}
        ]),
        "hints": [r"$\boldsymbol{x}$ je paralelan s $\boldsymbol{b}\times\boldsymbol{c}=(3,-3,-2)$.", r"Postavite $\boldsymbol{x}=k(3,-3,-2)$ i odredite $k$ iz $\boldsymbol{a}\cdot\boldsymbol{x}=1$."]
    },
    {
        "tekst": r"Dan je trokut $\triangle ABC$ s vrhovima $A=(1,3,1)$, $B=(1,3,2)$ i $C=(-2,3,-1)$. Odredite unutrašnji kut trokuta pridružen vrhu $B$ (u stupnjevima).",
        "tip": "auto",
        "tocan_odgovor": "45",
        "rjesenje": "45",
        "hints": [r"$\boldsymbol{BA}=(0,0,-1)$, $\boldsymbol{BC}=(-3,0,-3)$.", r"$\cos\beta=\tfrac{\boldsymbol{BA}\cdot\boldsymbol{BC}}{\|\boldsymbol{BA}\|\|\boldsymbol{BC}\|}$."]
    },
    {
        "tekst": r"Čine li vektori $\boldsymbol{a}=5\boldsymbol{i}-2\boldsymbol{j}+\boldsymbol{k}$, $\boldsymbol{b}=-\boldsymbol{i}+\boldsymbol{j}$, $\boldsymbol{c}=\boldsymbol{i}+\boldsymbol{j}+\boldsymbol{k}$ bazu u $X_0(E)$? Odgovorite s 'da' ili 'ne'.",
        "tip": "auto",
        "tocan_odgovor": "da",
        "rjesenje": "da",
        "hints": [r"Izračunajte determinantu matrice čiji su stupci vektori $\boldsymbol{a},\boldsymbol{b},\boldsymbol{c}$."]
    },
    {
        "tekst": r"U ravnini $M$ s bazom $\boldsymbol{a}=2\boldsymbol{i}-\boldsymbol{j}+2\boldsymbol{k}$, $\boldsymbol{b}=2\boldsymbol{i}+\boldsymbol{j}$ odredite ortogonalnu projekciju radijvektora točke $C=(3,0,3)$ na ravninu $M$:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "$p_1$ =", "answer": "1"},
            {"label": "$p_2$ =", "answer": "1"},
            {"label": "$p_3$ =", "answer": "2"}
        ]),
        "rjesenje": multi([
            {"label": "$p_1$ =", "answer": "1"},
            {"label": "$p_2$ =", "answer": "1"},
            {"label": "$p_3$ =", "answer": "2"}
        ]),
        "hints": [r"Normala ravnine: $\boldsymbol{n}=\boldsymbol{a}\times\boldsymbol{b}=(-2,4,4)$.", r"$\boldsymbol{p}=\boldsymbol{r}_C-\tfrac{\boldsymbol{r}_C\cdot\boldsymbol{n}}{\|\boldsymbol{n}\|^2}\boldsymbol{n}$."]
    },
    {
        "tekst": r"Dane su matrice: $$A=\begin{pmatrix}1&1\\-2&0\\1&3\end{pmatrix},\quad B=\begin{pmatrix}-1&0&2\\1&3&0\end{pmatrix}$$ Izračunajte umnožak $A^T\cdot B^T$:",
        "tip": "matrix",
        "tocan_odgovor": matrix([[-1,7],[5,10]]),
        "rjesenje": matrix([[-1,7],[5,10]]),
        "hints": [r"$A^T$ je $2\times 3$, $B^T$ je $3\times 2$. Rezultat je $2\times 2$."]
    },
    {
        "tekst": r"Dane su matrice: $$C=\begin{pmatrix}2&-2\\-2&4\end{pmatrix},\quad D=\begin{pmatrix}1&\lambda\\\tfrac{1}{2}&\tfrac{1}{2}\end{pmatrix}$$ Odredite $\lambda\in\mathbb{R}$ za koji matrice $C$ i $D$ komutiraju.",
        "tip": "auto",
        "tocan_odgovor": "-1",
        "rjesenje": "-1",
        "hints": [r"Izračunajte $C\cdot D$ i $D\cdot C$ i izjednačite po elementima."]
    },
    {
        "tekst": r"U ovisnosti o parametru $\lambda\in\mathbb{R}$, provjerite linearnu nezavisnost vektora $\boldsymbol{a}=\boldsymbol{i}+\boldsymbol{j}+2\boldsymbol{k}$, $\boldsymbol{b}=\boldsymbol{i}+2\boldsymbol{j}+4\boldsymbol{k}$, $\boldsymbol{c}=3\boldsymbol{i}+\boldsymbol{j}+\lambda\boldsymbol{k}$. Za koju vrijednost $\lambda$ su vektori linearno ovisni?",
        "tip": "auto",
        "tocan_odgovor": "2",
        "rjesenje": "2",
        "hints": [r"Izračunajte determinantu.", r"$\det=\lambda-2=0\Rightarrow\lambda=2$."]
    },
    {
        "tekst": r"Riješite matričnu jednadžbu $\tfrac{1}{2}XB=C$: $$B=\begin{pmatrix}1&1&1\\2&1&2\\1&0&0\end{pmatrix},\quad C=\begin{pmatrix}1&1&0\\0&1&0\\2&5&1\end{pmatrix}$$ Unesite matricu $X$:",
        "tip": "matrix",
        "tocan_odgovor": matrix([[2,0,0],[0,2,-2],[-2,2,4]]),
        "rjesenje": matrix([[2,0,0],[0,2,-2],[-2,2,4]]),
        "hints": [r"$X=2CB^{-1}$.", r"Izračunajte $B^{-1}$ pa umnožak."]
    },
    {
        "tekst": r"Izračunajte determinantu reda 4 matrice: $$\begin{pmatrix}0&1&2&3\\1&0&1&2\\2&1&0&1\\3&2&1&0\end{pmatrix}$$",
        "tip": "auto",
        "tocan_odgovor": "-12",
        "rjesenje": "-12",
        "hints": [r"Oduzimajte susjedne retke da dobijete nule.", r"Opća formula: $D_n=(-1)^{n-1}(n-1)2^{n-2}$."]
    },
    {
        "tekst": r"Za sustav $$x_1+x_3=3,\quad 2x_1+\lambda x_2=0,\quad 3x_1+x_2+\lambda x_3=3$$ odredite:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Prva kritična vrijednost λ =", "answer": "0"},
            {"label": "Druga kritična vrijednost λ =", "answer": "2"}
        ]),
        "rjesenje": multi([
            {"label": "Prva kritična vrijednost λ =", "answer": "0"},
            {"label": "Druga kritična vrijednost λ =", "answer": "2"}
        ]),
        "hints": [r"Glavna determinanta: $D=\lambda^2-2\lambda=\lambda(\lambda-2)$.", r"Sustav nema jedinstveno rješenje kad je $D=0$."]
    },
    {
        "tekst": r"Odredite udaljenost paralelnih pravaca zadanih parametarski: $$p_1:\begin{cases}x=2-2\lambda\\y=1+2\lambda\\z=-2-\lambda\end{cases}\quad p_2:\begin{cases}x=1-2\lambda\\y=-2+2\lambda\\z=4-\lambda\end{cases}$$",
        "tip": "auto",
        "tocan_odgovor": "sqrt(35)/3",
        "rjesenje": "sqrt(35)/3",
        "hints": [r"Uzmite po jednu točku s svakog pravca i vektor smjera.", r"$d=\tfrac{\|\boldsymbol{P_1P_2}\times\boldsymbol{v}\|}{\|\boldsymbol{v}\|}$."]
    },
    {
        "tekst": r"Odredite udaljenost točke $Q=(3,-1,-3)$ do ravnine $M$ koja sadrži $P=(7,2,4)$ i paralelna je s $M_1: 2x-y+7z-5=0$.",
        "tip": "auto",
        "tocan_odgovor": "37*sqrt(6)/18",
        "rjesenje": "37*sqrt(6)/18",
        "hints": [r"Normala ravnine $M$ je ista kao od $M_1$: $\boldsymbol{n}=(2,-1,7)$.", r"$d=\tfrac{|(Q-P)\cdot\boldsymbol{n}|}{\|\boldsymbol{n}\|}$."]
    },
    {
        "tekst": r"U ovisnosti o $\lambda\in\mathbb{R}$, ispitajte regularnost matrice: $$A=\begin{pmatrix}2&\lambda&1&-3\\3&-4&-9&-8\\-2&1&5&2\lambda\\1&-1&-4&-2\end{pmatrix}$$ Za koju vrijednost $\lambda$ je matrica singularna?",
        "tip": "auto",
        "tocan_odgovor": "2",
        "rjesenje": "2",
        "hints": [r"Izračunajte determinantu razvojem ili transformacijama.", r"$\det(A)=-3(\lambda-2)=0\Rightarrow\lambda=2$."]
    },
    {
        "tekst": r"Za $\lambda=1$ riješite sustav $Ax=b$ gdje je $b=(-5,1,2,1)^T$ (matrica $A$ iz prethodnog zadatka):",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "$x_1$ =", "answer": "-3"},
            {"label": "$x_2$ =", "answer": "2"},
            {"label": "$x_3$ =", "answer": "-1"},
            {"label": "$x_4$ =", "answer": "0"}
        ]),
        "rjesenje": multi([
            {"label": "$x_1$ =", "answer": "-3"},
            {"label": "$x_2$ =", "answer": "2"},
            {"label": "$x_3$ =", "answer": "-1"},
            {"label": "$x_4$ =", "answer": "0"}
        ]),
        "hints": [r"Napišite proširenu matricu s $\lambda=1$ i primijenite Gauss-Jordan.", r"Svedite lijevi dio na jediničnu matricu."]
    },
    {
        "tekst": r"Riješite matričnu jednadžbu $XA=7(B+I)$: $$A=\begin{pmatrix}-2&1&0\\1&0&-1\\-2&4&1\end{pmatrix},\quad B=\begin{pmatrix}-1&2&1\\0&-2&0\\1&0&-1\end{pmatrix}$$ Unesite matricu $X$:",
        "tip": "matrix",
        "tocan_odgovor": matrix([[28,21,14],[-7,-7,-7],[7,7,7]]),
        "rjesenje": matrix([[28,21,14],[-7,-7,-7],[7,7,7]]),
        "hints": [r"$X=7(B+I)A^{-1}$.", r"Izračunajte $A^{-1}$ pa umnožak."]
    },
    {
        "tekst": r"Izračunajte determinantu reda $n$ matrice: $$\begin{pmatrix}1&1&1&\cdots&1\\1&2&2&\cdots&2\\1&2&3&\cdots&3\\\vdots&&&\ddots&\vdots\\1&2&3&\cdots&n\end{pmatrix}$$ Koliki je $D_n$ za svaki $n$?",
        "tip": "auto",
        "tocan_odgovor": "1",
        "rjesenje": "1",
        "hints": [r"Oduzimajte prvi redak od svih ostalih.", r"Matrica postaje trokutasta s $1$ na dijagonali."]
    },
    {
        "tekst": r"Za sustav $$x_1+x_2+x_3=6,\quad x_1+2x_2+3x_3=10,\quad x_1+2x_2+\lambda x_3=0$$ odredite:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Kritična vrijednost λ =", "answer": "3"}
        ]),
        "rjesenje": multi([
            {"label": "Kritična vrijednost λ =", "answer": "3"}
        ]),
        "hints": [r"Glavna determinanta: $D=\lambda-3$.", r"$D=0\Rightarrow\lambda=3$."]
    },
    {
        "tekst": r"Ravnina $M$ sadrži pravac kroz $A=(-2,2,3)$ i $B=(-1,1,5)$ i okomita je na $M_1: 3x-y+z-6=0$. Odredite koeficijente jednadžbe ravnine $ax+by+cz+d=0$:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "a =", "answer": "1"},
            {"label": "b =", "answer": "-5"},
            {"label": "c =", "answer": "-8"},
            {"label": "d =", "answer": "36"}
        ]),
        "rjesenje": multi([
            {"label": "a =", "answer": "1"},
            {"label": "b =", "answer": "-5"},
            {"label": "c =", "answer": "-8"},
            {"label": "d =", "answer": "36"}
        ]),
        "hints": [r"$\boldsymbol{v}=(1,-1,2)$, $\boldsymbol{n}_1=(3,-1,1)$.", r"$\boldsymbol{n}=\boldsymbol{v}\times\boldsymbol{n}_1=(1,-5,-8)$. Uvrstite točku $A$."]
    },
    {
        "tekst": r"Odredite projekciju $Q'$ točke $Q=(1,1,1)$ na pravac određen točkama $A=(-2,2,3)$ i $B=(-1,1,5)$:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "$Q'_1$ =", "answer": "-11/6"},
            {"label": "$Q'_2$ =", "answer": "11/6"},
            {"label": "$Q'_3$ =", "answer": "8/3"}
        ]),
        "rjesenje": multi([
            {"label": "$Q'_1$ =", "answer": "-11/6"},
            {"label": "$Q'_2$ =", "answer": "11/6"},
            {"label": "$Q'_3$ =", "answer": "8/3"}
        ]),
        "hints": [r"$Q'=A+t\boldsymbol{v}$ gdje $t=\tfrac{\boldsymbol{AQ}\cdot\boldsymbol{v}}{\|\boldsymbol{v}\|^2}$.", r"Uvrstite $t$ u parametarsku jednadžbu."]
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
    finally:
        db.close()

if __name__ == "__main__":
    run()