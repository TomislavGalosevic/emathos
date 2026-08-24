"""Jednokratni uvoz teorije za kolegij 'Integralni racun'."""

from .database import SessionLocal
from . import models

COURSE_NAME = "Integralni racun"

# ---------------------------------------------------------------------------
# Tocno / Netocno (50)
# ---------------------------------------------------------------------------
TRUEFALSE = [
    ("Pseudotrapez je skup točaka u ravnini omeđen grafom funkcije $f$, osi $x$ te pravcima $x=a$ i $x=b$.", True),
    ("Subdivizija (particija) segmenta $[a,b]$ definira se kao konačan skup točaka s osobinom $a = x_0 > x_1 > \\dots > x_n = b$.", False),
    ("Dijametar subdivizije $P$ predstavlja maksimalnu udaljenost između bilo koje dvije susjedne točke $x_i - x_{i-1}$.", True),
    ("Kod ekvidistantne subdivizije duljina svakog podsegmenta iznosi $\\Delta x = \\frac{b-a}{n}$.", True),
    ("Ako je $P'$ profinjenje subdivizije $P$, onda $P'$ sadrži manje točaka od $P$.", False),
    ("Površina pseudotrapeza može se aproksimirati izborom proizvoljne točke $x_i^* \\in [x_{i-1}, x_i]$ za visinu pravokutnika.", True),
    ("Donja Darbouxova suma definira se pomoću supremuma $M_i$ funkcije $f$ na podsegmentu $[x_{i-1}, x_i]$.", False),
    ("Gornja Darbouxova suma $S(f,P)$ jednaka je $\\sum_{i=1}^{n} M_i (x_i - x_{i-1})$.", True),
    ("Za bilo koju točku $x_i^* \\in [x_{i-1}, x_i]$ vrijedi nejednakost $m_i \\le f(x_i^*) \\le M_i$.", True),
    ("Integralna suma $s(f,P,x_1^*,\\dots,x_n^*)$ uvijek leži između donje $s(f,P)$ i gornje $S(f,P)$ Darbouxove sume.", True),
    ("Ako subdiviziju profinimo s konačno mnogo točaka, donja Darbouxova suma se može smanjiti.", False),
    ("Bilo koja donja Darbouxova suma nije veća od bilo koje gornje Darbouxove sume.", True),
    ("Skup svih donjih Darbouxovih suma omeđen je odozdo.", False),
    ("Donji Riemannov integral definira se kao supremum skupa svih donjih Darbouxovih suma.", True),
    ("Gornji Riemannov integral definira se kao infimum skupa svih gornjih Darbouxovih suma.", True),
    ("Funkcija $f$ je integrabilna u Riemannovom smislu ako su donji i gornji Riemannov integral međusobno jednaki.", True),
    ("Po definiciji, $\\int_a^a f(x)dx = 1$.", False),
    ("Po definiciji, $\\int_a^b f(x)dx = -\\int_b^a f(x)dx$.", True),
    ("Dirichletova funkcija je primjer omeđene funkcije koja je Riemann integrabilna na $[0,1]$.", False),
    ("Ako je funkcija $f$ negativna na $[a,b]$, površina pseudotrapeza iznosi $P(T) = -\\int_a^b f(x)dx$.", True),
    ("Svaka neprekidna funkcija na segmentu $[a,b]$ je i Riemann integrabilna na tom segmentu.", True),
    ("Svaka monotona funkcija na segmentu $[a,b]$ je integrabilna.", True),
    ("Ako je funkcija integrabilna na $[a,b]$, ona mora biti neprekidna na tom segmentu.", False),
    ("Ako je $f(x) = c$ konstanta, tada je $\\int_a^b c \\, dx = c(b-a)$.", True),
    ("Svojstvo aditivnosti integrala po području integracije glasi $\\int_a^b f(x)dx = \\int_a^c f(x)dx + \\int_c^b f(x)dx$ za $c \\in [a,b]$.", True),
    ("Određeni integral je linearan operator.", True),
    ("Ako je $f(x) \\le g(x)$ za sve $x \\in [a,b]$, tada je $\\int_a^b f(x)dx \\ge \\int_a^b g(x)dx$.", False),
    ("Funkcija koja je neprekidna na $[a,b]$ osim u konačno mnogo točaka i dalje je integrabilna na $[a,b]$.", True),
    ("Prema Teoremu srednje vrijednosti za integral, postoji $c \\in [a,b]$ takav da je $\\int_a^b f(x)dx = f(c)(b-a)$.", True),
    ("Vrijednost $f(c) = \\frac{1}{b-a}\\int_a^b f(x)dx$ naziva se srednja vrijednost funkcije $f$ na $[a,b]$.", True),
    ("Primitivna funkcija $F$ funkcije $f$ zadovoljava uvjet $F'(x) = f(x)$.", True),
    ("Dvije primitivne funkcije iste funkcije $f$ mogu se razlikovati za proizvoljnu funkciju $g(x)$.", False),
    ("Funkcija $g(x) = \\int_a^x f(t)dt$ je derivabilna i vrijedi $g'(x) = f(x)$ ako je $f$ neprekidna.", True),
    ("Newton-Leibnizova formula glasi $\\int_a^b f(x)dx = F(b) - F(a)$.", True),
    ("Neodređeni integral predstavlja točno jednu funkciju.", False),
    ("Operacija integriranja neodređenog integrala je inverzna operacija deriviranju.", True),
    ("Ako je $f(x) = \\frac{P_k(x)}{Q_l(x)}$ i $k \\ge l$, funkcija $f$ je prava racionalna funkcija.", False),
    ("Binomni integral je oblika $\\int x^m (a + b x^n)^p dx$.", True),
    ("Čebišev je dokazao da je binomni integral iskaziv pomoću elementarnih funkcija u samo tri slučaja.", True),
    ("Nepravi integral $\\int_a^{+\\infty} f(x)dx$ definira se kao $\\lim_{b \\to +\\infty} \\int_a^b f(x)dx$.", True),
    ("Nepravi integral $\\int_1^{+\\infty} \\frac{dx}{x^p}$ konvergira za $p \\le 1$.", False),
    ("Ako nepravi integral $\\int_a^{+\\infty} |f(x)|dx$ konvergira, tada konvergira i $\\int_a^{+\\infty} f(x)dx$.", True),
    ("Iz konvergencije integrala $\\int_a^{+\\infty} f(x)dx$ nužno slijedi apsolutna konvergencija.", False),
    ("Nužan uvjet za konvergenciju reda $\\sum a_n$ je da $\\lim_{n \\to \\infty} a_n = 0$.", True),
    ("Ako je $\\lim_{n \\to \\infty} a_n = 0$, red $\\sum a_n$ sigurno konvergira.", False),
    ("Harmonijski red $\\sum \\frac{1}{n}$ je konvergentan red.", False),
    ("Geometrijski red $\\sum a_1 q^{n-1}$ konvergira ako i samo ako je $|q| < 1$.", True),
    ("Prema D'Alembertovom kriteriju u formi limesa, ako je $L = \\lim_{n \\to \\infty} \\frac{a_{n+1}}{a_n} = 1$, red konvergira.", False),
    ("Cauchyjev kriterij je jači od D'Alembertovog kriterija.", True),
    ("Svaki alternirani red koji zadovoljava da $|a_n|$ monotono opada prema 0 konvergira prema Leibnizovom kriteriju.", True),
]

