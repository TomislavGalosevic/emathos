"""Jednokratni uvoz teorije za kolegij 'Vektorski prostori'."""

from .database import SessionLocal
from . import models

COURSE_NAME = "Vektorski prostori"

# ---------------------------------------------------------------------------
# Tocno / Netocno (50)
# ---------------------------------------------------------------------------
TRUEFALSE = [
    ("Uređeni par $(G, +)$ nepraznog skupa $G$ i binarne operacije $+$ je grupa ako zadovoljava svojstva asocijativnosti, postojanja neutralnog i postojanja inverznog elementa.", True),
    ("Grupa $(G, +)$ je Abelova ako za sve $a, b \\in G$ vrijedi $a + b = b + a$.", True),
    ("U definiciji polja $K$, struktura $(K, \\cdot)$ sa svim svojim elementima mora tvoriti Abelovu grupu.", False),
    ("Skup cijelih brojeva s operacijom oduzimanja $(Z, -)$ tvori Abelovu grupu.", False),
    ("Trojka $(V, +, \\cdot)$ je vektorski prostor nad poljem $K$ ako je $(V, +)$ Abelova grupa i vrijede distributivna, kvaziasocijativna i skalarna svojstva.", True),
    ("U vektorskom prostoru $V$ nad poljem $K$, za svaki vektor $a \\in V$ i neutralni element $1 \\in K$ vrijedi $1 \\cdot a = a$.", True),
    ("Svaki podskup $W \\subseteq V$ vektorskog prostora $V$ ujedno je i njegov potprostor $W \\le V$.", False),
    ("Kriterij potprostora glasi: neprazan $W \\subseteq V$ je potprostor akko za sve $\\lambda, \\mu \\in K$ i $a, b \\in W$ vrijedi $\\lambda a + \\mu b \\in W$.", True),
    ("Linearna ljuska $[S]$ definira se kao unija svih potprostora koji sadrže skup $S$.", False),
    ("Linearna ljuska $[S]$ jednaka je skupu svih konačnih linearnih kombinacija vektora iz skupa $S$.", True),
    ("Ako je $[S] = W$, kažemo da skup $S$ razapinje potprostor $W$.", True),
    ("Skup $S$ je linearno nezavisan ako se nul-vektor može prikazati kao netrivijalna linearna kombinacija elemenata iz $S$.", False),
    ("Skup $S$ je linearno nezavisan ako i samo ako niti jedan vektor iz $S$ nije linearna kombinacija ostalih vektora iz $S$.", True),
    ("Baza vektorskog prostora $V$ je bilo koji skup koji razapinje prostor $V$.", False),
    ("Vektorski prostor $V$ je konačnodimenzionalan ako postoji konačan podskup $S \\subseteq V$ koji ga razapinje.", True),
    ("Bilo koje dvije baze konačnodimenzionalnog vektorskog prostora $V$ imaju jednak broj elemenata.", True),
    ("Dimenzija sume potprostora izračunava se po formuli $\\dim(U+W) = \\dim U + \\dim W + \\dim(U \\cap W)$.", False),
    ("Suma potprostora $U + W$ je direktna ako i samo ako je njihov presjek prazan skup $\\emptyset$.", False),
    ("Suma $U + W$ je direktna ako i samo ako se svaki vektor $v \\in U+W$ jedinstveno prikazuje u obliku $v = u + w$ ($u \\in U, w \\in W$).", True),
    ("Potprostor $W \\le V$ je direktan komplement potprostora $U \\le V$ ako je $V = U + W$ direktna suma.", True),
    ("Kvocijentni prostor $V/W$ sastoji se od klasa ekvivalencije $[x] = x + W$ i njegova dimenzija iznosi $\\dim V / \\dim W$.", False),
    ("Operator $A: V \\to W$ je aditivan ako za sve $v_1, v_2 \\in V$ vrijedi $A(v_1 + v_2) = A v_1 + A v_2$.", True),
    ("Operator $A: V \\to W$ je homogen ako za sve $\\lambda \\in K$ i $v \\in V$ vrijedi $A(\\lambda v) = \\lambda A v$.", True),
    ("Skup svih linearnih operatora $L(V, W)$ je vektorski prostor dimenzije $\\dim V + \\dim W$.", False),
    ("Slika operatora $\\text{Im}\\,A$ je potprostor domene $V$.", False),
    ("Rang operatora $r(A)$ definira se kao dimenzija slike $\\text{Im}\\,A$, a defekt $d(A)$ kao dimenzija jezgre $\\text{Ker}\\,A$.", True),
    ("Injektivan linearni operator naziva se epimorfizam.", False),
    ("Dva vektorska prostora nad istim poljem su izomorfna ako i samo ako imaju jednake dimenzije.", True),
    ("Slične matrice $A$ i $B$ zadovoljavaju relaciju $A = T^{-1} B T$ za neku regularnu matricu $T$.", True),
    ("Slične matrice imaju jednaku determinantu i jednaki trag.", True),
    ("Dualni prostor $V'$ je prostor svih linearnih funkcionala s $V$ u $K$ i vrijedi $\\dim V' = \\dim V$.", True),
    ("Za bazu $e = \\{e_1, \\dots, e_n\\}$ prostora $V$, dualna baza $e'$ definira se sa $e'_j(e_i) = 1$ za $i \\ne j$ i $0$ za $i = j$.", False),
    ("Anhilator skupa $S \\subseteq V$ je potprostor dualnog prostora $V'$.", True),
    ("Za potprostor $W \\le V$ vrijedi formula $\\dim W^\\circ = \\dim V - \\dim W$.", True),
    ("Minimalni polinom $\\mu_A(\\lambda)$ je bilo koji polinom s vodećim koeficijentom $1$ za koji vrijedi $\\mu_A(A) = 0$.", False),
    ("Operator $A \\in L(V)$ je invertibilan ako i samo ako je $\\mu_A(0) \\ne 0$.", True),
    ("Spektar operatora $\\sigma(A)$ predstavlja skup svih svojstvenih vektora operatora $A$.", False),
    ("Minimalni polinom $\\mu_A$ dijeli karakteristični polinom $k_A$.", True),
    ("Svojstveni potprostor $V_\\lambda = \\{v \\in V : A v = \\lambda v\\}$ je $A$-invarijantan potprostor.", True),
    ("Linearni operator $P \\in L(V)$ je projektor ako i samo ako vrijedi $P^2 = P$.", True),
    ("Operator $A$ je nilpotentan ako postoji $k \\in \\mathbb{N}$ takav da je $A^k = I$.", False),
    ("Indeks nilpotentnosti je broj $k \\in \\mathbb{N}$ takav da je $A^k = 0$ i $A^{k-1} \\ne 0$.", True),
    ("Elementarna Jordanova klijetka ima jedinice na glavnoj dijagonali i nule drugdje.", False),
    ("U Fittingovoj dekompoziciji $V = V^0(A) + V^1(A)$, restrikcija operatora $A$ na $V^0(A)$ je nilpotentna, a na $V^1(A)$ regularna.", True),
    ("Svaka funkcija operatora $f(A)$ jednaka je nekom polinomu u operatoru $A$.", True),
    ("Skalarni produkt je po definiciji linearan u obje varijable nad poljem $\\mathbb{C}$.", False),
    ("Za svaki vektor $u$ u unitarnom prostoru vrijedi $(u|u) \\ge 0$, pri čemu je $(u|u) = 0$ ako i samo ako je $u = 0$.", True),
    ("Skup vektora $S$ u unitarnom prostoru je ortonormiran ako su svaka dva različita vektora ortogonalna i norma svakog vektora iznosi $1$.", True),
    ("Skup vektora je linearno nezavisan ako i samo ako je njegova Gramova determinanta jednaka $0$.", False),
    ("Operator $A^*$ je adjungirani operator operatora $A$ ako za sve $x, y$ vrijedi $(Ax|y) = (x|A^* y)$.", True),
]

