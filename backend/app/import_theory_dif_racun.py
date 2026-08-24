"""Jednokratni uvoz teorije za kolegij 'Diferencijalni racun'."""

from .database import SessionLocal
from . import models

COURSE_NAME = "Diferencijalni racun"

# ---------------------------------------------------------------------------
# Tocno / Netocno (50)
# ---------------------------------------------------------------------------
TRUEFALSE = [
    ("Svaka injektivna funkcija $f:A\\to B$ ujedno je i surjektivna.", False),
    ("Ako je funkcija $f$ strogo rastuća na cijeloj domeni, onda je sigurno injektivna (1-1).", True),
    ("Funkcija $f(x) = x^3 - x$ je parna funkcija.", False),
    ("Zbroj dviju neparnih funkcija uvijek je neparna funkcija.", True),
    ("Umnožak dviju neparnih funkcija uvijek je neparna funkcija.", False),
    ("Ako je funkcija $f$ strogo padajuća, onda je njezina inverzna funkcija $f^{-1}$ također strogo padajuća.", True),
    ("Kompozicija dviju parnih funkcija uvijek je parna funkcija.", True),
    ("Prirodna domena funkcije $f(x) = \\ln(x^2-4)$ je interval $\\langle 2, +\\infty\\rangle$.", False),
    ("Funkcija $f(x) = \\sin(x^2)$ je periodična s temeljnim periodom $2\\pi$.", False),
    ("Funkcija $f(x) = 2^x$ je strogo rastuća na cijelom skupu $\\mathbb{R}$ i preslikava $\\mathbb{R}$ na interval $\\langle 0, +\\infty\\rangle$.", True),
    ("Svaki omeđen skup realnih brojeva ima i supremum i infimum u skupu $\\mathbb{R}$.", True),
    ("Ako je skup $A \\subseteq \\mathbb{R}$ omeđen odozgo, njegov supremum $\\sup(A)$ mora pripadati skupu $A$.", False),
    ("Ako je $\\sup(A) = M$, onda za svaki $\\varepsilon>0$ postoji $x\\in A$ takav da je $x > M-\\varepsilon$.", True),
    ("Svaki konačan skup realnih brojeva je omeđen.", True),
    ("Ako je funkcija $f$ omeđena na intervalu $\\langle a,b\\rangle$, ona mora dostizati svoj maksimum na tom intervalu.", False),
    ("Svaki monotoni niz realnih brojeva je konvergentan.", False),
    ("Svaki omeđeni niz realnih brojeva ima konvergentan podniz (Bolzano–Weierstrassov teorem).", True),
    ("Ako niz $(a_n)$ konvergira prema $0$, a niz $(b_n)$ je omeđen, tada niz $(a_n b_n)$ konvergira prema $0$.", True),
    ("Ako su nizovi $(a_n)$ i $(b_n)$ divergentni, onda je i njihov zbroj $(a_n+b_n)$ sigurno divergentan.", False),
    ("Limes niza $a_n = (1+\\frac{1}{n})^n$ kada $n\\to\\infty$ jednak je $1$.", False),
    ("Ako je $\\lim_{n\\to\\infty} a_n = A$ i $a_n>0$ za sve $n$, tada mora vrijediti $A>0$.", False),
    ("Svaki konvergentan niz je omeđen.", True),
    ("Ako niz $(|a_n|)$ konvergira prema $0$, tada niz $(a_n)$ također konvergira prema $0$.", True),
    ("Limes niza $a_n = \\frac{\\sin(n)}{n}$ kada $n\\to\\infty$ ne postoji jer $\\sin(n)$ oscilira.", False),
    ("Da bi postojala granična vrijednost $\\lim_{x\\to a} f(x)$, funkcija $f$ mora biti definirana u točki $a$.", False),
    ("Ako postoje lijevi i desni limes funkcije u točki $a$ i jednaki su, tada postoji i limes $\\lim_{x\\to a} f(x)$.", True),
    ("Vrijedi $\\lim_{x\\to 0} \\frac{\\sin(x)}{x} = 1$.", True),
    ("Ako je funkcija $f$ neprekidna na zatvorenom intervalu $[a,b]$, onda je ona omeđena na tom intervalu (Weierstrassov teorem).", True),
    ("Funkcija $f(x) = \\frac{x^2-1}{x-1}$ ima uklonjivi prekid u točki $x=1$.", True),
    ("Ako je funkcija $f$ neprekidna na $[a,b]$ i $f(a)\\cdot f(b) < 0$, onda postoji barem jedna točka $c\\in\\langle a,b\\rangle$ takva da je $f(c)=0$ (Bolzanov teorem).", True),
    ("Zbroj dviju prekidnih funkcija u točki $a$ uvijek je prekidna funkcija u točki $a$.", False),
    ("Vrijedi $\\lim_{x\\to 0} (1+x)^{1/x} = e$.", True),
    ("Funkcija $f(x) = |x|$ nije neprekidna u točki $x=0$.", False),
    ("Ako je $\\lim_{x\\to a^+} f(x) = +\\infty$, pravac $x=a$ je vertikalna asimptota funkcije $f$.", True),
    ("Funkcija može imati najviše jednu horizontalnu asimptotu (zajedno za $x\\to+\\infty$ i $x\\to-\\infty$).", False),
    ("Graf funkcije nikada ne smije presjeći svoju kosu ili horizontalnu asimptotu.", False),
    ("Ako funkcija ima horizontalnu asimptotu kada $x\\to+\\infty$, onda u tom smjeru ne može imati kosu asimptotu.", True),
    ("Racionalna funkcija $f(x) = \\frac{P(x)}{Q(x)}$ ima kosu asimptotu kada je stupanj polinoma $P(x)$ točno za $1$ veći od stupnja polinoma $Q(x)$.", True),
    ("Ako je funkcija $f$ neprekidna u točki $a$, ona je u toj točki sigurno i derivabilna.", False),
    ("Ako je funkcija $f$ derivabilna u točki $a$, onda je ona u toj točki sigurno neprekidna.", True),
    ("Derivacija funkcije $f(x) = |x|$ u točki $x=0$ iznosi $0$.", False),
    ("Derivacija umnoška dviju funkcija jednaka je umnošku njihovih derivacija: $(f\\cdot g)' = f'\\cdot g'$.", False),
    ("Koeficijent smjera (nagib) tangente na graf funkcije $f$ u točki $(x_0, f(x_0))$ jednak je $f'(x_0)$.", True),
    ("Derivacija funkcije $f(x) = a^x$ (gdje je $a>0$, $a\\neq 1$) iznosi $f'(x) = a^x \\ln(a)$.", True),
    ("Rolleov teorem jamči postojanje stacionarne točke pod uvjetom da je funkcija neprekidna na $[a,b]$, derivabilna na $\\langle a,b\\rangle$ i da je $f(a)=f(b)$.", True),
    ("Ako je $f'(x) > 0$ za sve $x\\in\\langle a,b\\rangle$, tada je funkcija $f$ strogo rastuća na tom intervalu.", True),
    ("Ako je $f'(x_0) = 0$, funkcija $f$ u točki $x_0$ sigurno ima lokalni ekstrem.", False),
    ("L'Hospitalovo pravilo se smije izravno primijeniti na neodređeni oblik $0/0$ ili $\\infty/\\infty$.", True),
    ("Ako je druga derivacija $f''(x) > 0$ na intervalu $I$, graf funkcije $f$ je konkavan (konkavan prema dolje) na tom intervalu.", False),
    ("Točka $x_0$ u kojoj je druga derivacija $f''(x_0) = 0$ i u kojoj druga derivacija mijenja znak naziva se točka infleksije (prevoja).", True),
]