# ---------------------------------------------------------------------------
# Nadopuni recenicu (50) - odgovor je OBICAN TEKST (usporeduje se doslovno)
# ---------------------------------------------------------------------------
FILLIN = [
    ("Skup točaka u ravnini omeđen grafom funkcije $f$, osi $x$ i pravcima $x=a$ i $x=b$ zove se ___.", "pseudotrapez"),
    ("Najveća od udaljenosti $x_i - x_{i-1}$ zove se ___ subdivizije $P$.", "dijametar"),
    ("Za subdiviziju kod koje su svi podsegmenti jednake duljine kažemo da je ___.", "ekvidistantna"),
    ("Ako je $P \\subseteq P'$, za subdiviziju $P'$ kažemo da je ___ subdivizije $P$.", "profinjenje"),
    ("Donja Darbouxova suma definiše se pomoću ___ funkcije $f$ na podsegmentima.", "infimuma"),
    ("Gornja Darbouxova suma definiše se pomoću ___ funkcije $f$ na podsegmentima.", "supremuma"),
    ("Nejednakost $m(b-a) \\le s(f,P) \\le S(f,P^*,x_1^*,\\dots,x_n^*) \\le S(f,P) \\le M(b-a)$ povezuje Darbouxove i ___ sume.", "integralne"),
    ("Profinjenjem subdivizije donja Darbouxova suma se neće ___.", "smanjiti"),
    ("Profinjenjem subdivizije gornja Darbouxova suma se neće ___.", "povecati"),
    ("Bilo koja donja Darbouxova suma nije ___ od bilo koje gornje Darbouxove sume.", "veca"),
    ("Supremum skupa svih donjih Darbouxovih suma zove se ___ Riemannov integral.", "donji"),
    ("Infimum skupa svih gornjih Darbouxovih suma zove se ___ Riemannov integral.", "gornji"),
    ("Ako su donji i gornji Riemannov integral jednaki, kažemo da je funkcija $f$ ___ u Riemannovom smislu.", "integrabilna"),
    ("Određeni integral funkcije na segmentu $[a,a]$ po definiciji iznosi ___.", "0"),
    ("Zbog zamjene granica integracije vrijedi $\\int_a^b f(x)dx = -$ ___.", "int_b^a f(x)dx"),
    ("Funkcija $f(x) = 1$ za $x \\in \\mathbb{Q}$ i $f(x) = 0$ za $x \\in \\mathbb{I}$ zove se ___ funkcija.", "Dirichletova"),
    ("Površina omeđena grafovima funkcija $f(x)$ i $g(x)$ gdje je $f(x) \\ge g(x)$ računa se kao $P(A) = \\int_a^b$ ___ $dx$.", "f(x)-g(x)"),
    ("Pomoćna lema navodi da je $f$ integrabilna akko za svaki $\\epsilon > 0$ postoji subdivizija $P$ t.d. je $S(f,P) - s(f,P) <$ ___.", "epsilon"),
    ("Riemannov teorem garantira da je svaka ___ funkcija na $[a,b]$ ujedno i integrabilna.", "neprekidna"),
    ("Svaka ___ funkcija na $[a,b]$ je integrabilna na tom segmentu.", "monotona"),
    ("Prema Darbouxovom teoremu, ako niz subdivizija ima dijametar koji teži k nuli, nizovi Darbouxovih suma su ___.", "konvergentni"),
    ("Svojstvo $\\int_a^b (c_1 f(x) + c_2 g(x)) dx = c_1 \\int_a^b f(x)dx + c_2 \\int_a^b g(x)dx$ naziva se ___ određenog integrala.", "linearnost"),
    ("Za neprekidnu funkciju $f$, broj $\\frac{1}{b-a}\\int_a^b f(x)dx$ naziva se ___ vrijednost funkcije $f$ na segmentu $[a,b]$.", "srednja"),
    ("Funkcija $F$ za koju vrijedi $F'(x) = f(x)$ naziva se ___ funkcija funkcije $f$.", "primitivna"),
    ("Bilo koje dvije primitivne funkcije iste funkcije razlikuju se za ___.", "konstantu"),
    ("Prvi dio osnovnog teorema dif. i integ. računa tvrdi da je funkcija $g(x) = \\int_a^x f(t)dt$ ___ na $[a,b]$.", "derivabilna"),
    ("Formula $\\int_a^b f(x)dx = F(b) - F(a)$ zove se ___ formula.", "Newton-Leibnizova"),
    ("Skup svih primitivnih funkcija funkcije $f$ zove se ___ integral.", "neodredjeni"),
    ("Postupak traženja neodređenog integrala zove se ___.", "integriranje"),
    ("Ako je u racionalnoj funkciji stupanj brojnika manji od stupnja nazivnika, radi se o ___ racionalnoj funkciji.", "pravoj"),
    ("Metoda zamjene varijable u integralu naziva se metoda ___.", "supstitucije"),
    ("Formula $\\int u \\, dv = u \\cdot v - \\int v \\, du$ predstavlja formulu za ___ integraciju.", "parcijalnu"),
    ("Integral oblika $\\int x^m (a + b x^n)^p dx$ naziva se ___ integral.", "binomni"),
    ("Ako je $p \\in \\mathbb{Z}$ u binomnom integralu, koristimo supstituciju $x=t^s$ gdje je $s$ zajednički nazivnik od $m$ i ___.", "n"),
    ("Ako je kod nepravog integrala granica integracije $+\\infty$, riječ je o nepravom integralu na ___ intervalu.", "neomedjenom"),
    ("Nepravi integral $\\int_a^{+\\infty} \\frac{dx}{x^p}$ konvergira ako i samo ako je $p >$ ___.", "1"),
    ("Test za ispitivanje konvergencije integrala usporedbom s $x^p$ naziva se ___-test.", "p"),
    ("Za red $\\sum a_n$, niz $s_n = \\sum_{k=1}^n a_k$ naziva se niz ___ suma.", "parcijalnih"),
    ("Ako postoji konačan limes niza parcijalnih suma, kažemo da red ___.", "konvergira"),
    ("Ako red ne konvergira, kažemo da ___.", "divergira"),
    ("Red $\\sum_{n=1}^\\infty \\frac{1}{n}$ zove se ___ red.", "harmonijski"),
    ("Ako red $\\sum |a_n|$ konvergira, onda red $\\sum a_n$ ___ konvergira.", "apsolutno"),
    ("Ako red $\\sum a_n$ konvergira, ali $\\sum |a_n|$ divergira, red konvergira ___.", "uvjetno"),
    ("Kriterij konvergencije reda koji promatra limes $\\lim_{n \\to \\infty} \\left|\\frac{a_{n+1}}{a_n}\\right|$ naziva se ___ kriterij.", "D'Alembertov"),
    ("Kriterij koji promatra limes $\\lim_{n \\to \\infty} \\sqrt[n]{|a_n|}$ naziva se ___ kriterij.", "Cauchyjev"),
    ("Za alternirane redove koristi se ___ kriterij konvergencije.", "Leibnizov"),
    ("Red oblika $\\sum_{n=0}^\\infty a_n (x-c)^n$ naziva se red ___ oko točke $c$.", "potencija"),
    ("Broj $r$ takav da red potencija konvergira za $|x-c| < r$ zove se ___ konvergencije.", "radijus"),
    ("Formula $r = \\frac{1}{\\limsup \\sqrt[n]{|a_n|}}$ zove se Cauchy-___ formula.", "Hadamardova"),
    ("Red oblika $\\sum_{k=0}^\\infty \\frac{f^{(k)}(c)}{k!}(x-c)^k$ zove se ___ red funkcije $f$ oko točke $c$.", "Taylorov"),
]