# ---------------------------------------------------------------------------
# Nadopuni recenicu (50) - odgovor je OBICAN TEKST (usporeduje se doslovno)
# ---------------------------------------------------------------------------
FILLIN = [
    ("Uređeni par $(G, +)$ nepraznog skupa $G$ i binarne operacije $+$ u kojem vrijedi asocijativnost, postojanje neutralnog i inverznog elementa naziva se ___.", "grupa"),
    ("Ako je operacija u grupi komutativna, grupa se naziva ___ grupa.", "Abelova"),
    ("U polju $K$, skup $\\{K \\setminus \\{0\\}, \\cdot\\}$ mora tvoriti ___ grupu s neutralnim elementom 1.", "Abelovu"),
    ("Povezanost zbrajanja i množenja u polju osigurana je svojstvom ___ množenja prema zbrajanju.", "distributivnosti"),
    ("Uređena trojka $(V, +, \\cdot)$ nad poljem $K$ naziva se ___ prostor.", "vektorski"),
    ("Neutralni element za zbrajanje u vektorskom prostoru naziva se ___-vektor.", "nul"),
    ("Neprazan podskup $W \\subseteq V$ koji je i sam vektorski prostor s obzirom na iste operacije naziva se ___ od $V$.", "potprostor"),
    ("Kriterij potprostora zahtijeva da za sve skalare $\\lambda, \\mu \\in K$ i vektore $a, b \\in W$ vrijedi $\\lambda a + \\mu b \\in$ ___.", "W"),
    ("Izraz $\\lambda_1 v_1 + \\dots + \\lambda_n v_n$ naziva se ___ kombinacija vektora $v_1, \\dots, v_n$.", "linearna"),
    ("Presjek svih potprostora od $V$ koji sadrže skup $S$ naziva se ___ ljuska skupa $S$.", "linearna"),
    ("Linearna ljuska $[S]$ predstavlja skup svih ___ linearnih kombinacija vektora iz $S$.", "konacnih"),
    ("Ako za skup $S$ vrijedi $[S] = W$, kažemo da skup $S$ ___ potprostor $W$.", "razapinje"),
    ("Skup $S$ je linearno ___ ako niti jedan njegov vektor nije linearna kombinacija ostalih.", "nezavisan"),
    ("Iz jednakosti $\\lambda_1 x_1 + \\dots + \\lambda_n x_n = 0$ za linearno nezavisan skup slijedi da su svi skalari jednaki ___.", "0"),
    ("Podskup $B \\subseteq V$ koji je linearno nezavisan i razapinje prostor $V$ naziva se ___ prostora $V$.", "baza"),
    ("Vektorski prostor je konačnodimenzionalan ako postoji ___ podskup koji ga razapinje.", "konacan"),
    ("Broj elemenata proizvoljne baze konačnodimenzionalnog vektorskog prostora zove se ___ prostora.", "dimenzija"),
    ("Za potprostore $U, W \\le V$, skup $\\{u + w : u \\in U, w \\in W\\}$ predstavlja ___ potprostora $U$ i $W$.", "sumu"),
    ("Dimenzija sume izračunava se formulom $\\dim(U+W) = \\dim U + \\dim W -$ ___.", "dim(U presjek W)"),
    ("Suma potprostora $U + W$ je direktna ako je $U \\cap W =$ ___.", "{0}"),
    ("Ako je $V = U \\dot{+} W$, potprostor $W$ naziva se direktan ___ potprostora $U$ u $V$.", "komplement"),
    ("Skup svih klasa $[x] = x + W$ uz odgovarajuće operacije čini ___ prostor $V/W$.", "kvocijentni"),
    ("Dimenzija kvocijentnog prostora izračunava se po formuli $\\dim(V/W) = \\dim V -$ ___.", "dim(W)"),
    ("Operator $A: V \\to W$ je ___ ako vrijedi $A(v_1 + v_2) = A v_1 + A v_2$.", "aditivan"),
    ("Operator je ___ ako je istovremeno aditivan i homogen.", "linearan"),
    ("Skup svih linearnih operatora s $V$ u $W$ označava se sa ___.", "L(V,W)"),
    ("Dimenzija prostora $L(V, W)$ jednaka je umnošku $\\dim V \\cdot$ ___.", "dim(W)"),
    ("Skup $\\text{Im}\\,A = \\{A v : v \\in V\\}$ naziva se ___ operatora $A$.", "slika"),
    ("Skup $\\text{Ker}\\,A = \\{v \\in V : A v = 0\\}$ naziva se ___ operatora $A$.", "jezgra"),
    ("Dimenzija slike operatora $r(A) = \\dim(\\text{Im}\\,A)$ zove se ___ operatora.", "rang"),
    ("Dimenzija jezgre operatora $d(A) = \\dim(\\text{Ker}\\,A)$ zove se ___ operatora.", "defekt"),
    ("Linearan operator koji je injekcija zove se ___.", "monomorfizam"),
    ("Linearan operator koji je bijekcija zove se ___.", "izomorfizam"),
    ("Dva prostora su izomorfna ako i samo ako imaju jednake ___.", "dimenzije"),
    ("Regularan operator $A \\in L(V)$ je operator koji je ___.", "invertibilan"),
    ("Matrice $A$ i $B$ su slične ako postoji regularna matrica $T$ takva da je $A =$ ___.", "T^-1*B*T"),
    ("Vektorski prostor $L(V, K)$ naziva se ___ prostor prostora $V$ i označava s $V'$.", "dualni"),
    ("Element dualnog prostora $f: V \\to K$ naziva se linearni ___.", "funkcional"),
    ("Za podskup $S \\subseteq V$, skup $S^\\circ = \\{f \\in V' : f(v) = 0, \\forall v \\in S\\}$ zove se ___ skupa $S$.", "anhilator"),
    ("Za potprostor $W \\le V$ vrijedi $\\dim W^\\circ = \\dim V -$ ___.", "dim(W)"),
    ("Normirani polinom najnižeg stupnja koji poništava operator $A$ naziva se ___ polinom.", "minimalni"),
    ("Operator $A$ je invertibilan ako i samo ako je $\\mu_A(0) \\ne$ ___.", "0"),
    ("Skup svih svojstvenih vrijednosti operatora $A$ zove se ___ operatora $A$.", "spektar"),
    ("Polinom $k_A(\\lambda) = \\det(\\lambda I - A)$ naziva se ___ polinom.", "karakteristicni"),
    ("Operator $P \\in L(V)$ je projektor ako i samo ako vrijedi $P^2 =$ ___.", "P"),
    ("Operator $A$ je nilpotentan ako postoji $k \\in \\mathbb{N}$ takav da je $A^k =$ ___.", "0"),
    ("Rastav $V = \\text{Ker}\\,A^k \\dot{+} \\text{Im}\\,A^k$ zove se ___ dekompozicija prostora $V$.", "Fittingova"),
    ("Vektorski prostor na kojem je zadan skalarni produkt naziva se ___ prostor.", "unitaran"),
    ("Preslikavanje $\\|u\\| = \\sqrt{(u|u)}$ naziva se ___ vektora $u$.", "norma"),
    ("Za operator $A^*$ u unitarnom prostoru koji zadovoljava $(Ax|y) = (x|A^* y)$ kažemo da je ___ operator operatora $A$.", "adjungirani"),
]

