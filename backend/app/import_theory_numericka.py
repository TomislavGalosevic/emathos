"""Jednokratni uvoz teorije za kolegij 'Numericka matematika'."""

from .database import SessionLocal
from . import models

COURSE_NAME = "Numericka matematika"

# ---------------------------------------------------------------------------
# Tocno / Netocno (50)
# ---------------------------------------------------------------------------
TRUEFALSE = [
    ("Ako je $a^*$ aproksimacija realnog broja $a$, njene prve $n$ znamenke nazivamo signifikantnima ako apsolutna pogreška zadovoljava uvjet $\\Delta a^* \\le \\frac{1}{2}\\cdot 10^{m-n+1}$.", True),
    ("Pogreška u izračunavanju vrijednosti funkcije $f:\\mathbb{R}^n\\to\\mathbb{R}$ s više varijabli aproksimira se sumom umnožaka apsolutnih vrijednosti parcijalnih derivacija i pogrešaka pripadnih varijabli.", True),
    ("Kod određivanja pogreške u varijablama pri računanju vrijednosti funkcije (inverzni problem) koristi se princip jednakih efekata.", True),
    ("Interpolacijski polinom $P_n$ stupnja najviše $n$ koji u $n+1$ različitih čvorova poprima zadane vrijednosti $y_i$ postoji i jedinstven je.", True),
    ("Konstrukcija Lagrangeovog interpolacijskog polinoma koristi pomoćne polinome $p_i(x)$ za koje vrijedi $p_i(x_j)=1$ za $i=j$, odnosno $0$ za $i\\ne j$.", True),
    ("Newtonov oblik interpolacijskog polinoma koristi podijeljene razlike čvorova interpolacije.", True),
    ("Kubični interpolacijski spline na razdiobi s $n$ podintervala definiran je pomoću $n$ kubičnih polinoma i ukupno $4n$ nepoznatih koeficijenata.", True),
    ("Prirodni uvjeti za kubični interpolacijski spline zahtijevaju da su druge derivacije u rubnim čvorovima $x_0$ i $x_n$ jednake nuli.", True),
    ("Pogreška linearnog splinea na intervalu duljine $h_i$ omeđena je s $\\frac{M_2}{8}h_i^2$, gdje je $M_2$ gornja granica druge derivacije funkcije.", True),
    ("Metoda bisekcije ima linearnu brzinu konvergencije ($r=1$).", True),
    ("Newtonova metoda tangenti ima kvadratnu brzinu konvergencije ($r=2$).", True),
    ("Metoda bisekcije za funkciju neprekidnu na $[a,b]$ uz $f(a)\\cdot f(b) < 0$ jamči konvergenciju prema nultočki.", True),
    ("Pretpostavka teorema o konvergenciji metode jednostavnih iteracija $x=\\varphi(x)$ zahtijeva da je $|\\varphi'(x)| \\le q < 1$ na uočenom segmentu.", True),
    ("Teorem o konvergenciji Newtonove metode tangenti zahtijeva da prva i druga derivacija funkcije $f$ na intervalu imaju stalni predznak te da je $f(x_0)\\cdot f''(x_0) > 0$ za početnu aproksimaciju $x_0$.", True),
    ("U linearnom problemu najmanjih kvadrata (LPNK) za matricu $J$ dimenzije $m\\times n$ ($m \\gg n$), sustav normalnih jednadžbi ima oblik $(J^T J)a = J^T y$.", True),
    ("Ako su stupci matrice sustava $J$ u LPNK linearno nezavisni, sustav normalnih jednadžbi ima jedinstveno rješenje.", True),
    ("Frobeniusova norma matrice $A \\in \\mathbb{R}^{n\\times n}$ definira se kao korijen iz sume kvadrata svih elemenata matrice $A$.", True),
    ("Euklidska kondicija $\\text{cond}_2(A)$ matrice $A$ jednaka je omjeru najveće i najmanje singularne vrijednosti matrice $A$.", True),
    ("Vandermondeova matrica predstavlja primjer loše uvjetovane matrice.", True),
    ("Pogreška jednostavne trapezne formule pri numeričkoj integraciji omeđena je s $\\frac{(b-a)^3}{12}M_2$.", True),
    ("Kod produljene trapezne formule s $n$ jednakih podintervala širine $h$, pogreška je omeđena s $\\frac{b-a}{12}h^2 M_2$.", True),
    ("Newton-Cotesove formule dobivaju se interpoliranjem integranda Lagrangeovim polinomom na ekvidistantnoj razdiobi čvorova.", True),
    ("Simpsonova formula numeričke integracije dobiva se iz Newton-Cotesovih formula za $n=2$.", True),
    ("Kod produljene Simpsonove formule segment integracije $[a,b]$ dijeli se na paran broj podintervala $n=2m$.", True),
    ("Rješavanje LPNK pomoću QR dekompozicije svodi se na rješavanje gornjetrokutastog sustava $R_n a^* = Q_n^T y$.", True),
    ("Interpolacija je postupak kojim tražimo funkciju koja minimizira odstupanja po cijeloj domeni, umjesto prolaska kroz zadane čvorove.", False),
    ("Postoji više različitih interpolacijskih polinoma stupnja najviše $n$ koji prolaze kroz $n+1$ zadanih čvorova.", False),
    ("Vandermondeova matrica sustava za određivanje koeficijenata interpolacijskog polinoma je singularna ako su svi čvorovi $x_i$ međusobno različiti.", False),
    ("Za određivanje kubičnog interpolacijskog splinea na razdiobi od $n$ podintervala uvjeti kontinuiteta funkcije i derivacija daju točno $4n$ uvjeta.", False),
    ("Newtonova metoda tangenti ima linearnu brzinu konvergencije $r=1$.", False),
    ("Metoda bisekcije konvergira brže od Newtonove metode tangenti.", False),
    ("Ocjena pogreške $n$-te aproksimacije $x_n$ u metodi bisekcije iznosi $|\\xi - x_n| \\le \\frac{b_0-a_0}{2^{n-1}}$.", False),
    ("Metoda jednostavnih iteracija $x_n = \\varphi(x_{n-1})$ konvergira za bilo koju diferencijabilnu funkciju $\\varphi$.", False),
    ("Ako je $\\text{cond}(A) \\gg 1$ za matricu $A$, kažemo da je linearni sustav $Ax=b$ dobro uvjetovan.", False),
    ("Matrica je dobro uvjetovana ako je njezina kondicija $\\text{cond}(A)$ blizu beskonačnosti.", False),
    ("Jednostavna trapezna formula aproksimira područje ispod funkcije pomoću parabole.", False),
    ("Simpsonova formula za integraciju koristi interpolacijski polinom stupnja 1.", False),
    ("U produljenoj Simpsonovoj formuli broj podintervala $n$ može biti proizvoljan neparan broj.", False),
    ("Teorem o srednjoj vrijednosti za integrale ne može se primijeniti pri izvođenju pogreške trapezne formule.", False),
    ("Kod SVD dekompozicije matrice $J = U\\Sigma V^T$, matrica $\\Sigma$ je uvijek kvadratna i invertibilna matrica bez obzira na rang.", False),
    ("Problem najmanjih kvadrata nastoji maksimizirati euklidsku normu reziduala $\\|Ja-y\\|_2$.", False),
    ("Pravac usvojen u smislu najmanjih kvadrata za zadane podatke nikada nije jedinstven.", False),
    ("Konvergencija niza u metodi jednostavnih iteracija ovisi isključivo o odabiru početne točke $x_0$, a ne o funkciji $\\varphi$.", False),
    ("Linearni interpolacijski spline ima neprekidnu drugu derivaciju u čvorovima interpolacije.", False),
    ("Podijeljena razlika 0-tog reda $f[x_0]$ jednaka je $0$ za svaku funkciju $f$.", False),
    ("Ako funkcija $f$ nije neprekidna na segmentu $[a,b]$, metoda bisekcije uvijek konvergira prema točnom rješenju.", False),
    ("Što je manja širina koraka $h$ u produljenoj trapeznoj formuli, to je ocjena pogreške integracije veća.", False),
    ("Za računanje euklidske norme matrice $\\|A\\|_2$ nije potrebno poznavati singularne vrijednosti matrice $A$.", False),
    ("Kod nelinearnog problema najmanjih kvadrata funkcija koju minimiziramo uvijek je linearna po parametrima.", False),
    ("Kod interpolacije funkcije stupanj interpolacijskog polinoma s $n+1$ čvorova može biti proizvoljno velik, neovisno o broju čvorova.", False),
]