# ---------------------------------------------------------------------------
# Nadopuni recenicu (50) - odgovor je OBICAN TEKST (usporeduje se doslovno)
# ---------------------------------------------------------------------------
FILLIN = [
    ("Funkcija $f$ je injektivna ako iz uvjeta $f(x_1) = f(x_2)$ nužno slijedi ___.", "x1=x2"),
    ("Ako za svaki $x$ iz domene vrijedi $f(-x) = -f(x)$, funkcija $f$ je ___.", "neparna"),
    ("Kompozicija dviju neparnih funkcija uvijek je ___ funkcija.", "neparna"),
    ("Prirodna domena funkcije $f(x) = \\sqrt{9-x^2}$ je zatvoreni interval ___.", "[-3,3]"),
    ("Ako je funkcija $f$ strogo rastuća na cijeloj domeni, njezina inverzna funkcija $f^{-1}$ je strogo ___.", "rastuća"),
    ("Najmanji pozitivan broj $T$ za koji vrijedi $f(x+T) = f(x)$ naziva se ___ period funkcije $f$.", "temeljni"),
    ("Funkcija $f(x) = a^x$ za $a>1$ je strogo ___.", "rastuća"),
    ("Kodomena funkcije $f(x) = \\cos(x)$ je zatvoreni interval ___.", "[-1,1]"),
    ("Zbroj dviju parnih funkcija je ___ funkcija.", "parna"),
    ("Skup svih izlaza $f(x)$ koje funkcija poprima za elemente iz domene naziva se ___ funkcije.", "slika"),
    ("Najmanja gornja međa omeđenog skupa $A$ naziva se ___.", "supremum"),
    ("Najveća donja međa omeđenog skupa $A$ naziva se ___.", "infimum"),
    ("Ako je supremum skupa $A$ ujedno i element skupa $A$, onda je on ujedno i ___ tog skupa.", "maksimum"),
    ("Skup koji je omeđen i odozgo i odozdo naziva se ___ skup.", "omeđen"),
    ("Svaki neprazan odozgo omeđen podskup skupa realnih brojeva ima supremum u $\\mathbb{R}$ prema aksiomu ___.", "potpunosti"),
    ("Niz koji ima konačnu graničnu vrijednost naziva se ___ niz.", "konvergentan"),
    ("Niz koji nije konvergentan naziva se ___ niz.", "divergentan"),
    ("Svaki omeđeni i monotoni niz realnih brojeva je ___.", "konvergentan"),
    ("Prema Bolzano-Weierstrassovom teoremu, svaki omeđeni niz realnih brojeva ima konvergentan ___.", "podniz"),
    ("Umnožak nula-niza i omeđenog niza je ___.", "nula-niz"),
    ("Limes niza $a_n = (1+\\frac{1}{n})^n$ kada $n\\to\\infty$ jednak je broju ___.", "e"),
    ("Niz $a_n = (-1)^n$ je omeđen, ali je ___ jer oscilira između $-1$ i $1$.", "divergentan"),
    ("Ako je $\\lim a_n = A$ i $\\lim b_n = B$, tada je limes njihovog zbroja $\\lim(a_n+b_n)$ = ___.", "A+B"),
    ("Limes niza $a_n = 1/n^p$ za $p>0$ kada $n\\to\\infty$ iznosi ___.", "0"),
    ("Funkcija $f$ je neprekidna u točki $a$ ako je definirana u $a$, postoji $\\lim_{x\\to a} f(x)$ i taj limes je jednak ___.", "f(a)"),
    ("Značajni limes $\\lim_{x\\to 0} \\frac{\\sin(x)}{x}$ jednak je ___.", "1"),
    ("Prema prvom Weierstrassovom teoremu, neprekidna funkcija na zatvorenom intervalu $[a,b]$ je ___.", "omeđena"),
    ("Prema drugom Weierstrassovom teoremu, neprekidna funkcija na zatvorenom intervalu $[a,b]$ dostiže svoj minimum i ___.", "maksimum"),
    ("Prema Bolzanovom teoremu, ako je $f$ neprekidna na $[a,b]$ i $f(a)\\cdot f(b) < 0$, postoji $c\\in\\langle a,b\\rangle$ tako da je $f(c)$ = ___.", "0"),
    ("Limes $\\lim_{x\\to 0} (1+x)^{1/x}$ jednak je ___.", "e"),
    ("Ako postoje jednostrani limesi u točki $a$ i jednaki su $L$, tada je obostrani limes $\\lim_{x\\to a} f(x)$ jednak ___.", "L"),
    ("Ako u točki $a$ postoji limes funkcije, ali $f(a)$ nije definirana ili nije jednaka limesu, radi se o ___ prekidu.", "uklonjivom"),
    ("Funkcija $f(x) = |x|$ je neprekidna u $x=0$, ali u toj točki nije ___.", "derivabilna"),
    ("Ako je $\\lim_{x\\to a} f(x) = +\\infty$ ili $-\\infty$, pravac $x=a$ naziva se ___ asimptota.", "vertikalna"),
    ("Pravac $y=L$ naziva se horizontalna asimptota ako je $\\lim_{x\\to+\\infty} f(x)$ = ___.", "L"),
    ("Pravac $y = kx+l$ je kosa asimptota, pri čemu se koeficijent $k$ računa kao $\\lim_{x\\to\\infty}$ ___.", "f(x)/x"),
    ("Ako funkcija ima horizontalnu asimptotu kada $x\\to+\\infty$, koeficijent smjera $k$ njezine kose asimptote iznosi ___.", "0"),
    ("Racionalna funkcija $P(x)/Q(x)$ ima kosu asimptotu ako je stupanj polinoma $P(x)$ za točno ___ veći od stupnja polinoma $Q(x)$.", "1"),
    ("Derivacija funkcije $f$ u točki $x_0$ definira se kao limes omjera prirasta $f'(x_0) = \\lim_{h\\to 0}$ ___.", "(f(x0+h)-f(x0))/h"),
    ("Geometrijski gledano, derivacija $f'(x_0)$ predstavlja ___ tangente na graf funkcije u točki $x_0$.", "koeficijent smjera"),
    ("Pravilo za derivaciju umnoška glasi: $(f\\cdot g)'$ = ___.", "f'*g+f*g'"),
    ("Pravilo za derivaciju kompozicije (lančano pravilo) glasi: $(f(g(x)))'$ = ___.", "f'(g(x))*g'(x)"),
    ("Derivacija funkcije $f(x) = x^n$ iznosi ___.", "n*x^(n-1)"),
    ("Derivacija prirodnog logaritma $f(x) = \\ln(x)$ iznosi ___.", "1/x"),
    ("Ako je funkcija derivabilna u točki $a$, ona je u toj točki sigurno i ___.", "neprekidna"),
    ("Rolleov teorem tvrdi da ako je $f$ neprekidna na $[a,b]$, derivabilna na $\\langle a,b\\rangle$ i $f(a)=f(b)$, postoji $c\\in\\langle a,b\\rangle$ gdje je $f'(c)$ = ___.", "0"),
    ("Lagrangeov teorem o srednjoj vrijednosti tvrdi da postoji $c\\in\\langle a,b\\rangle$ takav da je $f'(c)$ = ___.", "(f(b)-f(a))/(b-a)"),
    ("Ako je $f'(x) > 0$ na nekom intervalu, funkcija $f$ je na tom intervalu strogo ___.", "rastuća"),
    ("L'Hospitalovo pravilo omogućuje računanje limesa oblika $0/0$ ili $\\infty/\\infty$ pomoću limesa omjera ___.", "derivacija"),
    ("Točka u kojoj graf funkcije prelazi iz konveksnosti u konkavnost (ili obratno) naziva se točka ___.", "infleksije"),
]

