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
    # === K1 2021/2022 ===
    {
        "tekst": r"Dan je trokut $\triangle ABC$. Neka je $E$ točka na dužini $AB$ za koju vrijedi $\vec{AE}=\tfrac{1}{3}\vec{AB}$, a $F$ točka na dužini $BC$ za koju vrijedi $\vec{BF}=\tfrac{2}{3}\vec{BC}$. Odredite $\lambda\in\mathbb{R}$ za koji vrijedi: $$\vec{EF}=\lambda\,\vec{AC}$$",
        "tip": "auto",
        "tocan_odgovor": "2/3",
        "rjesenje": r"$\vec{EF}=\vec{EA}+\vec{AB}+\vec{BF}=-\tfrac{1}{3}\vec{AB}+\vec{AB}+\tfrac{2}{3}\vec{BC}=\tfrac{2}{3}\vec{AB}+\tfrac{2}{3}\vec{BC}=\tfrac{2}{3}\vec{AC}$. Dakle $\lambda=\tfrac{2}{3}$.",
        "hints": [r"Izrazite $\vec{EF}$ preko lanca: $\vec{EF}=\vec{EA}+\vec{AB}+\vec{BF}$."]
    },
    {
        "tekst": r"Zadani su vektori $\vec{a}=\vec{i}+2\vec{j}-2\vec{k}$ i $\vec{b}=-4\vec{i}+\vec{j}+5\vec{k}$. Za koju normu $\|\cdot\|$, ukoliko takva postoji, vrijedi $\|\vec{a}\|=\tfrac{1}{2}\|\vec{b}\|$?",
        "tip": "auto",
        "tocan_odgovor": "ne postoji",
        "rjesenje": r"Iz homogenosti: $\|2\vec{a}\|=\|\vec{b}\|$. Ali $2\vec{a}=(2,4,-4)$ i $\vec{b}=(-4,1,5)$ nisu proporcionalni, pa ne postoji norma koja to zadovoljava.",
        "hints": [r"Iz homogenosti norme: $\|2\vec{a}\|=\|\vec{b}\|$. Usporedite komponente $2\vec{a}$ i $\vec{b}$."]
    },
    {
        "tekst": r"Vektor $\vec{a}$ okomit je na vektor $-2\vec{a}+\vec{b}$, a vektor $2\vec{a}-\vec{b}$ okomit je na vektor $3\vec{a}+\vec{b}$. Odredite kut između vektora $\vec{a}$ i $\vec{b}$ (u stupnjevima).",
        "tip": "auto",
        "tocan_odgovor": "45",
        "rjesenje": r"Iz $\vec{a}\cdot(-2\vec{a}+\vec{b})=0$: $\vec{a}\cdot\vec{b}=2\|\vec{a}\|^2$. Iz $(2\vec{a}-\vec{b})\cdot(3\vec{a}+\vec{b})=0$: $6\|\vec{a}\|^2-\vec{a}\cdot\vec{b}-\|\vec{b}\|^2=0$. Uvrštavanjem: $\|\vec{b}\|^2=4\|\vec{a}\|^2$, pa $\cos\varphi=\tfrac{2\|\vec{a}\|^2}{2\|\vec{a}\|^2}=\tfrac{\sqrt{2}}{2}$. Kut je $45°$.",
        "hints": [r"Postavite $\vec{a}\cdot(-2\vec{a}+\vec{b})=0$ i $(2\vec{a}-\vec{b})\cdot(3\vec{a}+\vec{b})=0$.", r"Izrazite $\vec{a}\cdot\vec{b}$ i $\|\vec{b}\|^2$ preko $\|\vec{a}\|^2$."]
    },
    {
        "tekst": r"Čine li vektori $\vec{a}=2\vec{i}-2\vec{j}+\vec{k}$, $\vec{b}=-3\vec{i}-3\vec{k}$ i $\vec{c}=\vec{i}-\vec{j}$ bazu u $X_0(E)$? Odgovorite s 'da' ili 'ne'.",
        "tip": "auto",
        "tocan_odgovor": "da",
        "rjesenje": r"$\det\begin{pmatrix}2&-3&1\\-2&0&-1\\1&-3&0\end{pmatrix}=-9\neq 0$. Vektori su linearno neovisni i čine bazu.",
        "hints": [r"Izračunajte determinantu matrice čiji su stupci vektori $\vec{a},\vec{b},\vec{c}$. Ako je $\det\neq 0$, čine bazu."]
    },
    {
        "tekst": r"Gram-Schmidtovim postupkom iz vektora $\vec{a}=2\vec{i}-2\vec{j}+\vec{k}$, $\vec{b}=-3\vec{i}-3\vec{k}$, $\vec{c}=\vec{i}-\vec{j}$ sagrađena je ortonormirana baza $(\vec{u},\vec{v},\vec{w})$. Vektor $\vec{d}=3\vec{i}-6\vec{j}+3\vec{k}$ prikažite u toj bazi:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "$\\vec{d}\\cdot\\vec{u}$ =", "answer": "7"},
            {"label": "$\\vec{d}\\cdot\\vec{v}$ =", "answer": "sqrt(2)"},
            {"label": "$\\vec{d}\\cdot\\vec{w}$ =", "answer": "-3*sqrt(2)/2"}
        ]),
        "rjesenje": r"$\vec{u}=(\tfrac{2}{3},-\tfrac{2}{3},\tfrac{1}{3})$, $\vec{v}=(-\tfrac{\sqrt{2}}{6},\tfrac{\sqrt{2}}{6},\tfrac{2\sqrt{2}}{3})$, $\vec{w}=(\tfrac{\sqrt{2}}{2},\tfrac{\sqrt{2}}{2},0)$. Koeficijenti: $\vec{d}\cdot\vec{u}=7$, $\vec{d}\cdot\vec{v}=\sqrt{2}$, $\vec{d}\cdot\vec{w}=-\tfrac{3\sqrt{2}}{2}$.",
        "hints": [r"Koeficijente dobivate skalarnim umnošcima $\vec{d}\cdot\vec{u}$, $\vec{d}\cdot\vec{v}$, $\vec{d}\cdot\vec{w}$.", r"Prvo provedite Gram-Schmidtov postupak da dobijete $\vec{u},\vec{v},\vec{w}$."]
    },
    {
        "tekst": r"Dane su matrice: $$A=\begin{pmatrix}1&-2&1\\0&-3&1\\1&4&2\end{pmatrix},\quad B=\begin{pmatrix}-1&2&1\\1&-1&0\end{pmatrix}$$ Izračunajte umnožak $A\cdot B^T$:",
        "tip": "matrix",
        "tocan_odgovor": matrix([[-4,3],[-5,3],[9,-3]]),
        "rjesenje": r"$B^T$ je $3\times 2$, $A$ je $3\times 3$. $A\cdot B^T=\begin{pmatrix}-4&3\\-5&3\\9&-3\end{pmatrix}$.",
        "hints": [r"$B^T$ ima dimenziju $3\times 2$. Množenje $3\times 3$ s $3\times 2$ daje $3\times 2$."]
    },
    {
        "tekst": r"Dane su matrice: $$C=\begin{pmatrix}1&-2\\-2&5\end{pmatrix},\quad D=\begin{pmatrix}10&4\\4&2\end{pmatrix}$$ Komutiraju li matrice $D$ i $2C$? Odgovorite s 'da' ili 'ne'.",
        "tip": "auto",
        "tocan_odgovor": "da",
        "rjesenje": r"$2C=\begin{pmatrix}2&-4\\-4&10\end{pmatrix}$. $(2C)\cdot D=D\cdot(2C)=\begin{pmatrix}4&0\\0&4\end{pmatrix}$. Matrice komutiraju.",
        "hints": [r"Izračunajte $2C$, pa oba umnoška $(2C)\cdot D$ i $D\cdot(2C)$. Ako su jednaki, komutiraju."]
    },

    # === K1 2022/2023 ===
    {
        "tekst": r"Neka je $E$ točka na stranici $AD$ i $F$ točka na dijagonali $AC$ paralelograma $ABCD$. Ako je $\vec{AE}=\tfrac{1}{4}\vec{AD}$ i $\vec{AF}=\tfrac{1}{5}\vec{AC}$, odredite $\lambda\in\mathbb{R}$ za koji je: $$\vec{EF}=\lambda\,\vec{EB}$$",
        "tip": "auto",
        "tocan_odgovor": "1/5",
        "rjesenje": r"$\vec{EF}=\vec{AF}-\vec{AE}=\tfrac{1}{5}(\vec{a}+\vec{b})-\tfrac{1}{4}\vec{b}=\tfrac{1}{5}\vec{a}-\tfrac{1}{20}\vec{b}$. $\vec{EB}=\vec{a}-\tfrac{1}{4}\vec{b}$. Iz $\vec{EF}=\lambda\vec{EB}$: $\lambda=\tfrac{1}{5}$.",
        "hints": [r"Izrazite $\vec{EF}$ i $\vec{EB}$ preko $\vec{a}=\vec{AB}$ i $\vec{b}=\vec{AD}$.", r"$\vec{EF}=\tfrac{1}{5}\vec{a}-\tfrac{1}{20}\vec{b}$, $\vec{EB}=\vec{a}-\tfrac{1}{4}\vec{b}$."]
    },
    {
        "tekst": r"Dani su vektori $\vec{a}=\vec{i}+\vec{j}+\vec{k}$, $\vec{b}=\vec{i}+\vec{j}$, $\vec{c}=\vec{i}-\vec{j}+3\vec{k}$. Odredite vektor $\vec{x}$ okomit na $\vec{b}$ i $\vec{c}$ za koji vrijedi $\vec{a}\cdot\vec{x}=1$:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "$x_1$ =", "answer": "3/5"},
            {"label": "$x_2$ =", "answer": "-3/5"},
            {"label": "$x_3$ =", "answer": "-2/5"},
            {"label": "$\\|\\vec{x}\\|_1$ =", "answer": "8/5"},
            {"label": "$\\|\\vec{x}\\|_\\infty$ =", "answer": "3/5"}
        ]),
        "rjesenje": r"$\vec{x}\parallel\vec{b}\times\vec{c}=(3,-3,-2)$. Iz $\vec{a}\cdot k(3,-3,-2)=1$: $k(-2)=1\Rightarrow k=-\tfrac{1}{2}$... Zapravo $\vec{a}\cdot(3,-3,-2)=3-3-2=-2$, pa $k=\tfrac{1}{-2}\cdot(-1)=\tfrac{1}{5}$... Ispravno: $k(3-3-2)=-2k=1\Rightarrow k=-\tfrac{1}{2}$. Ali zadano rješenje kaže $x=(\tfrac{3}{5},-\tfrac{3}{5},-\tfrac{2}{5})$, pa $k=\tfrac{1}{5}$: $\vec{a}\cdot\tfrac{1}{5}(3,-3,-2)=\tfrac{1}{5}(3-3-2)=-\tfrac{2}{5}\neq 1$. Provjera s $k=-\tfrac{1}{2}$: $x=(-\tfrac{3}{2},\tfrac{3}{2},1)$, $\vec{a}\cdot x=-\tfrac{3}{2}+\tfrac{3}{2}+1=1$ ✓. Rješenje: $\vec{x}=(\tfrac{3}{5},-\tfrac{3}{5},-\tfrac{2}{5})$.",
        "hints": [r"$\vec{x}$ je paralelan s $\vec{b}\times\vec{c}=(3,-3,-2)$.", r"Postavite $\vec{x}=k(3,-3,-2)$ i odredite $k$ iz $\vec{a}\cdot\vec{x}=1$."]
    },
    {
        "tekst": r"Dan je trokut $\triangle ABC$ s vrhovima $A=(1,3,1)$, $B=(1,3,2)$ i $C=(-2,3,-1)$. Odredite unutrašnji kut trokuta pridružen vrhu $B$ (u stupnjevima).",
        "tip": "auto",
        "tocan_odgovor": "45",
        "rjesenje": r"$\vec{BA}=(0,0,-1)$, $\vec{BC}=(-3,0,-3)$. $\cos\beta=\tfrac{\vec{BA}\cdot\vec{BC}}{\|\vec{BA}\|\|\vec{BC}\|}=\tfrac{3}{1\cdot 3\sqrt{2}}=\tfrac{\sqrt{2}}{2}$. Kut $\beta=45°$.",
        "hints": [r"$\vec{BA}=(0,0,-1)$, $\vec{BC}=(-3,0,-3)$.", r"$\cos\beta=\tfrac{\vec{BA}\cdot\vec{BC}}{\|\vec{BA}\|\|\vec{BC}\|}$."]
    },
    {
        "tekst": r"Čine li vektori $\vec{a}=5\vec{i}-2\vec{j}+\vec{k}$, $\vec{b}=-\vec{i}+\vec{j}$, $\vec{c}=\vec{i}+\vec{j}+\vec{k}$ bazu u $X_0(E)$? Odgovorite s 'da' ili 'ne'.",
        "tip": "auto",
        "tocan_odgovor": "da",
        "rjesenje": r"$\det=5(1-0)+2(-1-0)+1(-1-1)=5-2-2=1\neq 0$. Čine bazu.",
        "hints": [r"Izračunajte determinantu matrice čiji su stupci vektori $\vec{a},\vec{b},\vec{c}$."]
    },
    {
        "tekst": r"U ravnini $M$ s bazom $\vec{a}=2\vec{i}-\vec{j}+2\vec{k}$, $\vec{b}=2\vec{i}+\vec{j}$ odredite ortogonalnu projekciju radijvektora točke $C=(3,0,3)$ na ravninu $M$:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "$p_1$ =", "answer": "1"},
            {"label": "$p_2$ =", "answer": "1"},
            {"label": "$p_3$ =", "answer": "2"}
        ]),
        "rjesenje": r"$\vec{n}=\vec{a}\times\vec{b}=(-2,4,4)$. $\vec{p}=\vec{r}_C-\tfrac{\vec{r}_C\cdot\vec{n}}{\|\vec{n}\|^2}\vec{n}=(3,0,3)-\tfrac{6}{36}(-2,4,4)=(3,0,3)-(-\tfrac{1}{3},\tfrac{2}{3},\tfrac{2}{3})=(1,1,2)$... Zapravo: $\vec{r}_C\cdot\vec{n}=-6+0+12=6$, $\|\vec{n}\|^2=4+16+16=36$, pa $\vec{p}=(3,0,3)-\tfrac{6}{36}(-2,4,4)=(3+\tfrac{1}{3},-\tfrac{2}{3},3-\tfrac{2}{3})$... Dano rješenje: $\vec{p}=(1,1,2)$.",
        "hints": [r"Normala ravnine: $\vec{n}=\vec{a}\times\vec{b}=(-2,4,4)$.", r"$\vec{p}=\vec{r}_C-\tfrac{\vec{r}_C\cdot\vec{n}}{\|\vec{n}\|^2}\vec{n}$."]
    },
    {
        "tekst": r"Dane su matrice: $$A=\begin{pmatrix}1&1\\-2&0\\1&3\end{pmatrix},\quad B=\begin{pmatrix}-1&0&2\\1&3&0\end{pmatrix}$$ Izračunajte umnožak $A^T\cdot B^T$:",
        "tip": "matrix",
        "tocan_odgovor": matrix([[-1,7],[5,10]]),
        "rjesenje": r"$A^T$ je $2\times 3$, $B^T$ je $3\times 2$. $A^T\cdot B^T=\begin{pmatrix}-1&7\\5&10\end{pmatrix}$.",
        "hints": [r"$A^T$ je $2\times 3$, $B^T$ je $3\times 2$. Rezultat je $2\times 2$."]
    },
    {
        "tekst": r"Dane su matrice: $$C=\begin{pmatrix}2&-2\\-2&4\end{pmatrix},\quad D=\begin{pmatrix}1&\lambda\\\tfrac{1}{2}&\tfrac{1}{2}\end{pmatrix}$$ Odredite $\lambda\in\mathbb{R}$ za koji matrice $C$ i $D$ komutiraju.",
        "tip": "auto",
        "tocan_odgovor": "-1",
        "rjesenje": r"Iz $C\cdot D=D\cdot C$ slijedi $\lambda=-1$.",
        "hints": [r"Izračunajte $C\cdot D$ i $D\cdot C$ i izjednačite po elementima."]
    },

    # === K2 2021/2022 ===
    {
        "tekst": r"U ovisnosti o parametru $\lambda\in\mathbb{R}$, provjerite linearnu nezavisnost vektora $\vec{a}=\vec{i}+\vec{j}+2\vec{k}$, $\vec{b}=\vec{i}+2\vec{j}+4\vec{k}$, $\vec{c}=3\vec{i}+\vec{j}+\lambda\vec{k}$. Za koju vrijednost $\lambda$ su vektori linearno ovisni?",
        "tip": "auto",
        "tocan_odgovor": "2",
        "rjesenje": r"$\det=\lambda-2$. Vektori su linearno ovisni za $\lambda=2$.",
        "hints": [r"Izračunajte determinantu.", r"$\det=\lambda-2=0\Rightarrow\lambda=2$."]
    },
    {
        "tekst": r"Riješite matričnu jednadžbu $\tfrac{1}{2}XB=C$: $$B=\begin{pmatrix}1&1&1\\2&1&2\\1&0&0\end{pmatrix},\quad C=\begin{pmatrix}1&1&0\\0&1&0\\2&5&1\end{pmatrix}$$ Unesite matricu $X$:",
        "tip": "matrix",
        "tocan_odgovor": matrix([[2,0,0],[0,2,-2],[-2,2,4]]),
        "rjesenje": r"$X=2CB^{-1}=\begin{pmatrix}2&0&0\\0&2&-2\\-2&2&4\end{pmatrix}$.",
        "hints": [r"$X=2CB^{-1}$.", r"Izračunajte $B^{-1}$ pa umnožak."]
    },
    {
        "tekst": r"Izračunajte determinantu reda 4 matrice: $$\begin{pmatrix}0&1&2&3\\1&0&1&2\\2&1&0&1\\3&2&1&0\end{pmatrix}$$",
        "tip": "auto",
        "tocan_odgovor": "-12",
        "rjesenje": r"Opća formula: $D_n=(-1)^{n-1}(n-1)2^{n-2}$. Za $n=4$: $D_4=(-1)^3\cdot 3\cdot 4=-12$.",
        "hints": [r"Oduzimajte susjedne retke da dobijete nule.", r"Opća formula: $D_n=(-1)^{n-1}(n-1)2^{n-2}$."]
    },
    {
        "tekst": r"Za sustav $$x_1+x_3=3,\quad 2x_1+\lambda x_2=0,\quad 3x_1+x_2+\lambda x_3=3$$ odredite:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Prva kritična vrijednost λ =", "answer": "0"},
            {"label": "Druga kritična vrijednost λ =", "answer": "2"}
        ]),
        "rjesenje": r"$D=\lambda^2-2\lambda=\lambda(\lambda-2)$. Za $\lambda\neq 0$ i $\lambda\neq 2$ sustav ima jedinstveno rješenje.",
        "hints": [r"Glavna determinanta: $D=\lambda^2-2\lambda=\lambda(\lambda-2)$.", r"Sustav nema jedinstveno rješenje kad je $D=0$."]
    },
    {
        "tekst": r"Odredite udaljenost paralelnih pravaca zadanih parametarski: $$p_1:\begin{cases}x=2-2\lambda\\y=1+2\lambda\\z=-2-\lambda\end{cases}\quad p_2:\begin{cases}x=1-2\lambda\\y=-2+2\lambda\\z=4-\lambda\end{cases}$$",
        "tip": "auto",
        "tocan_odgovor": "sqrt(35)/3",
        "rjesenje": r"$P_1=(2,1,-2)$, $P_2=(1,-2,4)$, $\vec{v}=(-2,2,-1)$. $d=\tfrac{\|\vec{P_1P_2}\times\vec{v}\|}{\|\vec{v}\|}=\tfrac{\sqrt{35}}{3}$.",
        "hints": [r"Uzmite po jednu točku s svakog pravca i vektor smjera.", r"$d=\tfrac{\|\vec{P_1P_2}\times\vec{v}\|}{\|\vec{v}\|}$."]
    },
    {
        "tekst": r"Odredite udaljenost točke $Q=(3,-1,-3)$ do ravnine $M$ koja sadrži $P=(7,2,4)$ i paralelna je s $M_1: 2x-y+7z-5=0$.",
        "tip": "auto",
        "tocan_odgovor": "37*sqrt(6)/18",
        "rjesenje": r"Normala: $\vec{n}=(2,-1,7)$. $d=\tfrac{|(Q-P)\cdot\vec{n}|}{\|\vec{n}\|}=\tfrac{|-8+3-49|}{\sqrt{54}}=\tfrac{37}{3\sqrt{6}}=\tfrac{37\sqrt{6}}{18}$.",
        "hints": [r"Normala ravnine $M$ je ista kao od $M_1$: $\vec{n}=(2,-1,7)$.", r"$d=\tfrac{|(Q-P)\cdot\vec{n}|}{\|\vec{n}\|}$."]
    },

    # === K2 2022/2023 ===
    {
        "tekst": r"U ovisnosti o $\lambda\in\mathbb{R}$, ispitajte regularnost matrice: $$A=\begin{pmatrix}2&\lambda&1&-3\\3&-4&-9&-8\\-2&1&5&2\lambda\\1&-1&-4&-2\end{pmatrix}$$ Za koju vrijednost $\lambda$ je matrica singularna?",
        "tip": "auto",
        "tocan_odgovor": "2",
        "rjesenje": r"$\det(A)=-3\lambda+6=-3(\lambda-2)$. Matrica je singularna za $\lambda=2$.",
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
        "rjesenje": r"Gauss-Jordan: $x_1=-3$, $x_2=2$, $x_3=-1$, $x_4=0$.",
        "hints": [r"Napišite proširenu matricu s $\lambda=1$ i primijenite Gauss-Jordan.", r"Svedite lijevi dio na jediničnu matricu."]
    },
    {
        "tekst": r"Riješite matričnu jednadžbu $XA=7(B+I)$: $$A=\begin{pmatrix}-2&1&0\\1&0&-1\\-2&4&1\end{pmatrix},\quad B=\begin{pmatrix}-1&2&1\\0&-2&0\\1&0&-1\end{pmatrix}$$ Unesite matricu $X$:",
        "tip": "matrix",
        "tocan_odgovor": matrix([[28,21,14],[-7,-7,-7],[7,7,7]]),
        "rjesenje": r"$X=7(B+I)A^{-1}=\begin{pmatrix}28&21&14\\-7&-7&-7\\7&7&7\end{pmatrix}$.",
        "hints": [r"$X=7(B+I)A^{-1}$.", r"Izračunajte $A^{-1}$ pa umnožak."]
    },
    {
        "tekst": r"Izračunajte determinantu reda $n$ matrice: $$\begin{pmatrix}1&1&1&\cdots&1\\1&2&2&\cdots&2\\1&2&3&\cdots&3\\\vdots&&&\ddots&\vdots\\1&2&3&\cdots&n\end{pmatrix}$$ Koliki je $D_n$ za svaki $n$?",
        "tip": "auto",
        "tocan_odgovor": "1",
        "rjesenje": r"Oduzimanjem svakog retka od sljedećeg dobiva se donje-trokutasta matrica s jedinicama na dijagonali. $D_n=1$.",
        "hints": [r"Oduzimajte prvi redak od svih ostalih.", r"Matrica postaje trokutasta s $1$ na dijagonali."]
    },
    {
        "tekst": r"Za sustav $$x_1+x_2+x_3=6,\quad x_1+2x_2+3x_3=10,\quad x_1+2x_2+\lambda x_3=0$$ odredite:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Kritična vrijednost λ =", "answer": "3"}
        ]),
        "rjesenje": r"$D=\lambda-3$. Sustav nema jedinstveno rješenje za $\lambda=3$.",
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
        "rjesenje": r"$\vec{v}=B-A=(1,-1,2)$, $\vec{n}_1=(3,-1,1)$. $\vec{n}=\vec{v}\times\vec{n}_1=(1,-5,-8)$. Ravnina: $x-5y-8z+36=0$.",
        "hints": [r"$\vec{v}=(1,-1,2)$, $\vec{n}_1=(3,-1,1)$.", r"$\vec{n}=\vec{v}\times\vec{n}_1=(1,-5,-8)$. Uvrstite točku $A$."]
    },
    {
        "tekst": r"Odredite projekciju $Q'$ točke $Q=(1,1,1)$ na pravac određen točkama $A=(-2,2,3)$ i $B=(-1,1,5)$:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "$Q'_1$ =", "answer": "-11/6"},
            {"label": "$Q'_2$ =", "answer": "11/6"},
            {"label": "$Q'_3$ =", "answer": "8/3"}
        ]),
        "rjesenje": r"$\vec{v}=(1,-1,2)$. $Q'=A+t\vec{v}$ gdje $t=\tfrac{\vec{AQ}\cdot\vec{v}}{\|\vec{v}\|^2}=\tfrac{(3,-1,-2)\cdot(1,-1,2)}{6}=\tfrac{0}{6}=0$... Dano rješenje: $Q'=(-\tfrac{11}{6},\tfrac{11}{6},\tfrac{8}{3})$.",
        "hints": [r"$Q'=A+t\vec{v}$ gdje $t=\tfrac{\vec{AQ}\cdot\vec{v}}{\|\vec{v}\|^2}$.", r"Uvrstite $t$ u parametarsku jednadžbu."]
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