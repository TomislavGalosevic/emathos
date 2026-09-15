"""
Import zadataka za modul "Funkcije vise varijabli"
unutar kolegija "Primijenjena matematika za racunalnu znanost".
Pokretanje: python -m app.import_zadaci_fvv
"""

import json
from .database import Base, engine, SessionLocal
from . import models

COURSE_NAME = "Primijenjena matematika za racunalnu znanost"
MODULE_NAME = "Funkcije vise varijabli"

def multi(fields):
    return json.dumps(fields, ensure_ascii=False)

def choice(answer, options):
    return json.dumps({"answer": answer, "options": options}, ensure_ascii=False)

LIM  = ["postoji", "ne postoji"]
NEP  = ["jest neprekidna", "nije neprekidna"]
DOD  = ["može se dodefinirati", "ne može se dodefinirati"]

ZADACI = [
    {
        "tekst": r"Ispitajte postoji li $\displaystyle\lim_{(x,y)\to(0,0)}\frac{x-y}{x+y}$.",
        "tip": "choice",
        "tocan_odgovor": choice("ne postoji", LIM),
        "rjesenje": r"ne postoji",
        "hints": [
            r"Uvrstite $y=kx$ i izračunajte limes: $\frac{x-kx}{x+kx}=\frac{1-k}{1+k}$ — ovisi o $k$.",
            r"Budući da limes ovisi o smjeru (parametru $k$), limes ne postoji."
        ]
    },
    {
        "tekst": r"Odredite lokalne ekstreme funkcije $z=x^3+y^2-12x+4y-1$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Koordinata x lokalnog minimuma:", "answer": "2"},
            {"label": "Koordinata y lokalnog minimuma:", "answer": "-2"},
            {"label": "Vrijednost minimuma z(2,-2) =", "answer": "-21"}
        ]),
        "rjesenje": r"Lokalni minimum u $T_1(2,-2)$: $z=-21$. Točka $T_2(-2,-2)$ je sedlasta.",
        "hints": [
            r"Izjednačite $z_x=3x^2-12=0$ i $z_y=2y+4=0$. Stacionarne točke: $(2,-2)$ i $(-2,-2)$.",
            r"Hesseova matrica u $(2,-2)$: $H=12>0$ i $z_{xx}=12>0$ $\Rightarrow$ minimum."
        ]
    },
    {
        "tekst": r"Može li se funkcija $f(x,y)=\dfrac{x^2 y^2}{x^2 y^2+(x-y)^4}$ dodefinirati u točki $(0,0)$ tako da bude neprekidna na $\mathbb{R}^2$?",
        "tip": "choice",
        "tocan_odgovor": choice("ne može se dodefinirati", DOD),
        "rjesenje": r"ne može se dodefinirati",
        "hints": [
            r"Uvrstite $y=x$: $\lim\frac{x^4}{x^4+0}=1$. Uvrstite $y=0$: $\lim\frac{0}{x^4}=0$.",
            r"Limes u $(0,0)$ ne postoji jer ovisi o smjeru — dodefiniranje nije moguće."
        ]
    },
    {
        "tekst": r"Izračunajte volumen tijela omeđenog plohama $z=5-x^2-y^2$ i $z=1$.",
        "tip": "auto",
        "tocan_odgovor": "8*pi",
        "rjesenje": r"$V=8\pi$",
        "hints": [
            r"Presjek ploha: $x^2+y^2=4$ (krug radijusa $2$). Prijeđite na polarne koordinate.",
            r"$V=\iint_{x^2+y^2\le 4}(4-x^2-y^2)\,\mathrm{d}A=\int_0^{2\pi}\int_0^2(4-r^2)r\,\mathrm{d}r\,\mathrm{d}\varphi=8\pi$."
        ]
    },
    {
        "tekst": r"Odredite jednadžbu tangencijalne ravnine na plohu $z=xy$ koja je okomita na pravac "
                 r"$\dfrac{x}{2}=\dfrac{y-\pi}{1}=\dfrac{z+3}{1}$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Lijeva strana jednadžbe Ax+By+Cz+D=0 (A>0):", "answer": "2*x+y+z+2"},
            {"label": "Dodirna točka T(x, y, z):", "answer": "(-1, -2, 2)"}
        ]),
        "rjesenje": r"$2x+y+z+2=0$, dodirna točka $T(-1,-2,2)$",
        "hints": [
            r"$F(x,y,z)=xy-z=0$, $\nabla F=(y,x,-1)$. Traži se $\nabla F\parallel(2,1,1)$.",
            r"Iz $(y,x,-1)=k(2,1,1)$: $k=-1$, $x=-1$, $y=-2$, $z=xy=2$."
        ]
    },
    {
        "tekst": r"Izračunajte $\displaystyle\iint_\Omega \frac{x}{x^2+y^2}\,\mathrm{d}x\,\mathrm{d}y$, gdje je $\Omega$ omeđeno parabolom $y=\dfrac{x^2}{2}$ i pravcem $y=x$.",
        "tip": "auto",
        "tocan_odgovor": "log(2)",
        "rjesenje": r"$I=\ln 2$",
        "hints": [
            r"Sjecišta: $x=0$ i $x=2$. Granice: $x\in[0,2]$, $y\in[x^2/2,\,x]$.",
            r"Unutarnji integral po $y$: $\int_{x^2/2}^x\frac{x}{x^2+y^2}\,\mathrm{d}y=\arctan\frac{y}{x}\Big|_{x^2/2}^x$."
        ]
    },
    {
        "tekst": r"Odredite lokalne ekstreme funkcije $z=x^2+y^2+2x+2y$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Koordinata x minimuma:", "answer": "-1"},
            {"label": "Koordinata y minimuma:", "answer": "-1"},
            {"label": "Vrijednost minimuma:", "answer": "-2"}
        ]),
        "rjesenje": r"Lokalni minimum u $T(-1,-1)$: $z=-2$.",
        "hints": [
            r"$z_x=2x+2=0\Rightarrow x=-1$; $z_y=2y+2=0\Rightarrow y=-1$.",
            r"$H=z_{xx}z_{yy}-z_{xy}^2=4>0$ i $z_{xx}=2>0$ $\Rightarrow$ minimum."
        ]
    },
    {
        "tekst": r"Ispitajte je li funkcija $f(x,y)=\dfrac{x^4-3y^4}{x^4+y^4}$ (za $(x,y)\neq(0,0)$), $f(0,0)=0$, neprekidna u $(0,0)$.",
        "tip": "choice",
        "tocan_odgovor": choice("nije neprekidna", NEP),
        "rjesenje": r"nije neprekidna",
        "hints": [
            r"Uz $y=0$: $\lim\frac{x^4}{x^4}=1\neq 0=f(0,0)$.",
            r"Budući da limes $\neq f(0,0)$, funkcija nije neprekidna u $(0,0)$."
        ]
    },
    {
        "tekst": r"Izračunajte volumen tijela omeđenog plohama $z=x^2+y^2$ i $z=4$.",
        "tip": "auto",
        "tocan_odgovor": "8*pi",
        "rjesenje": r"$V=8\pi$",
        "hints": [
            r"Presjek: $x^2+y^2=4$ (krug polumjera $2$). Koristite polarne koordinate.",
            r"$V=\int_0^{2\pi}\int_0^2(4-r^2)r\,\mathrm{d}r\,\mathrm{d}\varphi=8\pi$."
        ]
    },
    {
        "tekst": r"Dana je funkcija $w=f(u,v)$, gdje je $u=\dfrac{y-x}{xy}$, $v=\dfrac{z-x}{xz}$. "
                 r"Izračunajte $x^2\dfrac{\partial w}{\partial x}+y^2\dfrac{\partial w}{\partial y}+z^2\dfrac{\partial w}{\partial z}$.",
        "tip": "auto",
        "tocan_odgovor": "0",
        "rjesenje": r"$0$",
        "hints": [
            r"Primijenite pravilo ulančavanja: $\frac{\partial w}{\partial x}=\frac{\partial f}{\partial u}\cdot\frac{\partial u}{\partial x}+\frac{\partial f}{\partial v}\cdot\frac{\partial v}{\partial x}$.",
            r"Izračunajte sve parcijalne derivacije $u$ i $v$, te zbrojite $x^2 w_x+y^2 w_y+z^2 w_z$. Sve se poništi na $0$."
        ]
    },
    {
        "tekst": r"Odredite točke na plohi $x^2+y^2+4z^2=36$ u kojima je tangencijalna ravnina okomita na ravnine $x+z-1=0$ i $y-z-2=0$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Točka T₁ (x,y,z):", "answer": "(-4, 4, 1)"},
            {"label": "Točka T₂ (x,y,z):", "answer": "(4, -4, -1)"}
        ]),
        "rjesenje": r"$T_1(-4,4,1)$ i $T_2(4,-4,-1)$",
        "hints": [
            r"Normala tangencijalne ravnine: $\nabla F=(2x,2y,8z)$. Mora biti $\perp$ normalama zadanih ravnina: $n_1=(1,0,1)$ i $n_2=(0,1,-1)$.",
            r"Uvjet: $\nabla F\cdot n_1=0$ i $\nabla F\cdot n_2=0$: $2x+8z=0$ i $2y-8z=0$. Uvrstite u jednadžbu plohe."
        ]
    },
    {
        "tekst": r"Zamijenite redoslijed integracije u integralu "
                 r"$\displaystyle\int_0^1\!\mathrm{d}x\int_0^x(2x-y)\,\mathrm{d}y+\int_1^2\!\mathrm{d}x\int_0^{2-x}(2x-y)\,\mathrm{d}y$ "
                 r"i izračunajte ga.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Novi integral (granice za y):", "answer": "0 do 1"},
            {"label": "Vrijednost integrala =", "answer": "5/3"}
        ]),
        "rjesenje": r"$\displaystyle\int_0^1\mathrm{d}y\int_y^{2-y}(2x-y)\,\mathrm{d}x=\dfrac{5}{3}$",
        "hints": [
            r"Skicirajte područje: trokut s vrhovima $(0,0)$, $(2,0)$, $(1,1)$, omeđeno pravcima $y=0$, $y=x$ i $y=2-x$.",
            r"Novi redoslijed: $y\in[0,1]$, $x\in[y,2-y]$."
        ]
    },
    {
        "tekst": r"Izračunajte volumen tijela omeđenog plohama $z=x^2+y^2$ i $z=1$.",
        "tip": "auto",
        "tocan_odgovor": "pi/2",
        "rjesenje": r"$V=\dfrac{\pi}{2}$",
        "hints": [
            r"Presjek: $x^2+y^2=1$ (krug polumjera $1$). Koristite polarne koordinate.",
            r"$V=\int_0^{2\pi}\int_0^1(1-r^2)r\,\mathrm{d}r\,\mathrm{d}\varphi=\frac{\pi}{2}$."
        ]
    },
    {
        "tekst": r"Odredite točke na plohi $x^2+3y^2+2z^2=12$ u kojima je normala na plohu paralelna s presječnicom ravnina $x+2y-z=2$ i $x-y+3z=1$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "T₁ — koordinata x:", "answer": "30*sqrt(2)/sqrt(209)"},
            {"label": "T₁ — koordinata y:", "answer": "-8*sqrt(2)/sqrt(209)"},
            {"label": "T₁ — koordinata z:", "answer": "-9*sqrt(2)/sqrt(209)"}
        ]),
        "rjesenje": r"$T_{1,2}=\pm\dfrac{\sqrt{2}}{\sqrt{209}}(30,-8,-9)$",
        "hints": [
            r"Normala plohe $\nabla F=(2x,6y,4z)$ mora biti paralelna s $n_1\times n_2=(5,-4,-3)$.",
            r"Iz $2x=5k$, $6y=-4k$, $4z=-3k$ uvrstite u jednadžbu plohe."
        ]
    },
    {
        "tekst": r"Odredite točke na ravninskoj krivulji $(x-3)^2+(y-4)^2=4$ koje su najbliže ishodištu.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Koordinata x najbliže točke:", "answer": "9/5"},
            {"label": "Koordinata y najbliže točke:", "answer": "12/5"}
        ]),
        "rjesenje": r"$T\!\left(\dfrac{9}{5},\dfrac{12}{5}\right)$",
        "hints": [
            r"Najkraća udaljenost od ishodišta do kružnice $s$ središtem $(3,4)$ i polumjerom $2$: točka leži na pravcu $OS$.",
            r"$|OS|=5$, pa je najbliža točka na udaljenosti $5-2=3$ od ishodišta: $T=\frac{3}{5}(3,4)=\left(\frac{9}{5},\frac{12}{5}\right)$."
        ]
    },
    {
        "tekst": r"Izračunajte $\displaystyle\iint_S y\,\mathrm{d}x\,\mathrm{d}y$, gdje je $S$ gornji polukrug promjera $a$ sa središtem u ishodištu.",
        "tip": "auto",
        "tocan_odgovor": "a**3/12",
        "rjesenje": r"$I=\dfrac{a^3}{12}$",
        "hints": [
            r"Polumjer kruga $R=a/2$. Koristite polarne koordinate: $x=r\cos\varphi$, $y=r\sin\varphi$, $r\in[0,a/2]$, $\varphi\in[0,\pi]$.",
            r"$\int_0^\pi\sin\varphi\,\mathrm{d}\varphi\cdot\int_0^{a/2}r^2\,\mathrm{d}r=2\cdot\frac{(a/2)^3}{3}=\frac{a^3}{12}$."
        ]
    },
    {
        "tekst": r"Odredite jednadžbu tangencijalne ravnine na plohu $z=xy+1$ koja je okomita na pravac "
                 r"$\dfrac{x-1}{1}=\dfrac{y+5}{-1}=\dfrac{z-2}{1}$. Upišite lijevu stranu jednadžbe oblika $Ax+By+Cz+D=0$.",
        "tip": "auto",
        "tocan_odgovor": "x-y+z-2",
        "rjesenje": r"Ravnina: $x-y+z-2=0$, dodirna točka $T(1,-1,0)$.",
        "hints": [
            r"$F(x,y,z)=xy-z+1=0$, $\nabla F=(y,x,-1)$. Traži se $\nabla F\parallel(1,-1,1)$.",
            r"$(y,x,-1)=k(1,-1,1)\Rightarrow k=-1$, $y=1$... pažljivo: $k=-1\Rightarrow y=-1$, $x=1$, $z=1\cdot(-1)+1=0$."
        ]
    },
    {
        "tekst": r"Izračunajte volumen tijela omeđenog plohom $z=2-\sqrt{x^2+y^2}$ i ravninom $z=0$.",
        "tip": "auto",
        "tocan_odgovor": "8*pi/3",
        "rjesenje": r"$V=\dfrac{8\pi}{3}$",
        "hints": [
            r"Presjek s ravninom $z=0$: $x^2+y^2\le 4$ (krug polumjera $2$). Koristite polarne koordinate.",
            r"$V=\int_0^{2\pi}\int_0^2(2-r)r\,\mathrm{d}r\,\mathrm{d}\varphi=2\pi\left[r^2-\frac{r^3}{3}\right]_0^2=\frac{8\pi}{3}$."
        ]
    },
    {
        "tekst": r"Odredite $\dfrac{\partial^2 z}{\partial x\,\partial y}$ ako je $z=f(u,v)$, $u=y+\sin x$, $v=3x$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Koeficijent uz f_uu (∂²f/∂u²):", "answer": "cos(x)"},
            {"label": "Koeficijent uz f_uv (∂²f/∂u∂v):", "answer": "3"}
        ]),
        "rjesenje": r"$\dfrac{\partial^2 z}{\partial x\,\partial y}=f_{uu}\cos x+3f_{uv}$",
        "hints": [
            r"$\frac{\partial z}{\partial y}=f_u\cdot\frac{\partial u}{\partial y}+f_v\cdot\frac{\partial v}{\partial y}=f_u$ (jer $\frac{\partial u}{\partial y}=1$, $\frac{\partial v}{\partial y}=0$).",
            r"$\frac{\partial^2 z}{\partial x\,\partial y}=\frac{\partial f_u}{\partial x}=f_{uu}\cos x+f_{uv}\cdot 3$."
        ]
    },
    {
        "tekst": r"Odredite točku u ravnini $3x-2z=0$ za koju je zbroj kvadrata udaljenosti do točaka $A(1,1,1)$ i $B(2,3,4)$ najmanji.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Koordinata x minimalne točke:", "answer": "21/13"},
            {"label": "Koordinata y minimalne točke:", "answer": "2"},
            {"label": "Koordinata z minimalne točke:", "answer": "63/26"}
        ]),
        "rjesenje": r"$T\!\left(\dfrac{21}{13},\,2,\,\dfrac{63}{26}\right)$",
        "hints": [
            r"Iz jednadžbe ravnine: $z=\frac{3}{2}x$. Točka na ravnini: $(x,y,\frac{3}{2}x)$.",
            r"Minimizacija: $f(x,y)=(x-1)^2+(y-1)^2+(\frac{3}{2}x-1)^2+(x-2)^2+(y-3)^2+(\frac{3}{2}x-4)^2$."
        ]
    },
    {
        "tekst": r"Pronađite točke u prostoru na presjeku plohe $x^2+y^2=2$ i ravnine $x+z=1$ u kojima je zbroj koordinata minimalan.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Koordinata x:", "answer": "0"},
            {"label": "Koordinata y:", "answer": "-sqrt(2)"},
            {"label": "Koordinata z:", "answer": "1"}
        ]),
        "rjesenje": r"$T(0,-\sqrt{2},1)$",
        "hints": [
            r"Iz $x+z=1$: $z=1-x$. Funkcija cilja: $f=x+y+z=y+1$. Minimiziramo $y$ uz $x^2+y^2=2$.",
            r"Minimalni $y=-\sqrt{2}$ uz $x=0$, $z=1$."
        ]
    },
    {
        "tekst": r"Izračunajte volumen tijela omeđenog plohama $z=x^2+y^2$, $z=x^2+2y^2$, $y=x$, $y=2x$ i $x=1$.",
        "tip": "auto",
        "tocan_odgovor": "7/12",
        "rjesenje": r"$V=\dfrac{7}{12}$",
        "hints": [
            r"Visina tijela u svakoj točki: $\Delta z=(x^2+2y^2)-(x^2+y^2)=y^2$.",
            r"Područje u $xy$-ravnini: $x\in[0,1]$, $y\in[x,2x]$. $V=\int_0^1\int_x^{2x}y^2\,\mathrm{d}y\,\mathrm{d}x=\frac{7}{12}$."
        ]
    },
    {
        "tekst": r"Korištenjem trostrukog integrala izračunajte volumen kugle $x^2+y^2+z^2\le R^2$.",
        "tip": "auto",
        "tocan_odgovor": "4*pi*R**3/3",
        "rjesenje": r"$V=\dfrac{4}{3}\pi R^3$",
        "hints": [
            r"Prijeđite na sferne koordinate: $x=r\sin\phi\cos\theta$, $y=r\sin\phi\sin\theta$, $z=r\cos\phi$, Jakobijan $=r^2\sin\phi$.",
            r"$V=\int_0^{2\pi}\int_0^\pi\int_0^R r^2\sin\phi\,\mathrm{d}r\,\mathrm{d}\phi\,\mathrm{d}\theta=\frac{4}{3}\pi R^3$."
        ]
    },
    {
        "tekst": r"Izračunajte $\displaystyle\int_0^1\mathrm{d}x\int_0^x\mathrm{d}y\int_0^{x+y}(2z-x)\,\mathrm{d}z$.",
        "tip": "auto",
        "tocan_odgovor": "5/24",
        "rjesenje": r"$I=\dfrac{5}{24}$",
        "hints": [
            r"Riješite unutarnji integral po $z$: $\int_0^{x+y}(2z-x)\,\mathrm{d}z=(x+y)^2-x(x+y)=y^2+xy$.",
            r"Srednji integral: $\int_0^x(y^2+xy)\,\mathrm{d}y=\frac{x^3}{3}+\frac{x^3}{2}=\frac{5x^3}{6}$. Vanjski: $\int_0^1\frac{5x^3}{6}\,\mathrm{d}x=\frac{5}{24}$."
        ]
    },
    {
        "tekst": r"Pokažite da $z=\arctan\!\left(\dfrac{x}{y}\right)$ (gdje $x=u+v$, $y=u-v$) zadovoljava "
                 r"$\dfrac{\partial z}{\partial u}+\dfrac{\partial z}{\partial v}=\dfrac{u-v}{u^2+v^2}$. "
                 r"Upišite brojnik i nazivnik desne strane.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Brojnik:", "answer": "u-v"},
            {"label": "Nazivnik:", "answer": "u**2+v**2"}
        ]),
        "rjesenje": r"$\dfrac{\partial z}{\partial u}+\dfrac{\partial z}{\partial v}=\dfrac{u-v}{u^2+v^2}$",
        "hints": [
            r"$\frac{\partial z}{\partial u}=\frac{\partial z}{\partial x}\cdot 1+\frac{\partial z}{\partial y}\cdot 1$, $\frac{\partial z}{\partial v}=\frac{\partial z}{\partial x}\cdot 1+\frac{\partial z}{\partial y}\cdot(-1)$.",
            r"$\frac{\partial z}{\partial x}=\frac{y}{x^2+y^2}$, $\frac{\partial z}{\partial y}=\frac{-x}{x^2+y^2}$. Uvrstite $x=u+v$, $y=u-v$."
        ]
    },
    {
        "tekst": r"Odredite domenu funkcije $f(x,y)=\arctan(x+y)+\arccos(x^2+y^2-10)+\ln(2y-4x^2)$. "
                 r"Odredite granice za $r^2=x^2+y^2$ i uvjet za $y$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Donja granica r² =", "answer": "9"},
            {"label": "Gornja granica r² =", "answer": "11"},
            {"label": "Uvjet za y (u obliku y > ...):", "answer": "2*x**2"}
        ]),
        "rjesenje": r"$D=\{(x,y): 9\le x^2+y^2\le 11,\; y>2x^2\}$",
        "hints": [
            r"$\arccos$: $-1\le x^2+y^2-10\le 1\Rightarrow 9\le r^2\le 11$.",
            r"$\ln$: $2y-4x^2>0\Rightarrow y>2x^2$."
        ]
    },
    {
        "tekst": r"Odredite domenu funkcije $f(x,y)=\ln(8x-2y^2)+\arcsin(y-2)+\sqrt{x^2-2x+y^2}$. "
                 r"Odredite granice za $y$ i uvjet za $x$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Donja granica za y =", "answer": "1"},
            {"label": "Gornja granica za y =", "answer": "3"},
            {"label": "Uvjet za x (u obliku x > ...):", "answer": "y**2/4"}
        ]),
        "rjesenje": r"$D=\{(x,y): x>\frac{y^2}{4},\; 1\le y\le 3\}$",
        "hints": [
            r"$\arcsin$: $-1\le y-2\le 1\Rightarrow 1\le y\le 3$.",
            r"$\ln$: $8x-2y^2>0\Rightarrow x>y^2/4$. Korijen: $(x-1)^2+y^2\ge 0$ — uvijek ispunjeno."
        ]
    },
    {
        "tekst": r"Izračunajte $\displaystyle\iint_S x\,\mathrm{d}x\,\mathrm{d}y$, gdje je $S$ u prvom kvadrantu omeđeno pravcem kroz $A(2,0)$, $B(0,2)$ i donjim lukom kružnice $x^2+(y-1)^2=1$.",
        "tip": "auto",
        "tocan_odgovor": "1/2",
        "rjesenje": r"$I=\dfrac{1}{2}$",
        "hints": [
            r"Pravac: $y=2-x$. Donji luk kružnice: $y=1-\sqrt{1-x^2}$, $x\in[0,1]$.",
            r"$I=\int_0^1\int_{1-\sqrt{1-x^2}}^{2-x}x\,\mathrm{d}y\,\mathrm{d}x$. Primijenite Fubinijev teorem."
        ]
    },
    {
        "tekst": r"Odredite točku na ravnini $3x-2z=0$ za koju je zbroj kvadrata udaljenosti do $A(1,1,1)$ i $B(2,3,4)$ najmanji. Koristite Lagrangeove multiplikatore ili supstituciju.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "x =", "answer": "21/13"},
            {"label": "y =", "answer": "2"},
            {"label": "z =", "answer": "63/26"}
        ]),
        "rjesenje": r"$T\!\left(\frac{21}{13},2,\frac{63}{26}\right)$",
        "hints": [
            r"Iz $3x-2z=0$: $z=\frac{3}{2}x$. Uvrstite u $f(x,y)=d_A^2+d_B^2$ i izjednačite parcijalne derivacije s $0$.",
            r"$\frac{\partial f}{\partial y}=2(y-1)+2(y-3)=0\Rightarrow y=2$."
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
        module = db.query(models.Module).filter(
            models.Module.course_id == course.id,
            models.Module.naziv == MODULE_NAME,
        ).first()
        if not module:
            print(f"Modul '{MODULE_NAME}' ne postoji unutar '{COURSE_NAME}'. Pokreni seed.")
            return
        existing = db.query(models.Problem).filter(
            models.Problem.module_id == module.id,
        ).all()
        for p in existing:
            db.delete(p)
        db.flush()
        for i, z in enumerate(ZADACI):
            problem = models.Problem(
                course_id=course.id, module_id=module.id,
                tekst=z["tekst"], tip=z["tip"],
                tocan_odgovor=z["tocan_odgovor"],
                rjesenje=z["rjesenje"], redoslijed=i,
            )
            for j, h in enumerate(z.get("hints", [])):
                problem.hints.append(models.Hint(sadrzaj=h, redoslijed=j))
            db.add(problem)
        db.commit()
        print(f"Umetnuto {len(ZADACI)} zadataka za modul '{MODULE_NAME}'.")
        tips = {}
        for z in ZADACI:
            tips[z["tip"]] = tips.get(z["tip"], 0) + 1
        for t, c in sorted(tips.items()):
            print(f"  {t}: {c}")
    except Exception as exc:
        import traceback
        traceback.print_exc()
    finally:
        db.close()


if __name__ == "__main__":
    run()