# ---------------------------------------------------------------------------
# Flash kartice (25)
# ---------------------------------------------------------------------------
FLASHCARD = [
    ("Što znači da je funkcija $f$ injektivna (1-1)?",
     "Znači da različitim elementima iz domene pridružuje različite vrijednosti u kodomeni. Ako je $f(x_1) = f(x_2)$, onda mora biti $x_1 = x_2$."),
    ("Kakva je to parna, a kakva neparna funkcija i kakva im je simetrija?",
     "Parna: $f(-x) = f(x)$ → graf je simetričan s obzirom na $y$-os.\nNeparna: $f(-x) = -f(x)$ → graf je simetričan s obzirom na ishodište."),
    ("Što definira periodičnu funkciju i što je temeljni period?",
     "Funkcija je periodična ako postoji broj $T>0$ takav da je $f(x+T) = f(x)$ za svaki $x$. Najmanji takav pozitivan broj $T$ naziva se temeljni period."),
    ("Kako se definira supremum, a kako infimum skupa $A$?",
     "Supremum ($\\sup A$) je najmanja gornja međa skupa $A$.\nInfimum ($\\inf A$) je najveća donja međa skupa $A$."),
    ("Koja je razlika između supremuma i maksimuma skupa?",
     "Supremum ne mora pripadati skupu (npr. $\\sup\\langle 0,1\\rangle = 1$), dok maksimum mora biti element tog skupa (npr. $\\max[0,1] = 1$)."),
    ("Što glasi teorem o supremumu (aksiom potpunosti)?",
     "Svaki neprazan i odozgo omeđen podskup skupa realnih brojeva $\\mathbb{R}$ ima supremum u $\\mathbb{R}$."),
    ("Što je to konvergentan niz?",
     "Niz $(a_n)$ je konvergentan ako postoji realan broj $L$ (limes) takav da se članovi niza proizvoljno približavaju broju $L$ kada $n\\to\\infty$."),
    ("Što glasi teorem o monotonom nizu?",
     "Svaki niz koji je omeđen i monoton (rastući ili padajući) ujedno je i konvergentan."),
    ("Što glasi Bolzano-Weierstrassov teorem za nizove?",
     "Svaki omeđeni niz realnih brojeva ima barem jedan konvergentan podniz."),
    ("Koliko iznosi limes niza $a_n = (1+\\frac{1}{n})^n$ kada $n\\to\\infty$?",
     "Limes iznosi $e$ (Eulerov broj, $e \\approx 2.71828$)."),
    ("Koja su 3 uvjeta za neprekidnost funkcije $f$ u točki $a$?",
     "1. Funkcija $f$ je definirana u točki $a$.\n2. Postoji granična vrijednost $\\lim_{x\\to a} f(x)$.\n3. Limes je jednak vrijednosti funkcije u točki $a$: $\\lim_{x\\to a} f(x) = f(a)$."),
    ("Koliko iznosi značajni limes $\\lim_{x\\to 0} \\frac{\\sin(x)}{x}$?",
     "Limes iznosi $1$."),
    ("Što glasi Prvi, a što Drugi Weierstrassov teorem?",
     "Prvi: Ako je $f$ neprekidna na zatvorenom intervalu $[a,b]$, ona je na njemu omeđena.\nDrugi: Neprekidna funkcija na $[a,b]$ dostiže svoj minimum i maksimum na tom intervalu."),
    ("Što glasi Bolzanov teorem o međuvrijednostima (o nultočki)?",
     "Ako je $f$ neprekidna na $[a,b]$ i $f(a)\\cdot f(b) < 0$, tada postoji barem jedna točka $c\\in\\langle a,b\\rangle$ u kojoj je $f(c) = 0$."),
    ("Kada pravac $x=a$ predstavlja vertikalnu asimptotu?",
     "Kada je barem jedan od jednostranih limesa u točki $a$ jednak beskonačnosti: $\\lim_{x\\to a^+} f(x) = \\pm\\infty$ ili $\\lim_{x\\to a^-} f(x) = \\pm\\infty$."),
    ("Kako se računaju koeficijenti $k$ i $l$ za kosu asimptotu $y = kx+l$?",
     "$k = \\lim_{x\\to\\infty} \\frac{f(x)}{x}$\n$l = \\lim_{x\\to\\infty} [f(x) - kx]$"),
    ("Što je koeficijent $k$ ako funkcija ima horizontalnu asimptotu?",
     "Koeficijent $k$ je jednak $0$, jer je horizontalna asimptota samo poseban slučaj kose asimptote bez nagiba ($y=l$)."),
    ("Kako se definira derivacija funkcije $f$ u točki $x_0$?",
     "$f'(x_0) = \\lim_{h\\to 0} \\frac{f(x_0+h)-f(x_0)}{h}$, pod uvjetom da taj limes postoji i konačan je."),
    ("Koje je geometrijsko značenje derivacije $f'(x_0)$?",
     "$f'(x_0)$ predstavlja koeficijent smjera (nagib) tangente na graf funkcije $f$ u točki $(x_0, f(x_0))$."),
    ("Kakav je odnos između neprekidnosti i derivabilnosti?",
     "Ako je funkcija derivabilna u točki $a$, ona je u njoj SIGURNO i neprekidna.\nObrat ne vrijedi (neprekidna funkcija ne mora biti derivabilna, npr. $f(x)=|x|$ u $x=0$)."),
    ("Koje je pravilo za derivaciju umnoška i kvocijenta dviju funkcija?",
     "Umnožak: $(f\\cdot g)' = f'\\cdot g + f\\cdot g'$\nKvocijent: $(f/g)' = \\frac{f'\\cdot g - f\\cdot g'}{g^2}$"),
    ("Što glasi Rolleov teorem?",
     "Ako je $f$ neprekidna na $[a,b]$, derivabilna na $\\langle a,b\\rangle$ i $f(a)=f(b)$, tada postoji barem jedna točka $c\\in\\langle a,b\\rangle$ u kojoj je $f'(c) = 0$."),
    ("Što glasi Lagrangeov teorem o srednjoj vrijednosti?",
     "Ako je $f$ neprekidna na $[a,b]$ i derivabilna na $\\langle a,b\\rangle$, postoji $c\\in\\langle a,b\\rangle$ takav da je $f'(c) = \\frac{f(b)-f(a)}{b-a}$."),
    ("Kada se primjenjuje L'Hospitalovo pravilo i kako glasi?",
     "Primjenjuje se na neodređene oblike $0/0$ i $\\infty/\\infty$. Glasi: $\\lim \\frac{f(x)}{g(x)} = \\lim \\frac{f'(x)}{g'(x)}$, ako taj limes postoji."),
    ("Kako predznak prve i druge derivacije određuje ponašanje grafa?",
     "$f'(x) > 0$ → funkcija raste.\n$f'(x) < 0$ → funkcija pada.\n$f''(x) > 0$ → graf je konveksan.\n$f''(x) < 0$ → graf je konkavan."),
]