# ---------------------------------------------------------------------------
# Nadopuni recenicu (50) - odgovor je OBICAN TEKST (usporeduje se doslovno)
# ---------------------------------------------------------------------------
FILLIN = [
    ("Prvih $n$ znamenaka aproksimacije $a^*$ za koje vrijedi $\\Delta a^* \\le \\frac{1}{2}\\cdot 10^{m-n+1}$ nazivaju se ___ znamenke.", "signifikantne"),
    ("Razlika između stvarne vrijednosti funkcije i aproksimacije u jednoj varijabli aproksimira se pomoću Lagrangeovog teorema kao $\\Delta z^* \\approx |f'(x)| \\cdot$ ___.", "Delta x*"),
    ("Za određivanje pogreške u varijablama pri zadanoj pogrešci funkcije koristi se princip ___.", "jednakih efekata"),
    ("Postupak traženja funkcije koja u zadanim čvorovima poprima točno predefinirane vrijednosti naziva se ___.", "interpolacija"),
    ("Postupak zamjene funkcije jednostavnijom pri čemu se minimizira odstupanje na cijeloj domeni naziva se ___.", "aproksimacija"),
    ("Za $n+1$ različitih čvorova $x_0<x_1<\\dots<x_n$ postoji jedinstveni interpolacijski polinom $P_n$ stupnja najviše ___.", "n"),
    ("Matrica čija se determinanta pojavljuje pri dokazu jedinstvenosti interpolacijskog polinoma i ne poništava se za različite čvorove je ___ matrica.", "Vandermondeova"),
    ("Pomoćne funkcije $p_i(x)$ u Lagrangeovom interpolacijskom polinomu zadovoljavaju $p_i(x_j) =$ ___ za $i=j$.", "1"),
    ("Podijeljena razlika $k$-tog reda $f[x_0,x_1,\\dots,x_k]$ definira se kao omjer $(f[x_1,\\dots,x_k]-f[x_0,\\dots,x_{k-1}])/($ ___ $)$.", "x_k-x_0"),
    ("Polinom oblika $P_n(x) = f[x_0] + f[x_0,x_1](x-x_0) + \\dots$ naziva se ___ oblik interpolacijskog polinoma.", "Newtonov"),
    ("Polinom kojim po dijelovima interpoliramo funkciju na manjim podintervalima naziva se ___.", "spline"),
    ("Za određivanje kubičnog interpolacijskog splinea potrebno je odrediti ukupno ___ koeficijenata.", "4n"),
    ("Prirodni uvjeti za kubični spline glase $c''(x_0)=0$ i ___.", "c''(x_n)=0"),
    ("Ocjena pogreške linearnog splinea s maksimalnim korakom $h_{max}$ glasi $|f(x)-\\varphi(x)| \\le$ ___ $\\cdot h_{max}^2$.", "M_2/8"),
    ("Ako niz aproksimacija $e_n$ zadovoljava $|e_{n+1}| \\le A|e_n|^r$, broj $r$ naziva se ___ konvergencije.", "brzina"),
    ("Metoda bisekcije ima ___ brzinu konvergencije.", "linearnu"),
    ("Newtonova metoda tangenti ima ___ brzinu konvergencije.", "kvadratnu"),
    ("Ocjena pogreške $n$-te aproksimacije $x_n$ u metodi bisekcije glasi $|\\xi - x_n| \\le$ ___.", "(1/2^n)*(b0-a0)"),
    ("U metodi jednostavnih iteracija početna jednadžba $f(x)=0$ prevodi se u oblik ___.", "x=phi(x)"),
    ("Teorem o konvergenciji metode jednostavnih iteracija zahtijeva postojanje $q \\in \\langle 0,1\\rangle$ takvog da je $|\\varphi'(x)| \\le$ ___.", "q"),
    ("Jednadžba tangente u točki $x_0$ pri izvođenju Newtonove metode glasi $t_0(x) = f(x_0) +$ ___.", "f'(x0)*(x-x0)"),
    ("Rekurzivna relacija za Newtonovu metodu tangenti glasi $x_{n+1} = x_n -$ ___.", "f(xn)/f'(xn)"),
    ("U teoremu o konvergenciji Newtonove metode tangenti uvjet za početnu aproksimaciju $x_0$ je $f(x_0)\\cdot f''(x_0) >$ ___.", "0"),
    ("Kriterijska funkcija u problemu aproksimacije definira se kao kvadrat ___ funkcija $f$ i $g$.", "udaljenosti"),
    ("Sustav jednadžbi dobiven parcijalnim deriviranjem kriterijske funkcije po koeficijentima sadrži ___ matricu.", "Gramovu"),
    ("Linija koja u smislu najmanjih kvadrata najbolje aproksimira podatke minimizira sumu ___ udaljenosti.", "vertikalnih"),
    ("U općem linearnom problemu najmanjih kvadrata zadan je sustav s matricom $J$ dimenzije $m\\times n$ pri čemu je $m$ ___ $n$.", ">>"),
    ("Sustav normalnih jednadžbi u LPNK glasi ___ $\\cdot a = J^T y$.", "J^T*J"),
    ("Vektor reziduala definira se izrazom $r =$ ___.", "y-J*a"),
    ("Kod QR dekompozicije matrica $J$ zapiše se kao umnožak $Q\\cdot R$ gdje je $Q$ ortogonalna, a $R$ ___ matrica.", "gornjetrokutasta"),
    ("Frobeniusova norma matrice $A$ izračunava se kao korijen iz sume ___ svih elemenata matrice.", "kvadrata"),
    ("$p$-norma matrice definira se kao $\\max_{x\\ne 0} (\\|Ax\\|_p /$ ___ $)$.", "||x||_p"),
    ("Mjera osjetljivosti rješenja sustava $Ax=b$ na male promjene desne strane zove se ___ matrice.", "kondicija"),
    ("Kondicija matrice $A$ u euklidskoj normi definira se kao $\\text{cond}_2(A) = \\sigma_{max} /$ ___.", "sigma_min"),
    ("Sustav za koji je $\\text{cond}(A) \\approx 1$ naziva se ___ uvjetovan.", "dobro"),
    ("Jednostavna trapezna formula aproksimira integral funkcije $f$ na $[a,b]$ izrazom $(b-a)\\cdot($ ___ $)/2$.", "f(a)+f(b)"),
    ("Pogreška jednostavne trapezne formule gornje je omeđena s $\\frac{(b-a)^3}{12}\\cdot$ ___.", "M_2"),
    ("Kod produljene trapezne formule korak ekvidistantne razdiobe definiran je kao $h =$ ___.", "(b-a)/n"),
    ("Aproksimacija integrala u produljenoj trapeznoj formuli iznosi $I^* = \\frac{h}{2}(y_0 + 2\\sum_{i=1}^{n-1} y_i +$ ___ $)$.", "y_n"),
    ("Newton-Cotesove formule dobivaju se integriranjem ___ polinoma stupnja $n$.", "Lagrangeovog"),
    ("Simpsonova formula dobiva se iz Newton-Cotesovih formula uvrštavanjem $n=$ ___.", "2"),
    ("Čvorovi za jednostavnu Simpsonovu formulu na segmentu $[a,b]$ su $x_0=a$, $x_1=(a+b)/2$ i $x_2=$ ___.", "b"),
    ("Aproksimacija integrala Simpsonovom formulom glasi $I^* \\approx \\frac{b-a}{6}(f(a) + 4f(\\frac{a+b}{2}) +$ ___ $)$.", "f(b)"),
    ("Kod produljene Simpsonove formule ukupan broj podintervala $n$ mora biti ___.", "paran"),
    ("Formula produljene Simpsonove integracije koristi faktor ___ ispred zagrade s težinama.", "h/3"),
    ("Težinski koeficijenti uz neparne indekse $y_{2k+1}$ u produljenoj Simpsonovoj formuli iznose ___.", "4"),
    ("Težinski koeficijenti uz parne unutrašnje indekse $y_{2k}$ u produljenoj Simpsonovoj formuli iznose ___.", "2"),
    ("SVD dekompozicija zapiše matricu $J$ kao umnožak $U\\Sigma$ ___.", "V^T"),
    ("Kod nelinearnog problema najmanjih kvadrata minimiziramo funkciju $F(a,b) = \\frac{1}{2}\\sum_{i=1}^m ($ ___ $)^2$.", "f(xi;a,b)-yi"),
    ("Pri izvođenju pogreške trapezne formule primjenjuje se teorem o ___ vrijednosti za integrale.", "srednjoj"),
]

