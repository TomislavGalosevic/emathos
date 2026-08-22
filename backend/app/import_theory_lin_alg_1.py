"""Jednokratni uvoz teorije za kolegij 'Linearna algebra I'.

Pokretanje (iz mape backend/, s aktiviranim venv):
    python -m app.import_theory_lin_alg_1

Skripta NIJE idempotentna - ako je pokrenes dvaput, dobit ces duplikate.
"""

from .database import SessionLocal
from . import models

COURSE_NAME = "Linearna algebra I"

# ---------------------------------------------------------------------------
# Tocno / Netocno (50)
# ---------------------------------------------------------------------------
TRUEFALSE = [
    ("Vektori su ekvivalentni ako postoji translacija prostora koja prvi prevodi u drugi.", True),
    ("Skup svih vektora u prostoru označava se s $X_0(P)$.", False),
    ("Vektori su komplanarni ako njihovi reprezentanti leže na istom pravcu ili paralelnim pravcima.", False),
    ("Radijvektor je usmjerena dužina s početkom u fiksnoj točki $O$ (ishodištu) do neke točke $P$.", True),
    ("Zbrajanje vektora je operacija koja zadovoljava svojstva komutativnosti i asocijativnosti.", True),
    ("Neutralni element za zbrajanje vektora je jedinični vektor.", False),
    ("Operacija množenja vektora sa skalarom zadovoljava obje distributivnosti (na vektor i na skalar).", True),
    ("Skup vektora je linearno zavisan ako se njihova linearna kombinacija jednaka nul-vektoru može dobiti isključivo na trivijalan način.", False),
    ("Norma vektora je funkcija koja svakom vektoru pridružuje nenegativan realan broj.", True),
    ("Ako je $\\|\\vec{a}\\| = 0$, onda vektor $\\vec{a}$ ne mora biti nul-vektor.", False),
    ("Čebiševljeva norma vektora $\\vec{a} = (a_1,a_2,a_3)$ definira se kao $\\|\\vec{a}\\|_\\infty = \\max\\{|a_1|,|a_2|,|a_3|\\}$.", True),
    ("Skalarni umnožak dviju nenul vektora jednak je nuli ako i samo ako su vektori paralelni.", False),
    ("Skalarni umnožak vektora je komutativna operacija ($\\vec{a}\\cdot\\vec{b} = \\vec{b}\\cdot\\vec{a}$).", True),
    ("Za vektore $\\vec{a}=a_1\\vec{i}+a_2\\vec{j}+a_3\\vec{k}$ i $\\vec{b}=b_1\\vec{i}+b_2\\vec{j}+b_3\\vec{k}$ vrijedi $\\vec{a}\\cdot\\vec{b} = a_1b_1+a_2b_2+a_3b_3$.", True),
    ("Vektorski produkt dvaju vektora $\\vec{a}\\times\\vec{b}$ daje skalar.", False),
    ("Duljina vektorskog produkta $\\|\\vec{a}\\times\\vec{b}\\|$ jednaka je površini paralelograma kojeg zatvaraju vektori $\\vec{a}$ i $\\vec{b}$.", True),
    ("Vektorski produkt ima svojstvo komutativnosti.", False),
    ("Ako su vektori $\\vec{a}$ i $\\vec{b}$ kolinearni, njihov vektorski produkt jednak je nul-vektoru.", True),
    ("Ako je skup vektora linearno zavisan, barem jedan vektor se može prikazati kao linearna kombinacija ostalih.", True),
    ("Baza vektorskog prostora $X_0(E)$ u prostoru je bilo koji uređeni par linearno nezavisnih vektora.", False),
    ("Mješoviti produkt triju vektora definira se kao skalar $(\\vec{a}\\times\\vec{b})\\cdot\\vec{c}$.", True),
    ("Apsolutna vrijednost mješovitog produkta $|(\\vec{a}\\times\\vec{b})\\cdot\\vec{c}|$ predstavlja volumen paralelopipeda.", True),
    ("Mješoviti produkt $(\\vec{a}\\times\\vec{b})\\cdot\\vec{c}$ jednak je nuli ako i samo ako su vektori $\\vec{a},\\vec{b},\\vec{c}$ komplanarni.", True),
    ("Višestruki vektorski produkt zadovoljava zakon asocijativnosti: $(\\vec{a}\\times\\vec{b})\\times\\vec{c} = \\vec{a}\\times(\\vec{b}\\times\\vec{c})$.", False),
    ("Matrica je kvadratna ako je broj redaka $m$ jednak broju stupaca $n$.", True),
    ("U jediničnoj matrici $I$ svi elementi na glavnoj dijagonali jednaki su $0$, a izvan nje $1$.", False),
    ("Matrica $A$ je simetrična ako je $A^T = -A$.", False),
    ("Elementi na glavnoj dijagonali antisimetrične matrice moraju biti jednaki nuli.", True),
    ("Zbrajanje matrica moguće je provesti za bilo koje dvije matrice bez obzira na njihove dimenzije.", False),
    ("Množenje matrica je općenito komutativno ($A\\cdot B = B\\cdot A$).", False),
    ("Moguće je da su matrice $A$ i $B$ različite od nula-matrice, a da je njihov umnožak $A\\cdot B = 0$.", True),
    ("Kvadratna matrica $A$ je regularna ako postoji matrica $B$ takva da je $A\\cdot B = B\\cdot A = I$.", True),
    ("Matrica koja nema inverz naziva se singularna matrica.", True),
    ("Rang matrice po stupcima može biti različit od ranga matrice po retcima.", False),
    ("Zamjena mjesta dvaju redaka matrice je elementarna transformacija nad matricom.", True),
    ("Množenje jednog retka matrice skalarom $\\lambda = 0$ je dopuštena elementarna transformacija.", False),
    ("Determinanta je funkcija definirana na skupu svih pravokutnih matrica.", False),
    ("Matrica $A$ i njezina transponirana matrica $A^T$ imaju jednake determinante ($\\det A = \\det A^T$).", True),
    ("Ako matrica $A$ ima dva jednaka stupca, njezina determinanta jednaka je nuli.", True),
    ("Množenjem matrice $A$ skalarom $\\lambda$, njezina determinanta se množi s $\\lambda$.", False),
    ("Dodavanjem linearne kombinacije ostalih stupaca nekom stupcu, determinanta ne mijenja svoju vrijednost.", True),
    ("Algebarski komplement (kofaktor) elementa $a_{ik}$ računa se kao $(-1)^{i+k}\\det(A_{ik})$.", True),
    ("Prema Binet-Cauchyjevom teoremu vrijedi $\\det(A\\cdot B) = \\det A \\cdot \\det B$ za kvadratne matrice $A$ i $B$.", True),
    ("Cramerovo pravilo se može primijeniti na bilo koji sustav od $m$ jednadžbi s $n$ nepoznanica.", False),
    ("Ako je determinanta sustava $D\\neq 0$, kvadratni sustav ima jedinstveno rješenje $x_i = D_i/D$.", True),
    ("Vandermondeova determinanta koristi se u problemima interpolacije polinoma.", True),
    ("Projekcija vektora $\\vec{a}$ na pravac s jediničnim vektorom smjera $\\vec{n}$ iznosi $(\\vec{n}\\cdot\\vec{a})\\vec{n}$.", True),
    ("Vektor $\\vec{n}\\times(\\vec{a}\\times\\vec{n})$ predstavlja projekciju vektora $\\vec{a}$ na ravninu kojoj je $\\vec{n}$ vektor normale.", True),
    ("Gram-Schmidtov postupak služi za pretvaranje skupa linearno zavisnih vektora u ortogonalni skup.", False),
    ("Prema Kronecker-Capellijevom teoremu, sustav $A\\vec{x}=\\vec{b}$ ima rješenje ako i samo ako je $r(A) = r(A|b)$.", True),
]