# ---------------------------------------------------------------------------
# Flash kartice (25)
# ---------------------------------------------------------------------------
FLASHCARD = [
    ("Što je dijametar subdivizije $d(P)$?",
     "Maksimalna duljina podintervala u subdiviziji $P$: $d(P) = \\max\\{x_i - x_{i-1} : i=1,\\dots,n\\}$."),
    ("Definirajte donju Darbouxovu sumu $s(f,P)$.",
     "$s(f,P) = \\sum_{i=1}^n m_i(x_i-x_{i-1})$, gdje je $m_i = \\inf\\{f(x): x\\in[x_{i-1},x_i]\\}$."),
    ("Definirajte gornju Darbouxovu sumu $S(f,P)$.",
     "$S(f,P) = \\sum_{i=1}^n M_i(x_i-x_{i-1})$, gdje je $M_i = \\sup\\{f(x): x\\in[x_{i-1},x_i]\\}$."),
    ("Kakav je odnos donjeg i gornjeg Riemannovog integrala?",
     "Donji je uvijek manji ili jednak gornjem."),
    ("Kada je omeđena funkcija $f$ integrabilna u Riemannovom smislu?",
     "Kada su joj donji i gornji Riemannov integral jednaki."),
    ("Navedite iskaz Riemannovog teorema o integrabilnosti neprekidne funkcije.",
     "Ako je $f:[a,b]\\to\\mathbb{R}$ neprekidna na $[a,b]$, onda je ona i integrabilna na $[a,b]$."),
    ("Navedite teorem o integrabilnosti monotone funkcije.",
     "Svaka monotona funkcija $f:[a,b]\\to\\mathbb{R}$ je integrabilna na $[a,b]$."),
    ("Navedite Teorem srednje vrijednosti za integral neprekidne funkcije.",
     "Ako je $f:[a,b]\\to\\mathbb{R}$ neprekidna, postoji $c\\in[a,b]$ t.d. je $\\int_a^b f(x)dx = f(c)(b-a)$."),
    ("Što je primitivna funkcija (antiderivacija)?",
     "Funkcija $F$ za koju vrijedi $F'(x)=f(x)$ za sve $x\\in[a,b]$."),
    ("Navedite Prvi dio osnovnog teorema diferencijalnog i integralnog računa.",
     "Ako je $f$ neprekidna na $[a,b]$, funkcija $g(x)=\\int_a^x f(t)dt$ je derivabilna na $[a,b]$ i vrijedi $g'(x)=f(x)$."),
    ("Iskažite Newton-Leibnizovu formulu.",
     "Ako je $f$ neprekidna na $[a,b]$ i $F$ njena primitivna funkcija, tada je $\\int_a^b f(x)dx = F(b)-F(a)$."),
    ("Koja je formula za parcijalnu integraciju?",
     "$\\int u\\,dv = u\\cdot v - \\int v\\,du$."),
    ("Što je to prava racionalna funkcija?",
     "Omjer dvaju polinoma $\\frac{P(x)}{Q(x)}$ gdje je stupanj $P(x)$ strogo manji od stupnja $Q(x)$."),
    ("Koja su 3 slučaja rješivosti binomnog integrala $\\int x^m(a+bx^n)^p dx$ prema Čebiševu?",
     "1. $p\\in\\mathbb{Z}$; 2. $\\frac{m+1}{n}\\in\\mathbb{Z}$; 3. $\\frac{m+1}{n}+p\\in\\mathbb{Z}$."),
    ("Kada nepravi integral $\\int_a^{+\\infty} \\frac{dx}{x^p}$ ($a>0$) konvergira, a kada divergira?",
     "Konvergira za $p>1$, a divergira za $p\\le 1$."),
    ("Iskažite nužan uvjet za konvergenciju reda $\\sum a_n$.",
     "$\\lim_{n\\to\\infty} a_n = 0$."),
    ("Kada geometrijski red $\\sum a_1 q^{n-1}$ konvergira i kolika mu je suma?",
     "Konvergira za $|q|<1$, a suma iznosi $S=\\frac{a_1}{1-q}$."),
    ("Što tvrdi Poredbeni (komparacijski) kriterij za redove kada je $a_n \\le c\\cdot b_n$?",
     "Ako $\\sum b_n$ konvergira, konvergira i $\\sum a_n$; ako $\\sum a_n$ divergira, divergira i $\\sum b_n$."),
    ("Iskažite D'Alembertov kriterij u formi limesa.",
     "Neka je $L=\\lim \\frac{a_{n+1}}{a_n}$. Za $L<1$ konvergira, za $L>1$ divergira, za $L=1$ nema odluke."),
    ("Iskažite Cauchyjev kriterij u formi limesa.",
     "Neka je $L=\\lim \\sqrt[n]{a_n}$. Za $L<1$ konvergira, za $L>1$ divergira, za $L=1$ nema odluke."),
    ("Što je to alternirani red?",
     "Red čiji članovi naizmjence mijenjaju predznak, oblika $\\sum(-1)^{n-1}a_n$ uz $a_n\\ge 0$."),
    ("Navedite uvjete Leibnizovog teorema za alternirane redove.",
     "Niz $|a_n|$ mora biti padajući i $\\lim_{n\\to\\infty} a_n = 0$."),
    ("Koja je razlika između apsolutne i uvjetne konvergencije reda?",
     "Apsolutno konvergira ako konvergira $\\sum|a_n|$. Uvjetno konvergira ako $\\sum a_n$ konvergira, ali $\\sum|a_n|$ divergira."),
    ("Što predstavlja radijus konvergencije $r$ reda potencija?",
     "Polumjer intervala $\\langle c-r,c+r\\rangle$ unutar kojeg red potencija apsolutno konvergira."),
    ("Kako glasi Cauchy-Hadamardova formula?",
     "$r = \\frac{1}{\\limsup_{n\\to\\infty}\\sqrt[n]{|a_n|}}$."),
]

