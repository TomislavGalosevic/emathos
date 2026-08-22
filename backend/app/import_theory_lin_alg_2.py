"""Jednokratni uvoz teorije za kolegij 'Linearna algebra II'.

Pokretanje (iz mape backend/, s aktiviranim venv):
    python -m app.import_theory_lin_alg_2

Skripta NIJE idempotentna - ako je pokrenes dvaput, dobit ces duplikate.
"""

from .database import SessionLocal
from . import models

COURSE_NAME = "Linearna algebra II"

# ---------------------------------------------------------------------------
# Tocno / Netocno (50)
# ---------------------------------------------------------------------------
TRUEFALSE = [
    ("Binarna operacija na skupu $G$ pridružuje svakom paru elemenata iz $G \\times G$ jedinstveni element iz skupa $G$, pod uvjetom da je $G$ neprazan skup.", True),
    ("Skup prirodnih brojeva s operacijom oduzimanja $(N, -)$ tvori grupu.", False),
    ("Uređeni par $(G, +)$ je grupa ako zadovoljava svojstva asocijativnosti, te postojanja neutralnog i inverznog elementa.", True),
    ("Skup racionalnih brojeva s operacijom množenja $(Q, \\cdot)$ je grupa.", False),
    ("Uređena trojka $(F, +, \\cdot)$ je polje ako je $(F, +)$ Abelova grupa i $(F, \\cdot)$ Abelova grupa te vrijedi distributivnost.", False),
    ("Distributivnost množenja prema zbrajanju obavezno je svojstvo svake strukture polja.", True),
    ("Skup cijelih brojeva uz zbrajanje $(Z, +)$ primjer je Abelove grupe.", True),
    ("U definiciji vektorskog prostora $V$ nad poljem $F$, operacija množenja skalarom uzima dva elementa iz $V$ i daje skalar iz $F$.", False),
    ("Za neutralni element $1 \\in F$ i svaki vektor $a \\in V$ u vektorskom prostoru vrijedi $1 \\cdot a = a$.", True),
    ("U vektorskom prostoru $V$, trojka $(V, +, \\cdot)$ je po sebi polje.", False),
    ("Vektor $a = \\alpha_1 a_1 + \\alpha_2 a_2 + \\dots + \\alpha_n a_n$ naziva se linearna kombinacija vektora $a_i$ uz skalare $\\alpha_i$.", True),
    ("Skup vektora $S = \\{a_1, \\dots, a_n\\}$ je linearno nezavisan ako u njihovoj linearnoj kombinaciji koja daje nul-vektor postoji barem jedan skalar jednak nuli.", False),
    ("Skup vektora je linearno zavisan ako linearna kombinacija iščezava na netrivijalan način (postoji $\\alpha_i \\ne 0$).", True),
    ("Linearna ljuska $[S]$ skupa $S$ definiše se kao skup svih mogućih beskonačnih suma vektora iz $S$.", False),
    ("Podskup $S \\subseteq V$ je sustav izvodnica za $V$ ako i samo ako je njegova linearna ljuska jednaka čitavom prostoru $V$, tj. $[S] = V$.", True),
    ("Svaki sustav izvodnica za vektorski prostor $V$ ujedno je i baza tog prostora.", False),
    ("Baza je konačan skup koji je linearno nezavisan sustav izvodnica za $V$.", True),
    ("Svaki vektor $v \\in V$ može se prikazati kao linearna kombinacija elemenata baze $B$.", True),
    ("Ako vektorski prostor $V \\ne \\{0\\}$ ima jednu bazu s $n$ elemenata, on može imati i drugu bazu s $m$ elemenata gdje je $n \\ne m$.", False),
    ("Dimenzija nul-vektorskog prostora $\\{0\\}$ iznosi $1$.", False),
    ("Ako je $M$ vektorski potprostor od $V$, tada $M$ mora biti vektorski prostor nad istim poljem $F$ i uz iste operacije kao $V$.", True),
    ("Svaki vektorski potprostor $M \\le V$ obavezno sadrži nul-vektor.", True),
    ("Suma potprostora $L$ i $M$ definiše se kao njihov presjek $L \\cap M$.", False),
    ("Za sumu potprostora $L + M$ kažemo da je direktna ako je $L \\cap M = \\{0\\}$.", True),
    ("Potprostor $M$ je direktan komplement potprostora $L$ ako vrijedi $L + M = V$ i pritom je $L \\cap M = \\emptyset$.", False),
    ("Preslikavanje $A: V \\to W$ je linearan operator ako zadovoljava $A(\\alpha x + \\beta y) = \\alpha A(x) + \\beta A(y)$.", True),
    ("Slika operatora $\\text{Im}\\,A$ je vektorski potprostor domene $V$.", False),
    ("Jezgra operatora $\\text{Ker}\\,A$ definira se kao skup $A^{-1}(\\{0\\}) = \\{x \\in V : A x = 0\\}$.", True),
    ("Jezgra operatora $\\text{Ker}\\,A$ je vektorski potprostor kodomene $W$.", False),
    ("Rang operatora $r(A)$ predstavlja dimenziju jezgre $\\text{Ker}\\,A$.", False),
    ("Defekt operatora $d(A)$ definiše se kao $d(A) = \\dim(\\text{Ker}\\,A)$.", True),
    ("Prema Teoremu o rangu i defektu vrijedi $r(A) + d(A) = \\dim W$ za operator $A: V \\to W$.", False),
    ("Skup svih linearnih operatora $L(V, W)$ tvori vektorski prostor nad poljem $F$ uz operacije zbrajanja operatora i množenja skalarom.", True),
    ("Matrica $B$ je slična matrici $A$ ako postoji bilo kakva matrica $S$ takva da je $B = S A S$.", False),
    ("Nul-vektor $x = 0$ može biti svojstveni vektor operatora $A$ ako odgovara svojstvenoj vrijednosti $\\lambda_0 = 0$.", False),
    ("Skalar $\\lambda_0$ je svojstvena vrijednost ako postoji $x \\ne 0$ takav da je $A x = \\lambda_0 x$.", True),
    ("Spektar operatora $A$, označen s $\\sigma(A)$, predstavlja skup svih svojstvenih vektora operatora $A$.", False),
    ("Svojstveni polinom kvadratne matrice $A$ definiran je izrazom $k_A(\\alpha) = \\det(A - \\alpha I)$.", True),
    ("Minimalni polinom matrice $A$ je bilo koji polinom koji matrica $A$ poništava.", False),
    ("Skalarni produkt na $V$ je preslikavanje koje zadovoljava svojstva nenegativnosti, strogosti, aditivnosti, homogenosti i hermitske simetričnosti.", True),
    ("Unitaran prostor je vektorski prostor na kojem je definiran skalarni produkt.", True),
    ("U ortogonalnom skupu vektora, skalarni produkt bilo koja dva različita vektora iznosi $1$.", False),
    ("Vektor je normiran ako je njegova norma (duljina) jednaka $1$.", True),
    ("Skup vektora je ortonormiran ako su vektori međusobno ortogonalni i svi su normirani.", True),
    ("Ortogonalni komplement $M^\\perp$ potprostora $M \\le V$ sadrži sve vektore iz $V$ čiji je skalarni produkt s barem jednim vektorom iz $M$ jednak $0$.", False),
    ("Za kvadratnu matricu $A$ kažemo da je hermitska ako vrijedi $A^* = A$.", True),
    ("Za linearni operator $A: V \\to V$ kažemo da je izometrija ako mijenja skalarni produkt vektora ovisno o skalaru.", False),
    ("Za kvadratnu matricu $A$ kažemo da je unitarna ako vrijedi $A \\cdot A^* = A^* \\cdot A = I$.", True),
    ("Za matricu $A$ kažemo da je ortogonalna ako vrijedi $A^T \\cdot A = A \\cdot A^T = I$.", True),
    ("Hermitski adjungirana matrica $A^*$ dobiva se samo transponiranjem matrice $A$ bez promjene elemenata.", False),
]

