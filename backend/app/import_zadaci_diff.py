"""
Import 40 zadataka za kolegij "Diferencijalni racun".
Pokretanje: python -m app.import_zadaci_diff
"""

import json
from .database import Base, engine, SessionLocal
from . import models

COURSE_NAME = "Diferencijalni racun"

def multi(fields):
    return json.dumps(fields, ensure_ascii=False)

ZADACI = [
    {
        "tekst": r"Izračunajte: $$\sqrt[3]{20+14\sqrt{2}}+\sqrt[3]{20-14\sqrt{2}}$$",
        "tip": "auto",
        "tocan_odgovor": "4",
        "rjesenje": r"Postavimo $x = \sqrt[3]{20+14\sqrt{2}} + \sqrt[3]{20-14\sqrt{2}}$. Kubiranjem uz $ab=2$ dobivamo $x^3-6x-40=0$. Jedino realno rješenje je $x=4$.",
        "hints": [r"Iskoristite $(a+b)^3 = a^3+b^3+3ab(a+b)$.", r"Kubna jednadžba $x^3-6x-40=0$ ima rješenje $x=4$."]
    },
    {
        "tekst": r"Ako je $f(x)=\sin^4 x + \cos^4 x$ i vrijedi $\sin 2x_0 = \tfrac{2}{3}$, izračunajte $f(x_0)$.",
        "tip": "auto",
        "tocan_odgovor": "7/9",
        "rjesenje": r"$f(x) = 1 - \tfrac{1}{2}\sin^2 2x$. Uvrštavanjem: $f(x_0) = 1 - \tfrac{1}{2}\cdot\tfrac{4}{9} = \tfrac{7}{9}$.",
        "hints": [r"$\sin^4 x+\cos^4 x = 1-2\sin^2 x\cos^2 x$.", r"$f(x) = 1-\tfrac{1}{2}\sin^2(2x)$."]
    },
    {
        "tekst": r"Za skup $$S = \left\{\frac{2n+5}{n+2} : n \in \mathbb{N}\right\}$$ odredite:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "inf S =", "answer": "2"},
            {"label": "sup S =", "answer": "7/3"},
            {"label": "min S =", "answer": "ne postoji"},
            {"label": "max S =", "answer": "7/3"}
        ]),
        "rjesenje": r"$a_n = 2+\tfrac{1}{n+2}$, niz je padajući. $\inf S=2$, $\sup S=\max S=\tfrac{7}{3}$, $\min S$ ne postoji.",
        "hints": [r"$a_n = 2+\tfrac{1}{n+2}$.", r"Niz je padajući — prvi član je max/sup, limes je inf."]
    },
    {
        "tekst": r"Za skup $$S = \left\{\frac{3n+1}{2n+1} : n \in \mathbb{N}\right\}$$ odredite:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "inf S =", "answer": "4/3"},
            {"label": "sup S =", "answer": "3/2"}
        ]),
        "rjesenje": r"$a_n = \tfrac{3}{2}-\tfrac{1}{2(2n+1)}$, niz je rastući. $\inf S=\min S=\tfrac{4}{3}$, $\sup S=\tfrac{3}{2}$.",
        "hints": [r"$a_n = \tfrac{3}{2}-\tfrac{1}{2(2n+1)}$.", r"Niz je rastući, $\inf=a_1$, $\sup$ je limes."]
    },
    {
        "tekst": r"Za rekurzivno zadan niz $a_1=1$, $$a_n = \frac{1}{7}(a_{n-1}^{2}+10),\quad n\ge 2$$ odredite $\lim_{n\to\infty} a_n$.",
        "tip": "auto",
        "tocan_odgovor": "2",
        "rjesenje": r"Iz $L=\tfrac{1}{7}(L^2+10)$: $L^2-7L+10=0$, $L=2$ ili $L=5$. Indukcijom $a_n\le 2$, pa $L=2$.",
        "hints": [r"$L^2-7L+10=0$.", r"$L=2$ ili $L=5$, ali niz je omeđen s $2$."]
    },
    {
        "tekst": r"Zbroj prvih 11 članova geometrijskog niza čini 20% od zbroja sljedećih 11 članova. Koliko iznosi $a_{11}:a_1$?",
        "tip": "auto",
        "tocan_odgovor": "5^(10/11)",
        "rjesenje": r"$q^{11}=5$. Omjer: $q^{10}=5^{10/11}$.",
        "hints": [r"Zbroj sljedećih 11 članova je $q^{11}\cdot S_{11}$.", r"$q^{10}=(q^{11})^{10/11}=5^{10/11}$."]
    },
    {
        "tekst": r"Umnožak trećeg i devetog člana geometrijskog niza s pozitivnim članovima jednak je 9. Koliko iznosi umnožak prvih jedanaest članova?",
        "tip": "auto",
        "tocan_odgovor": "177147",
        "rjesenje": r"$a_3 a_9 = a_1^{2}q^{10}=9$. $P_{11}=9^{11/2}=3^{11}=177147$.",
        "hints": [r"$a_3\cdot a_9 = a_1^{2}q^{10}=9$.", r"$P_{11}=9^{11/2}=3^{11}$."]
    },
    {
        "tekst": r"Za $\epsilon=0.02$ odredite $n_0(\epsilon)$ iz definicije limesa niza $$\lim_{n\to\infty}\frac{n-1}{2n+1}=\frac{1}{2}$$",
        "tip": "auto",
        "tocan_odgovor": "38",
        "rjesenje": r"$\tfrac{3}{2(2n+1)}<0.02 \Rightarrow n>37$. Za $n=37$ jednako, ne strogo manje. $n_0=38$.",
        "hints": [r"Razlika s limesom je $\tfrac{3}{2(2n+1)}$.", r"$n>37$, pa $n_0=38$."]
    },
    {
        "tekst": r"Izračunajte: $$\lim_{n\to\infty} n^{11/2}\!\left(\sqrt{n^{11}+1}-\sqrt{n^{11}}\right)$$",
        "tip": "auto",
        "tocan_odgovor": "1/2",
        "rjesenje": r"Množimo konjugatom: $\tfrac{n^{11/2}}{\sqrt{n^{11}+1}+\sqrt{n^{11}}}\to\tfrac{1}{2}$.",
        "hints": [r"Pomnožite konjugatom.", r"Dijeljenjem s $n^{11/2}$ dobiva se $\tfrac{1}{2}$."]
    },
    {
        "tekst": r"Izračunajte: $$\lim_{n\to\infty}\left(\frac{2n^{2}+1}{2n^{2}-1}\right)^{\!\tfrac{3n^{2}+1}{n-1}}$$",
        "tip": "auto",
        "tocan_odgovor": "1",
        "rjesenje": r"Baza $=1+\tfrac{2}{2n^{2}-1}$. Produkt u eksponentu $\to 0$. Limes $e^0=1$.",
        "hints": [r"Baza: $1+\tfrac{2}{2n^{2}-1}$.", r"Produkt teži k $0$, limes je $1$."]
    },
    {
        "tekst": r"Izračunajte: $$\lim_{n\to\infty}\left(\frac{1}{2\cdot 5}+\frac{1}{5\cdot 8}+\cdots+\frac{1}{(3n\!-\!1)(3n\!+\!2)}\right)$$",
        "tip": "auto",
        "tocan_odgovor": "1/6",
        "rjesenje": r"Parcijalni razlomci, teleskopska suma: $\tfrac{1}{3}(\tfrac{1}{2}-\tfrac{1}{3n+2})\to\tfrac{1}{6}$.",
        "hints": [r"Rastavite na parcijalne razlomke.", r"Suma je teleskopska."]
    },
    {
        "tekst": r"Izračunajte: $$\lim_{n\to\infty}\frac{\displaystyle 1 + \frac{1}{4} + \frac{1}{4^{2}} + \cdots + \frac{1}{4^{n}}}{\displaystyle \frac{1}{7} + \frac{1}{7^{2}} + \cdots + \frac{1}{7^{n}}}$$","tip": "auto",
        "tocan_odgovor": "8",
        "rjesenje": r"Brojnik: $\tfrac{4}{3}$. Nazivnik: $\tfrac{1}{6}$. Limes: $8$.",
        "hints": [r"Geometrijski redovi: brojnik $\tfrac{4}{3}$, nazivnik $\tfrac{1}{6}$."]
    },
    {
        "tekst": r"Izračunajte: $$\lim_{n\to\infty}\frac{\sin(2n+1)\cos(n^{3}+3n)}{n^{2}+1}$$",
        "tip": "auto",
        "tocan_odgovor": "0",
        "rjesenje": r"$|\sin(\cdot)\cos(\cdot)|\le 1$, $n^{2}+1\to\infty$. Teorem o sendviču: $0$.",
        "hints": [r"Teorem o sendviču — omeđen brojnik, nazivnik $\to\infty$."]
    },
    {
        "tekst": r"Izračunajte: $$\lim_{n\to\infty}\frac{\sqrt{n+\sqrt{n+\sqrt{n+\sqrt{n+\sqrt{n}}}}}}{\sqrt{n+3}}$$",
        "tip": "auto",
        "tocan_odgovor": "1",
        "rjesenje": r"Podijelimo s $\sqrt{n}$. Dominantni članovi daju $1$.",
        "hints": [r"Podijelite sve pod korijenima s $\sqrt{n}$."]
    },
    {
        "tekst": r"Izračunajte: $$\lim_{n\to\infty}\left(\frac{3n^{2}-2}{3n^{2}+1}\right)^{\!n^{2}-4}$$",
        "tip": "auto",
        "tocan_odgovor": "1/e",
        "rjesenje": r"$(1-\tfrac{3}{3n^{2}+1})^{n^{2}-4}$. Eksponent $\to -1$. Limes: $e^{-1}$.",
        "hints": [r"Baza: $1-\tfrac{3}{3n^{2}+1}$.", r"Limes je $e^{-1}$."]
    },
    {
        "tekst": r"Odredite $\lambda\in\mathbb{R}$ takav da za niz $$a_n=\sqrt{n^{2}-\lambda n+7}-\sqrt{n^{2}-2n+5}$$ vrijedi $\lim_{n\to\infty}a_n=1$.",
        "tip": "auto",
        "tocan_odgovor": "0",
        "rjesenje": r"Množimo konjugatom: limes je $\tfrac{2-\lambda}{2}$. Iz $\tfrac{2-\lambda}{2}=1$: $\lambda=0$.",
        "hints": [r"Konjugatom: $\tfrac{(2-\lambda)n+2}{\sqrt{\cdots}+\sqrt{\cdots}}$.", r"$\tfrac{2-\lambda}{2}=1\Rightarrow\lambda=0$."]
    },
    {
        "tekst": r"Ako je $f(x)=\log\tfrac{1+x}{1-x}$ i $g(x)=\tfrac{x^{3}+3x}{3x^{2}+1}$, izračunajte $(f\circ g)(x)-3f(x)$.",
        "tip": "auto",
        "tocan_odgovor": "0",
        "rjesenje": r"$\tfrac{1+g(x)}{1-g(x)}=\left(\tfrac{1+x}{1-x}\right)^{3}$. Dakle $f(g(x))=3f(x)$, rezultat $0$.",
        "hints": [r"Pokažite $\tfrac{1+g(x)}{1-g(x)}=\left(\tfrac{1+x}{1-x}\right)^{3}$.", r"$f(g(x))=3f(x)$."]
    },
    {
        "tekst": r"Za funkcije $f(x)=x-1$ i $g(x)=\tfrac{x-3}{x-2}$ odredite:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "$(f\\circ g)(x) =$", "answer": "-1/(x-2)"},
            {"label": "$(g\\circ f)(x) =$", "answer": "(x-4)/(x-3)"}
        ]),
        "rjesenje": r"$(f\circ g)(x)=\tfrac{x-3}{x-2}-1=\tfrac{-1}{x-2}$. $(g\circ f)(x)=\tfrac{x-4}{x-3}$.",
        "hints": [r"$(f\circ g)(x)=g(x)-1$.", r"$(g\circ f)(x)=g(x-1)$."]
    },
    {
        "tekst": r"Bez L'Hospitalovog pravila izračunajte: $$\lim_{x\to 0}\frac{x}{\sqrt[3]{x+1}-1}$$",
        "tip": "auto",
        "tocan_odgovor": "3",
        "rjesenje": r"Razlika kubova: izraz $=\sqrt[3]{(x+1)^{2}}+\sqrt[3]{x+1}+1\to 3$.",
        "hints": [r"$a-1=\tfrac{a^{3}-1}{a^{2}+a+1}$ za $a=\sqrt[3]{x+1}$.", r"Izraz $\to 1+1+1=3$."]
    },
    {
        "tekst": r"Bez L'Hospitalovog pravila izračunajte: $$\lim_{x\to 0^{+}}(3x+1)^{\,1/(e^{4x}-1)}$$",
        "tip": "auto",
        "tocan_odgovor": "e^(3/4)",
        "rjesenje": r"$\lim\tfrac{\ln(1+3x)}{e^{4x}-1}=\tfrac{3}{4}$. Limes: $e^{3/4}$.",
        "hints": [r"Oblik $e^{\lim\frac{\ln(1+3x)}{e^{4x}-1}}$.", r"Pomnožite s $\tfrac{3x}{3x}$ i $\tfrac{4x}{4x}$."]
    },
    {
        "tekst": r"Bez L'Hospitalovog pravila izračunajte: $$\lim_{x\to 0}\frac{x\sin x}{1-\cos 2x}$$",
        "tip": "auto",
        "tocan_odgovor": "1/2",
        "rjesenje": r"$1-\cos 2x=2\sin^{2}x$. Izraz: $\tfrac{1}{2}\cdot\tfrac{x}{\sin x}\to\tfrac{1}{2}$.",
        "hints": [r"$1-\cos 2x=2\sin^{2}x$.", r"$\tfrac{x\sin x}{2\sin^{2}x}=\tfrac{1}{2}\cdot\tfrac{x}{\sin x}$."]
    },
    {
        "tekst": r"Bez L'Hospitalovog pravila izračunajte: $$\lim_{x\to 0}\frac{\ln(1+x\cos x)}{x}$$",
        "tip": "auto",
        "tocan_odgovor": "1",
        "rjesenje": r"$\tfrac{\ln(1+x\cos x)}{x\cos x}\cdot\cos x\to 1$.",
        "hints": [r"Napišite kao $\tfrac{\ln(1+x\cos x)}{x\cos x}\cdot\cos x$."]
    },
    {
        "tekst": r"Bez L'Hospitalovog pravila izračunajte: $$\lim_{x\to\infty}\frac{\ln(x^{2}-2x+7)}{\ln(x^{10}+6x+4)}$$",
        "tip": "auto",
        "tocan_odgovor": "1/5",
        "rjesenje": r"Brojnik $\approx 2\ln x$, nazivnik $\approx 10\ln x$. Limes: $\tfrac{1}{5}$.",
        "hints": [r"Izlučite najveću potenciju u logaritmima.", r"$\tfrac{2\ln x}{10\ln x}=\tfrac{1}{5}$."]
    },
    {
        "tekst": r"Bez L'Hospitalovog pravila izračunajte: $$\lim_{x\to 1/5}\frac{5x^{2}-6x+1}{5x-1}$$",
        "tip": "auto",
        "tocan_odgovor": "-4/5",
        "rjesenje": r"$(5x-1)(x-1)/(5x-1)=x-1$. Za $x=\tfrac{1}{5}$: $-\tfrac{4}{5}$.",
        "hints": [r"Rastavite brojnik: $(5x-1)(x-1)$.", r"Skratite i uvrstite."]
    },
    {
        "tekst": r"Dodefinirajte funkciju $$f(x)=\frac{1}{e^{x}-1}-\frac{1}{x}$$ u točki $x=0$ tako da bude neprekidna. Koliki je $f(0)$?",
        "tip": "auto",
        "tocan_odgovor": "-1/2",
        "rjesenje": r"Zajednički nazivnik: $\tfrac{x-(e^{x}-1)}{x(e^{x}-1)}$. Taylor: brojnik $\approx -\tfrac{x^{2}}{2}$, nazivnik $\approx x^{2}$. Limes: $-\tfrac{1}{2}$.",
        "hints": [r"Svedite na zajednički nazivnik.", r"Taylor: $e^{x}\approx 1+x+\tfrac{x^{2}}{2}$."]
    },
    {
        "tekst": r"Odredite proširenje po neprekidnosti funkcije $$f(x)=\frac{\sin(8x)(\cos(5x)-1)}{x^{3}}$$ u točki $x=0$. Koliki je $f(0)$?",
        "tip": "auto",
        "tocan_odgovor": "-100",
        "rjesenje": r"$\tfrac{\sin 8x}{x}\to 8$, $\tfrac{\cos 5x-1}{x^{2}}\to -\tfrac{25}{2}$. Umnožak: $-100$.",
        "hints": [r"Rastavite kao $\tfrac{\sin 8x}{x}\cdot\tfrac{\cos 5x-1}{x^{2}}$.", r"$8\cdot(-\tfrac{25}{2})=-100$."]
    },
    {
        "tekst": r"Odredite parametar $h$ tako da funkcija bude neprekidna: $$f(x)=\begin{cases}14+\tfrac{2|x-5|}{x-5},&x<5\\\tfrac{2\ln(x-4)}{x-5}+10h,&x\ge 5\end{cases}$$",
        "tip": "auto",
        "tocan_odgovor": "1",
        "rjesenje": r"Lijevi limes: $12$. Desni: $2+10h$. $2+10h=12\Rightarrow h=1$.",
        "hints": [r"Lijevi limes u $x=5$: $14+2(-1)=12$.", r"$2+10h=12\Rightarrow h=1$."]
    },
    {
        "tekst": r"Odredite $a$ tako da funkcija bude neprekidna u $x_0=-2$: $$f(x)=\begin{cases}\ln(x+5),&-5<x\le -2\\4-ax^{3},&x>-2\end{cases}$$",
        "tip": "auto",
        "tocan_odgovor": "(ln(3)-4)/8",
        "rjesenje": r"$f(-2)=\ln 3$. Desni: $4+8a=\ln 3\Rightarrow a=\tfrac{\ln 3-4}{8}$.",
        "hints": [r"$f(-2)=\ln 3$.", r"$4+8a=\ln 3$."]
    },
    {
        "tekst": r"Za funkciju $$f(x)=\frac{x^{2}+2}{\sqrt{x}}$$ u točki $x_0=1$ odredite:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Jednadžba tangente: y =", "answer": "(1/2)x+5/2"},
            {"label": "Jednadžba normale: y =", "answer": "-2x+5"}
        ]),
        "rjesenje": r"$f(1)=3$, $f'(1)=\tfrac{1}{2}$. Tangenta: $y=\tfrac{1}{2}x+\tfrac{5}{2}$. Normala: $y=-2x+5$.",
        "hints": [r"$f(1)=3$ i $f'(1)=\tfrac{1}{2}$.", r"Tangenta: $y-3=\tfrac{1}{2}(x-1)$."]
    },
    {
        "tekst": r"Odredite jednadžbu normale na graf funkcije $$f(x)=\ln\sqrt{\frac{e^{2x}}{2e^{2x}-1}}$$ u točki $x_0=0$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Jednadžba normale: y =", "answer": "x"}
        ]),
        "rjesenje": r"$f(0)=0$, $f'(0)=-1$. $k_n=1$. Normala: $y=x$.",
        "hints": [r"$f(0)=0$ i $f'(0)=-1$.", r"$k_n=-1/f'(0)=1$."]
    },
    {
        "tekst": r"Za funkciju $f(x)=x|x-3|$ odredite:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "$f'_{-}(3) =$", "answer": "-3"},
            {"label": "$f'_{+}(3) =$", "answer": "3"}
        ]),
        "rjesenje": r"Za $x<3$: $f=-x^{2}+3x$, $f'(3^{-})=-3$. Za $x>3$: $f=x^{2}-3x$, $f'(3^{+})=3$.",
        "hints": [r"Za $x<3$: $f(x)=-x^{2}+3x$.", r"Za $x>3$: $f(x)=x^{2}-3x$."]
    },
    {
        "tekst": r"Krivulja $f(x)=\tfrac{ax+b}{cx+d}$ prolazi točkom $T=(1,3)$ i ima asimptote $x=2$ i $y=1$. Odredite:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "a =", "answer": "1"},
            {"label": "b =", "answer": "-4"},
            {"label": "c =", "answer": "1"},
            {"label": "d =", "answer": "-2"}
        ]),
        "rjesenje": r"$x=2\Rightarrow d=-2c$. $y=1\Rightarrow a=c$. $f(1)=3\Rightarrow b=-4c$. Uz $c=1$: $a=1,b=-4,d=-2$.",
        "hints": [r"Iz asimptota: $d=-2c$, $a=c$.", r"Iz $f(1)=3$: $b=-4c$."]
    },
    {
        "tekst": r"Odredite $\alpha$ i $\beta$ tako da $y=3x-9$ bude kosa asimptota funkcije: $$f(x)=\frac{\alpha x^{2}+3}{x+\beta}$$",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "α =", "answer": "3"},
            {"label": "β =", "answer": "3"}
        ]),
        "rjesenje": r"$k=\alpha=3$. $l=-3\beta=-9\Rightarrow\beta=3$.",
        "hints": [r"$k=\lim f(x)/x=\alpha$.", r"$l=\lim(f(x)-\alpha x)=-3\beta$."]
    },
    {
        "tekst": r"Primjenom L'Hospitalovog pravila izračunajte: $$\lim_{x\to 0}\frac{\ln\cos 3x}{\ln\cos 5x}$$",
        "tip": "auto",
        "tocan_odgovor": "9/25",
        "rjesenje": r"L'Hospital: $\tfrac{3\tan 3x}{5\tan 5x}$. Još jednom: $\tfrac{3}{5}\cdot\tfrac{3}{5}=\tfrac{9}{25}$.",
        "hints": [r"Oblik $\tfrac{0}{0}$. L'Hospital.", r"$\tfrac{3}{5}\cdot\tfrac{3}{5}=\tfrac{9}{25}$."]
    },
    {
        "tekst": r"Primjenom L'Hospitalovog pravila izračunajte: $$\lim_{x\to 1}\frac{(5x)^{x}-5}{x-1}$$",
        "tip": "auto",
        "tocan_odgovor": "5*(ln(5)+1)",
        "rjesenje": r"$(5x)^{x}=e^{x\ln 5x}$. Derivacija brojnika za $x=1$: $5(\ln 5+1)$.",
        "hints": [r"$(5x)^{x}=e^{x\ln(5x)}$.", r"Derivacija za $x=1$: $5(\ln 5+1)$."]
    },
    {
        "tekst": r"Za $f(x)=\ln x$ i $g(x)=3x$ na $[1,2]$ odredite međutočku $c$ iz Cauchyjeva teorema.",
        "tip": "auto",
        "tocan_odgovor": "1/ln(2)",
        "rjesenje": r"$\tfrac{1/c}{3}=\tfrac{\ln 2}{3}\Rightarrow c=\tfrac{1}{\ln 2}$.",
        "hints": [r"Cauchy: $\tfrac{f'(c)}{g'(c)}=\tfrac{f(2)-f(1)}{g(2)-g(1)}$.", r"$c=\tfrac{1}{\ln 2}$."]
    },
    {
        "tekst": r"Za funkciju $$f(x)=(x^{2}+3)\sqrt{x+2}$$ odredite:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Lokalni maksimum u x =", "answer": "-1"},
            {"label": "Lokalni minimum u x =", "answer": "-3/5"}
        ]),
        "rjesenje": r"$f'(x)=\tfrac{(5x+3)(x+1)}{2\sqrt{x+2}}$. Raste na $(-2,-1)$ i $(-\tfrac{3}{5},\infty)$, opada na $(-1,-\tfrac{3}{5})$.",
        "hints": [r"$f'(x)=\tfrac{(5x+3)(x+1)}{2\sqrt{x+2}}$.", r"Stacionarne točke: $x=-1$ i $x=-\tfrac{3}{5}$."]
    },
    {
        "tekst": r"Za funkciju $$f(x)=e^{-2x^{2}-2x+1}$$ odredite:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Prva točka infleksije: x =", "answer": "-1"},
            {"label": "Druga točka infleksije: x =", "answer": "0"}
        ]),
        "rjesenje": r"$f''(x)=16x(x+1)e^{-2x^{2}-2x+1}$. Konveksna na $(-\infty,-1)$ i $(0,\infty)$, konkavna na $(-1,0)$.",
        "hints": [r"$f''(x)=16x(x+1)e^{(\cdots)}$.", r"$f''=0$ za $x=0$ i $x=-1$."]
    },
    {
        "tekst": r"Za funkciju $$f(x)=\frac{4x}{1+x^{2}}$$ odredite:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Lokalni maksimum u x =", "answer": "1"},
            {"label": "Lokalni minimum u x =", "answer": "-1"}
        ]),
        "rjesenje": r"$f'(x)=\tfrac{4(1-x^{2})}{(1+x^{2})^{2}}$. Raste na $(-1,1)$, opada inače. $f(1)=2$, $f(-1)=-2$.",
        "hints": [r"$f'(x)=\tfrac{4(1-x^{2})}{(1+x^{2})^{2}}$.", r"Predznak ovisi o $(1-x^{2})$."]
    },
    {
        "tekst": r"Za funkciju $$f(x)=\frac{\sqrt{x}}{(\ln x)^{2}}$$ odredite:",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Lokalni minimum u x =", "answer": "e^4"},
            {"label": "Točka infleksije u x =", "answer": "e^6"}
        ]),
        "rjesenje": r"$f'(x)=\tfrac{\ln x-4}{2\sqrt{x}(\ln x)^{3}}$. Opada na $(1,e^{4})$, raste na $(e^{4},\infty)$. Min u $x=e^{4}$. Infleksija u $x=e^{6}$.",
        "hints": [r"$f'=0$ za $\ln x=4\Rightarrow x=e^{4}$.", r"Druga derivacija: predznak ovisi o $6-\ln x$."]
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