# ---------------------------------------------------------------------------
# Visestruki odabir (20)
# ---------------------------------------------------------------------------
MCQ = [
    ("Dijametar $d(P)$ subdivizije $P=\\{x_0,x_1,\\dots,x_n\\}$ definira se kao:",
     ["$\\min_i(x_i-x_{i-1})$", "$\\max_i(x_i-x_{i-1})$", "$\\frac{b-a}{n}$", "$x_n-x_0$"], 1),
    ("Ako je $P'$ profinjenje subdivizije $P$, koja je relacija točna za donje Darbouxove sume?",
     ["$s(f,P') \\le s(f,P)$", "$s(f,P') \\ge s(f,P)$", "$s(f,P') = S(f,P)$", "$s(f,P') = 0$"], 1),
    ("Odnos donjeg $\\underline{I}$ i gornjeg $\\overline{I}$ Riemannovog integrala za bilo koju omeđenu funkciju je:",
     ["$\\underline{I} > \\overline{I}$", "$\\underline{I} \\le \\overline{I}$", "$\\underline{I} \\cdot \\overline{I} = 1$", "Nisu usporedivi"], 1),
    ("Dirichletova funkcija na segmentu $[0,1]$:",
     ["Je integrabilna i integral joj iznosi 1", "Je integrabilna i integral joj iznosi 0",
      "Nije integrabilna u Riemannovom smislu", "Je neprekidna funkcija"], 2),
    ("Riemannov teorem tvrdi da je funkcija integrabilna na $[a,b]$ ako je:",
     ["Samo omeđena", "Neprekidna na $[a,b]$", "Pozitivna", "Polinom strogog stupnja $n \\ge 2$"], 1),
    ("Ako je $f$ integrabilna na $[a,b]$ i $c \\in [a,b]$, tada je $\\int_a^b f(x)dx$ jednak:",
     ["$\\int_a^c f(x)dx \\cdot \\int_c^b f(x)dx$", "$\\int_a^c f(x)dx + \\int_c^b f(x)dx$",
      "$\\int_a^c f(x)dx - \\int_c^b f(x)dx$"], 1),
    ("Srednja vrijednost neprekidne funkcije $f$ na segmentu $[a,b]$ definirana je s:",
     ["$\\int_a^b f(x)dx$", "$\\frac{f(a)+f(b)}{2}$", "$\\frac{1}{b-a}\\int_a^b f(x)dx$", "$f\\left(\\frac{a+b}{2}\\right)$"], 2),
    ("Ako je $g(x) = \\int_a^x f(t)dt$ gdje je $f$ neprekidna, tada je $g'(x)$ jednako:",
     ["$f'(x)$", "$f(x)$", "$F(b) - F(a)$", "$0$"], 1),
    ("Newton-Leibnizova formula izražava određeni integral pomoću:",
     ["Darbouxovih suma", "Primitivne funkcije", "Derivacije u rubovima", "Limesa nizova"], 1),
    ("Formula parcijalne integracije izlazi iz pravila za:",
     ["Deriviranje kvocijenta", "Deriviranje umnoška", "Lančano pravilo", "Zbrajanje derivacija"], 1),
    ("Racionalna funkcija $\\frac{P(x)}{Q(x)}$ je prava racionalna funkcija ako:",
     ["$\\deg(P) \\ge \\deg(Q)$", "$\\deg(P) < \\deg(Q)$", "$\\deg(P) = \\deg(Q)$", "$Q(x) = 1$"], 1),
    ("Nepravi integral $\\int_1^{+\\infty} \\frac{dx}{x^2}$ iznosi:",
     ["$0$", "$1$", "$+\\infty$", "Divergira"], 1),
    ("Nepravi integral $\\int_1^{+\\infty} \\frac{dx}{x^p}$ konvergira ako i samo ako je:",
     ["$p < 1$", "$p \\le 1$", "$p > 1$", "$p = 1$"], 2),
    ("Ako red $\\sum a_n$ konvergira, tada je $\\lim_{n \\to \\infty} a_n$ jednak:",
     ["$1$", "$0$", "$+\\infty$", "Ne mora postojati"], 1),
    ("Harmonijski red $\\sum_{n=1}^\\infty \\frac{1}{n}$:",
     ["Konvergira prema 0", "Konvergira prema 1", "Divergira", "Apsolutno konvergira"], 2),
    ("Geometrijski red $\\sum_{n=0}^\\infty q^n$ konvergira za:",
     ["$q > 1$", "$|q| < 1$", "$q \\le -1$", "Sve $q \\in \\mathbb{R}$"], 1),
    ("Ako u D'Alembertovom kriteriju dobijemo $L = \\lim \\left|\\frac{a_{n+1}}{a_n}\\right| = 0.5$, red:",
     ["Apsolutno konvergira", "Uvjetno konvergira", "Divergira", "Kriterij ne daje odluku"], 0),
    ("Ako u Cauchyjevom kriteriju dobijemo $L = 1$, zaključujemo da:",
     ["Red konvergira", "Red divergira", "Kriterij ne daje odluku", "Red je alternirani"], 2),
    ("Alternirani red $\\sum_{n=1}^\\infty \\frac{(-1)^{n-1}}{n}$:",
     ["Divergira", "Apsolutno konvergira", "Uvjetno konvergira", "Nema definiranu sumu"], 2),
    ("Koeficijenti $a_n$ u Taylorovom redu $\\sum a_n (x-c)^n$ dane funkcije $f$ jednaki su:",
     ["$f^{(n)}(c)$", "$\\frac{f^{(n)}(c)}{n!}$", "$\\frac{f(c)}{n!}$", "$\\frac{n!}{f^{(n)}(c)}$"], 1),
]


def run():
    db = SessionLocal()
    try:
        course = db.query(models.Course).filter(models.Course.naziv == COURSE_NAME).first()
        if not course:
            print(f"[!] Kolegij '{COURSE_NAME}' ne postoji u bazi. Prekidam.")
            return

        n = 0
        for tvrdnja, tocno in TRUEFALSE:
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