# ---------------------------------------------------------------------------
# Nadopuni recenicu (50) - odgovor je OBICAN TEKST (usporeduje se doslovno)
# ---------------------------------------------------------------------------
FILLIN = [
    ("Operacija koja uzima dva elementa iz nepraznog skupa $G$ i daje element iz skupa $G$ zove se ___ operacija.", "binarna"),
    ("Uređeni par $(G, +)$ koji zadovoljava asocijativnost, postojanje neutralnog i inverznog elementa naziva se ___.", "grupa"),
    ("Ako u grupi vrijedi i komutativnost, takva grupa naziva se ___ grupa.", "Abelova"),
    ("Skup cijelih brojeva uz operaciju zbrajanja $(Z, +)$ primjer je ___ grupe.", "Abelove"),
    ("Skup prirodnih brojeva $N$ uz zbrajanje nije grupa jer nema ___ element i inverzne elemente.", "neutralni"),
    ("Neprazan skup $F$ s dvije binarne operacije (zbrajanje i množenje) u kojem je $(F, +)$ Abelova grupa naziva se ___.", "polje"),
    ("U polju $(F, +, \\cdot)$, skup $F \\setminus \\{0\\}$ uz množenje mora činiti ___ grupu.", "Abelovu"),
    ("Povezanost množenja i zbrajanja u polju osigurana je svojstvom ___ množenja prema zbrajanju.", "distributivnosti"),
    ("Uređena trojka $(V, +, \\cdot)$ naziva se ___ prostor nad poljem $F$.", "vektorski"),
    ("U vektorskom prostoru $V$, za neutralni element $1 \\in F$ i svaki $a \\in V$ mora vrijediti $1 \\cdot a =$ ___.", "a"),
    ("Izraz $\\alpha_1 a_1 + \\alpha_2 a_2 + \\dots + \\alpha_n a_n$ predstavlja ___ kombinaciju vektora.", "linearnu"),
    ("Skup vektora je linearno ___ ako njihova linearna kombinacija iščezava jedino na trivijalan način.", "nezavisan"),
    ("Kod trivijalne linearne kombinacije svi skalari $\\alpha_1, \\alpha_2, \\dots, \\alpha_n$ jednaki su ___.", "0"),
    ("Ako u linearnoj kombinaciji koja daje nul-vektor postoji skalar $\\alpha_i \\ne 0$, skup vektora je linearno ___.", "zavisan"),
    ("Skup svih konačnih linearnih kombinacija elemenata skupa $S$ naziva se linearna ___ skupa $S$.", "ljuska"),
    ("Linearna ljuska skupa $S$ označava se sa ___.", "[S]"),
    ("Ako je $[S] = V$, tada za skup $S$ kažemo da je sustav ___ za $V$.", "izvodnica"),
    ("Baza vektorskog prostora je konačan skup koji je linearno nezavisan sustav ___.", "izvodnica"),
    ("Prema fundamentalnom rezultatu linearne algebre, svaki vektor $v \\in V$ može se prikazati kao linearna kombinacija elemenata ___.", "baze"),
    ("Broj elemenata bilo koje baze vektorskog prostora $V \\ne \\{0\\}$ naziva se ___ prostora $V$.", "dimenzija"),
    ("Dimenzija nul-prostora $\\{0\\}$ iznosi ___.", "0"),
    ("Sve baze konačnodimenzionalnog vektorskog prostora $V \\ne \\{0\\}$ su ___.", "jednakobrojne"),
    ("Neprazan podskup $M \\subseteq V$ koji je i sam vektorski prostor uz iste operacije naziva se vektorski ___.", "potprostor"),
    ("Vektorski potprostor $M$ mora obavezno sadržavati ___-vektor.", "nul"),
    ("Suma potprostora $L$ i $M$ označava se s $[L \\cup$ ___ $]$.", "M"),
    ("Za sumu potprostora $L$ i $M$ kažemo da je ___ ako je $L \\cap M = \\{0\\}$.", "direktna"),
    ("Potprostor $M$ je direktan komplement potprostora $L$ ako je $L + M = V$ i suma je ___.", "direktna"),
    ("Preslikavanje $A: V \\to W$ koje čuva linearne kombinacije naziva se linearan ___.", "operator"),
    ("Skup $A(V) = \\{A v : v \\in V\\}$ naziva se ___ operatora $A$.", "slika"),
    ("Slika operatora $A: V \\to W$ je vektorski potprostor prostora ___.", "W"),
    ("Skup svih vektora $x \\in V$ za koje je $A x = 0$ naziva se ___ operatora $A$.", "jezgra"),
    ("Jezgra operatora $A: V \\to W$ je vektorski potprostor prostora ___.", "V"),
    ("Dimenzija slike operatora $A$ naziva se ___ operatora i označava s $r(A)$.", "rang"),
    ("Dimenzija jezgre operatora $A$ naziva se ___ operatora i označava s $d(A)$.", "defekt"),
    ("Teorem o rangu i defektu iskazuje se formulom $r(A) + d(A) =$ ___.", "dim(V)"),
    ("Za dvije kvadratne matrice $A$ i $B$ kažemo da su slične ako postoji regularna matrica $S$ takva da je $B =$ ___ $\\cdot A \\cdot S$.", "S^-1"),
    ("Skalar $\\lambda_0$ za koji postoji nenul vektor $x$ takav da je $A x = \\lambda_0 x$ naziva se ___ vrijednost.", "svojstvena"),
    ("Skup svih svojstvenih vrijednosti operatora $A$ naziva se ___ operatora $A$.", "spektar"),
    ("Spektar operatora $A$ označava se grčkim slovom ___.", "sigma"),
    ("Polinom $k_A(\\alpha) = \\det(A - \\alpha I)$ naziva se ___ polinom matrice $A$.", "svojstveni"),
    ("Normirani polinom najmanjeg stupnja kojeg matrica $A$ poništava naziva se ___ polinom.", "minimalni"),
    ("Preslikavanje $\\langle \\cdot, \\cdot \\rangle: V \\times V \\to F$ koje zadovoljava nenegativnost, strogost, aditivnost, homogenost i hermitsku simetričnost je ___ produkt.", "skalarni"),
    ("Vektorski prostor s definiranim skalarnim produktom naziva se ___ prostor.", "unitaran"),
    ("Skup vektora je ___ ako su svi njegovi vektori međusobno okomiti i svaki ima normu jednaku 1.", "ortonormiran"),
    ("Vektor čija je norma jednaka 1 naziva se ___ vektor.", "normiran"),
    ("Skup svih vektora iz $V$ okomitih na potprostor $M$ naziva se ortogonalni ___ potprostora $M$.", "komplement"),
    ("Za operator $A$ na unitarnom prostoru kažemo da je hermitski ako vrijedi $A^* =$ ___.", "A"),
    ("Linearni operator koji čuva skalarni produkt (i time duljinu vektora) naziva se ___.", "izometrija"),
    ("Kvadratna matrica $A$ za koju vrijedi $A \\cdot A^* = A^* \\cdot A = I$ naziva se ___ matrica.", "unitarna"),
    ("Kvadratna matrica $A$ za koju vrijedi $A^T \\cdot A = A \\cdot A^T = I$ naziva se ___ matrica.", "ortogonalna"),
]