# ---------------------------------------------------------------------------
# Nadopuni recenicu (50) - odgovor je OBICAN TEKST (usporeduje se doslovno)
# ---------------------------------------------------------------------------
FILLIN = [
    ("Vektor je klasa ___ međusobno ekvivalentnih usmjerenih dužina.", "ekvivalencije"),
    ("Skup svih radijvektora s početkom u fiksnoj točki $O$ označava se s ___.", "X0(E)"),
    ("Vektori su ___ ako njihovi reprezentanti leže na istom ili paralelnim pravcima.", "kolinearni"),
    ("Kartezijev koordinatni sustav u prostoru tvori uređena četvorka $(O,(\\vec{e}_1,\\vec{e}_2,\\vec{e}_3))$ gdje je trojka $(\\vec{e}_1,\\vec{e}_2,\\vec{e}_3)$ ___.", "ortonormirana baza"),
    ("Skup vektora uz operaciju zbrajanja čini ___ grupu.", "Abelovu"),
    ("Svojstvo $(\\lambda\\mu)\\vec{a} = \\lambda(\\mu\\vec{a})$ pri množenju vektora skalarom naziva se ___.", "kvaziasocijativnost"),
    ("Skup vektora $X_0$ nadijeljen operacijama zbrajanja i množenja sa skalarom koji zadovoljava svih 8 svojstava naziva se ___.", "vektorski prostor"),
    ("Izraz $\\vec{a}=\\lambda_1\\vec{a}_1+\\lambda_2\\vec{a}_2+\\dots+\\lambda_n\\vec{a}_n$ naziva se ___ vektora $\\vec{a}_1,\\dots,\\vec{a}_n$.", "linearna kombinacija"),
    ("Svojstvo $\\|\\lambda\\vec{a}\\| = |\\lambda|\\|\\vec{a}\\|$ naziva se ___.", "homogenost"),
    ("Nejednakost $\\|\\vec{a}+\\vec{b}\\| \\le \\|\\vec{a}\\|+\\|\\vec{b}\\|$ poznata je kao nejednakost ___.", "trokuta"),
    ("Euklidska norma vektora $\\vec{a}=(a_1,a_2,a_3)$ računa se po formuli $\\|\\vec{a}\\|_2$ = ___.", "sqrt(a1^2+a2^2+a3^2)"),
    ("Skalarni produkt dviju nenul vektora $\\vec{a}$ i $\\vec{b}$ definira se izrazom $\\vec{a}\\cdot\\vec{b}$ = ___.", "||a||*||b||*cos(fi)"),
    ("Nužan i dovoljan uvjet da bi dva nenul vektora $\\vec{a}$ i $\\vec{b}$ bila ortogonalna jest da je njihov skalarni produkt jednak ___.", "0"),
    ("Skalarni kvadrat vektora $\\vec{a}\\cdot\\vec{a}$ jednak je ___ duljine vektora $\\vec{a}$.", "kvadratu"),
    ("Vektorski produkt dviju nenul vektora $\\vec{a}$ i $\\vec{b}$ je vektor $\\vec{c}$ čiji je smjer određen pravilom ___.", "desnog vijka"),
    ("Vektorski produkt ima svojstvo antikomutativnosti, što znači da vrijedi $\\vec{a}\\times\\vec{b}$ = ___.", "-(b x a)"),
    ("Vektorski produkt $\\vec{a}\\times\\vec{b}$ preko komponenata možemo zapisati pomoću determinante reda ___.", "3"),
    ("Ako su $\\vec{a}$ i $\\vec{b}$ linearno nezavisni vektori u ravnini, tada se svaki vektor $\\vec{c}$ iz $X_0(M)$ na ___ način može prikazati kao njihova linearna kombinacija.", "jedinstven"),
    ("Baza vektorskog prostora $X_0(P)$ na pravcu $p$ je bilo koji ___ vektor.", "nenul"),
    ("Mješoviti produkt vektora $\\vec{a},\\vec{b},\\vec{c}$ računa se kao skalarni umnožak vektora ___ i vektora $\\vec{c}$.", "a x b"),
    ("Mješoviti produkt jednak je ___ čiji su retci komponente vektora $\\vec{a},\\vec{b},\\vec{c}$.", "determinanti"),
    ("Ako je mješoviti produkt $(\\vec{a}\\times\\vec{b})\\cdot\\vec{c} = 0$, vektori $\\vec{a},\\vec{b},\\vec{c}$ su ___.", "komplanarni"),
    ("Preslikavanje $A:\\{1,\\dots,m\\}\\times\\{1,\\dots,n\\}\\to\\mathbb{R}$ naziva se ___.", "matrica"),
    ("Matrica u kojoj su svi elementi izvan glavne dijagonale jednaki nuli naziva se ___ matrica.", "dijagonalna"),
    ("Ako je $A$ kvadratna matrica kod koje su svi elementi ispod glavne dijagonale jednaki nuli, kažemo da je $A$ ___ matrica.", "gornje-trokutasta"),
    ("Matrica koja se dobije zamjenom redaka i stupaca matrice $A$ naziva se ___ matrica i označava s $A^T$.", "transponirana"),
    ("Za matricu $B$ kažemo da je antisimetrična ako vrijedi $B^T$ = ___.", "-B"),
    ("Množenje matrica $A$ i $B$ definirano je samo ako su matrice ___, tj. ako je broj stupaca matrice $A$ jednak broju redaka matrice $B$.", "ulancane"),
    ("Element $c_{ij}$ u umnošku matrica $C=A\\cdot B$ izračunava se po formuli $c_{ij}$ = ___.", "suma(aik*bkj)"),
    ("Maksimalan broj linearno nezavisnih stupaca matrice naziva se ___ matrice po stupcima.", "rang"),
    ("Transformacija u kojoj se neki redak pomnožen skalarom doda drugom retku naziva se ___ transformacija nad retcima.", "elementarna"),
    ("Za dvije matrice kažemo da su ___ ako se jedna iz druge mogu dobiti primjenom konačno mnogo elementarnih transformacija.", "ekvivalentne"),
    ("Determinanta gornje-trokutaste matrice jednaka je ___ elemenata na glavnoj dijagonali.", "umnosku"),
    ("Ako u determinanti dva stupca zamijene mjesta, determinanta mijenja ___.", "predznak"),
    ("Ako su svi elementi jednog stupca matrice jednaki nuli, determinanta te matrice jednaka je ___.", "0"),
    ("Laplaceov razvoj determinante po $i$-tom retku koristi formulu $\\det A = \\sum_{k=1}^n a_{ik}$ ___.", "(-1)^(i+k)*det(Aik)"),
    ("Minor ili subdeterminanta elementa $a_{ik}$ dobiva se ispuštanjem $i$-tog retka i ___ stupca.", "k-tog"),
    ("Kvadratni sustav od $n$ jednadžbi s $n$ nepoznanica ima jedinstveno rješenje ako i samo ako je determinanta sustava $D$ različita od ___.", "0"),
    ("Ako je u kvadratnom sustavu $D=0$ i barem jedan $D_i\\neq 0$, sustav nema ___.", "rjesenja"),
    ("Cauchy-Schwarz-Bunjakowsky nejednakost za realne brojeve tvrdi da je $(\\sum a_kb_k)^2 \\le$ ___.", "(suma ak^2)*(suma bk^2)"),
    ("Jednakost u Cauchy-Schwarz-Bunjakowsky nejednakosti vrijedi ako i samo ako su nizovi $a_k$ i $b_k$ ___.", "proporcionalni"),
    ("Traženje polinoma $P_n(x)$ koji u točkama $x_i$ poprima unaprijed zadane vrijednosti $y_i$ naziva se ___ polinoma.", "interpolacija"),
    ("Vektor $\\vec{a}$ može se rastaviti na zbroj dviju komponenti u odnosu na jedinični vektor $\\vec{n}$ po formuli $\\vec{a} = (\\vec{n}\\cdot\\vec{a})\\vec{n}$ + ___.", "n x (a x n)"),
    ("Kanonski oblik jednadžbe pravca u prostoru glasi $\\frac{x-x_0}{a_x} = \\frac{y-y_0}{a_y}$ = ___.", "(z-z0)/az"),
    ("Opći oblik jednadžbe ravnine u prostoru glasi $Ax+By+Cz+D$ = ___.", "0"),
    ("U općem obliku jednadžbe ravnine $Ax+By+Cz+D=0$, vektor $\\vec{n}=A\\vec{i}+B\\vec{j}+C\\vec{k}$ predstavlja vektor ___ na ravninu.", "normale"),
    ("Segmentni oblik jednadžbe ravnine glasi $\\frac{x}{m}+\\frac{y}{n}+\\frac{z}{p}$ = ___.", "1"),
    ("Vektori koji su međusobno okomiti i imaju jediničnu duljinu nazivaju se ___ vektori.", "ortonormirani"),
    ("Gram-Schmidtov postupak ortogonalizacije prvi ortogonalni vektor $u_1$ postavlja jednako vektoru ___.", "v1"),
    ("Proširena matrica sustava $A\\vec{x}=\\vec{b}$ označava se s ___.", "(A|b)"),
]

