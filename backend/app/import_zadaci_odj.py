"""
Import zadataka za kolegij "Obicne diferencijalne jednadzbe".
Pokretanje: python -m app.import_zadaci_odj
"""

import json
from .database import Base, engine, SessionLocal
from . import models

COURSE_NAME = "Obicne diferencijalne jednadzbe"

def multi(fields):
    return json.dumps(fields, ensure_ascii=False)

ZADACI = [
    {
        "tekst": r"Crna rupa nastaje s početnom masom $6\times10^{31}$ kg. Zakon: $m'\cdot m^2=k$, $k=-1{,}26\times10^{23}$ kg³/god. "
                 r"Koliko dugo je potrebno crnoj rupi da potpuno nestane? Odgovorite u godinama u obliku $\frac{a}{b}\times 10^{72}$.",
        "tip": "auto",
        "tocan_odgovor": "Rational(4,7)*10**72",
        "rjesenje": "Rational(4,7)*10**72",
        "hints": [
            r"Separacija varijabli: $m^2\,\mathrm{d}m = k\,\mathrm{d}t \Rightarrow m^3 = 3kt + c$, $c=m(0)^3=(6\times10^{31})^3=2{,}16\times10^{95}$.",
            r"$m(t)=0$: $t=-c/(3k)=2{,}16\times10^{95}/(3\times1{,}26\times10^{23})=(4/7)\times10^{72}$."
        ]
    },
    {
        "tekst": r"Nuklearni reaktor: za $15$ godina raspadne se $0{,}043\%$ početne količine plutonija $239$. "
                 r"Odredite vrijeme poluraspada (u godinama, zaokruženo na $2$ decimale).",
        "tip": "auto",
        "tocan_odgovor": "24174.37",
        "rjesenje": "24174.37",
        "hints": [
            r"$y(x)=y_0 e^{kx}$; iz $y(15)=0{,}99957\,y_0$: $k=\ln(0{,}99957)/15$.",
            r"$T_{1/2}=\ln(0{,}5)/k=15\ln 2/(-\ln 0{,}99957)\approx 24174{,}37$."
        ]
    },
    {
        "tekst": r"Građevinska firma prekopava površinu $400$ m². Brzina prekapanja proporcionalna je razlici "
                 r"ukupne i već prekopanoj površini. Za $2$ dana prekopano $80$ m². "
                 r"Koliko dana je potrebno za prekopati pola površine?",
        "tip": "auto",
        "tocan_odgovor": "2*log(2)/log(Rational(5,4))",
        "rjesenje": "2*log(2)/log(Rational(5,4))",
        "hints": [
            r"$y'=k(400-y)$, $y(0)=0$, $y(2)=80$. Rješenje: $y(x)=400(1-e^{-kx})$.",
            r"Iz $y(2)=80$: $e^{-2k}=4/5\Rightarrow k=\ln(5/4)/2$. Za $y=200$: $x=2\ln2/\ln(5/4)$."
        ]
    },
    {
        "tekst": r"Dana je Cauchyjeva zadaća $y'=(x-x^2)(y-1)$, $y(0)=-1$. Odredite $u_1(x)$ (prvu Picardovu iteraciju).",
        "tip": "auto",
        "tocan_odgovor": "-1 - x**2 + Rational(2,3)*x**3",
        "rjesenje": "-1 - x**2 + Rational(2,3)*x**3",
        "hints": [
            r"$u_0(x)=-1$; $u_1(x)=y_0+\int_0^x f(s,u_0(s))\,\mathrm{d}s$.",
            r"$f(s,-1)=(s-s^2)(-1-1)=-2s+2s^2$. $u_1=-1+\int_0^x(-2s+2s^2)\,\mathrm{d}s=-1-x^2+\frac{2}{3}x^3$."
        ]
    },
    {
        "tekst": r"Za zadaću $y'=(x-x^2)(y-1)$, $y(0)=-1$ odredite $u_2(x)$ (drugu Picardovu iteraciju).",
        "tip": "auto",
        "tocan_odgovor": "-1 - x**2 + Rational(2,3)*x**3 - x**4/4 + x**5/3 - x**6/9",
        "rjesenje": "-1 - x**2 + Rational(2,3)*x**3 - x**4/4 + x**5/3 - x**6/9",
        "hints": [
            r"$u_2(x)=-1+\int_0^x(s-s^2)(u_1(s)-1)\,\mathrm{d}s$.",
            r"$(u_1-1)=-x^2+\frac{2}{3}x^3$; pomnožite s $(s-s^2)$ i integrirajte."
        ]
    },
    {
        "tekst": r"Dana je Cauchyjeva zadaća $y'=x^2 y-x$, $y(0)=1$. Odredite $u_1(x)$ (prvu Picardovu iteraciju).",
        "tip": "auto",
        "tocan_odgovor": "1 - x**2/2 + x**3/3",
        "rjesenje": "1 - x**2/2 + x**3/3",
        "hints": [
            r"$u_0=1$; $u_1=1+\int_0^x(s^2\cdot u_0-s)\,\mathrm{d}s=1+\int_0^x(s^2-s)\,\mathrm{d}s$.",
        ]
    },
    {
        "tekst": r"Za zadaću $y'=x^2 y-x$, $y(0)=1$ odredite $u_2(x)$ (drugu Picardovu iteraciju).",
        "tip": "auto",
        "tocan_odgovor": "1 - x**2/2 + x**3/3 - x**5/10 + x**6/18",
        "rjesenje": "1 - x**2/2 + x**3/3 - x**5/10 + x**6/18",
        "hints": [
            r"$u_2=1+\int_0^x(s^2\cdot u_1(s)-s)\,\mathrm{d}s$; uvrstite $u_1$ i integrirajte.",
        ]
    },
    {
        "tekst": r"Riješite Cauchyjevu zadaću $e^{2x+y}\cdot y'=2$, $y(0)=0$.",
        "tip": "auto",
        "tocan_odgovor": "log(2-exp(-2*x))",
        "rjesenje": "log(2-exp(-2*x))",
        "hints": [
            r"Separacija varijabli: $e^y\,\mathrm{d}y=2e^{-2x}\,\mathrm{d}x\Rightarrow e^y=-e^{-2x}+C$.",
            r"Iz $y(0)=0$: $1=-1+C\Rightarrow C=2$. Dakle $y=\ln(2-e^{-2x})$."
        ]
    },
    {
        "tekst": r"Riješite Cauchyjevu zadaću $xy'-\ln(y^y)=y-\ln(x^y)$, $y(1)=e$.",
        "tip": "auto",
        "tocan_odgovor": "x*exp(x)",
        "rjesenje": "x*exp(x)",
        "hints": [
            r"Jednadžba se svodi na $y'-\frac{y}{x}\ln\frac{y}{x}=\frac{y}{x}(1-\ln x)$. Supstitucija $y=zx$.",
            r"$z'x=z\ln z$; separacija: $\frac{\mathrm{d}z}{z\ln z}=\frac{\mathrm{d}x}{x}$. $\ln(\ln z)=\ln x+C$. Iz $y(1)=e$: $C=0$."
        ]
    },
    {
        "tekst": r"Riješite Cauchyjevu zadaću $3(1+x^2)y'=2xy(y^3-1)$, $y(0)=1$.",
        "tip": "auto",
        "tocan_odgovor": "1",
        "rjesenje": "1",
        "hints": [
            r"Bernoulllijeva jednadžba: $z=y^{-3}$, $z'-(2x/(1+x^2))z=-2x/(1+x^2)$.",
            r"Opće rješenje: $y=(1+D(1+x^2))^{-1/3}$. Iz $y(0)=1$: $D=0\Rightarrow y=1$."
        ]
    },
    {
        "tekst": r"Riješite Cauchyjevu zadaću $y'\cos x-y(\sin x+y^3\cos^2 x)=0$, $y(0)=0$.",
        "tip": "auto",
        "tocan_odgovor": "0",
        "rjesenje": "0",
        "hints": [
            r"Bernoulllijeva jednadžba po $z=y^{-3}$: $z'+3z\tan x=-3\cos x$.",
            r"Iz $y(0)=0$: trivijalno rješenje $y\equiv 0$."
        ]
    },
    {
        "tekst": r"Odredite sve konstante $c\in\mathbb{R}$ za koje su $f(x)=cx^2$ rješenja jednadžbe "
                 r"$x^3y'+x^2y-y^2=2x^4$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "c₁ =", "answer": "1"},
            {"label": "c₂ =", "answer": "2"}
        ]),
        "rjesenje": multi([
            {"label": "c₁ =", "answer": "1"},
            {"label": "c₂ =", "answer": "2"}
        ]),
        "hints": [
            r"Uvrstite $y=cx^2$: $x^3\cdot 2cx+x^2\cdot cx^2-c^2x^4=2x^4$.",
            r"$3cx^4-c^2x^4=2x^4\Rightarrow c(3-c)=2\Rightarrow c^2-3c+2=0\Rightarrow c=1,\,2$."
        ]
    },
    {
        "tekst": r"Odredite karakteristične korijene homogene jednadžbe $y^{(4)}-4y=0$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "λ₁ =", "answer": "sqrt(2)"},
            {"label": "λ₂ =", "answer": "-sqrt(2)"},
            {"label": "λ₃ =", "answer": "sqrt(2)*I"},
            {"label": "λ₄ =", "answer": "-sqrt(2)*I"}
        ]),
        "rjesenje": multi([
            {"label": "λ₁ =", "answer": "sqrt(2)"},
            {"label": "λ₂ =", "answer": "-sqrt(2)"},
            {"label": "λ₃ =", "answer": "sqrt(2)*I"},
            {"label": "λ₄ =", "answer": "-sqrt(2)*I"}
        ]),
        "hints": [
            r"Karakteristična jednadžba: $\lambda^4-4=0\Rightarrow\lambda^4=4$.",
            r"$\lambda^2=\pm 2\Rightarrow\lambda=\pm\sqrt{2}$ ili $\lambda=\pm i\sqrt{2}$."
        ]
    },
    {
        "tekst": r"Odredite karakteristične korijene homogene jednadžbe $y^{(4)}+y''-2y=0$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "λ₁ =", "answer": "1"},
            {"label": "λ₂ =", "answer": "-1"},
            {"label": "λ₃ =", "answer": "sqrt(2)*I"},
            {"label": "λ₄ =", "answer": "-sqrt(2)*I"}
        ]),
        "rjesenje": multi([
            {"label": "λ₁ =", "answer": "1"},
            {"label": "λ₂ =", "answer": "-1"},
            {"label": "λ₃ =", "answer": "sqrt(2)*I"},
            {"label": "λ₄ =", "answer": "-sqrt(2)*I"}
        ]),
        "hints": [
            r"Supstitucija $\mu=\lambda^2$: $\mu^2+\mu-2=0\Rightarrow\mu=1$ ili $\mu=-2$.",
            r"$\lambda^2=1\Rightarrow\lambda=\pm 1$; $\lambda^2=-2\Rightarrow\lambda=\pm i\sqrt{2}$."
        ]
    },
    {
        "tekst": r"Odredite partikularno rješenje jednadžbe $y^{(4)}-4y=7te^{2t}$.",
        "tip": "auto",
        "tocan_odgovor": "(7*t/12 - 14/9)*exp(2*t)",
        "rjesenje": "(7*t/12 - 14/9)*exp(2*t)",
        "hints": [
            r"Pretpostavka: $y_p=(At+B)e^{2t}$. Karakteristična jednadžba nema $\lambda=2$.",
            r"Uvrstite $y_p$ u jednadžbu i izjednačite koeficijente: $A=7/12$, $B=-14/9$."
        ]
    },
    {
        "tekst": r"Odredite partikularno rješenje jednadžbe $y^{(4)}+y''-2y=-3\cos x$.",
        "tip": "auto",
        "tocan_odgovor": "3*cos(x)/2",
        "rjesenje": "3*cos(x)/2",
        "hints": [
            r"Pretpostavka: $y_p=A\cos x+B\sin x$ (jer $\lambda=\pm i$ nisu korijeni karakteristične jednadžbe $\lambda^4+\lambda^2-2=0$).",
            r"Uvrstite: $A+(-A)-2A\cos x=(-2A)\cos x=-3\cos x\Rightarrow A=3/2$, $B=0$."
        ]
    },
    {
        "tekst": r"Odredite partikularno rješenje jednadžbe $y'''-3y''+3y'=(2x-3)e^{-x}$.",
        "tip": "auto",
        "tocan_odgovor": "-(2*x/7 + 3/49)*exp(-x)",
        "rjesenje": "-(2*x/7 + 3/49)*exp(-x)",
        "hints": [
            r"Karakteristični korijeni: $0$, $\frac{3\pm i\sqrt{3}}{2}$. Budući da $-1$ nije korijen, pretpostavite $y_p=(Ax+B)e^{-x}$.",
            r"Uvrstite u jednadžbu i izjednačite koeficijente uz $xe^{-x}$ i $e^{-x}$."
        ]
    },
    {
        "tekst": r"Odredite svojstvene vrijednosti matrice sustava $\mathbf{y}'=A\mathbf{y}$ za "
                 r"$A=\begin{pmatrix}-2&2&1\\-7&4&2\\5&0&0\end{pmatrix}$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "λ₁ =", "answer": "0"},
            {"label": "λ₂ =", "answer": "1"},
            {"label": "λ₃ (višestrukost 2) =", "answer": "1"}
        ]),
        "rjesenje": multi([
            {"label": "λ₁ =", "answer": "0"},
            {"label": "λ₂ =", "answer": "1"},
            {"label": "λ₃ (višestrukost 2) =", "answer": "1"}
        ]),
        "hints": [
            r"Karakteristična jednadžba: $\det(A-\lambda I)=-\lambda(\lambda-1)^2=0$.",
        ]
    },
    {
        "tekst": r"Odredite svojstvene vrijednosti matrice sustava $\mathbf{y}'=A\mathbf{y}$ za "
                 r"$A=\begin{pmatrix}-1&2&0\\1&-2&1\\6&-12&4\end{pmatrix}$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "λ₁ (višestrukost 2) =", "answer": "0"},
            {"label": "λ₂ =", "answer": "1"}
        ]),
        "rjesenje": multi([
            {"label": "λ₁ (višestrukost 2) =", "answer": "0"},
            {"label": "λ₂ =", "answer": "1"}
        ]),
        "hints": [
            r"Karakteristična jednadžba: $\det(A-\lambda I)=-\lambda^2(\lambda-1)=0$.",
        ]
    },
    {
        "tekst": r"Laplaceovom transformacijom riješite $y''+4y'+5y=\delta(t-2)$, $y(0)=0$, $y'(0)=1$. "
                 r"Upišite homogeni dio rješenja (bez Heavisidea) i prisilni dio (koeficijent uz $u(t-2)$).",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Homogeni dio:", "answer": "exp(-2*t)*sin(t)"},
            {"label": "Prisilni koef. uz u(t-2):", "answer": "exp(-2*(t-2))*sin(t-2)"}
        ]),
        "rjesenje": multi([
            {"label": "Homogeni dio:", "answer": "exp(-2*t)*sin(t)"},
            {"label": "Prisilni koef. uz u(t-2):", "answer": "exp(-2*(t-2))*sin(t-2)"}
        ]),
        "hints": [
            r"$\mathcal{L}\{y''+4y'+5y\}=(s^2+4s+5)Y-s\cdot0-1=e^{-2s}$.",
            r"$Y=\frac{1}{(s+2)^2+1}+\frac{e^{-2s}}{(s+2)^2+1}$; inverzna transformacija s teoremom pomaka."
        ]
    },
    {
        "tekst": r"Laplaceovom transformacijom riješite $y''+3y=s(t-2)$, $y(0)=3$, $y'(0)=1$. "
                 r"Upišite homogeni dio i koeficijent uz $u(t-2)$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Homogeni dio:", "answer": "3*cos(sqrt(3)*t) + sin(sqrt(3)*t)/sqrt(3)"},
            {"label": "Koef. uz u(t-2):", "answer": "Rational(1,3)*(1 - cos(sqrt(3)*(t-2)))"}
        ]),
        "rjesenje": multi([
            {"label": "Homogeni dio:", "answer": "3*cos(sqrt(3)*t) + sin(sqrt(3)*t)/sqrt(3)"},
            {"label": "Koef. uz u(t-2):", "answer": "Rational(1,3)*(1 - cos(sqrt(3)*(t-2)))"}
        ]),
        "hints": [
            r"$(s^2+3)Y=3s+1+\frac{e^{-2s}}{s^2}$... pažnja: $s(t-2)$ je rampa $\Rightarrow\mathcal{L}=\frac{e^{-2s}}{s^2}$.",
            r"Parcijalni razlomci za $\frac{1}{s^2(s^2+3)}=\frac{1/3}{s^2}-\frac{1/3}{s^2+3}$."
        ]
    },
    {
        "tekst": r"Laplaceovom transformacijom riješite $3y''+6y'+12y=\delta(t-2)$, $y(0)=0$, $y'(0)=-1$. "
                 r"Upišite homogeni dio i koeficijent uz $u(t-2)$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Homogeni dio:", "answer": "-exp(-t)*sin(sqrt(3)*t)/sqrt(3)"},
            {"label": "Koef. uz u(t-2):", "answer": "exp(-(t-2))*sin(sqrt(3)*(t-2))/(3*sqrt(3))"}
        ]),
        "rjesenje": multi([
            {"label": "Homogeni dio:", "answer": "-exp(-t)*sin(sqrt(3)*t)/sqrt(3)"},
            {"label": "Koef. uz u(t-2):", "answer": "exp(-(t-2))*sin(sqrt(3)*(t-2))/(3*sqrt(3))"}
        ]),
        "hints": [
            r"$3(s^2+2s+4)Y=-3+e^{-2s}$. $s^2+2s+4=(s+1)^2+3$.",
            r"Inverzna LT: $\mathcal{L}^{-1}\{\frac{1}{(s+1)^2+3}\}=\frac{1}{\sqrt{3}}e^{-t}\sin(\sqrt{3}\,t)$."
        ]
    },
    {
        "tekst": r"Riješite jednadžbu $y^{(4)}+y''-2y=-3\cos x$. Upišite samo partikularno rješenje.",
        "tip": "auto",
        "tocan_odgovor": "3*cos(x)/2",
        "rjesenje": "3*cos(x)/2",
        "hints": [
            r"$\lambda^4+\lambda^2-2=0\Rightarrow(\lambda^2-1)(\lambda^2+2)=0\Rightarrow\lambda=\pm1,\,\pm i\sqrt{2}$.",
            r"$\lambda=\pm i$ nisu korijeni, pretpostavka $y_p=A\cos x+B\sin x$ daje $A=3/2$, $B=0$."
        ]
    },
    {
        "tekst": r"Singularno rješenje jednadžbe $xy'-y=\frac{5}{2}(y'^3-y')$ zadano je relacijom $135y^2=(2x+a)^3$. "
                 r"Koliko iznosi $a$?",
        "tip": "auto",
        "tocan_odgovor": "5",
        "rjesenje": "5",
        "hints": [
            r"Clairautov oblik: $y=xp-\frac{5}{2}(p^3-p)$. Uvjet za singularno rješenje: $\frac{\partial f}{\partial p}=0$.",
            r"$x=\frac{5}{2}(3p^2-1)\Rightarrow p=\pm\sqrt{(2x+5)/15}$. Uvrstite u $y$ i eliminirajte $p$."
        ]
    },
    {
        "tekst": r"Riješite Cauchyjevu zadaću $y''-y''\,y^2+y\,y'^2=0$, $y(0)=0$, $y'(0)=2$.",
        "tip": "auto",
        "tocan_odgovor": "sin(2*x)",
        "rjesenje": "sin(2*x)",
        "hints": [
            r"Supstitucija $y'=p(y)$: $y''=p'p$. Jednadžba: $p'p(1-y^2)+yp^2=0$.",
            r"Separacija: $\frac{p'}{p}=\frac{-y}{1-y^2}$. $p^2=C(1-y^2)$. Iz $y'(0)=2$: $C=4$.",
            r"$\frac{\mathrm{d}y}{\sqrt{1-y^2}}=\pm 2\,\mathrm{d}x$. Iz $y(0)=0$: $y=\sin(2x)$."
        ]
    },
    {
        "tekst": r"Riješite zadaću $\mathbf{y}'=A\mathbf{y}$ za $A=[[-2,2,1],[-7,4,2],[5,0,0]]$, $\mathbf{y}(0)=(0,1,2)^T$. "
                 r"Kolika je prva komponenta $y_1(t)$?",
        "tip": "auto",
        "tocan_odgovor": "4*t*exp(t)",
        "rjesenje": "4*t*exp(t)",
        "hints": [
            r"Svojstvene vrijednosti: $\lambda_1=0$, $\lambda_2=\lambda_3=1$. Za $\lambda=1$ postoji generalizirani s.v.",
            r"Opće rješenje: $y=c_1v_1+e^t(c_2v_2+c_3(tv_2+w))$. Uvrstite $y(0)=(0,1,2)^T$."
        ]
    },
    {
        "tekst": r"Za jednadžbu $y''-y''\,y^2+y\,y'^2=0$ s uvjetima $y(0)=0$, $y'(0)=2$ — "
                 r"kojom brzinom se mijenja $y$ u ishodištu?",
        "tip": "auto",
        "tocan_odgovor": "2",
        "rjesenje": "2",
        "hints": [r"Početni uvjet direktno daje $y'(0)=2$."]
    },
    {
        "tekst": r"Riješite Cauchyjevu zadaću $\mathbf{y}'=A\mathbf{y}$ za $A=[[4,-1,-1],[5,-2,-2],[4,0,0]]$. "
                 r"Koje su svojstvene vrijednosti matrice $A$?",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "λ₁ =", "answer": "0"},
            {"label": "λ₂ (višestrukost 2) =", "answer": "1"}
        ]),
        "rjesenje": multi([
            {"label": "λ₁ =", "answer": "0"},
            {"label": "λ₂ (višestrukost 2) =", "answer": "1"}
        ]),
        "hints": [
            r"$\det(A-\lambda I)=-\lambda(\lambda-1)^2=0$.",
        ]
    },
    {
        "tekst": r"Egzaktna jednadžba: $2(\cos x+e^{y^2})\,\mathrm{d}y=y\sin x\,\mathrm{d}x$. "
                 r"Upišite potencijal $F(x,y)$ (bez konstante) u obliku prikladnom za provjeru.",
        "tip": "auto",
        "tocan_odgovor": "-y**2*cos(x) - exp(y**2)",
        "rjesenje": r"$y^2 \cos x + e^{y^2}$",
        "hints": [
            r"Množite s $\mu(y)=y$: jednadžba postaje egzaktna. $M=y^2\sin x$, $N=-2y\cos x-2ye^{y^2}$.",
            r"$F=\int M\,\mathrm{d}x=-y^2\cos x+\phi(y)$. Iz $F_y=N$: $\phi'(y)=-2ye^{y^2}\Rightarrow\phi=-e^{y^2}$."
        ]
    },
    {
        "tekst": r"Riješite jednadžbu $(yx^2+y\ln y)\,\mathrm{d}x-(1-x)\,\mathrm{d}y=0$. "
                 r"Upišite potencijal $F(x,y)$ (bez konstante).",
        "tip": "auto",
        "tocan_odgovor": "x**3/3 + x*log(y) - log(y)",
        "rjesenje": "x**3/3 + x*log(y) - log(y)",
        "hints": [
            r"Integrirajući faktor $\mu(y)=1/y$: jednadžba postaje egzaktna. $M=(x^2+\ln y)$, $N=(x-1)/y$.",
            r"$F=\int M\,\mathrm{d}x=x^3/3+x\ln y+\phi(y)$. Iz $F_y=N$: $\phi'=-1/y\Rightarrow\phi=-\ln|y|$."
        ]
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