# ---------------------------------------------------------------------------
# Flash kartice (25)
# ---------------------------------------------------------------------------
FLASHCARD = [
    ("Što je grupa?",
     "Uređeni par $(G, +)$ nepraznog skupa $G$ i binarne operacije $+$ koji zadovoljava: asocijativnost, postojanje neutralnog elementa i postojanje inverznog elementa za svaki element."),
    ("Što je Abelova grupa?",
     "Grupa $(G, +)$ koja uz osnovna tri svojstva zadovoljava i svojstvo komutativnosti ($a + b = b + a$)."),
    ("Koja je definicija polja?",
     "Uređena trojka $(F, +, \\cdot)$ gdje je $(F, +)$ Abelova grupa, $(F \\setminus \\{0\\}, \\cdot)$ Abelova grupa, te vrijedi distributivnost množenja prema zbrajanju."),
    ("Koji su uvjeti da $(V, +, \\cdot)$ bude vektorski prostor nad poljem $F$?",
     "$(V, +)$ je Abelova grupa, vrijede distributivnost na zbrajanje u $V$, distributivnost na zbrajanje u $F$, kvaziasocijativnost te $1 \\cdot a = a$ za neutralni element $1 \\in F$."),
    ("Kako se definira linearna kombinacija vektora?",
     "Za vektore $a_1, \\dots, a_n \\in V$ i skalare $\\alpha_1, \\dots, \\alpha_n \\in F$, to je vektor $a = \\alpha_1 a_1 + \\alpha_2 a_2 + \\dots + \\alpha_n a_n$."),
    ("Kada je skup vektora $S = \\{a_1, \\dots, a_n\\}$ linearno nezavisan?",
     "Kada jednakost $\\alpha_1 a_1 + \\dots + \\alpha_n a_n = 0$ vrijedi jedino na trivijalan način, tj. $\\alpha_1 = \\alpha_2 = \\dots = \\alpha_n = 0$."),
    ("Što je linearna ljuska $[S]$?",
     "Skup svih konačnih linearnih kombinacija elemenata iz skupa $S \\subseteq V$."),
    ("Definirajte sustav izvodnica za $V$.",
     "Podskup $S \\subseteq V$ za koji vrijedi da je njegova linearna ljuska jednaka čitavom prostoru, tj. $[S] = V$."),
    ("Što je baza vektorskog prostora $V$?",
     "Konačan skup $B \\subset V$ koji je linearno nezavisan sustav izvodnica za $V$."),
    ("Kako se definira dimenzija konačnodimenzionalnog vektorskog prostora?",
     "Kao broj elemenata bilo koje njegove baze za $V \\ne \\{0\\}$, pri čemu je $\\dim\\{0\\} = 0$."),
    ("Što je vektorski potprostor $M \\le V$?",
     "Neprazan podskup od $V$ koji je i sam vektorski prostor nad poljem $F$ s obzirom na iste operacije zbrajanja i množenja skalarom kao u $V$."),
    ("Kada je suma potprostora $L + M$ direktna?",
     "Kada je njihov presjek trivijalan, odnosno $L \\cap M = \\{0\\}$."),
    ("Što je direktan komplement potprostora $L$ u $V$?",
     "Potprostor $M \\le V$ takav da je $L + M = V$ i pri tome je suma direktna ($L \\cap M = \\{0\\}$)."),
    ("Koje uvjete zadovoljava linearan operator $A: V \\to W$?",
     "$A(\\alpha x + \\beta y) = \\alpha A(x) + \\beta A(y)$ za sve $\\alpha, \\beta \\in F$ i sve $x, y \\in V$."),
    ("Kako su definirani slika i jezgra operatora $A: V \\to W$?",
     "Slika: $\\text{Im}\\,A = \\{Av : v \\in V\\} \\le W$. Jezgra: $\\text{Ker}\\,A = \\{x \\in V : Ax = 0\\} \\le V$."),
    ("Što su rang $r(A)$ i defekt $d(A)$ operatora $A$?",
     "Rang je dimenzija slike $r(A) = \\dim(\\text{Im}\\,A)$, a defekt je dimenzija jezgre $d(A) = \\dim(\\text{Ker}\\,A)$."),
    ("Iskažite Teorem o rangu i defektu.",
     "Neka je $A: V \\to W$ linearan operator i $\\dim V < \\infty$. Tada vrijedi $r(A) + d(A) = \\dim V$."),
    ("Kada su dvije kvadratne matrice $A$ i $B$ slične?",
     "Ako postoji regularna matrica $S$ takva da je $B = S^{-1} A S$."),
    ("Definirajte svojstvenu vrijednost i svojstveni vektor operatora $A$.",
     "Skalar $\\lambda_0 \\in F$ je svojstvena vrijednost ako postoji vektor $x \\ne 0$ takav da je $Ax = \\lambda_0 x$. Vektor $x$ je pripadni svojstveni vektor."),
    ("Što je svojstveni polinom matrice $A$?",
     "Polinom $k_A(\\alpha) = \\det(A - \\alpha I)$."),
    ("Što je minimalni polinom matrice $A$?",
     "Normirani polinom najmanjeg stupnja kojeg matrica $A$ poništava."),
    ("Koja svojstva ima skalarni produkt $\\langle \\cdot, \\cdot \\rangle$?",
     "Nenegativnost, strogost, aditivnost, homogenost i hermitsku simetričnost."),
    ("Što je ortogonalni komplement $M^\\perp$ potprostora $M \\le V$?",
     "Skup svih vektora iz $V$ okomitih na sve vektore iz $M$: $M^\\perp = \\{x \\in V : \\langle x, v \\rangle = 0, \\forall v \\in M\\}$."),
    ("Što je izometrija?",
     "Linearni operator $A: V \\to V$ u unitarnom prostoru koji čuva skalarni produkt: $\\langle A(u), A(v) \\rangle = \\langle u, v \\rangle$ za sve $u, v \\in V$."),
    ("Koja je definicija ortogonalne i unitarne matrice?",
     "Ortogonalna: $A^T A = A A^T = I$. Unitarna: $A A^* = A^* A = I$."),
]