# ---------------------------------------------------------------------------
# Flash kartice (25)
# ---------------------------------------------------------------------------
FLASHCARD = [
    ("Definirajte pojam grupe.",
     "Uređeni par $(G, +)$ nepraznog skupa $G$ i binarne operacije $+$ koji zadovoljava: (1) asocijativnost, (2) postojanje neutralnog elementa $e$, (3) postojanje inverznog elementa za svaki $a \\in G$."),
    ("Što je polje $K$?",
     "Neprazan skup $K$ s operacijama $+$ i $\\cdot$ gdje je $(K, +)$ Abelova grupa s neutralom $0$, $\\{K \\setminus \\{0\\}, \\cdot\\}$ Abelova grupa s neutralom $1$, te vrijedi distributivnost množenja prema zbrajanju."),
    ("Iskažite kriterij potprostora.",
     "Neprazan podskup $W \\subseteq V$ je potprostor od $V$ ($W \\le V$) ako i samo ako za sve $\\lambda, \\mu \\in K$ i sve $a, b \\in W$ vrijedi $\\lambda a + \\mu b \\in W$."),
    ("Što je linearna ljuska $[S]$?",
     "Presjek svih potprostora od $V$ koji sadrže $S$ (najmanji potprostor koji sadrži $S$), a jednak je skupu svih konačnih linearnih kombinacija vektora iz $S$."),
    ("Koji je kriterij za linearnu nezavisnost skupa $S$?",
     "Skup $S$ je linearno nezavisan akko iz $\\lambda_1 x_1 + \\dots + \\lambda_n x_n = 0$ (za različite $x_i \\in S$) slijedi da je $\\lambda_1 = \\dots = \\lambda_n = 0$."),
    ("Definirajte bazu vektorskog prostora.",
     "Podskup $B \\subseteq V$ koji je: (1) linearno nezavisan, (2) razapinje prostor $V$ (tj. $[B] = V$)."),
    ("Koja je formula za dimenziju sume potprostora?",
     "Za konačnodimenzionalne potprostore $U, W \\le V$ vrijedi: $\\dim(U+W) = \\dim U + \\dim W - \\dim(U \\cap W)$."),
    ("Kada je suma potprostora $U + W$ direktna suma?",
     "Kada je $U \\cap W = \\{0\\}$. Tada pišemo $U \\dot{+} W$, a svaki $v \\in U \\dot{+} W$ jedinstveno se prikazuje kao $v = u + w$."),
    ("Što je kvocijentni prostor $V/W$ i kolika mu je dimenzija?",
     "Skup klasa ekvivalencije $[x] = x + W$ uz operacije zbrajanja klasa i množenja skalarom. Vrijedi $\\dim(V/W) = \\dim V - \\dim W$."),
    ("Iskažite kriterij linearnosti operatora $A: V \\to W$.",
     "Operator $A$ je linearan akko je aditivan i homogen, tj. akko za sve $\\lambda_1, \\lambda_2 \\in K$ i $v_1, v_2 \\in V$ vrijedi $A(\\lambda_1 v_1 + \\lambda_2 v_2) = \\lambda_1 A v_1 + \\lambda_2 A v_2$."),
    ("Kolika je dimenzija prostora operatora $L(V, W)$?",
     "$\\dim L(V, W) = \\dim V \\cdot \\dim W$."),
    ("Definirajte sliku, jezgru, rang i defekt operatora.",
     "$\\text{Im}\\,A = \\{Av : v \\in V\\} \\le W$, $\\text{Ker}\\,A = \\{v \\in V : Av = 0\\} \\le V$. Rang je $r(A) = \\dim(\\text{Im}\\,A)$, a defekt $d(A) = \\dim(\\text{Ker}\\,A)$."),
    ("Kada su dva vektorska prostora izomorfna ($V \\cong W$)?",
     "Ako postoji izomorfizam (bijektivni linearan operator) $A: V \\to W$. To vrijedi akko je $\\dim V = \\dim W$."),
    ("Što su slične matrice i koje im je svojstvo?",
     "Matrice $A$ i $B$ za koje postoji regularna matrica $T$ t.d. $A = T^{-1} B T$. Slične matrice imaju jednaku determinantu i trag."),
    ("Definirajte dualni prostor $V'$ i dualnu bazu.",
     "Dualni prostor je $V' = L(V, K)$. Dualna baza $e' = \\{e'_1, \\dots, e'_n\\}$ baze $e$ definirana je s $e'_j(e_i) = 1$ za $i=j$, te $0$ za $i \\ne j$."),
    ("Što je anhilator skupa $S \\subseteq V$ i kolika je dimenzija za potprostor $W$?",
     "$S^\\circ = \\{f \\in V' : f(v) = 0, \\forall v \\in S\\} \\le V'$. Za potprostor $W \\le V$ vrijedi $\\dim W^\\circ = \\dim V - \\dim W$."),
    ("Definirajte minimalni polinom $\\mu_A(\\lambda)$.",
     "Normirani polinom najnižeg stupnja koji poništava operator $A$ ($\\mu_A(A) = 0$). Polinom $P$ poništava $A$ akko $\\mu_A$ dijeli $P$."),
    ("Koji je uvjet invertibilnosti operatora preko minimalnog polinoma?",
     "Operator $A \\in L(V)$ je invertibilan (regularan) ako i samo ako je $\\mu_A(0) \\ne 0$."),
    ("Što je spektar operatora $\\sigma(A)$?",
     "Skup svih svojstvenih vrijednosti operatora $A$. Jednak je skupu nultočaka minimalnog polinoma $\\mu_A$."),
    ("Što je projektor i koje je njegovo glavno svojstvo?",
     "Operator $P: V \\to V$ koji preslikava $v = x + y \\mapsto x$ za $V = X \\dot{+} Y$. Operator $P \\in L(V)$ je projektor akko je $P^2 = P$."),
    ("Definirajte nilpotentan operator i indeks nilpotentnosti.",
     "$A$ je nilpotentan ako postoji $k \\in \\mathbb{N}$ t.d. $A^k = 0$. Najmanji takav $k$ za koji je $A^{k-1} \\ne 0$ naziva se indeks nilpotentnosti."),
    ("Iskažite Fittingovu dekompoziciju prostora.",
     "Za nilindeks $k = \\nu(A)$, $V = \\text{Ker}\\,A^k \\dot{+} \\text{Im}\\,A^k = V^0(A) \\dot{+} V^1(A)$. Restrikcija $A$ na $V^0(A)$ je nilpotentna, a na $V^1(A)$ regularna."),
    ("Koja svojstva mora imati skalarni produkt?",
     "(1) Pozitivnost: $(v|v) \\ge 0$, (2) Definitnost: $(v|v) = 0 \\iff v=0$, (3) Linearnost u 1. varijabli, (4) Hermitska simetrija: $(x|y) = \\overline{(y|x)}$."),
    ("Kada su vektori linearno nezavisni preko Gramove matrice?",
     "Vektori $x_1, \\dots, x_n$ su linearno nezavisni akko je Gramova determinanta $\\Gamma(x_1, \\dots, x_n) \\ne 0$ (tj. Gramova matrica je regularna)."),
    ("Definirajte hermitski, unitaran i normalan operator.",
     "Hermitski: $A^* = A$; Unitaran: $A A^* = A^* A = I$ ($A^* = A^{-1}$); Normalan: $A A^* = A^* A$."),
]

