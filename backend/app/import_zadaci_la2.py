"""
Import zadataka za kolegij "Linearna algebra II".
Pokretanje: python -m app.import_zadaci_la2
"""

import json
from .database import Base, engine, SessionLocal
from . import models

COURSE_NAME = "Linearna algebra II"

def multi(fields):
    return json.dumps(fields, ensure_ascii=False)

def matrix(m):
    return json.dumps({"matrix": m}, ensure_ascii=False)

def choice(answer, options):
    return json.dumps({"answer": answer, "options": options}, ensure_ascii=False)

VP  = ["jest vektorski prostor", "nije vektorski prostor"]
LN  = ["jest linearno nezavisan", "nije linearno nezavisan"]
PS  = ["jest potprostor", "nije potprostor"]
LIN = ["jest linearan", "nije linearan"]
SP  = ["jest skalarni produkt", "nije skalarni produkt"]
HRM = ["jest hermitski", "nije hermitski"]
UNI = ["jest unitaran", "nije unitaran"]
KRV = ["elipsa", "hiperbola", "parabola", "točka ili prazno"]
DA_NE = ["da", "nije"]

ZADACI = [
    {
        "tekst": r"Je li preslikavanje $\langle A,B\rangle=\operatorname{tr}(B^T A)$, $A,B\in M_2(\mathbb{R})$, skalarni produkt?",
        "tip": "choice",
        "tocan_odgovor": choice("jest skalarni produkt", SP),
        "rjesenje": r"jest skalarni produkt",
        "hints": [r"Provjeri 4 aksioma: simetričnost, aditivnost, homogenost i pozitivnu definitnost.", r"$\langle A,A\rangle=\operatorname{tr}(A^T A)=\sum a_{ij}^2\ge 0$ s jednakošću samo za $A=0$."]
    },
    {
        "tekst": r"Neka je $V=\mathbb{R}^2$. Definiramo $x\oplus y=(x_1 y_1,\;x_2 y_2-1)$ i $\alpha\odot x=e^\alpha\cdot x$. Je li $V$ s ovim operacijama vektorski prostor?",
        "tip": "choice",
        "tocan_odgovor": choice("nije vektorski prostor", VP),
        "rjesenje": r"nije vektorski prostor",
        "hints": [r"Provjeri $(\alpha+\beta)\odot x \stackrel{?}{=} (\alpha\odot x)\oplus(\beta\odot x)$.", r"Lijeva strana: $e^{\alpha+\beta}x$. Desna se ne podudara."]
    },
    {
        "tekst": r"Dana je matrica $A=\begin{pmatrix}-1&2&0\\0&1&0\\3&1&2\end{pmatrix}$. (a) Odredite s.v. i s.v. vektore. (b) Odredite minimalni polinom. (c) Je li dijagonalizabilna?",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "λ₁ =", "answer": "-1"},
            {"label": "λ₂ =", "answer": "1"},
            {"label": "λ₃ =", "answer": "2"},
            {"label": "m_A(λ) =", "answer": "(lam+1)*(lam-1)*(lam-2)"},
            {"label": "Je li dijagonalizabilna?", "answer": "da", "type": "choice", "options": DA_NE}
        ]),
        "rjesenje": r"$\lambda_1=-1,\lambda_2=1,\lambda_3=2$; $m_A=(\lambda+1)(\lambda-1)(\lambda-2)$; dijagonalizabilna",
        "hints": [r"Tri različite jednostruke s.v. $\Rightarrow$ uvijek dijagonalizabilna.", r"Minimalni polinom jednak karakterističnom."]
    },
    {
        "tekst": r"Je li $A:\mathbb{R}^3\to\mathbb{R}^2$, $A(x_1,x_2,x_3)=(x_1+x_2,\;x_2+x_3)$ linearan operator? Ako jest, odredite rang i defekt.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "A je:", "answer": "jest linearan", "type": "choice", "options": LIN},
            {"label": "rang(A) =", "answer": "2"},
            {"label": "defekt(A) =", "answer": "1"}
        ]),
        "rjesenje": r"jest linearan; $\operatorname{rang}=2$, $\operatorname{def}=1$",
        "hints": [r"Provjeri aditivnost i homogenost.", r"Jezgra: baza $\{(1,-1,1)\}$."]
    },
    {
        "tekst": r"Odredite koja je krivulja dana jednadžbom $2x_1^2+2x_1 x_2+2x_2^2+2\sqrt{2}\,x_1+4\sqrt{2}\,x_2+4=0$.",
        "tip": "choice",
        "tocan_odgovor": choice("elipsa", KRV),
        "rjesenje": r"elipsa ($y_1^2/3+y_2^2=1$)",
        "hints": [r"S.v. matrice kvadratne forme $\lambda_1=3$, $\lambda_2=1$ — oba pozitivna $\Rightarrow$ elipsa."]
    },
    {
        "tekst": r"Neka je $V=\mathbb{R}^3$. Definiramo $x\oplus y=(x_1+y_1,\;2x_2+y_2,\;x_3+3y_3)$ i $\alpha\odot x=(x_1,x_2,x_3)$. Je li $V$ vektorski prostor?",
        "tip": "choice",
        "tocan_odgovor": choice("nije vektorski prostor", VP),
        "rjesenje": r"nije vektorski prostor",
        "hints": [r"Zbrajanje nije komutativno (2. i 3. komponenta).", r"Niti $\alpha\odot x=\alpha x$."]
    },
    {
        "tekst": r"Gram-Schmidtovim postupkom odredite ortonormiranu bazu $W=\operatorname{sp}\{(1,1,0),(0,1,0)\}$ i ortogonalni komplement $W^\perp$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "e₁ =", "answer": "[1/sqrt(2), 1/sqrt(2), 0]"},
            {"label": "e₂ =", "answer": "[-1/sqrt(2), 1/sqrt(2), 0]"},
            {"label": "W⊥ razapet s:", "answer": "[0, 0, 1]"}
        ]),
        "rjesenje": r"$e_1=\frac{1}{\sqrt{2}}(1,1,0)$, $e_2=\frac{1}{\sqrt{2}}(-1,1,0)$; $W^\perp=\operatorname{sp}\{(0,0,1)\}$",
        "hints": [r"$\tilde{e}_2=w_2-\frac{w_2\cdot w_1}{\|w_1\|^2}w_1=(-\tfrac{1}{2},\tfrac{1}{2},0)$.", r"Normiraj svaki vektor."]
    },
    {
        "tekst": r"Je li skup $S=\{(x_1,x_2)\in\mathbb{R}^2: x_1\cdot x_2>0\}$ potprostor od $\mathbb{R}^2$?",
        "tip": "choice",
        "tocan_odgovor": choice("nije potprostor", PS),
        "rjesenje": r"nije potprostor",
        "hints": [r"$(0,0)\notin S$ — potprostor mora sadržavati nul-vektor."]
    },
    {
        "tekst": r"Neka su $L$ i $M$ međusobno različiti potprostori $V$, $\dim L=\dim M=4$, $\dim V=5$. Odredite $\dim(L\cap M)$.",
        "tip": "auto",
        "tocan_odgovor": "3",
        "rjesenje": r"$\dim(L\cap M)=3$",
        "hints": [r"$\dim(L+M)=5$.", r"$\dim(L\cap M)=4+4-5=3$."]
    },
    {
        "tekst": r"Linearan operator $A:\mathbb{R}^3\to\mathbb{R}^3$ zadan je s $A(x_1,x_2,x_3)=(x_1+x_3,\;2x_2,\;x_1+x_2+x_3)$. Odredite matricu $[A]_e$ u kanonskoj bazi.",
        "tip": "matrix",
        "tocan_odgovor": matrix([[1,0,1],[0,2,0],[1,1,1]]),
        "rjesenje": r"$[A]_e=\begin{pmatrix}1&0&1\\0&2&0\\1&1&1\end{pmatrix}$",
        "hints": [r"Stupci: $Ae_1=(1,0,1)$, $Ae_2=(0,2,1)$, $Ae_3=(1,0,1)$."]
    },
    {
        "tekst": r"Je li skup $\{2t^3-t^2+2t+1,\; t^3+4t^2+2t-2,\; t^3-2t^2+t-1\}$ linearno nezavisan u $P_3$?",
        "tip": "choice",
        "tocan_odgovor": choice("jest linearno nezavisan", LN),
        "rjesenje": r"jest linearno nezavisan",
        "hints": [r"Postavi $\alpha p_1+\beta p_2+\gamma p_3=0$ i provjeri determinantu — $\det\neq 0$."]
    },
    {
        "tekst": r"Neka je $V=\mathbb{R}$. Definiramo $x\oplus y=x+y$ i $\alpha\odot x=x$. Je li $V$ vektorski prostor?",
        "tip": "choice",
        "tocan_odgovor": choice("nije vektorski prostor", VP),
        "rjesenje": r"nije vektorski prostor",
        "hints": [r"$\alpha\odot x=x\neq\alpha x$ općenito — ne vrijedi homogenost."]
    },
    {
        "tekst": r"Dana je matrica $A=\begin{pmatrix}2&0&-1\\3&-1&0\\0&0&-1\end{pmatrix}$. Odredite karakteristični polinom, s.v. i minimalni polinom.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "k_A(λ) =", "answer": "-(lam-2)*(lam+1)**2"},
            {"label": "λ₁ =", "answer": "2"},
            {"label": "λ₂ =", "answer": "-1"},
            {"label": "m_A(λ) =", "answer": "(lam-2)*(lam+1)"}
        ]),
        "rjesenje": r"$k_A(\lambda)=-(\lambda-2)(\lambda+1)^2$; $m_A=(\lambda-2)(\lambda+1)$",
        "hints": [r"$\det(A-\lambda I)=0$.", r"Ispitaj poništava li $(A-2I)(A+I)=0$."]
    },
    {
        "tekst": r"Je li $\langle p,q\rangle=(p(0))^2+(q(1))^2$ skalarni produkt na $P_1$?",
        "tip": "choice",
        "tocan_odgovor": choice("nije skalarni produkt", SP),
        "rjesenje": r"nije skalarni produkt",
        "hints": [r"$(p(0)+r(0))^2\neq(p(0))^2+(r(0))^2$ — nije aditivna."]
    },
    {
        "tekst": r"U $\mathbb{R}^3$ zadani su $L=\operatorname{sp}\{(1,2,1),(-1,-1,-1)\}$ i $M=\operatorname{sp}\{(-1,1,-3),(1,0,3)\}$. Odredite $\dim(L+M)$ i $\dim(L\cap M)$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "dim(L+M) =", "answer": "3"},
            {"label": "dim(L∩M) =", "answer": "1"}
        ]),
        "rjesenje": r"$\dim(L+M)=3$, $\dim(L\cap M)=1$",
        "hints": [r"Složite sve generatore i nađite rang.", r"$\dim(L\cap M)=2+2-3=1$."]
    },
    {
        "tekst": r"Neka je $\{e_1,e_2,e_3\}$ baza $V$ i $B:V\to V$: $Be_1=3e_1-2e_2+e_3$, $Be_2=e_1+e_2$, $Be_3=0$. Odredite rang i defekt.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "rang(B) =", "answer": "2"},
            {"label": "defekt(B) =", "answer": "1"}
        ]),
        "rjesenje": r"$\operatorname{rang}=2$, $\operatorname{def}=1$",
        "hints": [r"$Be_3=0\Rightarrow e_3\in\ker B$.", r"$Be_1$ i $Be_2$ su lin. neovisni."]
    },
    {
        "tekst": r"Je li $W=\{A\in M_2(\mathbb{R}): A=A^T,\;\operatorname{tr}(A)=0\}$ potprostor? Odredite $\dim W$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "W je:", "answer": "jest potprostor", "type": "choice", "options": PS},
            {"label": "dim W =", "answer": "2"}
        ]),
        "rjesenje": r"jest potprostor, $\dim W=2$",
        "hints": [r"Opći element: $\begin{pmatrix}a&b\\b&-a\end{pmatrix}$ — 2 slobodna parametra.", r"$\dim W=2$."]
    },
    {
        "tekst": r"Neka je skup $\{a,b,c\}$ linearno nezavisan. Je li $\{2a-b,\;b-c,\;2a+b+2c\}$ linearno nezavisan?",
        "tip": "choice",
        "tocan_odgovor": choice("jest linearno nezavisan", LN),
        "rjesenje": r"jest linearno nezavisan",
        "hints": [r"Matrica transformacije ima $\det\neq 0$."]
    },
    {
        "tekst": r"Linearan operator $A:\mathbb{R}^2\to\mathbb{R}^3$ zadan je s $A(x_1,x_2)=(x_1-x_2,\;2x_1+x_2,\;x_1)$. Odredite $[A]_e^f$ i $[Ax]^f$ za $x=(2,0)$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "[A]_e^f =", "answer": "[[1,-1],[2,1],[1,0]]", "type": "matrix"},
            {"label": "[Ax]^f za x=(2,0) =", "answer": "[[2],[4],[2]]", "type": "matrix"}
        ]),
        "rjesenje": r"$[A]_e^f=\begin{pmatrix}1&-1\\2&1\\1&0\end{pmatrix}$, $[Ax]^f=(2,4,2)^T$",
        "hints": [r"Stupci: $A(1,0)=(1,2,1)$ i $A(0,1)=(-1,1,0)$.", r"$[Ax]^f=[A]_e^f\cdot\begin{pmatrix}2\\0\end{pmatrix}$."]
    },
    {
        "tekst": r"Neka je skup $\{u,v,w\}$ linearno nezavisan. Je li $\{3u+2v-w,\;2u-v+3w,\;9u-v+8w\}$ linearno nezavisan?",
        "tip": "choice",
        "tocan_odgovor": choice("nije linearno nezavisan", LN),
        "rjesenje": r"nije linearno nezavisan",
        "hints": [r"$\det\begin{pmatrix}3&2&-1\\2&-1&3\\9&-1&8\end{pmatrix}=0$."]
    },
    {
        "tekst": r"Je li operator translacije $T:\mathbb{R}^2\to\mathbb{R}^2$, $T(x_1,x_2)=(x_1+a,\;x_2+b)$, $(a,b)\neq(0,0)$, linearan?",
        "tip": "choice",
        "tocan_odgovor": choice("nije linearan", LIN),
        "rjesenje": r"nije linearan",
        "hints": [r"$T(0,0)=(a,b)\neq(0,0)$."]
    },
    {
        "tekst": r"Odredite koja je krivulja dana jednadžbom $2x^2+6xy+2y^2+10x+10y+10=0$.",
        "tip": "choice",
        "tocan_odgovor": choice("hiperbola", KRV),
        "rjesenje": r"hiperbola ($5x'^2-y'^2=5$)",
        "hints": [r"S.v. $\lambda_1=5$, $\lambda_2=-1$ — različitih predznaka $\Rightarrow$ hiperbola."]
    },
    {
        "tekst": r"Neka je $\{e_1,e_2,e_3\}$ baza $V$, $\{f_1,f_2,f_3\}$ baza $W$. $A:V\to W$: $Ae_1=2f_1+3f_2-f_3$, $Ae_2=f_1-f_2+2f_3$, $Ae_3=2f_1+2f_2$. Odredite rang i defekt.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "rang(A) =", "answer": "2"},
            {"label": "defekt(A) =", "answer": "1"}
        ]),
        "rjesenje": r"$\operatorname{rang}=2$, $\operatorname{def}=1$",
        "hints": [r"$Ae_3=Ae_1+Ae_2\Rightarrow$ rang = $2$."]
    },
    {
        "tekst": r"Je li $\langle p,q\rangle=a_2 b_2+a_1 b_1+a_0 b_0$ skalarni produkt na $P_2(\mathbb{R})$?",
        "tip": "choice",
        "tocan_odgovor": choice("jest skalarni produkt", SP),
        "rjesenje": r"jest skalarni produkt",
        "hints": [r"Ekvivalentno standardnom sk. produktu na $\mathbb{R}^3$."]
    },
    {
        "tekst": r"Gram-Schmidtovim postupkom odredite ortonorm. bazu za $U=\operatorname{sp}\{(1,1,1),(1,3,-1)\}$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "u₁ (ortogonalni) =", "answer": "[1, 1, 1]"},
            {"label": "u₂ (ortogonalni) =", "answer": "[0, 2, -2]"},
            {"label": "e₁ =", "answer": "[1/sqrt(3), 1/sqrt(3), 1/sqrt(3)]"},
            {"label": "e₂ =", "answer": "[0, 1/sqrt(2), -1/sqrt(2)]"}
        ]),
        "rjesenje": r"$u_1=(1,1,1)$, $u_2=(0,2,-2)$; $e_1=\frac{1}{\sqrt{3}}(1,1,1)$, $e_2=\frac{1}{\sqrt{2}}(0,1,-1)$",
        "hints": [r"$u_2=v_2-\frac{v_2\cdot u_1}{\|u_1\|^2}u_1=(0,2,-2)$.", r"Normiraj: $e_i=u_i/\|u_i\|$."]
    },
    {
        "tekst": r"Je li $S=\left\{\begin{pmatrix}a&-a\\b&c\end{pmatrix}: a,b,c\in\mathbb{R}\right\}$ potprostor od $M_2(\mathbb{R})$? Odredite $\dim S$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "S je:", "answer": "jest potprostor", "type": "choice", "options": PS},
            {"label": "dim S =", "answer": "3"}
        ]),
        "rjesenje": r"jest potprostor, $\dim S=3$",
        "hints": [r"Zatvoren na zbrajanje i množenje skalarom, sadrži nul-matricu.", r"Tri slobodna parametra $a,b,c\Rightarrow\dim=3$."]
    },
    {
        "tekst": r"Dana je matrica $A=\begin{pmatrix}-1&0&2\\3&2&1\\0&0&1\end{pmatrix}$. Odredite s.v. i izračunajte $A^6$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "λ₁ =", "answer": "-1"},
            {"label": "λ₂ =", "answer": "2"},
            {"label": "λ₃ =", "answer": "1"},
            {"label": "A^6 =", "answer": "[[1,0,126],[63,64,63],[0,0,1]]", "type": "matrix"}
        ]),
        "rjesenje": r"$\lambda_1=-1,\lambda_2=2,\lambda_3=1$; $A^6=\begin{pmatrix}1&0&126\\63&64&63\\0&0&1\end{pmatrix}$",
        "hints": [r"Tri različite s.v. $\Rightarrow$ dijagonalizabilna.", r"$A^6=S\operatorname{diag}(1,64,1)S^{-1}$."]
    },
    {
        "tekst": r"Linearan operator $A:\mathbb{R}^2\to\mathbb{R}^2$ zadan je s $A(x_1,x_2)=(x_1+x_2,\;x_1-x_2)$. (a) Je li $A$ hermitski? (b) Je li $A$ unitaran?",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "A je hermitski:", "answer": "jest hermitski", "type": "choice", "options": HRM},
            {"label": "A je unitaran:", "answer": "nije unitaran", "type": "choice", "options": UNI}
        ]),
        "rjesenje": r"jest hermitski; nije unitaran",
        "hints": [r"Matrica $\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ je simetrična $\Rightarrow$ hermitski.", r"$A^T A=2I\neq I\Rightarrow$ nije unitaran."]
    },
    {
        "tekst": r"U $\mathbb{R}^4$ zadani su $L=\operatorname{sp}\{(1,1,1,2),(-1,1,0,-3),(2,0,1,5)\}$ i $M=\operatorname{sp}\{(0,1,1,4),(0,1,0,-5),(0,-1,1,14)\}$. Odredite $\dim(L+M)$ i $\dim(L\cap M)$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "dim(L+M) =", "answer": "4"},
            {"label": "dim(L∩M) =", "answer": "1"}
        ]),
        "rjesenje": r"$\dim(L+M)=4$, $\dim(L\cap M)=1$",
        "hints": [r"Rang svih 6 generatora = $\dim(L+M)$.", r"Grassmanova formula."]
    },
    {
        "tekst": r"Je li $F:\mathbb{R}^3\to\mathbb{R}^2$, $F(x,y,z)=(x+y,\;z^2)$ linearan?",
        "tip": "choice",
        "tocan_odgovor": choice("nije linearan", LIN),
        "rjesenje": r"nije linearan",
        "hints": [r"$z^2$ nije linearna u $z$."]
    },
    {
        "tekst": r"Je li $\langle x,y\rangle=5x_1 y_1-x_1 y_2-x_2 y_1+x_2 y_2$ skalarni produkt na $\mathbb{R}^2$?",
        "tip": "choice",
        "tocan_odgovor": choice("jest skalarni produkt", SP),
        "rjesenje": r"jest skalarni produkt",
        "hints": [r"Gramova matrica $G=\begin{pmatrix}5&-1\\-1&1\end{pmatrix}$: $\det G=4>0$, $5>0$ $\Rightarrow$ poz. definitna."]
    },
    {
        "tekst": r"Neka je $W=\{p\in P_3(\mathbb{R}): p_1-p_2-p_3=0,\;3p_2-2p_4=0\}$. Je li $W$ potprostor? Odredite $\dim W$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "W je:", "answer": "jest potprostor", "type": "choice", "options": PS},
            {"label": "dim W =", "answer": "2"}
        ]),
        "rjesenje": r"jest potprostor, $\dim W=2$",
        "hints": [r"Homogeni uvjeti čuvaju se pri zbrajanju.", r"2 slobodna parametra $\Rightarrow\dim=2$."]
    },
    {
        "tekst": r"Potprostor $U\le\mathbb{C}^3$ razapet je vektorom $(i,-i,-1)$. Odredite ortonorm. bazu $U^\perp$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "dim(U⊥) =", "answer": "2"},
            {"label": "e₁ =", "answer": "[1/sqrt(2), 0, -I/sqrt(2)]"},
            {"label": "e₂ =", "answer": "[-I/sqrt(6), -2*I/sqrt(6), 1/sqrt(6)]"}
        ]),
        "rjesenje": r"$\dim U^\perp=2$; $e_1=\frac{1}{\sqrt{2}}(1,0,-i)$, $e_2=\frac{1}{\sqrt{6}}(-i,-2i,1)$",
        "hints": [r"Nađi 2 vektora $\perp(i,-i,-1)$ s kompleksnim sk. produktom.", r"Gram-Schmidt s $\langle x,y\rangle=\sum x_k\bar{y}_k$."]
    },
    {
        "tekst": r"Neka matrica $A$ ima s.v. $\lambda_1=1$ ($v_1=(1,1,-4)^T$), $\lambda_2=-1$ ($v_2=(1,2,-1)^T$) i $\lambda_3=2$ ($v_3=(0,1,1)^T$). Je li $A$ dijagonalizabilna? Zapišite $S$ i $D$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Je li dijagonalizabilna?", "answer": "da", "type": "choice", "options": DA_NE},
            {"label": "S =", "answer": "[[1,1,0],[1,2,1],[-4,-1,1]]", "type": "matrix"},
            {"label": "D =", "answer": "[[1,0,0],[0,-1,0],[0,0,2]]", "type": "matrix"}
        ]),
        "rjesenje": r"dijagonalizabilna; $S=\begin{pmatrix}1&1&0\\1&2&1\\-4&-1&1\end{pmatrix}$, $D=\operatorname{diag}(1,-1,2)$",
        "hints": [r"Stupci $S$ su s.v. koji odgovaraju s.v. na dijagonali $D$.", r"$A=SDS^{-1}$."]
    },
    {
        "tekst": r"Linearan operator $A:\mathbb{R}^2\to\mathbb{R}^3$ zadan je s $A(x_1,x_2)=(3x_1-2x_2,\;x_2,\;x_1+2x_2)$. Odredite $[A]_e^f$ i $[Ax]^f$ za $x=(1,2)$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "[A]_e^f =", "answer": "[[3,-2],[0,1],[1,2]]", "type": "matrix"},
            {"label": "[Ax]^f za x=(1,2) =", "answer": "[[-1],[2],[5]]", "type": "matrix"}
        ]),
        "rjesenje": r"$[A]_e^f=\begin{pmatrix}3&-2\\0&1\\1&2\end{pmatrix}$, $[Ax]^f=(-1,2,5)^T$",
        "hints": [r"Stupci: $A(1,0)=(3,0,1)$ i $A(0,1)=(-2,1,2)$.", r"$A(1,2)=(-1,2,5)$."]
    },
    {
        "tekst": r"Matrica $A$ ima s.v. $\lambda_1=-1$ ($v_1=(1,0)$) i $\lambda_2=1$ ($v_2=(1,1)$). Izračunajte $A^7$.",
        "tip": "matrix",
        "tocan_odgovor": matrix([[-1,0],[0,1]]),
        "rjesenje": r"$A^7=\begin{pmatrix}-1&0\\0&1\end{pmatrix}$",
        "hints": [r"$(-1)^7=-1$, $1^7=1$, pa $A^7=A$."]
    },
    {
        "tekst": r"Neka je $V=\mathbb{R}^2$, $x\oplus y=(x_1+y_1,\;x_2 y_2-1)$, $\alpha\odot x=e^\alpha\cdot x$. Je li $V$ vektorski prostor?",
        "tip": "choice",
        "tocan_odgovor": choice("nije vektorski prostor", VP),
        "rjesenje": r"nije vektorski prostor",
        "hints": [r"$1\odot(x_1,x_2)=e\cdot(x_1,x_2)\neq(x_1,x_2)$."]
    },
    {
        "tekst": r"Linearan operator $A:\mathbb{R}^3\to\mathbb{R}^2$ zadan je s $A(x_1,x_2,x_3)=(2x_2+x_3,\;x_1-x_2+x_3)$. Odredite $[A]_e^f$ i $[Ax]^f$ za $x=(2,3,1)$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "[A]_e^f =", "answer": "[[0,2,1],[1,-1,1]]", "type": "matrix"},
            {"label": "[Ax]^f za x=(2,3,1) =", "answer": "[[7],[-1]]", "type": "matrix"}
        ]),
        "rjesenje": r"$[A]_e^f=\begin{pmatrix}0&2&1\\1&-1&1\end{pmatrix}$, $[Ax]^f=(7,-1)^T$",
        "hints": [r"Stupci: $A(1,0,0)=(0,1)$, $A(0,1,0)=(2,-1)$, $A(0,0,1)=(1,1)$.", r"$A(2,3,1)=(7,-1)$."]
    },
    {
        "tekst": r"Linearan operator $A:\mathbb{R}^3\to\mathbb{R}^3$: $A(x_1,x_2,x_3)=\left(\frac{\sqrt{2}}{2}x_1+\frac{\sqrt{2}}{2}x_2,\;x_3,\;-\frac{\sqrt{2}}{2}x_1+\frac{\sqrt{2}}{2}x_2\right)$. Je li unitaran? Je li hermitski?",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "A je unitaran:", "answer": "jest unitaran", "type": "choice", "options": UNI},
            {"label": "A je hermitski:", "answer": "nije hermitski", "type": "choice", "options": HRM}
        ]),
        "rjesenje": r"jest unitaran; nije hermitski",
        "hints": [r"Provjeri $A^T A=I$.", r"Matrica nije simetrična $\Rightarrow$ nije hermitski."]
    },
    {
        "tekst": r"Linearan operator $A:\mathbb{C}^3\to\mathbb{C}^3$: $A(x_1,x_2,x_3)=(x_1-ix_2,\;ix_1+x_3(1+i),\;x_2(1-i)+x_3)$. Je li hermitski? Je li unitaran?",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "A je hermitski:", "answer": "nije hermitski", "type": "choice", "options": HRM},
            {"label": "A je unitaran:", "answer": "nije unitaran", "type": "choice", "options": UNI}
        ]),
        "rjesenje": r"nije hermitski; nije unitaran",
        "hints": [r"Provjeri $[A]_e\stackrel{?}{=}[A]_e^*$.", r"Za unitarnost: $A^*A\stackrel{?}{=}I$."]
    },
    {
        "tekst": r"Za koje vrijednosti $k\in\mathbb{R}$ je skup $\left\{\begin{pmatrix}k&1\\1&1\end{pmatrix}, \begin{pmatrix}1&0\\0&1\end{pmatrix}, \begin{pmatrix}1&k\\1&0\end{pmatrix}, \begin{pmatrix}-1&1\\k&0\end{pmatrix}\right\}$ baza $M_2(\mathbb{R})$?",
        "tip": "auto",
        "tocan_odgovor": "ne postoji",
        "rjesenje": r"Za sve $k\in\mathbb{R}\setminus\{-1,1\}$",
        "hints": [r"Determinanta matrice koeficijenata mora biti $\neq 0$.", r"Nulira se za $k=-1$ i $k=1$."]
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