# ---------------------------------------------------------------------------
# Flash kartice (25)
# ---------------------------------------------------------------------------
FLASHCARD = [
    ("Što je vektor prema formalnoj matematičkoj definiciji?",
     "Vektor je klasa ekvivalencije međusobno ekvivalentnih usmjerenih dužina."),
    ("Koja 3 svojstva mora zadovoljavati funkcija normiranja $\\|\\cdot\\|$?",
     "1. Pozitivna definitnost: $\\|\\vec{a}\\|=0 \\Leftrightarrow \\vec{a}=0$\n2. Homogenost: $\\|\\lambda\\vec{a}\\| = |\\lambda|\\|\\vec{a}\\|$\n3. Nejednakost trokuta: $\\|\\vec{a}+\\vec{b}\\|\\le\\|\\vec{a}\\|+\\|\\vec{b}\\|$"),
    ("Koje su tri standardne norme za vektor $\\vec{a}=(a_1,a_2,a_3)$?",
     "1. $l_1$-norma: $\\|\\vec{a}\\|_1 = |a_1|+|a_2|+|a_3|$\n2. Euklidska norma: $\\|\\vec{a}\\|_2 = \\sqrt{a_1^2+a_2^2+a_3^2}$\n3. Čebiševljeva norma: $\\|\\vec{a}\\|_\\infty = \\max\\{|a_1|,|a_2|,|a_3|\\}$"),
    ("Koji je geometrijski uvjet za ortogonalnost dvaju vektora preko skalarnog produkta?",
     "Vektori $\\vec{a}$ i $\\vec{b}$ su ortogonalni ako i samo ako je $\\vec{a}\\cdot\\vec{b}=0$."),
    ("Što predstavlja duljina vektorskog produkta $\\|\\vec{a}\\times\\vec{b}\\|$?",
     "Površinu paralelograma kojeg zatvaraju vektori $\\vec{a}$ i $\\vec{b}$."),
    ("Zbog kojeg svojstva vrijedi $\\vec{a}\\times\\vec{b} = -(\\vec{b}\\times\\vec{a})$?",
     "Zbog svojstva antikomutativnosti vektorskog produkta."),
    ("Definiraj uvjet linearne nezavisnosti skupa vektora $\\{\\vec{a}_1,\\dots,\\vec{a}_n\\}$.",
     "Skup je linearno nezavisan ako iz $\\lambda_1\\vec{a}_1+\\dots+\\lambda_n\\vec{a}_n=0$ slijedi da svi skalari moraju biti $0$."),
    ("Što čini bazu vektorskog prostora $X_0(M)$ u ravnini?",
     "Bilo koji uređeni par linearno nezavisnih vektora iz ravnine $M$."),
    ("Kako glasi formula za volumen paralelopipeda razapetog vektorima $\\vec{a},\\vec{b},\\vec{c}$?",
     "$V = |(\\vec{a}\\times\\vec{b})\\cdot\\vec{c}|$"),
    ("Što navodi skripta o asocijativnosti višestrukog vektorskog produkta?",
     "Višestruki vektorski produkt NIJE asocijativan: $(\\vec{a}\\times\\vec{b})\\times\\vec{c} \\neq \\vec{a}\\times(\\vec{b}\\times\\vec{c})$."),
    ("Kada su dvije matrice $A$ i $B$ ulančane?",
     "Kada je broj stupaca matrice $A$ jednak broju redaka matrice $B$."),
    ("Koja je definicija regularne matrice?",
     "Kvadratna matrica $A$ je regularna ako postoji matrica $B$ takva da je $A\\cdot B = B\\cdot A = I$."),
    ("Što je rang matrice $r(A)$?",
     "Maksimalan broj linearno nezavisnih stupaca (ili redaka) matrice."),
    ("Navedi tri elementarne transformacije nad retcima matrice.",
     "1. Zamjena mjesta dvaju redaka\n2. Množenje retka skalarom $\\lambda\\neq 0$\n3. Dodavanje jednog retka (pomnoženog skalarom) drugom retku"),
    ("Kolika je determinanta trokutaste matrice?",
     "Jednaka je umnošku elemenata na glavnoj dijagonali: $\\det A = a_{11}a_{22}\\cdots a_{nn}$."),
    ("Što se događa s determinantom ako dva stupca zamijene mjesta?",
     "Determinanta mijenja predznak."),
    ("Kako glasi Binet-Cauchyjev teorem?",
     "Za dvije kvadratne matrice $A$ i $B$ istog reda vrijedi $\\det(A\\cdot B) = \\det A \\cdot \\det B$."),
    ("Kada kvadratni sustav prema Cramerovom pravilu nema rješenja?",
     "Kada je determinanta sustava $D=0$, a barem jedna $D_i\\neq 0$."),
    ("Kako glasi Cauchy-Schwarz-Bunjakowsky nejednakost za realne brojeve?",
     "$\\left(\\sum_{k=1}^n a_kb_k\\right)^2 \\le \\left(\\sum_{k=1}^n a_k^2\\right)\\left(\\sum_{k=1}^n b_k^2\\right)$"),
    ("Koji je uvjet rješivosti sustava za koeficijente interpolacijskog polinoma?",
     "Da su sve čvorne točke $x_i$ međusobno različite (tada je Vandermondeova determinanta različita od $0$)."),
    ("Kako glasi formula za ortogonalnu projekciju vektora $\\vec{a}$ na pravac s jediničnim vektorom $\\vec{n}$?",
     "Projekcija iznosi $(\\vec{n}\\cdot\\vec{a})\\vec{n}$."),
    ("Koji vektor predstavlja projekciju vektora $\\vec{a}$ na ravninu s normalom $\\vec{n}$?",
     "Vektor $\\vec{n}\\times(\\vec{a}\\times\\vec{n})$."),
    ("Kako glasi parametarski oblik jednadžbe pravca u prostoru?",
     "$x=x_0+\\lambda a_x,\\ y=y_0+\\lambda a_y,\\ z=z_0+\\lambda a_z$"),
    ("Kako glasi formula iterativnog koraka u Gram-Schmidtovom postupku?",
     "$u_k = v_k - \\sum_{j=1}^{k-1} \\frac{\\langle v_k,u_j\\rangle}{\\langle u_j,u_j\\rangle} u_j$"),
    ("Što tvrdi Kronecker-Capellijev teorem kada je $r(A)=r(A|b)=r$?",
     "Ako je $r=n$ (broj nepoznanica), sustav ima jedinstveno rješenje; ako je $r<n$, ima beskonačno mnogo rješenja."),
]