# ---------------------------------------------------------------------------
# Flash kartice (25)
# ---------------------------------------------------------------------------
FLASHCARD = [
    ("Kako se definiraju signifikantne znamenke broja?",
     "Prvih $n$ znamenaka aproksimacije $a^*$ za koje vrijedi $\\Delta a^* \\le \\frac{1}{2}\\cdot 10^{m-n+1}$, gdje $m$ označava red potencije vodeće znamenke."),
    ("Kako se procjenjuje pogreška funkcije $f(x,y,z)$ zadane s pogreškama varijabli?",
     "Koristi se formula $\\Delta z^* \\approx |\\partial_x f|\\Delta x^* + |\\partial_y f|\\Delta y^* + |\\partial_z f|\\Delta z^*$, gdje se derivacije računaju u aproksimativnoj točki."),
    ("Koja je osnovna razlika između interpolacije i aproksimacije?",
     "Interpolacija traži funkciju koja točno prolazi kroz sve zadane čvorove, dok aproksimacija traži funkciju koja minimizira ukupno odstupanje na domeni."),
    ("Iskaži teorem o egzistenciji i jedinstvenosti interpolacijskog polinoma.",
     "Za zadane točke $(x_i,y_i)$, $i=0,\\dots,n$ s $a=x_0<x_1<\\dots<x_n=b$, postoji jedinstveni polinom $P_n$ stupnja $\\deg P_n \\le n$ takav da je $P_n(x_i)=y_i$."),
    ("Kako glasi Lagrangeov oblik interpolacijskog polinoma?",
     "$P_n(x) = \\sum_{i=0}^n y_i p_i(x)$, gdje je $p_i(x) = \\prod_{j\\ne i} \\frac{x-x_j}{x_i-x_j}$."),
    ("Kako se rekurzivno definira podijeljena razlika $k$-tog reda?",
     "$f[x_0,x_1,\\dots,x_k] = \\frac{f[x_1,\\dots,x_k]-f[x_0,\\dots,x_{k-1}]}{x_k-x_0}$."),
    ("Što je to spline?",
     "Funkcija sastavljena od polinoma nižeg stupnja definiranih po dijelovima na podintervalima radi smanjenja odstupanja u interpolaciji."),
    ("Koji su prirodni uvjeti za kubični interpolacijski spline?",
     "Zahtjev da su druge derivacije kubičnog splinea u prvom i zadnjem čvoru jednake nuli: $c''(x_0)=0$ i $c''(x_n)=0$."),
    ("Kako glasi ocjena pogreške linearnog splinea?",
     "$|f(x)-\\varphi_i(x)| \\le \\frac{M_2}{8}h_i^2$, gdje je $h_i=x_i-x_{i-1}$ i $M_2=\\max|f''(x)|$."),
    ("Kako se definira brzina konvergencije numeričke metode?",
     "Metoda ima brzinu konvergencije $r$ ako postoje $A,r>0$ takvi da za pogreške $e_n=x_n-\\xi$ vrijedi $|e_{n+1}| \\le A|e_n|^r$."),
    ("Kako glasi ocjena pogreške $n$-te aproksimacije za metodu bisekcije?",
     "$|\\xi - x_n| \\le \\frac{1}{2^n}(b_0-a_0)$."),
    ("Iskaži uvjete teorema o konvergenciji metode jednostavnih iteracija $x=\\varphi(x)$.",
     "Funkcija $\\varphi$ mora preslikavati $[a,b]$ u $[a,b]$ i postojati $q\\in\\langle 0,1\\rangle$ takav da je $|\\varphi'(x)| \\le q$ za sve $x\\in[a,b]$."),
    ("Kako glasi rekurzivna formula za Newtonovu metodu tangenti?",
     "$x_{n+1} = x_n - \\frac{f(x_n)}{f'(x_n)}$ za $n=0,1,2,\\dots$"),
    ("Koji je geometrijski smisao Newtonove metode tangenti?",
     "Sljedeća aproksimacija $x_{n+1}$ dobiva se kao sjecište tangente povučene na graf funkcije u točki $(x_n,f(x_n))$ s $x$-osi."),
    ("Kako se formulira opći linearni problem najmanjih kvadrata (LPNK)?",
     "Za zadanu matricu $J\\in\\mathbb{R}^{m\\times n}$ ($m\\gg n$) i vektor $y\\in\\mathbb{R}^m$, traži se $a\\in\\mathbb{R}^n$ koji minimizira euklidsku normu reziduala $\\|Ja-y\\|_2$."),
    ("Kako glasi sustav normalnih jednadžbi za LPNK?",
     "$(J^T J)a = J^T y$."),
    ("Kako glasi rješenje LPNK preko QR dekompozicije?",
     "Rješenje $a^*$ dobiva se iz gornjetrokutastog sustava $R_n a^* = Q_n^T y$."),
    ("Kako se definira Frobeniusova norma matrice $A\\in\\mathbb{R}^{n\\times n}$?",
     "$\\|A\\|_F = \\sqrt{\\sum_{i=1}^n \\sum_{j=1}^n a_{ij}^2}$."),
    ("Što označava kondicija matrice $\\text{cond}(A)$?",
     "Mjeru osjetljivosti rješenja linearnog sustava na male promjene u ulaznim podacima: $\\text{cond}(A) = \\|A\\| \\cdot \\|A^{-1}\\|$."),
    ("Kako glasi jednostavna trapezna formula i ocjena njezine pogreške?",
     "Integral $\\approx \\frac{f(a)+f(b)}{2}(b-a)$, a pogreška $|\\Delta I^*| \\le \\frac{(b-a)^3}{12}M_2$."),
    ("Kako glasi produljena trapezna formula za integraciju?",
     "$I^* = \\frac{h}{2}\\left[y_0 + 2\\sum_{i=1}^{n-1} y_i + y_n\\right]$, gdje je $h=\\frac{b-a}{n}$."),
    ("Kako glasi ocjena pogreške produljene trapezne formule?",
     "$|\\Delta I^*| \\le \\frac{b-a}{12}h^2 M_2$, gdje je $M_2=\\max|f''(x)|$ na $[a,b]$."),
    ("Kako se definiraju Newton-Cotesove formule?",
     "Formule numeričke integracije dobivene zamjenom integranda Lagrangeovim interpolacijskim polinomom na ekvidistantnoj mreži."),
    ("Kako glasi jednostavna Simpsonova formula za integraciju na $[a,b]$?",
     "$I^* \\approx \\frac{b-a}{6}\\left[f(a) + 4f\\left(\\frac{a+b}{2}\\right) + f(b)\\right]$."),
    ("Kako glasi produljena Simpsonova formula za paran $n=2m$?",
     "$I^* = \\frac{h}{3}\\left[y_0 + 4\\sum_{k=0}^{m-1} y_{2k+1} + 2\\sum_{k=1}^{m-1} y_{2k} + y_{2m}\\right]$."),
]