# ---------------------------------------------------------------------------
# Visestruki odabir (20)
# ---------------------------------------------------------------------------
MCQ = [
    ("Neka je $f: A \\to B$ funkcija. Što je od navedenog SIGURNO točno ako je $f$ injektivna?",
     ["Svaki element iz $B$ ima barem jednu prasliku u $A$.",
      "Ako je $x_1 \\neq x_2$, onda je $f(x_1) \\neq f(x_2)$.",
      "Domena $A$ i kodomena $B$ moraju imati jednak broj elemenata.",
      "Funkcija $f$ mora imati lokalne ekstreme."], 1),
    ("Promatramo funkciju $f(x) = \\sin(x^2)$. Koja je tvrdnja o njezinoj periodičnosti točna?",
     ["Funkcija je periodična s temeljnim periodom $2\\pi$.",
      "Funkcija je periodična s temeljnim periodom $\\pi$.",
      "Funkcija nije periodična.",
      "Funkcija je periodična s temeljnim periodom $\\sqrt{2\\pi}$."], 2),
    ("Neka je skup $A = \\langle 0, 1]$ u $\\mathbb{R}$. Koja je tvrdnja točna za infimum, supremum, minimum i maksimum skupa $A$?",
     ["$\\inf(A)=0$, $\\sup(A)=1$, $\\min(A)$ ne postoji, $\\max(A)=1$",
      "$\\inf(A)=0$, $\\sup(A)=1$, $\\min(A)=0$, $\\max(A)=1$",
      "$\\inf(A)$ ne postoji, $\\sup(A)=1$, $\\min(A)$ ne postoji, $\\max(A)=1$",
      "$\\inf(A)=0$, $\\sup(A)$ ne postoji, $\\min(A)=0$, $\\max(A)$ ne postoji"], 0),
    ("Neka je $a_n = \\frac{(-1)^n}{n}$. Što vrijedi za niz $(a_n)$?",
     ["Divergira jer oscilira između pozitivnih i negativnih vrijednosti.",
      "Konvergira prema $0$ prema teoremu o uklještenim nizovima.",
      "Konvergira prema $1$.",
      "Neomeđen je odozgo i odozdo."], 1),
    ("Ako su nizovi $(a_n)$ i $(b_n)$ divergentni, što možemo tvrditi o nizu $c_n = a_n+b_n$?",
     ["Niz $c_n$ mora biti divergentan.",
      "Niz $c_n$ mora biti neomeđen.",
      "Niz $c_n$ može biti konvergentan.",
      "Limes niza $c_n$ je uvijek beskonačan."], 2),
    ("Koliko iznosi limes $\\lim_{x\\to\\infty} \\frac{\\sin(x)}{x}$?",
     ["$1$", "$0$", "Ne postoji jer $\\sin(x)$ oscilira.", "Beskonačno."], 1),
    ("Neka je $f(x) = \\frac{x^2-4}{x-2}$. Kakav prekid funkcija $f$ ima u točki $x=2$?",
     ["Prekid prve vrste (skok).",
      "Esencijalni (neuklonjivi) prekid druge vrste.",
      "Uklonjivi prekid jer $\\lim_{x\\to 2} f(x)$ postoji i iznosi $4$.",
      "Funkcija nema prekid u $x=2$."], 2),
    ("Koliko iznosi limes $\\lim_{x\\to 0} (1+2x)^{1/x}$?",
     ["$e$", "$e^2$", "$1$", "$2e$"], 1),
    ("Ako je funkcija $f$ neprekidna na OTVORENOM intervalu $\\langle a,b\\rangle$, što od navedenog MORA vrijediti prema Weierstrassovim teoremima?",
     ["Funkcija $f$ je sigurno omeđena na $\\langle a,b\\rangle$.",
      "Funkcija $f$ sigurno dostiže svoj maksimum na $\\langle a,b\\rangle$.",
      "Funkcija $f$ je derivabilna na $\\langle a,b\\rangle$.",
      "Ništa od navedenog – Weierstrassovi teoremi vrijede samo za ZATVORENI interval $[a,b]$."], 3),
    ("Za funkciju $f(x) = |x|$ u točki $x=0$ vrijedi:",
     ["Nije neprekidna i nije derivabilna.",
      "Neprekidna je, ali nije derivabilna jer su lijeva i desna derivacija različite.",
      "Derivabilna je i $f'(0)=0$.",
      "Nije neprekidna, ali je derivabilna."], 1),
    ("Koliko najviše horizontalnih asimptota može imati graf jedne realne funkcije $f(x)$?",
     ["Najviše $1$.",
      "Najviše $2$ (jednu za $x\\to+\\infty$, drugu za $x\\to-\\infty$).",
      "Neograničeno mnogo.",
      "Niti jednu ako ima vertikalne asimptote."], 1),
    ("Može li graf funkcije presjeći svoju vlastitu horizontalnu ili kosu asimptotu?",
     ["Nikada, asimptota je granična linija koju graf ne smije dodirnuti.",
      "Da, ali samo u konačno mnogo točaka.",
      "Da, može je presjeći konačno ili čak beskonačno mnogo puta.",
      "Može presjeći samo kosu, ali nikada horizontalnu."], 2),
    ("Ako je $f'(x_0) = 0$ u točki $x_0$, što možemo SIGURNO zaključiti?",
     ["Funkcija $f$ u $x_0$ ima lokalni maksimum.",
      "Funkcija $f$ u $x_0$ ima lokalni minimum.",
      "Točka $x_0$ je stacionarna točka, ali ne mora biti lokalni ekstrem.",
      "Funkcija $f$ u $x_0$ ima točku infleksije."], 2),
    ("Neka je $f(x) = x^3-3x$ na zatvorenom intervalu $[-2,2]$. Gdje funkcija dostiže svoj apsolutni (globalni) maksimum?",
     ["Samo u $x=-1$.",
      "Samo u $x=2$.",
      "U točkama $x=-1$ i $x=2$.",
      "U točki $x=0$."], 2),
    ("Što glasi pretpostavka Rolleovog teorema koja NIJE nužna za Lagrangeov teorem?",
     ["Neprekidnost na $[a,b]$.",
      "Derivabilnost na $\\langle a,b\\rangle$.",
      "$f(a)=f(b)$.",
      "$f'(x) > 0$ na $\\langle a,b\\rangle$."], 2),
    ("Ako je druga derivacija $f''(x) < 0$ na cijelom intervalu $I$, graf funkcije $f$ je na tom intervalu:",
     ["Konveksan (strogo udubljen prema gore).",
      "Konkavan (ispupčen prema gore / konkavan prema dolje).",
      "Strogo rastući.",
      "Strogo padajući."], 1),
    ("Zašto se L'Hospitalovo pravilo NE SMIJE izravno primijeniti na $\\lim_{x\\to 0} \\frac{\\cos(x)}{x}$?",
     ["Zato što je $\\cos(x)$ neprekidna funkcija.",
      "Zato što oblik nije neodređen (imamo oblik $1/0$, a ne $0/0$ ili $\\infty/\\infty$).",
      "Zato što derivacija od $\\cos(x)$ sadrži minus.",
      "Zato što pravilo vrijedi samo kada $x\\to\\infty$."], 1),
    ("Neka je $f(x) = e^{2x}$. Koliko iznosi $n$-ta derivacija $f^{(n)}(x)$?",
     ["$2 e^{2x}$", "$2^n e^{2x}$", "$n e^{2x}$", "$e^{2nx}$"], 1),
    ("Promatramo funkciju $f(x) = x\\cdot|x|$. Je li funkcija derivabilna u $x=0$?",
     ["Ne, jer sadrži apsolutnu vrijednost $|x|$.",
      "Da, i $f'(0)=0$.",
      "Da, i $f'(0)=1$.",
      "Ne, jer desna derivacija iznosi $1$, a lijeva $-1$."], 1),
    ("Ako je $f''(x_0)=0$ i $f'''(x_0)\\neq 0$, što je točka $x_0$ za funkciju $f$?",
     ["Sigurno lokalni maksimum.",
      "Sigurno lokalni minimum.",
      "Točka infleksije (prevoja).",
      "Točka prekida."], 2),
]