# ---------------------------------------------------------------------------
# Visestruki odabir (20)
# ---------------------------------------------------------------------------
MCQ = [
    ("Neka su $\\vec{u},\\vec{v},\\vec{w}$ tri nenul vektora u prostoru. Što možemo zaključiti ako je njihov mješoviti produkt $(\\vec{u}\\times\\vec{v})\\cdot\\vec{w}=0$?",
     ["Vektori $\\vec{u}$ i $\\vec{v}$ moraju biti međusobno okomiti.",
      "Vektor $\\vec{w}$ mora biti nul-vektor.",
      "Vektori $\\vec{u},\\vec{v},\\vec{w}$ su komplanarni.",
      "Vektori $\\vec{u}$ i $\\vec{v}$ su sigurno kolinearni."], 2),
    ("Ako je $\\|\\vec{a}+\\vec{b}\\| = \\|\\vec{a}\\|+\\|\\vec{b}\\|$, koji uvjet mora biti zadovoljen za nenul vektore $\\vec{a}$ i $\\vec{b}$?",
     ["Vektori $\\vec{a}$ i $\\vec{b}$ su međusobno okomiti.",
      "Vektori $\\vec{a}$ i $\\vec{b}$ su kolinearni i imaju isti smjer.",
      "Vektori $\\vec{a}$ i $\\vec{b}$ su kolinearni i imaju suprotan smjer.",
      "Jedan od vektora mora biti nul-vektor."], 1),
    ("Neka je $A$ kvadratna matrica reda $3$ s $\\det A = 5$. Koliko iznosi $\\det(2A)$?",
     ["$10$", "$30$", "$40$", "$120$"], 2),
    ("Što vrijedi za višestruki produkt vektora $(\\vec{i}\\times\\vec{j})\\times\\vec{i}$?",
     ["Jednak je nul-vektoru.",
      "Jednak je vektoru $\\vec{j}$.",
      "Jednak je vektoru $-\\vec{j}$.",
      "Jednak je vektoru $\\vec{k}$."], 1),
    ("Neka je $A$ antisimetrična matrica reda $3\\times 3$. Kolika je $\\det A$?",
     ["Uvijek $1$.", "Uvijek $0$.", "Ovisi o elementima izvan dijagonale.", "Ne može se odrediti bez uvjeta regularnosti."], 1),
    ("Ako je skup $\\{\\vec{a},\\vec{b},\\vec{c}\\}$ linearno nezavisan, što vrijedi za skup $\\{\\vec{a}+\\vec{b}, \\vec{b}+\\vec{c}, \\vec{a}+\\vec{c}\\}$?",
     ["Skup je uvijek linearno zavisan.",
      "Skup je uvijek linearno nezavisan.",
      "Skup je baza prostora samo ako su $\\vec{a},\\vec{b},\\vec{c}$ ortogonalni.",
      "Skup ne može razapinjati isti prostor."], 1),
    ("Što vrijedi za umnožak matrica $A$ i $B$ ako je $A\\cdot B = 0$?",
     ["Sigurno je $A=0$ ili $B=0$.",
      "Obje matrice moraju biti kvadratne i singularne.",
      "Moguće je da su obje matrice $A\\neq 0$ i $B\\neq 0$.",
      "Jedna od matrica mora biti jedinična."], 2),
    ("Zadana je ravnina $M$ jednadžbom $2x-3y+z-5=0$. Koji je vektor normale na tu ravninu?",
     ["$\\vec{n}=2\\vec{i}-3\\vec{j}-5\\vec{k}$",
      "$\\vec{n}=2\\vec{i}-3\\vec{j}+\\vec{k}$",
      "$\\vec{n}=-2\\vec{i}+3\\vec{j}+5\\vec{k}$",
      "$\\vec{n}=\\frac{1}{2}\\vec{i}-\\frac{1}{3}\\vec{j}+\\vec{k}$"], 1),
    ("Kolika je Čebiševljeva norma $\\|\\vec{a}\\|_\\infty$ za $\\vec{a}=(-5,2,4)$?",
     ["$-5$", "$3$", "$5$", "$\\sqrt{45}$"], 2),
    ("Što se događa s rangom matrice ako joj dodamo redak koji je linearna kombinacija postojećih redaka?",
     ["Rang se poveća za $1$.", "Rang se smanji za $1$.", "Rang ostaje nepromijenjen.", "Rang postaje jednak broju nepoznanica."], 2),
    ("Kolika je $\\det A$ kvadratne matrice $A$ reda $n$ za koju vrijedi $A^2=A$ (idempotentna)?",
     ["Samo $1$.", "Samo $0$.", "Može biti samo $0$ ili $1$.", "Bilo koji realan broj."], 2),
    ("U sustavu $A\\vec{x}=\\vec{b}$ broj nepoznanica je $n=4$, a $r(A)=r(A|b)=3$. Što vrijedi prema Kronecker-Capellijevom teoremu?",
     ["Sustav nema rješenja.",
      "Sustav ima jedinstveno rješenje.",
      "Sustav ima beskonačno mnogo rješenja s $1$ slobodnim parametrom.",
      "Sustav ima beskonačno mnogo rješenja s $3$ slobodna parametra."], 2),
    ("Koje svojstvo NE VRIJEDI općenito za skalarni produkt vektora?",
     ["$\\vec{a}\\cdot\\vec{b} = \\vec{b}\\cdot\\vec{a}$",
      "$(\\vec{a}+\\vec{b})\\cdot\\vec{c} = \\vec{a}\\cdot\\vec{c}+\\vec{b}\\cdot\\vec{c}$",
      "$(\\vec{a}\\cdot\\vec{b})\\cdot\\vec{c} = \\vec{a}\\cdot(\\vec{b}\\cdot\\vec{c})$",
      "$\\vec{a}\\cdot\\vec{a} = \\|\\vec{a}\\|^2$"], 2),
    ("Neka je $A$ gornje-trokutasta matrica $3\\times3$ s dijagonalnim elementima $2,-1,4$. Koliko je $\\det A$?",
     ["$5$", "$-8$", "$8$", "$0$"], 1),
    ("Kakva je relacija između $(\\vec{n}\\cdot\\vec{a})\\vec{n}$ i $\\vec{n}\\times(\\vec{a}\\times\\vec{n})$ pri rastavu vektora $\\vec{a}$?",
     ["Paralelni su.", "Međusobno su okomiti.", "Jednaki su po duljini.", "Poklapaju se po smjeru s $\\vec{n}$."], 1),
    ("Zašto je u Gram-Schmidtovom postupku nužno da je početni skup vektora linearno nezavisan?",
     ["Da bi matrice bile kvadratne.",
      "Da ne bismo dijelili s $0$ (norma jednaka $0$).",
      "Da bi svi vektori bili jedinični.",
      "Da bi determinanta bila jednaka $1$."], 1),
    ("Ako matrica $A$ ima inverz $A^{-1}$, koliko iznosi $\\det(A^{-1})$?",
     ["$-\\det A$", "$\\det A$", "$1/\\det A$", "$(\\det A)^2$"], 2),
    ("Za simetričnu matricu $S$ ($S^T=S$) i antisimetričnu $K$ ($K^T=-K$) istog reda, što vrijedi za matricu $A=S+K$?",
     ["Svaka kvadratna matrica može se na jedinstven način prikazati kao zbroj simetrične i antisimetrične matrice.",
      "Matrica $A$ mora biti simetrična.",
      "Matrica $A$ mora biti antisimetrična.",
      "$\\det A = 0$."], 0),
    ("Koja je uloga Vandermondeove matrice u interpolaciji?",
     ["Služi za izravno računanje vektorskog produkta.",
      "Njezina determinanta osigurava jedinstveno rješenje ako su čvorovi različiti.",
      "Služi za ortogonalizaciju baze prostora.",
      "Određuje kut između dviju ravnina."], 1),
    ("Koliki je rang matrice $A$ dimenzija $3\\times4$ čiji su svi elementi jednaki $2$?",
     ["$0$", "$1$", "$3$", "$4$"], 1),
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