# ---------------------------------------------------------------------------
# Visestruki odabir (20)
# ---------------------------------------------------------------------------
MCQ = [
    ("Koju formulu koristimo za aproksimaciju pogreške funkcije jedne varijable $f(x)$ za zadanu pogrešku $\\Delta x^*$?",
     ["$\\Delta z^* \\approx |f''(x)|(\\Delta x^*)^2$", "$\\Delta z^* \\approx |f'(x)|\\Delta x^*$",
      "$\\Delta z^* \\approx f(x)/\\Delta x^*$", "$\\Delta z^* \\approx |f'(x)|/2$"], 1),
    ("Koja se matrica javlja u sustavu jednadžbi pri određivanju koeficijenata interpolacijskog polinoma?",
     ["Gramova matrica", "Vandermondeova matrica", "Jacobijeva matrica", "Eulerova matrica"], 1),
    ("Za $n+1$ zadanih čvorova, stupanj interpolacijskog polinoma je:",
     ["Točno $n+1$", "Najviše $n$", "Najmanje $n+1$", "Uvijek $2$"], 1),
    ("Koliko dodatnih prirodnih uvjeta je potrebno postaviti za određivanje kubičnog splinea?",
     ["$1$", "$2$", "$4$", "$2n$"], 1),
    ("Koja je brzina konvergencije Newtonove metode tangenti?",
     ["Linearna ($r=1$)", "Kvadratna ($r=2$)", "Kubična ($r=3$)", "Eksponencijalna"], 1),
    ("U metodi bisekcije na intervalu $[a_0,b_0]$, pogreška $n$-te aproksimacije omeđena je s:",
     ["$(b_0-a_0)/n$", "$(b_0-a_0)/2^n$", "$(b_0-a_0)^2/2$", "$1/(2\\cdot n!)$"], 1),
    ("Koji je dovoljan uvjet za konvergenciju metode jednostavnih iteracija $x=\\varphi(x)$?",
     ["$|\\varphi'(x)| \\ge 1$", "$|\\varphi'(x)| \\le q < 1$", "$\\varphi''(x)=0$", "$\\varphi(x)>0$"], 1),
    ("U Newtonovoj metodi tangenti, uvjet za izbor početne aproksimacije $x_0$ glasi:",
     ["$f(x_0)\\cdot f'(x_0) < 0$", "$f(x_0)\\cdot f''(x_0) > 0$", "$f'(x_0)=0$", "$f''(x_0)<0$"], 1),
    ("Sustav normalnih jednadžbi u problemu najmanjih kvadrata za matricu $J$ glasi:",
     ["$Ja=y$", "$(J^T J)a = J^T y$", "$J^T a = y$", "$(JJ^T)a=y$"], 1),
    ("Koja se dekompozicija matrice koristi u LPNK za svođenje na gornjetrokutasti sustav?",
     ["LU dekompozicija", "QR dekompozicija", "Choleskyjeva dekompozicija", "Spektralna dekompozicija"], 1),
    ("Kako se definira euklidska kondicija matrice $\\text{cond}_2(A)$?",
     ["$\\det(A)$", "$\\sigma_{max}/\\sigma_{min}$", "$\\text{tr}(A)$", "$\\|A\\|_F^2$"], 1),
    ("Ako je $\\text{cond}(A) \\approx 1$, za linearni sustav kažemo da je:",
     ["Loše uvjetovan", "Dobro uvjetovan", "Singularan", "Neriješiv"], 1),
    ("Pogreška jednostavne trapezne formule pri integraciji na segmentu $[a,b]$ omeđena je s:",
     ["$\\frac{(b-a)^2}{2}M_1$", "$\\frac{(b-a)^3}{12}M_2$", "$\\frac{b-a}{6}M_2$", "$(b-a)^4 M_3$"], 1),
    ("U produljenoj trapeznoj formuli s $n$ podintervala, pogreška je proporcionalna s:",
     ["$h$", "$h^2$", "$h^3$", "$1/h$"], 1),
    ("Simpsonova formula numeričke integracije dobiva se interpolacijom integranda polinomom kojeg stupnja?",
     ["$1$", "$2$", "$3$", "$4$"], 1),
    ("Broj podintervala $n$ u produljenoj Simpsonovoj formuli mora biti:",
     ["Neparan", "Paran ($n=2m$)", "Prost broj", "Bilo koji cijeli broj"], 1),
    ("Faktor ispred zagrade u produljenoj Simpsonovoj formuli iznosi:",
     ["$h/2$", "$h/3$", "$h/6$", "$2h/3$"], 1),
    ("Kojom se normom u LPNK minimizira duljina vektora reziduala?",
     ["1-normom", "2-normom (euklidskom normom)", "Beskonačnom normom", "Frobeniusovom normom"], 1),
    ("Newtonov interpolacijski polinom za interpolaciju koristi:",
     ["Podijeljene razlike", "Potencije matrice $J$", "Trigonometrijske funkcije", "Eksponencijalne funkcije"], 0),
    ("Koja od navedenih metoda rješavanja nelinearnih jednadžbi ima najsporiju (linearnu) konvergenciju?",
     ["Newtonova metoda tangenti", "Metoda bisekcije", "Metoda sečice", "Halleyjeva metoda"], 1),
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