def run():
    db = SessionLocal()
    try:
        course = db.query(models.Course).filter(models.Course.naziv == COURSE_NAME).first()
        if not course:
            print(f"[!] Kolegij '{COURSE_NAME}' ne postoji u bazi. Prekidam.")
            return

        n = 0
        for i, (tvrdnja, tocno) in enumerate(TRUEFALSE):
            db.add(models.TheoryItem(
                course_id=course.id, module_id=None, tip="truefalse",
                sadrzaj={"tvrdnja": tvrdnja, "tocno": tocno}, redoslijed=n,
            ))
            n += 1

        for tekst, odgovor in FILLIN:
            db.add(models.TheoryItem(
                course_id=course.id, module_id=None, tip="fillin",
                sadrzaj={"tekst": tekst, "odgovor": odgovor}, redoslijed=n,
            ))
            n += 1

        for pitanje, odgovor in FLASHCARD:
            db.add(models.TheoryItem(
                course_id=course.id, module_id=None, tip="flashcard",
                sadrzaj={"pitanje": pitanje, "odgovor": odgovor}, redoslijed=n,
            ))
            n += 1

        for pitanje, opcije, tocna in MCQ:
            db.add(models.TheoryItem(
                course_id=course.id, module_id=None, tip="mcq",
                sadrzaj={"pitanje": pitanje, "opcije": opcije, "tocna": tocna}, redoslijed=n,
            ))
            n += 1

        db.commit()
        print(f"[+] Uvezeno {n} stavki teorije za '{COURSE_NAME}'.")
        print(f"    T/N: {len(TRUEFALSE)}, Nadopuni: {len(FILLIN)}, Flashcard: {len(FLASHCARD)}, MCQ: {len(MCQ)}")
    finally:
        db.close()


if __name__ == "__main__":
    run()