# ---------------------------------------------------------------------------
# Visestruki odabir (20)
# ---------------------------------------------------------------------------
MCQ = [
    ("Koja od navedenih struktura NIJE grupa?",
     ["$(Z, +)$", "$(Q \\setminus \\{0\\}, \\cdot)$", "$(N, +)$", "$(R, +)$"], 2),
    ("Abelova grupa se od obične grupe razlikuje po svojstvu:",
     ["Asocijativnosti", "Komutativnosti", "Distributivnosti", "Homogenosti"], 1),
    ("U strukturi polja $(F, +, \\cdot)$, skup $F \\setminus \\{0\\}$ uz množenje mora činiti:",
     ["Bilo kakav skup", "Abelovu grupu", "Vektorski prostor", "Monoid"], 1),
    ("Za neutralni element $1 \\in F$ u vektorskom prostoru $V$ vrijedi da je $1 \\cdot a$ jednako:",
     ["$0$", "$1$", "$a$", "$\\alpha a$"], 2),
    ("Skup vektora $S = \\{a_1, \\dots, a_n\\}$ je linearno nezavisan ako jednakost $\\alpha_1 a_1 + \\dots + \\alpha_n a_n = 0$ povlači:",
     ["Barem jedan $\\alpha_i \\ne 0$", "Sve $\\alpha_i = 0$", "$\\sum \\alpha_i = 1$", "$a_1 = a_2 = \\dots = a_n = 0$"], 1),
    ("Linearna ljuska $[S]$ skupa $S$ definiše se kao:",
     ["Skup svih umnožaka elemenata iz $S$", "Skup svih konačnih linearnih kombinacija elemenata iz $S$",
      "Presjek svih potprostora koji ne sadrže $S$", "Najveći potprostor u $V$"], 1),
    ("Baza vektorskog prostora $V$ je skup koji je:",
     ["Linearno zavisan sustav izvodnica", "Linearno nezavisan sustav izvodnica",
      "Bilo koji beskonačan skup", "Samo skup koji sadrži nul-vektor"], 1),
    ("Dimenzija nul-prostora $\\{0\\}$ iznosi:",
     ["$0$", "$1$", "Nepoznato", "Beskonačno"], 0),
    ("Suma potprostora $L$ i $M$ je direktna ako je $L \\cap M$ jednak:",
     ["$\\emptyset$", "$\\{0\\}$", "$V$", "$L \\cup M$"], 1),
    ("Potprostor $M$ je direktan komplement potprostora $L$ u $V$ ako je:",
     ["$L \\cap M = V$", "$L + M = V$ uz $L \\cap M = \\{0\\}$", "$L \\subseteq M$", "$L \\cup M = \\{0\\}$"], 1),
    ("Za linearan operator $A: V \\to W$, jezgra $\\text{Ker}\\,A$ je potprostor od:",
     ["Kodomene $W$", "Domene $V$", "Polja $F$", "Skupa $L(V,W)$"], 1),
    ("Rang operatora $r(A)$ predstavlja:",
     ["Dimenziju jezgre $\\text{Ker}\\,A$", "Dimenziju slike $\\text{Im}\\,A$", "Dimenziju domene $V$", "Dimenziju kodomene $W$"], 1),
    ("Prema Teoremu o rangu i defektu za $A: V \\to W$ uz $\\dim V < \\infty$ vrijedi:",
     ["$r(A) - d(A) = \\dim V$", "$r(A) + d(A) = \\dim V$", "$r(A) \\cdot d(A) = \\dim W$", "$r(A) + d(A) = \\dim W$"], 1),
    ("Matrica $B$ je slična matrici $A$ ako postoji regularna matrica $S$ takva da je:",
     ["$B = S A S$", "$B = S^{-1} A S$", "$B = A S^{-1}$", "$B = S A^{-1} S^{-1}$"], 1),
    ("Vektor $x$ u definiciji svojstvene vrijednosti $Ax = \\lambda_0 x$ mora zadovoljavati:",
     ["$x = 0$", "$x \\ne 0$", "$\\|x\\| = 0$", "$x \\in F$"], 1),
    ("Svojstveni polinom kvadratne matrice $A$ glasi:",
     ["$k_A(\\alpha) = \\det(A + \\alpha I)$", "$k_A(\\alpha) = \\det(A - \\alpha I)$",
      "$k_A(\\alpha) = \\text{tr}(A - \\alpha I)$", "$k_A(\\alpha) = A - \\alpha I$"], 1),
    ("Minimalni polinom matrice $A$ je normirani polinom kojega matrica $A$ poništava i koji ima:",
     ["Najveći stupanj", "Najmanji stupanj", "Stupanj jednak 1", "Neparni stupanj"], 1),
    ("Vektorski prostor s definiranim skalarnim produktom naziva se:",
     ["Normirani prostor", "Unitaran prostor", "Abelov prostor", "Baza prostora"], 1),
    ("Skup vektora je ortonormiran ako je skup ortogonalan i za svaki vektor $v$ iz skupa vrijedi:",
     ["$\\|v\\| = 0$", "$\\|v\\| = 1$", "$\\|v\\| = 2$", "$\\|v\\| < 0$"], 1),
    ("Za kvadratnu matricu $A$ kažemo da je ortogonalna ako vrijedi:",
     ["$A^* A = I$", "$A^T A = A A^T = I$", "$A^2 = I$", "$A^{-1} = A$"], 1),
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