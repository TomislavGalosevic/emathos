"""
Import zadataka za kolegij "Numericka matematika".
Pokretanje: python -m app.import_zadaci_numericka
"""

import json
from .database import Base, engine, SessionLocal
from . import models

COURSE_NAME = "Numericka matematika"

def multi(fields):
    return json.dumps(fields, ensure_ascii=False)

def choice(answer, options):
    return json.dumps({"answer": answer, "options": options}, ensure_ascii=False)

KONV = ["konvergira", "ne konvergira"]

ZADACI = [
    {
        "tekst": r"Pronađite pravac koji u smislu najmanjih kvadrata prolazi što bliže točkama $x=[1,4,-3,2]$, $y=[7,5,1,3]$.",
        "tip": "auto",
        "tocan_odgovor": "7*x/13 + 45/13",
        "rjesenje": r"$f(x)=\frac{7}{13}x+\frac{45}{13}\approx 0{,}5385x+3{,}4615$",
        "hints": [r"$A=\begin{pmatrix}1&1\\1&4\\1&-3\\1&2\end{pmatrix}$. Normalne jednadžbe: $(A^TA)a=A^Ty$.", r"$\sum x_i=4$, $\sum x_i^2=30$, $\sum y_i=16$, $\sum x_iy_i=28$."]
    },
    {
        "tekst": r"Odredite linearni interpolacijski spline za $f$ koja prolazi točkama $(-1,3)$, $(0,1)$, $(1,2)$. Izračunajte $S_1(-\tfrac{1}{2})$.",
        "tip": "auto",
        "tocan_odgovor": "2",
        "rjesenje": r"$S_1(x)=-2x+1$ na $[-1,0]$; $S_1(x)=x+1$ na $[0,1]$. $S_1(-\tfrac{1}{2})=2$",
        "hints": [r"Pravac kroz $(-1,3)$ i $(0,1)$: $y=-2x+1$. Pravac kroz $(0,1)$ i $(1,2)$: $y=x+1$.", r"$S_1(-1/2)=-2\cdot(-1/2)+1=2$."]
    },
    {
        "tekst": r"Odredite minimalni parni $n$ da se generaliziranom Simpsonovom formulom izračuna $\int_{2}^{3}xe^x\,\mathrm{d}x$ uz točnost $\epsilon=0{,}002$.",
        "tip": "auto",
        "tocan_odgovor": "4",
        "rjesenje": r"$n\ge 4$ (parno)",
        "hints": [r"$f^{(4)}(x)=(x+4)e^x$, $M_4=7e^3\approx140{,}6$.", r"$\frac{1}{180n^4}\cdot 7e^3<0{,}002\Rightarrow n\ge 4$."]
    },
    {
        "tekst": r"Koliko signifikantnih znamenki ima broj $a^*=31{,}479\pm 0{,}0003$?",
        "tip": "auto",
        "tocan_odgovor": "5",
        "rjesenje": r"$5$ signifikantnih znamenki",
        "hints": [r"Znamenka je signifikantna ako je apsolutna pogreška $\le$ polovici jedinice mjesta te znamenke.", r"$0{,}0003\le 0{,}0005$ — znamenka $9$ na $10^{-3}$ je signifikantna."]
    },
    {
        "tekst": r"Odredite konstante $a$, $b$ i $c$ tako da $C(x)$ bude prirodni kubični interpolacijski spline: $C_1(x)=-2x^3+5x-1$ na $[0,1]$, $C_2(x)=a(x-1)^3+b(x-1)^2+c(x-2)+2$ na $[1,2]$.",
        "tip": "multi",
        "tocan_odgovor": multi([{"label": "a =", "answer": "2"}, {"label": "b =", "answer": "-6"}, {"label": "c =", "answer": "0"}]),
        "rjesenje": r"$a=2$, $b=-6$, $c=0$",
        "hints": [r"Uvjeti na spojištu $x=1$: $C_1(1)=C_2(1)\Rightarrow c=0$.", r"$C_1''(1)=C_2''(1)$: $-12=-12+2b\Rightarrow b=-6$. Prirodni rubni: $C_2''(2)=0\Rightarrow 6a+2b=0\Rightarrow a=2$."]
    },
    {
        "tekst": r"Metodom bisekcije odredite negativnu nultočku $f(x)=e^x-3x-2$ uz $\epsilon=0{,}05$ na $[-1,0]$.",
        "tip": "auto",
        "tocan_odgovor": "-0.53125",
        "rjesenje": r"$x^*\approx -0{,}53125$ (nakon $5$ koraka)",
        "hints": [r"Sukcesivno dijeli $[-1,0]$ na pola i ispituj predznake.", r"Stani kad $b-a<2\epsilon=0{,}1$."]
    },
    {
        "tekst": r"Odredite Lagrangeov interpolacijski polinom za $f(x)=\sin(\pi(x+1))$ u čvorovima $0,\;\tfrac{1}{6},\;\tfrac{1}{2}$.",
        "tip": "auto",
        "tocan_odgovor": "3*x**2 - 7*x/2",
        "rjesenje": r"$L_2(x)=3x^2-\dfrac{7}{2}x$",
        "hints": [r"$f(0)=0$, $f(1/6)=-1/2$, $f(1/2)=-1$.", r"Formirajte bazne polinome $l_i(x)$ i zbrojite $L_2=\sum f(x_i)l_i(x)$."]
    },
    {
        "tekst": r"Procijenite apsolutnu i relativnu pogrešku volumena valjka $V=\pi r^2 h$ ako je $r=2\pm 0{,}02$ cm i $h=7{,}5\pm 0{,}03$ cm.",
        "tip": "multi",
        "tocan_odgovor": multi([{"label": "ΔV* =", "answer": "0.72*pi"}, {"label": "δV* (%) =", "answer": "2.4"}]),
        "rjesenje": r"$\Delta V^*=0{,}72\pi\approx 2{,}262$ cm³; $\delta V^*=2{,}4\%$",
        "hints": [r"$\Delta V^*\le|2\pi r h|\Delta r+|\pi r^2|\Delta h=0{,}6\pi+0{,}12\pi=0{,}72\pi$.", r"$\delta V=\Delta V/V=0{,}72\pi/(30\pi)=0{,}024=2{,}4\%$."]
    },
    {
        "tekst": r"Konvergira li iterativni proces $x_{n+1}=e^{-x_n/2}$ prema nultočki $f(x)=e^{-x/2}-x$ na $[0,1]$?",
        "tip": "choice",
        "tocan_odgovor": choice("konvergira", KONV),
        "rjesenje": r"konvergira",
        "hints": [r"$g(x)=e^{-x/2}$, $|g'(x)|=\frac{1}{2}e^{-x/2}\le\frac{1}{2}<1$ za sve $x\in[0,1]$."]
    },
    {
        "tekst": r"Odredite Newtonov interpolacijski polinom za $f(x)=\cos(\pi(x-1))$ u čvorovima $1,\;\tfrac{3}{2},\;2$.",
        "tip": "auto",
        "tocan_odgovor": "3-2*x",
        "rjesenje": r"$N_2(x)=3-2x$",
        "hints": [r"$f(1)=1$, $f(3/2)=0$, $f(2)=-1$. Podijeljena razlika $f[1,3/2]=-2$, $f[1,3/2,2]=0$.", r"$N_2(x)=1-2(x-1)=3-2x$."]
    },
    {
        "tekst": r"Odredite vrijednosti $C''(x_i)$ prirodnog kubičnog splinea za $f(x)=(x+1)\sin(\pi x/2)$ u čvorovima $0,1,2,3,4$.",
        "tip": "multi",
        "tocan_odgovor": multi([{"label": "C''(0) =", "answer": "0"}, {"label": "C''(1) =", "answer": "-33/7"}, {"label": "C''(2) =", "answer": "-36/7"}, {"label": "C''(3) =", "answer": "93/7"}, {"label": "C''(4) =", "answer": "0"}]),
        "rjesenje": r"$C''(0)=0$, $C''(1)=-\frac{33}{7}$, $C''(2)=-\frac{36}{7}$, $C''(3)=\frac{93}{7}$, $C''(4)=0$",
        "hints": [r"$f(0)=0$, $f(1)=2$, $f(2)=0$, $f(3)=-4$, $f(4)=0$.", r"Trodijagonalni sustav: $M_{i-1}+4M_i+M_{i+1}=6(y_{i+1}-2y_i+y_{i-1})$ uz $M_0=M_4=0$."]
    },
    {
        "tekst": r"Pronađite kvadratnu funkciju $f(x)=a_1(x-1)+a_2 x^2$ koja u smislu najmanjih kvadrata prolazi što bliže točkama $(-1,0)$, $(0,\frac{1}{3})$, $(1,2)$, $(2,1)$.",
        "tip": "auto",
        "tocan_odgovor": "x**2/3",
        "rjesenje": r"$f(x)=\dfrac{1}{3}x^2$",
        "hints": [r"Matrica dizajna: stupci su $\phi_1(x_i)=x_i-1$ i $\phi_2(x_i)=x_i^2$.", r"Normalne jednadžbe: $(A^TA)a=A^Ty$. Rješenje: $a_1=0$, $a_2=1/3$."]
    },
    {
        "tekst": r"Ocijenite pogrešku interpolacijskog polinoma $L_2$ za $f(x)=\sin(\pi(x+1))$ u točki $x=\tfrac{1}{3}$.",
        "tip": "auto",
        "tocan_odgovor": "pi**3/648",
        "rjesenje": r"$|f(\tfrac{1}{3})-L_2(\tfrac{1}{3})|\le\dfrac{\pi^3}{648}\approx 0{,}04785$",
        "hints": [r"$|R_2(x)|\le\frac{M_3}{3!}|w_3(x)|$ gdje je $M_3=\pi^3$.", r"$w_3(1/3)=\frac{1}{3}\cdot\frac{1}{6}\cdot(-\frac{1}{6})=-\frac{1}{108}$. $|R|\le\frac{\pi^3}{648}$."]
    },
    {
        "tekst": r"Koliko podintervala $n$ treba uzeti za aproksimaciju $f(x)=e^{3x/2}$ na $[0,2]$ linearnim splineom uz $\epsilon=0{,}001$?",
        "tip": "auto",
        "tocan_odgovor": "150",
        "rjesenje": r"$n\ge 150$",
        "hints": [r"$\|f-S_1\|_\infty\le\frac{h^2}{8}M_2<0{,}001$ gdje $h=2/n$ i $M_2=\frac{9}{4}e^3$.", r"$\frac{4/n^2}{8}\cdot\frac{9}{4}e^3<0{,}001\Rightarrow n\ge 150$."]
    },
    {
        "tekst": r"Odredite minimalni broj podintervala $n$ (parno) da se Simpsonovim pravilom izračuna $\int_{-1}^{0}(1-x)^{1/3}\,\mathrm{d}x$ uz $\epsilon=0{,}0003$.",
        "tip": "auto",
        "tocan_odgovor": "4",
        "rjesenje": r"$n\ge 4$",
        "hints": [r"$f^{(4)}(x)=-\frac{80}{81}(1-x)^{-11/3}$, $M_4=\frac{80}{81}$ (na $x=0$).", r"$\frac{1}{180n^4}\cdot\frac{80}{81}<0{,}0003\Rightarrow n\ge 4$."]
    },
    {
        "tekst": r"Odredite Lagrangeov interpolacijski polinom za funkciju koja prolazi točkama $(-1,-5)$, $(0,2)$, $(1,3)$.",
        "tip": "auto",
        "tocan_odgovor": "-3*x**2+4*x+2",
        "rjesenje": r"$L_2(x)=-3x^2+4x+2$",
        "hints": [r"$l_0(x)=\frac{x(x-1)}{2}$, $l_1(x)=-(x+1)(x-1)$, $l_2(x)=\frac{(x+1)x}{2}$.", r"$L_2=-5l_0+2l_1+3l_2$."]
    },
    {
        "tekst": r"Odredite vrijednosti $C''(x_i)$ prirodnog kubičnog splinea za $f(x)=(x-1)\cos(\pi x/2)$ u čvorovima $0,1,2,3,4$.",
        "tip": "multi",
        "tocan_odgovor": multi([{"label": "C''(0) =", "answer": "0"}, {"label": "C''(1) =", "answer": "9/7"}, {"label": "C''(2) =", "answer": "-36/7"}, {"label": "C''(3) =", "answer": "51/7"}, {"label": "C''(4) =", "answer": "0"}]),
        "rjesenje": r"$C''(0)=0$, $C''(1)=\frac{9}{7}$, $C''(2)=-\frac{36}{7}$, $C''(3)=\frac{51}{7}$, $C''(4)=0$",
        "hints": [r"$f(0)=-1$, $f(1)=0$, $f(2)=1$, $f(3)=0$, $f(4)=3$.", r"Trodijagonalni sustav: $M_{i-1}+4M_i+M_{i+1}=6(y_{i+1}-2y_i+y_{i-1})$."]
    },
    {
        "tekst": r"Treba načiniti pravilnu četverostranu piramidu $V=\frac{1}{3}a^2 h=6\pm 0{,}05$ m³, $a^*=2$ m. Odredite $h^*$, $\Delta a^*$ i $\Delta h^*$ po principu jednakih efekata.",
        "tip": "multi",
        "tocan_odgovor": multi([{"label": "h* =", "answer": "4.5"}, {"label": "Δa* ≤", "answer": "1/240"}, {"label": "Δh* ≤", "answer": "3/160"}]),
        "rjesenje": r"$h^*=4{,}5$ m; $\Delta a^*\le\frac{1}{240}$ m; $\Delta h^*\le\frac{3}{160}$ m",
        "hints": [r"$h^*=3V^*/a^{*2}=4{,}5$. $\frac{\partial V}{\partial a}=\frac{2}{3}ah=6$, $\frac{\partial V}{\partial h}=\frac{a^2}{3}=\frac{4}{3}$.", r"$\Delta x_i^*\le\frac{\Delta V}{n\cdot|\partial V/\partial x_i|}$ uz $n=2$, $\Delta V=0{,}05$."]
    },
    {
        "tekst": r"Primjenom generalizirane Simpsonove formule s $n=4$ odredite $\int_{-1}^{0}(1-x)^{1/3}\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "1.3211",
        "rjesenje": r"$I_S\approx 1{,}3211$",
        "hints": [r"$h=1/4$. Čvorovi: $-1,-3/4,-1/2,-1/4,0$. $I_S=\frac{h}{3}(f_0+4f_1+2f_2+4f_3+f_4)$."]
    },
    {
        "tekst": r"Konvergira li iterativni proces $x_{n+1}=-\frac{1}{2}e^{x_n}$ prema nultočki $f(x)=e^x+2x$ na $[-1,0]$?",
        "tip": "choice",
        "tocan_odgovor": choice("konvergira", KONV),
        "rjesenje": r"konvergira",
        "hints": [r"$g(x)=-\frac{1}{2}e^x$, $|g'(x)|=\frac{1}{2}e^x\le\frac{1}{2}<1$ za $x\in[-1,0]$."]
    },
    {
        "tekst": r"Ocijenite pogrešku Newtonovog interpolacijskog polinoma za $f(x)=\cos(\pi x/2)$ u čvorovima $0,\tfrac{3}{5},1$ u točki $\bar{x}=\tfrac{1}{2}$.",
        "tip": "auto",
        "tocan_odgovor": "pi**3/1920",
        "rjesenje": r"$|f(\tfrac{1}{2})-N_2(\tfrac{1}{2})|\le\dfrac{\pi^3}{1920}\approx 0{,}01615$",
        "hints": [r"$M_3=(\pi/2)^3$. $w_3(1/2)=\frac{1}{2}\cdot(-\frac{1}{10})\cdot(-\frac{1}{2})=\frac{1}{40}$.", r"$|R|\le\frac{\pi^3/8}{6}\cdot\frac{1}{40}=\frac{\pi^3}{1920}$."]
    },
    {
        "tekst": r"Neka je $J=\begin{pmatrix}1&-1\\1&1\\1&0\end{pmatrix}$, $y=(1,2,-1)^T$. Odredite $a$ koji minimizira $\|Ja-y\|_2$ (SVD/pseudoinverz).",
        "tip": "multi",
        "tocan_odgovor": multi([{"label": "a₁ =", "answer": "2/3"}, {"label": "a₂ =", "answer": "1/2"}]),
        "rjesenje": r"$a_1=\dfrac{2}{3}$, $a_2=\dfrac{1}{2}$",
        "hints": [r"$J^TJ=\begin{pmatrix}3&0\\0&2\end{pmatrix}$, pa $a=(J^TJ)^{-1}J^Ty$."]
    },
    {
        "tekst": r"Odredite linearni interpolacijski spline za $f$ koja prolazi točkama $(-2,-1)$, $(-1,3)$, $(0,2)$. Izračunajte $S_1(-\tfrac{3}{2})$.",
        "tip": "auto",
        "tocan_odgovor": "1",
        "rjesenje": r"$S_1(x)=4x+7$ na $[-2,-1]$; $S_1(x)=-x+2$ na $[-1,0]$. $S_1(-\tfrac{3}{2})=1$",
        "hints": [r"Pravac kroz $(-2,-1)$ i $(-1,3)$: nagib $4$, $y=4x+7$.", r"$S_1(-3/2)=4(-3/2)+7=1$."]
    },
    {
        "tekst": r"Koliko signifikantnih znamenki ima $a^*$ ($\Delta a^*\le\frac{1}{240}$ m) i $h^*=4{,}5$ m ($\Delta h^*\le\frac{3}{160}$ m)?",
        "tip": "multi",
        "tocan_odgovor": multi([{"label": "Signifikantne znamenke a*:", "answer": "3"}, {"label": "Signifikantne znamenke h*:", "answer": "2"}]),
        "rjesenje": r"$a^*$ ima $3$, $h^*$ ima $2$ signifikantne znamenke",
        "hints": [r"$\Delta a^*\approx0{,}00417$ — pola jedinice na $10^{-2}$ je $0{,}005>0{,}00417$ → $10^{-2}$ je signifikantno → $3$ znamenke.", r"$\Delta h^*=0{,}01875$ — pola jedinice na $10^{-1}$ je $0{,}05>0{,}01875$ → $2$ znamenke."]
    },
    {
        "tekst": r"Metodom bisekcije odredite pozitivnu nultočku $f(x)=e^x-2x-1$ uz $\epsilon=0{,}05$ na $[1,2]$.",
        "tip": "auto",
        "tocan_odgovor": "1.28125",
        "rjesenje": r"$x^*\approx 1{,}28125$ (nakon $5$ koraka)",
        "hints": [r"Svaki korak: izračunaj $c=(a+b)/2$ i provjeri predznak $f(c)$.", r"Stani kada $b-a<2\epsilon=0{,}1$."]
    },
    {
        "tekst": r"Ocijenite pogrešku linearnog interpolacijskog splinea za $f(x)=\sin(\pi x/3)$ u čvorovima $0,\tfrac{1}{2},1,\tfrac{3}{2},2$.",
        "tip": "auto",
        "tocan_odgovor": "pi**2*sqrt(3)/576",
        "rjesenje": r"$\|f-S_1\|_\infty\le\dfrac{\pi^2\sqrt{3}}{576}\approx 0{,}02967$",
        "hints": [r"$h=1/2$, $M_2=\frac{\pi^2\sqrt{3}}{18}$.", r"$\frac{(1/2)^2}{8}\cdot\frac{\pi^2\sqrt{3}}{18}=\frac{\pi^2\sqrt{3}}{576}$."]
    },
    {
        "tekst": r"Koliko signifikantnih znamenki ima broj $a^*=278{,}152\pm 0{,}001$?",
        "tip": "auto",
        "tocan_odgovor": "5",
        "rjesenje": r"$5$ signifikantnih znamenki",
        "hints": [r"$0{,}001\le 0{,}005$ (pola jedinice na $10^{-2}$) → zadnja signifikantna je $5$ na $10^{-2}$."]
    },
    {
        "tekst": r"Odredite konstante $a$, $b$ i $c$ tako da $C(x)$ bude prirodni kubični spline: $C_1(x)=4+3x-x^3$ na $[0,1]$, $C_2(x)=2+a(x-2)+b(x-1)^2+c(x-1)^3$ na $[1,2]$.",
        "tip": "multi",
        "tocan_odgovor": multi([{"label": "a =", "answer": "-4"}, {"label": "b =", "answer": "-3"}, {"label": "c =", "answer": "1"}]),
        "rjesenje": r"$a=-4$, $b=-3$, $c=1$",
        "hints": [r"$C_1(1)=C_2(1)$: $6=2-a\Rightarrow a=-4$. $C_1''(1)=C_2''(1)$: $-6=2b\Rightarrow b=-3$.", r"$C_2''(2)=0$: $2b+6c=0\Rightarrow c=1$."]
    },
    {
        "tekst": r"Pronađite pravac koji u smislu najmanjih kvadrata prolazi što bliže točkama $x=[1,-3,2,3]$, $y=[4,1,7,9]$.",
        "tip": "auto",
        "tocan_odgovor": "105*x/83 + 357/83",
        "rjesenje": r"$f(x)=\frac{105}{83}x+\frac{357}{83}\approx 1{,}265x+4{,}301$",
        "hints": [r"$\sum x_i=3$, $\sum x_i^2=23$, $\sum y_i=21$, $\sum x_iy_i=42$.", r"Normalne jednadžbe: $4a_0+3a_1=21$, $3a_0+23a_1=42$."]
    },
    {
        "tekst": r"Odredite linearni interpolacijski spline i ocijenite pogrešku za $f(x)=\cos(\pi x/2)$ u čvorovima $0,\tfrac{2}{3},1$.",
        "tip": "multi",
        "tocan_odgovor": multi([{"label": "S₁(x) na [0, 2/3] =", "answer": "1 - 3*x/4"}, {"label": "Ocjena pogreške ≤", "answer": "pi**2/72"}]),
        "rjesenje": r"$S_1(x)=1-\frac{3}{4}x$ na $[0,\frac{2}{3}]$; $S_1(x)=-2x+2$ na $[\frac{2}{3},1]$. Pogreška $\le\frac{\pi^2}{72}$",
        "hints": [r"$h_{\max}=2/3$, $M_2=(\pi/2)^2$.", r"$\frac{(2/3)^2}{8}\cdot\frac{\pi^2}{4}=\frac{\pi^2}{72}$."]
    },
    {
        "tekst": r"Newtonovom metodom odredite nultočku $f(x)=\ln x+x-2$ uz $\epsilon=0{,}00005$ (interval $[1,2]$).",
        "tip": "auto",
        "tocan_odgovor": "1.55714",
        "rjesenje": r"$\xi\approx 1{,}55714$",
        "hints": [r"$f(1)<0$, $f(2)>0$, $f''(x)=-1/x^2<0$. Biramo $x_0=2$.", r"$x_{n+1}=x_n-\frac{\ln x_n+x_n-2}{1/x_n+1}$."]
    },
    {
        "tekst": r"Koliko podintervala $n$ treba uzeti za aproksimaciju $f(x)=e^{3x}$ na $[1,2]$ linearnim splineom uz $\epsilon=0{,}005$?",
        "tip": "auto",
        "tocan_odgovor": "302",
        "rjesenje": r"$n\ge 302$",
        "hints": [r"$M_2=9e^6$, $h=1/n$. Uvjet: $\frac{1/n^2}{8}\cdot 9e^6<0{,}005$.", r"$n^2>\frac{9e^6}{0{,}04}\Rightarrow n\ge 302$."]
    },
    {
        "tekst": r"Pronađite kvadratnu funkciju $f(x)=a_1(x-1)+a_2 x^2$ koja u smislu najmanjih kvadrata prolazi što bliže točkama $(-2,0)$, $(-1,-2)$, $(0,3)$, $(1,1)$.",
        "tip": "multi",
        "tocan_odgovor": multi([{"label": "a₁ =", "answer": "-145/89"}, {"label": "a₂ =", "answer": "23/89"}]),
        "rjesenje": r"$a_1=-\dfrac{145}{89}$, $a_2=\dfrac{23}{89}$",
        "hints": [r"Matrica dizajna: $\phi_1(x_i)=x_i-1$, $\phi_2(x_i)=x_i^2$.", r"$(A^TA)a=A^Ty$."]
    },
    {
        "tekst": r"Primjenom generalizirane Simpsonove formule s $n=4$ odredite $\int_{2}^{3}xe^x\,\mathrm{d}x$.",
        "tip": "auto",
        "tocan_odgovor": "20.0862",
        "rjesenje": r"$I_S\approx 20{,}0862$",
        "hints": [r"$h=0{,}25$. Čvorovi: $2;\;2{,}25;\;2{,}5;\;2{,}75;\;3$. $I_S=\frac{h}{3}(f_0+4f_1+2f_2+4f_3+f_4)$."]
    },
    {
        "tekst": r"Dana je QR dekompozicija $J=QR$ (vidi zadatak). $y=(-1,2,2)^T$. Odredite $a$ koji minimizira $\|Ja-y\|_2$ rješavanjem $Ra=Q^Ty$.",
        "tip": "multi",
        "tocan_odgovor": multi([{"label": "a₁ =", "answer": "5/6"}, {"label": "a₂ =", "answer": "1/7"}]),
        "rjesenje": r"$a_1=\dfrac{5}{6}$, $a_2=\dfrac{1}{7}$",
        "hints": [r"Izračunajte $d=Q^Ty$ pa riješite gornje-trokutasti sustav $Ra=d$."]
    },
    {
        "tekst": r"Odredite minimalni $n$ da se generaliziranom trapeznom formulom izračuna $\int_{1}^{2}x^2\ln x\,\mathrm{d}x$ uz $\epsilon=0{,}009$.",
        "tip": "auto",
        "tocan_odgovor": "6",
        "rjesenje": r"$n\ge 6$",
        "hints": [r"$f''(x)=2\ln x+3$, $M_2=2\ln 2+3\approx4{,}386$ na $x=2$.", r"$\frac{1}{12n^2}(2\ln2+3)<0{,}009\Rightarrow n\ge 6$."]
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