# ---------------------------------------------------------------------------
# Visestruki odabir (20)
# ---------------------------------------------------------------------------
MCQ = [
    ("Uređeni par $(G, +)$ je grupa ako zadovoljava svojstva:",
     ["Asocijativnost, komutativnost i neutralni element", "Asocijativnost, neutralni element i inverzni element",
      "Komutativnost, distributivnost i inverzni element", "Homogenost, aditivnost i neutralni element"], 1),
    ("Koja od sljedećih tvrdnji je TOČNA za polje $K$?",
     ["$(K, \\cdot)$ je uvijek Abelova grupa", "$(K \\setminus \\{0\\}, \\cdot)$ je Abelova grupa",
      "Množenje ne mora biti distributivno prema zbrajanju", "Polje ima samo jednu binarnu operaciju"], 1),
    ("Neprazan podskup $W \\subseteq V$ je potprostor od $V$ akko za sve $\\lambda, \\mu \\in K$ i $a, b \\in W$ vrijedi:",
     ["$\\lambda a \\in W$", "$a + b \\in W$", "$\\lambda a + \\mu b \\in W$", "$\\lambda \\mu (a+b) \\in W$"], 2),
    ("Linearna ljuska $[S]$ skupa $S \\subseteq V$ je:",
     ["Najveći potprostor koji ne sadrži $S$", "Unija svih potprostora koji sadrže $S$",
      "Presjek svih potprostora koji sadrže $S$", "Bilo koji potprostor prostora $V$"], 2),
    ("Skup $S$ je linearno nezavisan ako iz $\\lambda_1 x_1 + \\dots + \\lambda_n x_n = 0$ slijedi:",
     ["Barem jedan skalar $\\lambda_i \\ne 0$", "Svi skalari $\\lambda_1 = \\dots = \\lambda_n = 0$",
      "$\\sum \\lambda_i = 1$", "Svi vektori $x_i = 0$"], 1),
    ("Ako su $U$ i $W$ konačnodimenzionalni potprostori od $V$, tada je $\\dim(U+W)$ jednaka:",
     ["$\\dim U + \\dim W$", "$\\dim U + \\dim W - \\dim(U \\cap W)$", "$\\dim U \\cdot \\dim W$",
      "$\\dim U - \\dim W + \\dim(U \\cap W)$"], 1),
    ("Suma potprostora $U + W$ je direktna ako i samo ako vrijedi:",
     ["$U \\cap W = \\emptyset$", "$U \\cap W = \\{0\\}$", "$U \\cup W = V$", "$\\dim U = \\dim W$"], 1),
    ("Dimenzija kvocijentnog prostora $V/W$ iznosi:",
     ["$\\dim V \\cdot \\dim W$", "$\\dim V / \\dim W$", "$\\dim V - \\dim W$", "$\\dim V + \\dim W$"], 2),
    ("Dimenzija prostora svih linearnih operatora $L(V, W)$ iznosi:",
     ["$\\dim V + \\dim W$", "$\\dim V \\cdot \\dim W$", "$(\\dim V)^{\\dim W}$", "$\\dim V - \\dim W$"], 1),
    ("Injektivan linearni operator zove se:",
     ["Epimorfizam", "Monomorfizam", "Izomorfizam", "Endomorfizam"], 1),
    ("Vektorski prostori $V$ i $W$ nad istim poljem $K$ su izomorfni ako i samo ako:",
     ["Sadrže iste vektore", "Imaju jednake dimenzije", "Su oba potprostori od $\\mathbb{R}^n$", "Su im jezgre jednake $\\{0\\}$"], 1),
    ("Ako su matrice $A$ i $B$ slične, tada one obavezno imaju:",
     ["Jednake sve elemente na dijagonali", "Jednaku determinantu i trag", "Jednake inverzne matrice", "Ortogonalne stupce"], 1),
    ("Dimenzija dualnog prostora $V' = L(V, K)$ jednaka je:",
     ["$1$", "$\\dim V$", "$(\\dim V)^2$", "$0$"], 1),
    ("Za potprostor $W \\le V$, dimenzija anhilatora $W^\\circ \\le V'$ iznosi:",
     ["$\\dim W$", "$\\dim V - \\dim W$", "$\\dim V + \\dim W$", "$\\dim V \\cdot \\dim W$"], 1),
    ("Minimalni polinom $\\mu_A(\\lambda)$ operatora $A$ definiše se kao:",
     ["Bilo koji polinom koji poništava $A$", "Normirani polinom najvišeg stupnja koji poništava $A$",
      "Normirani polinom najnižeg stupnja koji poništava $A$", "Polinom $\\det(\\lambda I - A)$"], 2),
    ("Operator $A \\in L(V)$ je invertibilan (regularan) ako i samo ako za njegov minimalni polinom $\\mu_A$ vrijedi:",
     ["$\\mu_A(0) = 0$", "$\\mu_A(0) \\ne 0$", "$\\deg \\mu_A = 1$", "$\\mu_A(1) = 0$"], 1),
    ("Linearni operator $P \\in L(V)$ je projektor ako i samo ako zadovoljava uvjet:",
     ["$P^* = P$", "$P^2 = P$", "$P^k = 0$", "$P P^* = I$"], 1),
    ("Najmanji broj $k \\in \\mathbb{N}$ za koji je $\\text{Ker}\\,A^k = \\text{Ker}\\,A^{k+1}$ naziva se:",
     ["Indeks nilpotentnosti", "Nilindeks operatora $A$", "Rang operatora $A$", "Dimenzija jezgre"], 1),
    ("Vektori $x_1, \\dots, x_n$ u unitarnom prostoru su linearno nezavisni ako i samo ako je njihova Gramova determinanta $\\Gamma(x_1, \\dots, x_n)$:",
     ["Jednaka $0$", "Različita od $0$", "Manja od $0$", "Jednaka $1$"], 1),
    ("Operator $A$ u unitarnom prostoru je unitaran ako zadovoljava uvjet:",
     ["$A^* = A$", "$A^* = -A$", "$A A^* = A^* A = I$", "$A^2 = I$"], 2),
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