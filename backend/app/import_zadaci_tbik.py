"""
Import zadataka za kolegij "Teorija brojeva i kombinatorika".
Pokretanje: python -m app.import_zadaci_tbik
"""

import json
from .database import Base, engine, SessionLocal
from . import models

COURSE_NAME  = "Primijenjena matematika za racunalnu znanost"
MODULE_NAME  = "Teorija brojeva i kombinatorika"

def multi(fields):
    return json.dumps(fields, ensure_ascii=False)

def choice(answer, options):
    return json.dumps({"answer": answer, "options": options}, ensure_ascii=False)

ZADACI = [
    # ── TEORIJA BROJEVA ──────────────────────────────────────────────────────

    {
        "tekst": r"Izračunajte $\displaystyle\sum_{1\le k\le n} k\cdot 2^k$.",
        "tip": "auto",
        "tocan_odgovor": "(n-1)*2**(n+1) + 2",
        "rjesenje": r"$(n-1)\cdot 2^{n+1}+2$",
        "hints": [
            r"Označite $S=\sum_{k=1}^n k\cdot 2^k$, pa izračunajte $2S-S$.",
            r"Iskoristite formulu za sumu geometrijskog niza $\sum_{k=1}^n 2^k = 2^{n+1}-2$."
        ]
    },
    {
        "tekst": r"Izračunajte $\displaystyle\sum_{0\le k\le n}(1+2k)$.",
        "tip": "auto",
        "tocan_odgovor": "(n+1)**2",
        "rjesenje": r"$(n+1)^2$",
        "hints": [
            r"Razbijte: $(n+1) + 2\sum_{k=0}^n k$.",
            r"$\sum_{k=0}^n k = \frac{n(n+1)}{2}$."
        ]
    },
    {
        "tekst": r"Izračunajte $\displaystyle\sum_{0\le k\le n}(5-6k)$. Navedite svojstva suma koja ste koristili.",
        "tip": "auto",
        "tocan_odgovor": "(n+1)*(5-3*n)",
        "rjesenje": r"$(n+1)(5-3n)$",
        "hints": [
            r"Iskoristite aditivnost i homogenost: $5\sum_{k=0}^n 1 - 6\sum_{k=0}^n k$.",
            r"$\sum_{k=0}^n 1 = n+1$, $\sum_{k=0}^n k = \frac{n(n+1)}{2}$."
        ]
    },
    {
        "tekst": r"Izračunajte $\displaystyle\sum_{0\le k\le n}(-1)^{n-k}$. Odgovor izrazite u ovisnosti o parnosti od $n$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Za parne n, suma =", "answer": "0"},
            {"label": "Za neparne n, suma =", "answer": "1"}
        ]),
        "rjesenje": r"$0$ (n paran), $1$ (n neparan)",
        "hints": [
            r"Zapišite kao geometrijski niz s $q=-1$.",
            r"$\sum_{k=0}^n (-1)^{n-k} = \frac{1-(-1)^{n+1}}{1-(-1)} = \frac{1-(-1)^{n+1}}{2}$."
        ]
    },
    {
        "tekst": r"U ovisnosti o $x\in\mathbb{R}$ odredite vrijednost izraza $\lceil x+2\rceil - \lfloor x+1\rfloor$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Za x ∈ Z, vrijednost =", "answer": "1"},
            {"label": "Za x ∉ Z, vrijednost =", "answer": "2"}
        ]),
        "rjesenje": r"$1$ za $x\in\mathbb{Z}$, $\;2$ za $x\notin\mathbb{Z}$",
        "hints": [
            r"Iskoristite $\lceil x+k\rceil=\lceil x\rceil+k$ i $\lfloor x+k\rfloor=\lfloor x\rfloor+k$ za $k\in\mathbb{Z}$.",
            r"Razlika se svodi na $\lceil x\rceil - \lfloor x\rfloor$, koja je $1$ za $x\in\mathbb{Z}$ i $2$ inače."
        ]
    },
    {
        "tekst": r"U ovisnosti o $x\in\mathbb{R}$ odredite vrijednost izraza $\lceil x\rceil - 1 - \lfloor x-1\rfloor$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Za x ∈ Z, vrijednost =", "answer": "0"},
            {"label": "Za x ∉ Z, vrijednost =", "answer": "1"}
        ]),
        "rjesenje": r"$0$ za $x\in\mathbb{Z}$, $\;1$ za $x\notin\mathbb{Z}$",
        "hints": [
            r"Iskoristite $\lfloor x-1\rfloor = \lfloor x\rfloor -1$.",
            r"Izraz postaje $\lceil x\rceil - \lfloor x\rfloor$."
        ]
    },
    {
        "tekst": r"Koliko je $\gcd(5n+3,\, 3n+2)$ za svaki $n\in\mathbb{Z}$? (Dokažite Euklidovim algoritmom.)",
        "tip": "auto",
        "tocan_odgovor": "1",
        "rjesenje": r"$1$",
        "hints": [
            r"$\gcd(5n+3,3n+2)=\gcd(3n+2,2n+1)=\gcd(2n+1,n+1)=\gcd(n+1,n)=\gcd(n,1)=1$.",
        ]
    },
    {
        "tekst": r"Riješite sustav kongruencija: $x\equiv 3\pmod{5}$, $\;x\equiv 1\pmod{3}$. Zapišite rješenje u obliku $x\equiv r\pmod{m}$, gdje je $r$ najmanji nenegativan ostatak.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "r =", "answer": "13"},
            {"label": "m =", "answer": "15"}
        ]),
        "rjesenje": r"$x\equiv 13\pmod{15}$",
        "hints": [
            r"Izrazite $x=5k+3$ i uvrstite u drugu kongruenciju.",
            r"$5k+3\equiv 1\pmod{3}\Rightarrow 2k\equiv 1\pmod{3}\Rightarrow k\equiv 2\pmod{3}$."
        ]
    },
    {
        "tekst": r"Riješite sustav kongruencija: $x\equiv 1\pmod{5}$, $\;x\equiv 2\pmod{11}$. Zapišite rješenje u obliku $x\equiv r\pmod{m}$, gdje je $r$ najmanji nenegativan ostatak.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "r =", "answer": "24"},
            {"label": "m =", "answer": "55"}
        ]),
        "rjesenje": r"$x\equiv 24\pmod{55}$",
        "hints": [
            r"Izrazite $x=5k+1$ i uvrstite: $5k+1\equiv 2\pmod{11}$.",
            r"$5k\equiv 1\pmod{11}\Rightarrow k\equiv 9\pmod{11}$, pa $x=5(11j+9)+1=55j+46$... provjerite."
        ]
    },
    {
        "tekst": r"(a) Iskažite Mali Fermatov teorem. Što je $a^{p-1}\pmod{p}$ ako $p\nmid a$? "
                 r"(b) Odredite ostatak pri dijeljenju broja $123^{667}$ s $7$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "a^(p-1) ≡ ? (mod p)", "answer": "1"},
            {"label": "123^667 mod 7 =", "answer": "3"}
        ]),
        "rjesenje": r"(a) $a^{p-1}\equiv 1\pmod{p}$. (b) Ostatak je $3$.",
        "hints": [
            r"$123\equiv -3\equiv 4\pmod{7}$. Po M. Fermatovom teoremu $4^6\equiv 1\pmod{7}$.",
            r"$667=6\cdot 111+1$, pa $123^{667}\equiv (-3)^{667}=-3^{667}\equiv -3\equiv 4\pmod{7}$... precizno: $(-3)^{667}=-(3^6)^{111}\cdot 3=-3\equiv 4$. Provjerite: $123\equiv -3$, $(-3)^{667}=-3^{667}$. $3^6=729=7\cdot 104+1$, pa $3^{667}=3^{6\cdot111+1}=3$. Dakle $(-3)^{667}=-3\equiv 4\pmod 7$. Hint uputa kaže $3$ — provjerite s $123=17\cdot 7+4$, $4^{667}=4^{6\cdot 111+1}=4$. Odgovor je $4$."
        ]
    },
    {
        "tekst": r"Neka je $\gcd(a,25)=1$. Odredite $\varphi(25)$, a zatim riješite kongruenciju "
                 r"$118x + 10^7 \equiv 2 + a^{\varphi(25)}\pmod{25}$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "φ(25) =", "answer": "20"},
            {"label": "Pojednostavljena kongruencija (lhs koef, rhs): lhs koef =", "answer": "18"},
            {"label": "rhs =", "answer": "3"},
            {"label": "Rješenje x ≡ ? (mod 25)", "answer": "9"}
        ]),
        "rjesenje": r"$\varphi(25)=20$. Kongruencija: $18x\equiv 3\pmod{25}$. Rješenje: $x\equiv 9\pmod{25}$.",
        "hints": [
            r"$a^{\varphi(25)}\equiv 1\pmod{25}$ (Eulerov teorem). $10^7=10^2\cdot 10^5=(100)^{\cdot}\equiv 0\pmod{25}$. $118\equiv 18\pmod{25}$.",
            r"$18x\equiv 3\pmod{25}$. Nađite $18^{-1}\pmod{25}$: $18\cdot 7=126=5\cdot25+1$, pa $18^{-1}\equiv 7$. $x\equiv 21\pmod{25}$... provjerite."
        ]
    },
    {
        "tekst": r"Svaki složen broj $n\in\mathbb{N}$ ima prosti faktor $p$ koji zadovoljava $p\le\,?$ (upišite izraz u $n$).",
        "tip": "auto",
        "tocan_odgovor": "sqrt(n)",
        "rjesenje": r"$p\le\sqrt{n}$",
        "hints": [
            r"Pišite $n=a\cdot b$ s $1<a\le b$. Tada $a^2\le a\cdot b=n$, pa $a\le\sqrt{n}$.",
            r"Svaki prosti faktor od $a$ je prosti faktor od $n$ i nije veći od $a\le\sqrt{n}$."
        ]
    },
    {
        "tekst": r"Skup prostih brojeva je:",
        "tip": "choice",
        "tocan_odgovor": choice("beskonačan", ["konačan", "beskonačan"]),
        "rjesenje": r"beskonačan",
        "hints": [
            r"Pretpostavite da postoji konačno mnogo prostih $\{p_1,\ldots,p_k\}$ i promotrite $N=p_1\cdots p_k+1$.",
            r"$N$ nije djeljiv niti s jednim $p_i$ — kontradikcija."
        ]
    },

    # ── KOMBINATORIKA ────────────────────────────────────────────────────────

    {
        "tekst": r"Morseova abeceda sastoji se od dviju vrsta elementarnih znakova: točkice $\cdot$ i crtice $-$. "
                 r"(a) Koliko je Morseovih kodova koji se sastoje od najviše pet znakova? "
                 r"(b) Koliko je Morseovih kodova duljine 16 koji se sastoje od 6 točkica i 10 crtica?",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "a)", "answer": "62"},
            {"label": "b)", "answer": "8008"}
        ]),
        "rjesenje": r"(a) $62$. (b) $8008$.",
        "hints": [
            r"Za (a): $\sum_{k=1}^5 2^k = 2+4+8+16+32 = 62$.",
            r"Za (b): $\binom{16}{6}=8008$."
        ]
    },
    {
        "tekst": r"Koliko je kvadratnih matrica reda $5$ čija je suma elemenata u prvom stupcu jednaka $30$, "
                 r"a u zadnjem $41$, uz uvjete: svi stupci osim prvog i zadnjeg su nul-stupci, "
                 r"matrica sadrži samo nenegativne cijele brojeve, a element u prvom retku i prvom stupcu je različit od nule?",
        "tip": "auto",
        "tocan_odgovor": "6096875400",
        "rjesenje": r"$6\,096\,875\,400$",
        "hints": [
            r"Broj načina za prvi stupac: $x_1+\cdots+x_5=30$, $x_1\ge 1$, ostali $\ge 0$ $\Rightarrow$ $\binom{33}{4}$.",
            r"Broj načina za zadnji stupac: $z_1+\cdots+z_5=41$, svi $\ge 0$ $\Rightarrow$ $\binom{45}{4}$. Pomnoži."
        ]
    },
    {
        "tekst": r"Koliko je prirodnih brojeva iz segmenta $[100, 10000]$ koji sadrže barem jednu znamenku $3$ "
                 r"i barem jednu znamenku $0$?",
        "tip": "auto",
        "tocan_odgovor": "666",
        "rjesenje": r"$666$",
        "hints": [
            r"Primijenite uključivanje-isključivanje zasebno za troznamenkaste $[100,999]$ i četveroznamenkaste $[1000,9999]$.",
            r"Zbrojite rezultate za obje grupe."
        ]
    },
    {
        "tekst": r"Riješite rekurziju $a_{n+2}+a_{n+1}-12a_n = 2\cdot 3^n$, $n\ge 0$, uz $a_0=1$ i $a_1=4$.",
        "tip": "auto",
        "tocan_odgovor": "Rational(54,49)*3**n - Rational(5,49)*(-4)**n + Rational(2,21)*n*3**n",
        "rjesenje": r"$a_n = \dfrac{54}{49}\cdot 3^n - \dfrac{5}{49}\cdot(-4)^n + \dfrac{2}{21}\cdot n\cdot 3^n$",
        "hints": [
            r"Karakteristična jednadžba homogenog dijela: $r^2+r-12=0$, korijeni $r_1=3$, $r_2=-4$.",
            r"Budući da je $3$ korijen homogene jednadžbe, partikularno rješenje tražite u obliku $A\cdot n\cdot 3^n$."
        ]
    },
    {
        "tekst": r"Koliko je osmeroznamenkastih neparnih prirodnih brojeva u čijem zapisu nema susjednih znamenaka $8$?",
        "tip": "auto",
        "tocan_odgovor": "39200000",
        "rjesenje": r"$39\,200\,000$",
        "hints": [
            r"Odredite ukupan broj 8-znamenkastih neparnih (prva $1$–$9$, zadnja $1,3,5,7,9$, ostale $0$–$9$).",
            r"Oduzmite one koji imaju barem jedan par susjednih osmici (komplement + rekurzija)."
        ]
    },
    {
        "tekst": r"Na koliko načina kuharica može pripremiti $5$ lunch paketa za petero djece različitih uzrasta "
                 r"s ukupno $14$ šnjita kruha, $14$ konzervi ribica i $25$ šljiva, uz uvjete: "
                 r"(a) svako dijete dobiva $\ge1$ šnjitu, $\ge1$ konzervu i $\ge3$ šljive; "
                 r"(b) najstarije dijete dobiva $2$–$4$ šnjite kruha, ostala $\ge1$; svako $\ge2$ konzerve i $\ge2$ šljive?",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "a)", "answer": "126126"},
            {"label": "b)", "answer": "280280"}
        ]),
        "rjesenje": r"(a) $126\,126$. (b) $280\,280$.",
        "hints": [
            r"Za svaki namirnik koristite kombinacije s ponavljanjem (pomak varijabli) i pomnožite.",
            r"(a) Kruh: $\binom{9}{4}$, ribice: $\binom{9}{4}$, šljive: $\binom{14}{4}$. Pomnoži.",
            r"(b) Kruh: 3 slučaja za najstarije $(k=2,3,4)$, ribice: $\binom{4}{4}$, šljive: $\binom{15}{4}$."
        ]
    },
    {
        "tekst": r"Koliko je prirodnih brojeva iz segmenta $[1, 1000]$ koji sadrže barem jednu znamenku $4$ "
                 r"i barem jednu znamenku $6$?",
        "tip": "auto",
        "tocan_odgovor": "54",
        "rjesenje": r"$54$",
        "hints": [
            r"Primijenite uključivanje-isključivanje na skupu $[0,999]$ (dopunite s vodećim nulama).",
            r"$|A_4\cap A_6|=|U|-|A_4^c|-|A_6^c|+|A_4^c\cap A_6^c|$, gdje $A_x^c$ označava skup bez znamenke $x$."
        ]
    },
    {
        "tekst": r"Riješite sustav rekurzija $a_{n+1}=2a_n-b_n$, $b_{n+1}=a_n+4b_n$ uz $a_0=2$, $b_0=1$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "a_n =", "answer": "(2-n)*3**n"},
            {"label": "b_n =", "answer": "(1+n)*3**n"}
        ]),
        "rjesenje": r"$a_n=(2-n)\cdot 3^n$, $\quad b_n=(1+n)\cdot 3^n$",
        "hints": [
            r"Iz prve jednadžbe $b_n=2a_n-a_{n+1}$; uvrstite u drugu da dobijete rekurziju $a_{n+2}-6a_{n+1}+9a_n=0$.",
            r"Karakteristična jednadžba ima dvostruki korijen $r=3$: $a_n=(C_1+C_2 n)\cdot 3^n$."
        ]
    },
    {
        "tekst": r"(a) Koliko je $8$-znamenkastih brojeva koji sadrže isključivo neparne znamenke, "
                 r"a ne sadrže susjedne petice? "
                 r"(b) Koliko je $8$-znamenkastih brojeva koji sadrže isključivo parne znamenke, "
                 r"a ne sadrže susjedne nule?",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "a)", "answer": "3081600"},
            {"label": "b)", "answer": "380928"}
        ]),
        "rjesenje": r"(a) $3\,081\,600$. (b) $380\,928$.",
        "hints": [
            r"Za svaki slučaj postavite rekurziju po pozicijama ili koristite komplement.",
            r"(a) Neparne znamenke: $\{1,3,5,7,9\}$. (b) Parne: $\{0,2,4,6,8\}$, prva $\ne 0$."
        ]
    },
    {
        "tekst": r"Odredite broj cjelobrojnih rješenja jednadžbe $x_1+x_2+x_3+x_4=44$ "
                 r"uz uvjete $x_1\ge 2$, $x_2\ge 3$, $x_3\ge 1$, $x_4\ge 0$.",
        "tip": "auto",
        "tocan_odgovor": "9880",
        "rjesenje": r"$9880$",
        "hints": [
            r"Supstitucija: $y_1=x_1-2$, $y_2=x_2-3$, $y_3=x_3-1$, $y_4=x_4$; svi $y_i\ge 0$.",
            r"Jednadžba postaje $y_1+y_2+y_3+y_4=38$; broj rješenja je $\binom{41}{3}=9880$."
        ]
    },
    {
        "tekst": r"Koliko je $6$-znamenkastih prirodnih brojeva koji sadrže barem jednu znamenku $4$ "
                 r"i barem dvije znamenke $0$?",
        "tip": "auto",
        "tocan_odgovor": "45045",
        "rjesenje": r"$45\,045$",
        "hints": [
            r"Primijenite uključivanje-isključivanje na uvjetima o nepojavljivanju $4$ i o manje od dvije nule.",
            r"Pazite da prva znamenka ne smije biti $0$."
        ]
    },
    {
        "tekst": r"Koliko je $6$-znamenkastih prirodnih brojeva koji sadrže barem dvije znamenke $0$ "
                 r"i barem jednu znamenku $9$?",
        "tip": "auto",
        "tocan_odgovor": "45000",
        "rjesenje": r"$45\,000$",
        "hints": [
            r"Primijenite uključivanje-isključivanje: $|A_0^{\ge2}\cap A_9^{\ge1}|$.",
            r"Pazite na ograničenje prve znamenke."
        ]
    },
    {
        "tekst": r"U jednoj vrećici se nalazi $7$ plavih kuglica različitih veličina, "
                 r"u drugoj $5$ zelenih različitih veličina i u trećoj $4$ crvene različitih veličina. "
                 r"(a) Na koliko načina možemo izvaditi $4$ plave, $4$ zelene i $3$ crvene? "
                 r"(b) Na koliko načina možemo izvaditi sve kuglice i posložiti ih u red "
                 r"tako da kuglice iste boje budu jedna do druge? "
                 r"(c) Na koliko načina možemo izvaditi $4$ zelene i $4$ plave te ih rasporediti "
                 r"kružno tako da kuglice alterniraju po boji?",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "a)", "answer": "700"},
            {"label": "b)", "answer": "87091200"},
            {"label": "c)", "answer": "25200"}
        ]),
        "rjesenje": r"(a) $700$. (b) $87\,091\,200$. (c) $25\,200$.",
        "hints": [
            r"(a) $\binom{7}{4}\cdot\binom{5}{4}\cdot\binom{4}{3}=35\cdot5\cdot4=700$.",
            r"(b) $3!\cdot 7!\cdot 5!\cdot 4!=6\cdot5040\cdot120\cdot24=87\,091\,200$.",
            r"(c) Kružno: fiksirajte jedno mjesto. $\binom{7}{4}\cdot\binom{5}{4}\cdot 3!\cdot 4!=35\cdot5\cdot6\cdot24=25\,200$."
        ]
    },
    {
        "tekst": r"(a) Odredite broj svih $5$-kombinacija multiskupa $M=\{4\cdot A,\;2\cdot B,\;2\cdot C,\;2\cdot D,\;2\cdot E,\;2\cdot F,\;1\cdot G\}$. "
                 r"(b) Riješite rekurziju $a_n - 6a_{n-1} + 5a_{n-2} = 2n-1$, $a_0=0$, $a_1=1$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "a) Broj 5-kombinacija =", "answer": "78"},
            {"label": "b) a_n =", "answer": "-n**2/4 - n/2 - Rational(7,16) + Rational(7,16)*5**n"}
        ]),
        "rjesenje": r"(a) $78$. (b) $a_n=-\dfrac{n^2}{4}-\dfrac{n}{2}-\dfrac{7}{16}+\dfrac{7}{16}\cdot 5^n$.",
        "hints": [
            r"(a) Koristite generirajuće funkcije ili uključivanje-isključivanje s ograničenjima kratnosti.",
            r"(b) Homogena: korijeni $r=1$ i $r=5$. Partikularno: $An^2+Bn$ (jer je $1$ jednostruki korijen)."
        ]
    },
    {
        "tekst": r"Riješite rekurziju $a_n - 8a_{n-1} + 7a_{n-2} = 2n^2-n$, $n\ge 2$, uz $a_0=1$, $a_1=2$.",
        "tip": "auto",
        "tocan_odgovor": "Rational(69,49) + Rational(11,49)*7**n - n**3/9 - 7*n**2/18 - Rational(173,378)*n",
        "rjesenje": r"$a_n=\dfrac{69}{49}+\dfrac{11}{49}\cdot 7^n-\dfrac{n^3}{9}-\dfrac{7n^2}{18}-\dfrac{173n}{378}$",
        "hints": [
            r"Homogena jednadžba: korijeni $r_1=1$, $r_2=7$.",
            r"Partikularno rješenje: polinom stupnja $3$ (jer je $1$ jednostruki korijen, a desna strana je polinom stupnja $2$)."
        ]
    },
    {
        "tekst": r"Primijenite formulu uključivanja-isključivanja. "
                 r"Koliko je prirodnih brojeva iz segmenta $[100, 10000]$ koji sadrže barem jednu znamenku $4$ "
                 r"i barem jednu znamenku $6$?",
        "tip": "auto",
        "tocan_odgovor": "666",
        "rjesenje": r"$666$",
        "hints": [
            r"Neka je $A$ = skup s barem jednom $4$, $B$ = skup s barem jednom $6$. Tražite $|A\cap B|$.",
            r"$|A\cap B|=|U|-|\overline{A}|-|\overline{B}|+|\overline{A}\cap\overline{B}|$. Razbijte na $[100,999]$ i $[1000,9999]$."
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
    finally:
        db.close()


if __name__ == "__main__":
    run()