"""
Import 48 zadataka za kolegij "Integralni racun".
Pokretanje: python -m app.import_zadaci_int
"""

import json
from .database import Base, engine, SessionLocal
from . import models

COURSE_NAME = "Integralni racun"

def multi(fields):
    """Više potpitanja s tekstualnim unosom."""
    return json.dumps(fields, ensure_ascii=False)

def choice(answer, options):
    """Jedno potpitanje s kliktanjem na jednu od ponuđenih opcija."""
    return json.dumps({"answer": answer, "options": options}, ensure_ascii=False)

KONV   = ["apsolutno konvergira", "uvjetno konvergira", "divergira"]
KONV_I = ["konvergira", "divergira"]

ZADACI = [
    {
        "tekst": r"Riješite integral $\displaystyle\int \sin^3 x \cos^2 x\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "cos(x)**5/5 - cos(x)**3/3",
        "rjesenje": r"$\dfrac{1}{5}\cos^5 x - \dfrac{1}{3}\cos^3 x + C$",
        "hints": [r"Rastavi $\sin^3 x = \sin x\,(1-\cos^2 x)$.", r"Uvedi supstituciju $u = \cos x$."]
    },
    {
        "tekst": r"Ispitajte konvergenciju reda $\displaystyle\sum_{n=1}^{\infty} \arctan\!\left(\frac{2^n}{n}\right)$.",
        "tip": "choice",
        "tocan_odgovor": choice("divergira", KONV),
        "rjesenje": r"divergira",
        "hints": [r"Izračunaj $\lim_{n\to\infty}\frac{2^n}{n}$ — eksponencijalna raste brže od linearne.", r"Ako $\lim a_n\neq 0$, red divergira."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int (x+3)\ln(x+2)\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "(x**2+6*x+8)/2 * log(x+2) - x**2/4 - x",
        "rjesenje": r"$\dfrac{x^2+6x+8}{2}\ln(x+2)-\dfrac{x^2}{4}-x+C$",
        "hints": [r"Parcijalna integracija: $u=\ln(x+2)$, $\mathrm{d}v=(x+3)\,\mathrm{d}x$.", r"$\mathrm{d}u=\frac{\mathrm{d}x}{x+2}$."]
    },
    {
        "tekst": r"Ispitajte konvergenciju reda $\displaystyle\sum_{n=1}^{\infty} (-1)^n \left(\frac{n-1}{n+1}\right)^{n(n+1)}$.",
        "tip": "choice",
        "tocan_odgovor": choice("apsolutno konvergira", KONV),
        "rjesenje": r"apsolutno konvergira",
        "hints": [r"Primijeni Cauchyjev korijenski kriterij na red apsolutnih vrijednosti.", r"$\lim\left(1-\frac{2}{n+1}\right)^n = e^{-2} < 1$."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int \frac{x^2}{\sqrt{9-x^2}}\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "9/2*asin(x/3) - x/2*sqrt(9-x**2)",
        "rjesenje": r"$\dfrac{9}{2}\arcsin\dfrac{x}{3}-\dfrac{x}{2}\sqrt{9-x^2}+C$",
        "hints": [r"Trigonometrijska supstitucija $x=3\sin t$.", r"$\int\sin^2 t\,\mathrm{d}t = \frac{1}{2}(t-\sin t\cos t)$."]
    },
    {
        "tekst": r"Odredite interval i radijus konvergencije reda potencija $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n n}{3^n}(x+2)^n$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Radijus konvergencije r =", "answer": "3"},
            {"label": "Interval konvergencije:", "answer": "<-5, 1>"}
        ]),
        "rjesenje": r"$r=3$, interval $\langle -5,1\rangle$",
        "hints": [r"Primijeni D'Alembertov kriterij: uvjet $|x+2|<3$.", r"Za $x=-5$ i $x=1$: nužan uvjet nije zadovoljen, red divergira."]
    },
    {
        "tekst": r"Izračunajte površinu područja omeđenog krivuljama $y=|3x-6|$ i $y=x(4-x)$.",
        "tip": "auto",
        "tocan_odgovor": "25/6",
        "rjesenje": r"$\dfrac{25}{6}$",
        "hints": [r"$|3x-6|=\begin{cases}6-3x,&x<2\\3x-6,&x\ge 2\end{cases}$.", r"Sjecišta s parabolom: $x=1$ i $x=3$. Integriraj na $[1,2]$ i $[2,3]$ zasebno."]
    },
    {
        "tekst": r"Ispitajte konvergenciju nepravog integrala $\displaystyle\int_0^5 \frac{x}{x-3}\,\mathrm{d}x$.",
        "tip": "choice",
        "tocan_odgovor": choice("divergira", KONV_I),
        "rjesenje": r"divergira",
        "hints": [r"Razbij integral u točki prekida $x=3$ na dva neprava integrala.", r"Neodređeni integral: $x+3\ln|x-3|+C$."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int \cos 5x\cos 4x\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "sin(9*x)/18 + sin(x)/2",
        "rjesenje": r"$\dfrac{1}{18}\sin(9x)+\dfrac{1}{2}\sin(x)+C$",
        "hints": [r"$\cos A\cos B=\frac{1}{2}[\cos(A+B)+\cos(A-B)]$."]
    },
    {
        "tekst": r"Ispitajte konvergenciju reda $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{\sqrt[3]{n(n+1)}}$.",
        "tip": "choice",
        "tocan_odgovor": choice("uvjetno konvergira", KONV),
        "rjesenje": r"uvjetno konvergira",
        "hints": [r"Red apsolut. vrijednosti usporedi s $\sum\frac{1}{n^{2/3}}$ — divergira.", r"Leibnizov kriterij: $\frac{1}{\sqrt[3]{n(n+1)}}$ je padajući niz koji teži u $0$."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int \frac{\mathrm{d}x}{\sqrt{-x^2+4x+5}}$.",
        "tip": "auto",
        "tocan_odgovor": "asin((x-2)/3)",
        "rjesenje": r"$\arcsin\dfrac{x-2}{3}+C$",
        "hints": [r"Dopuni na puni kvadrat: $-x^2+4x+5=9-(x-2)^2$.", r"Supstitucija $u=x-2$."]
    },
    {
        "tekst": r"Odredite interval i radijus konvergencije reda potencija $\displaystyle\sum_{n=1}^{\infty}\frac{(x-2)^n}{(2n-1)\cdot 2^n}$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Radijus konvergencije r =", "answer": "2"},
            {"label": "Interval konvergencije:", "answer": "[0, 4>"}
        ]),
        "rjesenje": r"$r=2$, interval $[0,4\rangle$",
        "hints": [r"D'Alembert ili Cauchy daje uvjet $|x-2|<2$.", r"Na rubu $x=0$: alternativni red — konvergira. Na rubu $x=4$: harmonijski — divergira."]
    },
    {
        "tekst": r"Ispitajte konvergenciju reda $\displaystyle\sum_{n=1}^{\infty}\sin\!\left(\frac{n\pi}{2n+3}\right)$.",
        "tip": "choice",
        "tocan_odgovor": choice("divergira", KONV),
        "rjesenje": r"divergira",
        "hints": [r"Provjeri nužan uvjet konvergencije: $\lim a_n\neq 0$."]
    },
    {
        "tekst": r"Zadana je funkcija $f:[1,4]\to\mathbb{R}$ formulom $f(x)=x^2-x+1$. Neka je $P_n=\{x_0,\ldots,x_n\}$ subdivizija segmenta $[1,4]$ sa $x_i=1+\frac{3}{n}\,i$. Izračunajte $\lim_{n\to\infty}S(f,P_n)$ (gornja Darbouxova suma).",
        "tip": "auto",
        "tocan_odgovor": "39/2",
        "rjesenje": r"$\dfrac{39}{2}$",
        "hints": [r"Za rastuću funkciju gornja Darbouxova suma koristi desne rubne točke.", r"$\sum_{i=1}^n i^2=\frac{n(n+1)(2n+1)}{6}$."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int \frac{\sqrt{5-x^2}}{x^4}\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "-(5-x**2)**(Rational(3,2))/(15*x**3)",
        "rjesenje": r"$-\dfrac{(5-x^2)^{3/2}}{15x^3}+C$",
        "hints": [r"Trigonometrijska supstitucija $x=\sqrt{5}\sin t$.", r"Svedi na $\int\operatorname{ctg}^2 t\cdot\operatorname{ctg} t\,\mathrm{d}t$."]
    },
    {
        "tekst": r"Ispitajte konvergenciju reda $\displaystyle\sum_{n=1}^{\infty}(-1)^n\frac{n^3}{3^n}$.",
        "tip": "choice",
        "tocan_odgovor": choice("apsolutno konvergira", KONV),
        "rjesenje": r"apsolutno konvergira",
        "hints": [r"Primijeni D'Alembertov kriterij: $\lim\frac{(n+1)^3}{3\cdot n^3}=\frac{1}{3}<1$."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int \frac{2x^2+5x+1}{x^2+2x+2}\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "2*x + log(x**2+2*x+2) - 3*atan(x+1)",
        "rjesenje": r"$2x+\ln(x^2+2x+2)-3\arctan(x+1)+C$",
        "hints": [r"Podijeli brojnik s nazivnikom: kvocijent $2$, ostatak $x-3$.", r"Rastavi ostatak na derivaciju nazivnika i dopuni na puni kvadrat."]
    },
    {
        "tekst": r"Ispitajte konvergenciju reda $\displaystyle\sum_{n=1}^{\infty}\frac{\sqrt{3n+n^2}}{n^2}$.",
        "tip": "choice",
        "tocan_odgovor": choice("divergira", KONV),
        "rjesenje": r"divergira",
        "hints": [r"$\frac{\sqrt{3n+n^2}}{n^2}\ge\frac{n}{n^2}=\frac{1}{n}$ za $n\ge 1$.", r"Poredbeni kriterij s harmonijskim redom."]
    },
    {
        "tekst": r"Ispitajte konvergenciju nepravog integrala $\displaystyle\int_{\pi/2}^{\pi}\frac{\cos x}{\sqrt{1-\sin x}}\,\mathrm{d}x$.",
        "tip": "choice",
        "tocan_odgovor": choice("konvergira", KONV_I),
        "rjesenje": r"konvergira, vrijednost $-2$",
        "hints": [r"Supstitucija $t=1-\sin x$, $\mathrm{d}t=-\cos x\,\mathrm{d}x$.", r"Limes kada donja granica teži k $\pi/2$ s desne strane."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int x\sin 2x\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "-x*cos(2*x)/2 + sin(2*x)/4",
        "rjesenje": r"$-\dfrac{x}{2}\cos(2x)+\dfrac{1}{4}\sin(2x)+C$",
        "hints": [r"Parcijalna integracija: $u=x$, $\mathrm{d}v=\sin(2x)\,\mathrm{d}x$."]
    },
    {
        "tekst": r"Ispitajte konvergenciju reda $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{\sqrt{n}}$.",
        "tip": "choice",
        "tocan_odgovor": choice("uvjetno konvergira", KONV),
        "rjesenje": r"uvjetno konvergira",
        "hints": [r"Red apsolutnih vrijednosti je $p$-red s $p=1/2$ — divergira.", r"Leibnizov kriterij: $\frac{1}{\sqrt{n}}$ pada i teži u $0$."]
    },
    {
        "tekst": r"Pomoću granične vrijednosti integralne sume izračunajte $\displaystyle\int_1^3 2^x\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "4/log(2)",
        "rjesenje": r"$\dfrac{4}{\ln 2}$",
        "hints": [r"Desne rubne točke: $x_i=1+\frac{2i}{n}$, duljina podintervala $\frac{2}{n}$.", r"Koristi $\lim_{h\to 0}\frac{2^h-1}{h}=\ln 2$."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int \frac{\sin(\ln x)-x^2}{x}\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "-cos(log(x)) - x**2/2",
        "rjesenje": r"$-\cos(\ln x)-\dfrac{x^2}{2}+C$",
        "hints": [r"Razdvoji: $\int\frac{\sin(\ln x)}{x}\,\mathrm{d}x - \int x\,\mathrm{d}x$.", r"Za prvi integral: supstitucija $u=\ln x$."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int \left(\frac{x-1}{x^2-2x+2}\right)^{\!2}\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "-1/(2*(x**2-2*x+2))",
        "rjesenje": r"$-\dfrac{1}{2(x^2-2x+2)}+C$",
        "hints": [r"Supstitucija $u=x^2-2x+2$, $\mathrm{d}u=2(x-1)\,\mathrm{d}x$."]
    },
    {
        "tekst": r"Izračunajte sumu reda $\displaystyle\sum_{n=2}^{\infty}\frac{2-n}{n(n^2-1)}$.",
        "tip": "auto",
        "tocan_odgovor": "1/4 - log(2)",
        "rjesenje": r"$\dfrac{1}{4}-\ln 2$",
        "hints": [r"Parcijalni razlomci: $\frac{2-n}{n(n-1)(n+1)}=\frac{A}{n}+\frac{B}{n-1}+\frac{C}{n+1}$.", r"Izračunaj limes parcijalnih suma."]
    },
    {
        "tekst": r"Ispitajte konvergenciju reda $\displaystyle\sum_{n=1}^{\infty}\frac{\ln n}{n^3+n+2}$.",
        "tip": "choice",
        "tocan_odgovor": choice("apsolutno konvergira", KONV),
        "rjesenje": r"apsolutno konvergira",
        "hints": [r"Iskoristi $\ln n < n$.", r"Usporedi s konvergentnim $p$-redom $\sum\frac{1}{n^2}$."]
    },
    {
        "tekst": r"Ispitajte konvergenciju reda $\displaystyle\sum_{n=1}^{\infty}(-1)^n\left(\frac{2n+1}{3n+1}\right)^{\!n}$.",
        "tip": "choice",
        "tocan_odgovor": choice("apsolutno konvergira", KONV),
        "rjesenje": r"apsolutno konvergira",
        "hints": [r"Cauchyjev korijenski kriterij.", r"$\lim\frac{2n+1}{3n+1}=\frac{2}{3}<1$."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int \frac{2x^2-x+3}{x^2-x+1}\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "2*x + log(x**2-x+1)/2 + sqrt(3)*atan((2*x-1)/sqrt(3))",
        "rjesenje": r"$2x+\dfrac{1}{2}\ln(x^2-x+1)+\sqrt{3}\arctan\dfrac{2x-1}{\sqrt{3}}+C$",
        "hints": [r"Podijeli brojnik s nazivnikom: kvocijent $2$, ostatak $x+1$.", r"Rastavi ostatak na derivaciju nazivnika i dopuni na puni kvadrat."]
    },
    {
        "tekst": r"Odredite površinu lika omeđenog krivuljama $y^2=2+x$ i $x=y$.",
        "tip": "auto",
        "tocan_odgovor": "9/2",
        "rjesenje": r"$\dfrac{9}{2}$",
        "hints": [r"Sjecišta: iz $y^2-2=y$ slijedi $y=-1$, $y=2$.", r"Integriraj po $y$: $P=\int_{-1}^{2}[y-(y^2-2)]\,\mathrm{d}y$."]
    },
    {
        "tekst": r"Ispitajte konvergenciju reda $\displaystyle\sum_{n=1}^{\infty}\cos\!\left(\frac{\pi}{3n^2}\right)$.",
        "tip": "choice",
        "tocan_odgovor": choice("divergira", KONV),
        "rjesenje": r"divergira",
        "hints": [r"Provjeri nužan uvjet: $\lim\cos\frac{\pi}{3n^2}=\cos 0=1\neq 0$."]
    },
    {
        "tekst": r"Ispitajte konvergenciju reda $\displaystyle\sum_{n=1}^{\infty}(-1)^n\frac{\ln n}{n^3+2}$.",
        "tip": "choice",
        "tocan_odgovor": choice("apsolutno konvergira", KONV),
        "rjesenje": r"apsolutno konvergira",
        "hints": [r"$\ln n < n$, pa $\frac{\ln n}{n^3+2}<\frac{1}{n^2}$."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int \frac{\sqrt[3]{1+\sqrt{x-1}}}{\sqrt{x-1}}\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "3/2*(1+sqrt(x-1))**Rational(4,3)",
        "rjesenje": r"$\dfrac{3}{2}\!\left(1+\sqrt{x-1}\right)^{4/3}+C$",
        "hints": [r"Supstitucija $u=1+\sqrt{x-1}$, $\mathrm{d}u=\frac{\mathrm{d}x}{2\sqrt{x-1}}$."]
    },
    {
        "tekst": r"Riješite nepravi integral $\displaystyle\int_{-\infty}^{0}\frac{e^{1/x}}{x^2}\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "1",
        "rjesenje": r"$1$",
        "hints": [r"Supstitucija $t=1/x$, $\mathrm{d}t=-\frac{\mathrm{d}x}{x^2}$."]
    },
    {
        "tekst": r"Ispitajte konvergenciju nepravog integrala $\displaystyle\int_1^3 \frac{4x}{\sqrt[3]{x^2-9}}\,\mathrm{d}x$.",
        "tip": "choice",
        "tocan_odgovor": choice("divergira", KONV_I),
        "rjesenje": r"divergira",
        "hints": [r"Napiši nepravi integral: $\lim_{t\to 3^{-}}\int_1^t\frac{4x}{\sqrt[3]{x^2-9}}\,\mathrm{d}x$.", r"Supstitucija $u=x^2-9$."]
    },
    {
        "tekst": r"Ispitajte konvergenciju reda $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{\sqrt[3]{n^2+1}}$.",
        "tip": "choice",
        "tocan_odgovor": choice("uvjetno konvergira", KONV),
        "rjesenje": r"uvjetno konvergira",
        "hints": [r"Red apsolut. vrijednosti usporedi s $\sum\frac{1}{n^{2/3}}$ — divergira.", r"Leibnizov kriterij za alternativni red."]
    },
    {
        "tekst": r"Funkciju $f(x)=\dfrac{5}{(x-4)(x+1)}$ razvijte u Maclaurinov red.",
        "tip": "auto",
        "tocan_odgovor": "Sum((-1/4**(n+1) - 1)*(-1)**n*x**n, (n, 0, oo))",
        "rjesenje": r"$\displaystyle\sum_{n=0}^{\infty}\!\left[-\frac{1}{4^{n+1}}-1\right](-1)^n x^n$, $|x|<1$",
        "hints": [r"Parcijalni razlomci: $\frac{5}{(x-4)(x+1)}=\frac{A}{x-4}+\frac{B}{x+1}$.", r"Zapiši oba razlomka kao geometrijski red oko $x=0$."]
    },
    {
        "tekst": r"Ispitajte konvergenciju reda $\displaystyle\sum_{n=1}^{\infty}\frac{(2n-1)!!}{(2n)!!\cdot 3^n}$.",
        "tip": "choice",
        "tocan_odgovor": choice("apsolutno konvergira", KONV),
        "rjesenje": r"apsolutno konvergira",
        "hints": [r"D'Alembertov kriterij: $\frac{a_{n+1}}{a_n}=\frac{2n+1}{3(2n+2)}\to\frac{1}{6}<1$."]
    },
    {
        "tekst": r"Odredite interval i radijus konvergencije reda potencija $\displaystyle\sum_{n=2}^{\infty}\frac{2^{n-1}\cdot(x-1)^n}{(n-1)\cdot 4^n}$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Radijus konvergencije r =", "answer": "2"},
            {"label": "Interval konvergencije:", "answer": "<-1, 3>"}
        ]),
        "rjesenje": r"$r=2$, interval $\langle -1,3\rangle$",
        "hints": [r"Cauchyjev kriterij korijena: $\sqrt[n]{|c_n|}\to\frac{1}{2}$, pa $r=2$.", r"Na rubovima $x=-1$ i $x=3$ red divergira."]
    },
    {
        "tekst": r"Izračunajte površinu područja $T=\{(x,y)\in\mathbb{R}^2: x\le 0,\; y=9-x^2,\; y=-8x,\; y=-\tfrac{5}{2}x\}$.",
        "tip": "auto",
        "tocan_odgovor": "99/8",
        "rjesenje": r"$\dfrac{99}{8}$",
        "hints": [r"Pronađi sjecišta parabole $y=9-x^2$ s pravcima $y=-8x$ i $y=-\frac{5}{2}x$ za $x\le 0$.", r"Podijeli na podintervale prema gornjoj/donjoj krivulji."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int \frac{1}{\sqrt{x+1}+\sqrt[3]{x+1}}\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "3*(x+1)**Rational(1,2) - 6*(x+1)**Rational(1,6) + 2*log((x+1)**Rational(1,6)+1) - 6*(x+1)**Rational(1,3) + 3*log((x+1)**Rational(1,3)+1)",
        "rjesenje": r"Supstitucija $t=(x+1)^{1/6}$: svodi se na $6\int\frac{t^3}{1+t}\,\mathrm{d}t$.",
        "hints": [r"Zajednički korijen: $t=(x+1)^{1/6}$, pa $\sqrt{x+1}=t^3$, $\sqrt[3]{x+1}=t^2$.", r"Dijeli $t^3\div(1+t)$, pa integriraj racionalni izraz."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int\!\sqrt[3]{x\cdot\sqrt{x\cdot\sqrt[4]{x}}}\;\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "24/19*x**Rational(19,24)",
        "rjesenje": r"$\dfrac{24}{19}\,x^{19/24}+C$",
        "hints": [r"Zapiši sve korijene kao potencije s racionalnim eksponentima.", r"Kombiniraj eksponente: izraz daje $x^{17/24}$, pa $\int x^{17/24}\,\mathrm{d}x=\frac{24}{19}x^{19/24}+C$."]
    },
    {
        "tekst": r"Ispitajte konvergenciju reda $\displaystyle\sum_{n=1}^{\infty}(-1)^{n-1}\frac{2n+1}{n(n+1)}$.",
        "tip": "choice",
        "tocan_odgovor": choice("uvjetno konvergira", KONV),
        "rjesenje": r"uvjetno konvergira",
        "hints": [r"Parcijalni razlomci: $\frac{2n+1}{n(n+1)}=\frac{1}{n}+\frac{1}{n+1}$ — red apsolutnih vrijednosti divergira.", r"Leibnizov kriterij: $\frac{2n+1}{n(n+1)}$ pada i teži u $0$."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int\frac{\sqrt{1+\ln x}-x\sin x}{3x}\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "2/9*(1+log(x))**Rational(3,2) + cos(x)/3",
        "rjesenje": r"$\dfrac{2}{9}(1+\ln x)^{3/2}+\dfrac{1}{3}\cos x+C$",
        "hints": [r"Razbij: $\frac{1}{3}\int\frac{\sqrt{1+\ln x}}{x}\,\mathrm{d}x-\frac{1}{3}\int\sin x\,\mathrm{d}x$.", r"Za prvi integral: $u=1+\ln x$."]
    },
    {
        "tekst": r"Neka je $f:[2,3]\to\mathbb{R}$ dana sa $f(x)=2^x$ i geometrijska particija $Q=\{x_i:x_i=x_{i-1}\cdot p\}$. Izračunajte $\int_2^3 f(x)\,\mathrm{d}x$ kao graničnu vrijednost donje Darbouxove sume.",
        "tip": "auto",
        "tocan_odgovor": "4/log(2)",
        "rjesenje": r"$\dfrac{4}{\ln 2}$",
        "hints": [r"Geometrijska particija: $x_i=2\cdot p^i$, $p=(3/2)^{1/n}$.", r"Donja suma za rastuću funkciju koristi lijeve rubne točke."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int\sin\frac{x}{3}\cos\frac{2x}{3}\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "-cos(x)/2 + 3*cos(x/3)/2",
        "rjesenje": r"$-\dfrac{1}{2}\cos x+\dfrac{3}{2}\cos\dfrac{x}{3}+C$",
        "hints": [r"$\sin A\cos B=\frac{1}{2}[\sin(A+B)+\sin(A-B)]$."]
    },
    {
        "tekst": r"Riješite integral $\displaystyle\int x\ln\!\left(\frac{1-x}{1+x}\right)\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "x**2/2*log((1-x)/(1+x)) + x - log((1+x)/(1-x))/2",
        "rjesenje": r"$\dfrac{x^2}{2}\ln\dfrac{1-x}{1+x}+x-\dfrac{1}{2}\ln\dfrac{1+x}{1-x}+C$",
        "hints": [r"$u=\ln\frac{1-x}{1+x}$, $\mathrm{d}v=x\,\mathrm{d}x$.", r"$u'=\frac{-2}{1-x^2}$."]
    },
    {
        "tekst": r"Izračunajte integral $\displaystyle\int_0^2\frac{1}{4\sqrt{x+1}+4(x+1)^{3/2}}\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "atan(sqrt(3)/2) - pi/6",
        "rjesenje": r"$\arctan\dfrac{\sqrt{3}}{2}-\dfrac{\pi}{6}$",
        "hints": [r"Supstitucija $u=\sqrt{x+1}$, $\mathrm{d}x=2u\,\mathrm{d}u$."]
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
    finally:
        db.close()

if __name__ == "__main__":
    run()