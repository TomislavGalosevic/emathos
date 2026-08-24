"""Jednokratni uvoz teorije za kolegij 'Obicne diferencijalne jednadzbe'."""

from .database import SessionLocal
from . import models

COURSE_NAME = "Obicne diferencijalne jednadzbe"

# ---------------------------------------------------------------------------
# Tocno / Netocno (50)
# ---------------------------------------------------------------------------
TRUEFALSE = [
    ("Obična diferencijalna jednadžba je jednadžba u kojoj je nepoznanica funkcija jedne varijable i u njoj se pojavljuju derivacije te nepoznate funkcije.", True),
    ("Red diferencijalne jednadžbe definira se kao najviši red derivacije nepoznate funkcije koji se pojavljuje u toj jednadžbi.", True),
    ("Za diferencijalnu jednadžbu $n$-tog reda potrebno je zadati $n$ početnih uvjeta u Cauchyjevoj zadaći.", True),
    ("Rješenje Cauchyjeve zadaće $y' = f(t,y)$, $y(t_0) = y_0$ je lokalno jedinstveno ako za svako drugo rješenje $v$ vrijedi da se $u$ i $v$ podudaraju na presjeku njihovih domena.", True),
    ("Vektor smjera tangente na graf rješenja diferencijalne jednadžbe $y' = f(t,y)$ u točki $(t_0, u(t_0))$ dan je s $v = \\vec{i} + f(t_0, u(t_0))\\vec{j}$.", True),
    ("Skup svih vektora $v = \\vec{i} + f(t,y)\\vec{j}$ za $(t,y) \\in \\Omega$ naziva se polje smjerova obične diferencijalne jednadžbe.", True),
    ("Prema Picardovom teoremu, ako je $f$ neprekidna na pravokutniku $S$ i Lipschitzova po drugoj varijabli, Cauchyjeva zadaća ima lokalno jedinstveno rješenje.", True),
    ("Picardov teorem daje informaciju o vremenu postojanja rješenja $T = \\min\\{a, b/M\\}$.", True),
    ("Prostor $C([a,b])$ svih realnih neprekidnih funkcija na $[a,b]$ uz normu $\\|f\\|_\\infty = \\max|f(x)|$ je realan Banachov prostor.", True),
    ("Normiran prostor je potpun ako i samo ako je u njemu svaki apsolutno konvergentan red ujedno i konvergentan.", True),
    ("Gronwallova lema se u teoriji običnih diferencijalnih jednadžbi često koristi za dokazivanje jedinstvenosti rješenja.", True),
    ("Prema Cauchyjevom teoremu o egzistenciji i jedinstvenosti, ako je parcijalna derivacija $\\partial_y f$ neprekidna na otvorenom skupu $\\Omega$, zadaća ima lokalno jedinstveno rješenje.", True),
    ("Niz Picardovih iteracija za Cauchyjevu zadaću $y' = y$, $y(0) = 1$ konvergira prema funkciji $u(t) = e^t$.", True),
    ("Peanov teorem zahtijeva samo neprekidnost funkcije $f$, ali jamči samo postojanje rješenja, ne i njegovu jedinstvenost.", True),
    ("Opće rješenje homogene linearne obične diferencijalne jednadžbe prvog reda $y' = a(t)y$ je oblika $y = c \\cdot e^{\\int a(t)\\,dt}$.", True),
    ("Metoda varijacije konstanti (Lagrangeova metoda) koristi se za pronalaženje općeg rješenja nehomogene linearne diferencijalne jednadžbe.", True),
    ("Bernoullijeva diferencijalna jednadžba $y' = a(t)y + b(t)y^\\alpha$ se za $\\alpha \\ne 0, 1$ supstitucijom $z = y^{1-\\alpha}$ svodi na linearnu diferencijalnu jednadžbu prvog reda.", True),
    ("Diferencijalna jednadžba $f_1(t,y)\\,dt + f_2(t,y)\\,dy = 0$ je egzaktna ako i samo ako je pripadno vektorsko polje $f = (f_1, f_2)$ potencijalno.", True),
    ("Nužan i dovoljan uvjet egzaktnosti na jednostavno povezanom području je jednakost parcijalnih derivacija $\\partial_y f_1 = \\partial_t f_2$.", True),
    ("Ako diferencijalna jednadžba nije egzaktna, množenjem s Eulerovim multiplikatorom $\\mu(t,y) \\ne 0$ možemo je pretvoriti u egzaktnu jednadžbu.", True),
    ("Singularno rješenje diferencijalne jednadžbe $y' = f(t,y)$ je rješenje u čijim se točkama gubi jedinstvenost Cauchyjeve zadaće.", True),
    ("Svaka obična diferencijalna jednadžba $n$-tog reda može se ekvivalentno prikazati kao sustav od $n$ običnih diferencijalnih jednadžbi prvog reda.", True),
    ("Skup svih globalnih rješenja homogenog linearnog sustava $y' = A(t)y$ dimenzije $n$ čini $n$-dimenzionalni vektorski potprostor.", True),
    ("Matrica Wronskog (ili fundamentalna matrica) sustava je matrica čiji stupci čine fundamentalni sustav rješenja.", True),
    ("Eksponencijalna matrična funkcija $E(t) = e^{tA}$ definira se redom $\\sum_{k=0}^{\\infty} \\frac{t^k A^k}{k!}$ i konvergira za svaku matricu $A \\in M_n(\\mathbb{R})$.", True),
    ("Ako je nepoznata funkcija u diferencijalnoj jednadžbi funkcija više varijabli, riječ je o običnoj diferencijalnoj jednadžbi.", False),
    ("Za diferencijalnu jednadžbu drugog reda dovoljan je samo jedan početni uvjet kako bismo imali jedinstveno rješenje.", False),
    ("Peanov teorem jamči da Cauchyjeva zadaća ima lokalno jedinstveno rješenje čim je funkcija $f$ neprekidna.", False),
    ("Svaki Banachov prostor ujedno je i Hilbertov prostor uz odgovarajući skalarni produkt.", False),
    ("Ako je funkcija $f$ neprekidna i Lipschitzova na cijelom $\\mathbb{R}^2$, rješenje Cauchyjeve zadaće može pobjeći u beskonačnost u konačnom vremenu.", False),
    ("Picardove iteracije uvijek konvergiraju prema rješenju Cauchyjeve zadaće, čim je funkcija $f$ neprekidna na domeni.", False),
    ("Opće rješenje nehomogene linearne jednadžbe dobiva se kao umnožak općeg rješenja homogene i jednog partikularnog rješenja.", False),
    ("Svaka diferencijalna jednadžba s odvojenim varijablama ujedno je i egzaktna diferencijalna jednadžba.", False),
    ("Eulerov multiplikator jedinstven je za svaku neegzaktnu diferencijalnu jednadžbu.", False),
    ("Riccatijeva diferencijalna jednadžba može se uvijek općenito riješiti kvadraturama bez poznavanja i jednog partikularnog rješenja.", False),
    ("Clairautova jednadžba ima samo jedno jedinstveno rješenje za svaki početni uvjet.", False),
    ("Odrednica Wronskog (Vronskijan) fundamentalnog sustava rješenja može biti jednaka nuli u nekim točkama, a različita od nule u drugima.", False),
    ("Svaka matrica $A \\in M_n(\\mathbb{R})$ može se dijagonalizirati u realnom području.", False),
    ("Vektorski prostor rješenja nehomogenog linearnog sustava $y' = A(t)y + b(t)$ je dimenzije $n$.", False),
    ("Svojstvene vrijednosti matrice $A$ jednake su svojstvenim vrijednostima matrice $e^{tA}$.", False),
    ("Svaki sustav autonomnih diferencijalnih jednadžbi $y' = f(y)$ ima isključivo periodična rješenja.", False),
    ("Linearna diferencijalna jednadžba $n$-tog reda s konstantnim koeficijentima uvijek ima međusobno različite svojstvene vrijednosti karakterističnog polinoma.", False),
    ("Ako je korijen karakterističnog polinoma $k$-struki kompleksni broj $\\lambda = a+ib$, tada su pripadna rješenja oblika $t^j e^{at}$ za $j=0,\\dots,k-1$.", False),
    ("Funkcija $f(t,y) = \\sqrt{|y|}$ zadovoljava Lipschitzov uvjet po $y$ na okolici ishodišta $(0,0)$.", False),
    ("Ako su $y_1$ i $y_2$ dva rješenja nehomogene linearne diferencijalne jednadžbe, tada je i $y_1+y_2$ također rješenje te iste nehomogene jednadžbe.", False),
    ("Matrica $e^{A+B}$ uvijek je jednaka $e^A e^B$ za bilo koje dvije kvadratne matrice $A$ i $B$.", False),
    ("Stabilnost po Ljapunovu stacionarne točke autonomnog sustava garantira da sva rješenja konvergiraju prema toj točki kada $t\\to\\infty$.", False),
    ("Ako je $\\det(A) > 0$, ishodište je uvijek stabilna ravnotežna točka linearnog sustava $y' = Ay$.", False),
    ("Svaka diferencijalna jednadžba reda $n$ može se eksplicitno riješiti pomoću elementarnih funkcija i integrala.", False),
    ("Metoda neodređenih koeficijenata primjenjiva je za traženje partikularnog rješenja nehomogene linearne jednadžbe s proizvoljnim, općim koeficijentima.", False),
]

# ---------------------------------------------------------------------------
# Nadopuni recenicu (50) - odgovor je OBICAN TEKST (usporeduje se doslovno)
# ---------------------------------------------------------------------------
FILLIN = [
    ("Jednadžba u kojoj je nepoznanica funkcija jedne varijable te se u njoj pojavljuju njezine derivacije naziva se ___.", "obicna diferencijalna jednadzba"),
    ("Najviši red derivacije nepoznate funkcije u diferencijalnoj jednadžbi definira se kao ___ diferencijalne jednadžbe.", "red"),
    ("Za Cauchyjevu zadaću $n$-tog reda potrebno je zadati ___ početnih uvjeta.", "n"),
    ("Skup svih vektora $(1, f(t,y))$ u prostor-vremenu za jednadžbu $y' = f(t,y)$ naziva se ___ smjerova.", "polje"),
    ("Ako diferencijalna jednadžba opisuje promjenu u kojoj brzina ovisi samo o stanju $y$, a ne i o vremenu $t$ ($y' = f(y)$), takva jednadžba naziva se ___.", "autonomna"),
    ("Točka $y_0$ za koju vrijedi $f(y_0) = 0$ u autonomnoj jednadžbi $y' = f(y)$ naziva se stacionarna točka ili ___ točka.", "ravnotezna"),
    ("Banachov prostor je potpun ___ prostor.", "normiran"),
    ("Preslikavanje $T$ sa metričkog prostora $(X,d)$ u samog sebe je kontrakcija ako postoji $q \\in [0,1)$ takav da za sve $x,y \\in X$ vrijedi $d(T(x), T(y)) \\le$ ___.", "q*d(x,y)"),
    ("Banachov teorem o fiksnoj točki jamči postojanje i jedinstvenost fiksne točke za preslikavanja koja su ___ na potpunom metričkom prostoru.", "kontrakcije"),
    ("Preslikavanje $f$ zadovoljava ___ uvjet po drugoj varijabli ako postoji $L>0$ takav da je $|f(t,y_1)-f(t,y_2)| \\le L|y_1-y_2|$.", "Lipschitzov"),
    ("Cauchyjeva zadaća $y'=f(t,y)$, $y(t_0)=y_0$ ekvivalentna je Volterrinoj ___ jednadžbi $y(t) = y_0 + \\int_{t_0}^t f(s,y(s))\\,ds$.", "integralnoj"),
    ("Metoda sukcesivnih aproksimacija za dokazivanje egzistencije rješenja naziva se i ___ iteracije.", "Picardove"),
    ("Picard-Lindelöfov teorem jamči lokalno postojanje i ___ rješenja Cauchyjeve zadaće pod uvjetom neprekidnosti i Lipschitzove svojstvenosti.", "jedinstvenost"),
    ("Peanov teorem o egzistenciji zahtijeva samo ___ funkcije $f$, ali ne jamči jedinstvenost rješenja.", "neprekidnost"),
    ("Nejednakost koja se koristi za ocjenu rješenja i dokazivanje jedinstvenosti u ODJ-u naziva se ___ lema.", "Gronwallova"),
    ("Diferencijalna jednadžba oblika $y' = g(t)h(y)$ zove se jednadžba s ___ varijablama.", "odvojenim"),
    ("Homogena diferencijalna jednadžba prvog reda oblika $y' = f(y/t)$ rješava se uvođenjem supstitucije $u =$ ___.", "y/t"),
    ("Linearna diferencijalna jednadžba prvog reda općeg je oblika $y' + a(t)y =$ ___.", "b(t)"),
    ("Opće rješenje homogene linearne jednadžbe $y' + a(t)y = 0$ dano je izrazom $y(t) = C \\cdot \\exp($ ___ $)$.", "-int(a(t)dt)"),
    ("Metoda traženja partikularnog rješenja nehomogene linearne jednadžbe pretpostavljanjem da je konstanta $C$ funkcija $C(t)$ naziva se ___.", "varijacija konstanti"),
    ("Jednadžba oblika $y' + a(t)y = b(t)y^\\alpha$ za $\\alpha \\ne 0,1$ naziva se ___ diferencijalna jednadžba.", "Bernoullijeva"),
    ("Bernoullijeva jednadžba svodi se na linearnu jednadžbu supstitucijom $z =$ ___.", "y^(1-alpha)"),
    ("Jednadžba oblika $y' + a(t)y + b(t)y^2 = c(t)$ naziva se ___ jednadžba.", "Riccatijeva"),
    ("Da bi se Riccatijeva jednadžba mogla općenito riješiti kvadraturama, potrebno je poznavati barem jedno ___ rješenje.", "partikularno"),
    ("Jednadžba $P(t,y)\\,dt + Q(t,y)\\,dy = 0$ je egzaktna ako postoji funkcija $U(t,y)$ takva da je $dU =$ ___.", "P(t,y)dt+Q(t,y)dy"),
    ("Nužan i dovoljan uvjet egzaktnosti na jednostavno povezanom području za $P\\,dt+Q\\,dy=0$ glasi $dP/dy =$ ___.", "dQ/dt"),
    ("Ako jednadžba $P\\,dt+Q\\,dy=0$ nije egzaktna, množenjem s funkcijom $\\mu(t,y)$ može se pretvoriti u egzaktnu. Funkcija $\\mu(t,y)$ naziva se ___.", "Eulerov multiplikator"),
    ("Jednadžba oblika $y = t y' + g(y')$ naziva se ___ jednadžba.", "Clairautova"),
    ("Jednadžba oblika $y = t f(y') + g(y')$ naziva se ___ jednadžba.", "Lagrangeova"),
    ("Rješenje u čijim se točkama ruši jedinstvenost Cauchyjeve zadaće te se ne može dobiti iz općeg rješenja uvrštavanjem konstante naziva se ___ rješenje.", "singularno"),
    ("Geometrijski gledano, singularno rješenje Clairautove jednadžbe predstavlja ___ familije pravaca zadanih općim rješenjem.", "anvelopu"),
    ("Sustav od $n$ diferencijalnih jednadžbi prvog reda $y'=f(t,y)$ može se zapisati u vektorskom obliku gdje je $y$ vektor u prostoru ___.", "R^n"),
    ("Ako su $y_1,\\dots,y_n$ rješenja homogenog linearnog sustava $y'=A(t)y$, matrica $X(t)$ čiji su stupci ta rješenja naziva se ___ matrica.", "fundamentalna"),
    ("Determinanta fundamentalne matrice naziva se ___.", "Vronskijan"),
    ("Liouvilleova formula povezuje Vronskijan s tragom matrice $A(t)$ izrazom $W(t) = W(t_0)\\exp(\\int_{t_0}^t$ ___ $ds)$.", "tr(A(s))"),
    ("Ako je Vronskijan u jednoj točki jednak nuli, tada su rješenja $y_1,\\dots,y_n$ linearno ___.", "zavisna"),
    ("Za matricu $A \\in M_n(\\mathbb{R})$, matrica $e^{tA}$ definira se redom $e^{tA} = \\sum_{k=0}^\\infty$ ___.", "(t^k*A^k)/k!"),
    ("Ako matrice $A$ i $B$ komutiraju ($AB=BA$), tada vrijedi $e^{A+B} =$ ___.", "e^A*e^B"),
    ("Rješenje homogene linearne jednadžbe s konstantnim koeficijentima traži se u obliku $y(t) = e^($ ___ $)$.", "lambda*t"),
    ("Polinom $P(\\lambda) = \\det(A-\\lambda I)$ ili polinom dobiven uvrštavanjem $y=e^{\\lambda t}$ u jednadžbu $n$-tog reda naziva se ___ polinom.", "karakteristicni"),
    ("Ako je $\\lambda = a+ib$ kompleksni korijen karakterističnog polinoma, realni dio rješenja dan je funkcijom $e^{at} \\cdot$ ___.", "cos(bt)"),
    ("Ako je $\\lambda$ $k$-struki realni korijen karakterističnog polinoma, pripadna baza rješenja uključuje funkcije $e^{\\lambda t}, te^{\\lambda t}, \\dots,$ ___.", "t^(k-1)*e^(lambda*t)"),
    ("Za određivanje partikularnog rješenja nehomogenog sustava $y'=Ay+b(t)$ može se upotrijebiti formula $y_p(t) = \\int_{t_0}^t e^{(t-s)A} \\cdot$ ___ $ds$.", "b(s)"),
    ("Linearni operator $L[y] = y'' + p(t)y' + q(t)y$ preslikava prostor $C^2(I)$ u prostor ___.", "C(I)"),
    ("Skup svih rješenja homogene linearne jednadžbe $n$-tog reda čini vektorski prostor dimenzije ___.", "n"),
    ("Ravnotežna točka $y^*$ je ___ po Ljapunovu ako za svaki $\\varepsilon>0$ postoji $\\delta>0$ takav da iz $\\|y(0)-y^*\\|<\\delta$ slijedi $\\|y(t)-y^*\\|<\\varepsilon$ za sve $t \\ge 0$.", "stabilna"),
    ("Ako je ravnotežna točka stabilna po Ljapunovu i dodatno $\\lim_{t\\to\\infty} y(t) = y^*$, tada je ona ___ stabilna.", "asimptotski"),
    ("Ako sve svojstvene vrijednosti matrice $A$ imaju strogo negativne realne dijelove, ishodište je ___ stabilna ravnotežna točka.", "asimptotski"),
    ("Ako barem jedna svojstvena vrijednost matrice $A$ ima pozitivan realni dio, ishodište je ___ ravnotežna točka.", "nestabilna"),
    ("Metoda traženja rješenja u obliku reda $y(t) = \\sum_{n=0}^\\infty a_n(t-t_0)^n$ primjenjuje se oko ___ točaka koeficijenata jednadžbe.", "regularnih"),
]

# ---------------------------------------------------------------------------
# Flash kartice (25)
# ---------------------------------------------------------------------------
FLASHCARD = [
    ("Što je to Cauchyjeva zadaća (problem početnih uvjeta) za ODJ prvog reda?",
     "Sastoji se od diferencijalne jednadžbe $y' = f(t,y)$ i početnog uvjeta $y(t_0) = y_0$. Traži se rješenje $y(t)$ definirano na intervalu koji sadrži $t_0$."),
    ("Kako glasi Picard-Lindelöfov teorem o egzistenciji i jedinstvenosti?",
     "Ako je $f(t,y)$ neprekidna na pravokutniku $S=[t_0-a,t_0+a]\\times[y_0-b,y_0+b]$ i zadovoljava Lipschitzov uvjet po $y$ na $S$, Cauchyjeva zadaća ima jedinstveno rješenje na $[t_0-h,t_0+h]$, gdje je $h=\\min\\{a,b/M\\}$, a $M=\\max|f(t,y)|$ na $S$."),
    ("Što tvrdi Peanov teorem i po čemu se razlikuje od Picardovog?",
     "Tvrdi da ako je $f$ neprekidna, rješenje Cauchyjeve zadaće postoji lokalno. Razlikuje se jer NE zahtijeva Lipschitzov uvjet i NE jamči jedinstvenost rješenja."),
    ("Što opisuje Gronwallova lema?",
     "Pokazuje da ako neprekidna funkcija $u(t)$ zadovoljava integralnu nejednakost $u(t) \\le \\alpha(t) + \\int \\beta(s)u(s)\\,ds$, tada se $u(t)$ može omeđiti odgovarajućom eksponencijalnom funkcijom. Koristi se za ocjene i jedinstvenost."),
    ("Koja je definicija Lipschitzovog uvjeta za funkciju $f(t,y)$?",
     "Funkcija $f$ je Lipschitzova po $y$ na $\\Omega$ ako postoji konstanta $L>0$ takva da za sve $(t,y_1), (t,y_2) \\in \\Omega$ vrijedi $|f(t,y_1)-f(t,y_2)| \\le L|y_1-y_2|$."),
    ("Kako se rješava jednadžba s odvojenim varijablama $y' = g(t)h(y)$?",
     "Napiše se u obliku $\\frac{dy}{h(y)} = g(t)\\,dt$ te se obje strane integriraju: $\\int \\frac{1}{h(y)}\\,dy = \\int g(t)\\,dt + C$."),
    ("Koji je opći oblik nehomogene linearne jednadžbe 1. reda i kako glasi njeno rješenje?",
     "Oblik: $y' + a(t)y = b(t)$. Rješenje: $y(t) = e^{-A(t)}\\left[\\int b(t)e^{A(t)}\\,dt + C\\right]$, gdje je $A(t) = \\int a(t)\\,dt$."),
    ("Koja je definicija Bernoullijeve jednadžbe i kojom se supstitucijom rješava?",
     "Jednadžba oblika $y' + a(t)y = b(t)y^\\alpha$ ($\\alpha \\ne 0,1$). Rješava se supstitucijom $z=y^{1-\\alpha}$, čime prelazi u linearnu jednadžbu po $z$."),
    ("Koja je definicija Riccatijeve jednadžbe i kako se svodi na Bernoullijevu?",
     "Oblik: $y' + a(t)y + b(t)y^2 = c(t)$. Ako je poznato jedno partikularno rješenje $y_1(t)$, supstitucijom $y(t)=y_1(t)+z(t)$ jednadžba prelazi u Bernoullijevu po $z$ s $\\alpha=2$."),
    ("Što je to egzaktna diferencijalna jednadžba?",
     "Jednadžba $P(t,y)dt+Q(t,y)dy=0$ je egzaktna ako je lijeva strana potpuni diferencijal neke funkcije $U(t,y)$, tj. $dU = P\\,dt+Q\\,dy$. Rješenje je $U(t,y)=C$."),
    ("Što je Eulerov multiplikator (integrirajući faktor)?",
     "Funkcija $\\mu(t,y)$ kojom se množi neegzaktna jednadžba $P\\,dt+Q\\,dy=0$ kako bi nova jednadžba $\\mu P\\,dt + \\mu Q\\,dy = 0$ postala egzaktna."),
    ("Što je to Clairautova jednadžba i kakva rješenja ima?",
     "Oblik: $y = t y' + g(y')$. Ima familiju općih rješenja $y = Ct + g(C)$ te jedno singularno rješenje dobiveno eliminacijom $p=y'$ iz sustava $y=tp+g(p)$ i $t+g'(p)=0$."),
    ("Što je singularno rješenje diferencijalne jednadžbe?",
     "Rješenje Cauchyjeve zadaće u čijoj se svakoj točki gubi jedinstvenost (siječe druga rješenja), te se ne može dobiti iz općeg rješenja izborom konstante $C$."),
    ("Što je fundamentalni sustav rješenja linearnog homogenog sustava?",
     "Skup od $n$ linearno neovisnih rješenja $\\{y_1(t),\\dots,y_n(t)\\}$ homogenog linearnog sustava $y'=A(t)y$ reda $n$."),
    ("Što je Vronskijan (determinanta Wronskog) i čemu služi?",
     "Determinanta fundamentalne matrice $X(t)$ nastale od stupčanih rješenja $y_1,\\dots,y_n$. Rješenja su linearno neovisna ako i samo ako je $W(t) \\ne 0$."),
    ("Kako glasi Liouvilleova formula za Vronskijan?",
     "$W(t) = W(t_0)\\exp\\left(\\int_{t_0}^t \\text{tr}(A(s))\\,ds\\right)$, gdje je $\\text{tr}(A(s))$ trag matrice $A(s)$."),
    ("Kako se izračunava matrična funkcija $e^{tA}$ ako se $A$ može dijagonalizirati ($A=PDP^{-1}$)?",
     "$e^{tA} = P e^{tD} P^{-1}$, gdje je $e^{tD}$ dijagonalna matrica s elementima $e^{t\\lambda_i}$ na dijagonali."),
    ("Što je Jordanova klijetka (blok) i kada se koristi pri računanju $e^{tA}$?",
     "Jordanova klijetka $J_k(\\lambda)$ je $k\\times k$ matrica s $\\lambda$ na dijagonali i $1$ iznad dijagonale. Koristi se za matrice koje se ne mogu dijagonalizirati."),
    ("Kako glasi formula za varijaciju konstanti kod nehomogenih linearnih sustava $y'=A(t)y+b(t)$?",
     "Ako je $X(t)$ fundamentalna matrica homogene zadaće, partikularno rješenje je $y_p(t) = X(t)\\int X(s)^{-1}b(s)\\,ds$."),
    ("Što je karakteristični polinom za linearnu jednadžbu s konstantnim koeficijentima?",
     "Polinom $P(\\lambda)$ dobiven uvrštavanjem pretpostavke $y=e^{\\lambda t}$ u jednadžbu. Njegove nultočke određuju eksponente u baznim rješenjima."),
    ("Ako je $\\lambda = a+ib$ kompleksni korijen karakterističnog polinoma, koja rješenja nastaju?",
     "Nastaju dva realna linearno neovisna rješenja: $y_1(t)=e^{at}\\cos(bt)$ i $y_2(t)=e^{at}\\sin(bt)$."),
    ("Što je stacionarna (ravnotežna) točka sustava $y'=f(y)$?",
     "Točka $y^* \\in \\mathbb{R}^n$ za koju vrijedi $f(y^*)=0$. Ako sustav krene u $y^*$, u njoj ostaje zauvijek."),
    ("Koja je definicija stabilnosti po Ljapunovu?",
     "Stacionarna točka $y^*$ je stabilna po Ljapunovu ako za svaki $\\varepsilon>0$ postoji $\\delta>0$ takav da za svako rješenje s $\\|y(0)-y^*\\|<\\delta$ vrijedi $\\|y(t)-y^*\\|<\\varepsilon$ za sve $t \\ge 0$."),
    ("Što označava asimptotska stabilnost ravnotežne točke?",
     "Znači da je točka stabilna po Ljapunovu i dodatno postoji $\\delta_0>0$ takav da ako je $\\|y(0)-y^*\\|<\\delta_0$, tada $\\lim_{t\\to\\infty} y(t)=y^*$."),
    ("Kako se stabilnost linearnog autonomnog sustava $y'=Ay$ određuje preko svojstvenih vrijednosti?",
     "Asimptotski stabilno: $\\text{Re}(\\lambda)<0$ za sve svojstvene vrijednosti. Nestabilno: barem jedna ima $\\text{Re}(\\lambda)>0$. Stabilno (ne asimptotski): barem jedna ima $\\text{Re}(\\lambda)=0$ (s jednostavnim Jordanovim blokovima), ostale $\\text{Re}(\\lambda)<0$."),
]

# ---------------------------------------------------------------------------
# Visestruki odabir (20)
# ---------------------------------------------------------------------------
MCQ = [
    ("Koji je red diferencijalne jednadžbe $(y'')^3 + t^4(y''')^2 + e^t y = 0$?",
     ["2", "3", "4", "6"], 1),
    ("Prema Picard-Lindelöfovom teoremu za $y'=f(t,y)$, koja svojstva funkcije $f$ osiguravaju jedinstvenost rješenja?",
     ["Neprekidnost po $t$ i Lipschitzov uvjet po $y$", "Samo omeđenost funkcije $f$",
      "Samo monotonost po $t$", "Diferencijabilnost po $t$"], 0),
    ("Za Cauchyjevu zadaću $y' = y^{1/3}$, $y(0)=0$ vrijedi:",
     ["Ima jedinstveno rješenje $y(t)=0$", "Nema nijedno rješenje",
      "Ima beskonačno mnogo rješenja jer desna strana nije Lipschitzova u $y=0$", "Rješenje ide u beskonačnost u konačnom vremenu"], 2),
    ("Jednadžba $y' + P(t)y = Q(t)y^n$ za $n=0$ predstavlja:",
     ["Bernoullijevu jednadžbu s $n=0$, što je zapravo nehomogena linearna jednadžba", "Riccatijevu jednadžbu",
      "Clairautovu jednadžbu", "Jednadžbu drugog reda"], 0),
    ("Opće rješenje jednadžbe s odvojenim varijablama $y' = 2ty$ je:",
     ["$y(t)=C+t^2$", "$y(t)=Ce^{t^2}$", "$y(t)=e^{2t}+C$", "$y(t)=Ct^2$"], 1),
    ("Supstitucija $u=y/t$ koristi se za rješavanje:",
     ["Egzaktnih jednadžbi", "Homogenih diferencijalnih jednadžbi prvog reda", "Bernoullijevih jednadžbi", "Riccatijevih jednadžbi"], 1),
    ("Uvjet da bi diferencijalni oblik $M(t,y)dt+N(t,y)dy$ bio egzaktan na jednostavno povezanom području jest:",
     ["$dM/dt = dN/dy$", "$dM/dy = dN/dt$", "$M \\cdot N = 1$", "$dM/dy + dN/dt = 0$"], 1),
    ("Eulerov multiplikator $\\mu(t)$ koji ovisi samo o $t$ postoji za $P\\,dt+Q\\,dy=0$ ako izraz $\\frac{1}{Q}(dP/dy - dQ/dt)$ ovisi samo o:",
     ["$y$", "$t$", "$t \\cdot y$", "konstanti"], 1),
    ("Opće rješenje Clairautove jednadžbe $y = ty' + (y')^2$ je familija:",
     ["Kružnica", "Pravaca $y=Ct+C^2$", "Parabola $y=Ct^2$", "Eksponencijalnih funkcija"], 1),
    ("Ako su $y_1(t)$ i $y_2(t)$ dva rješenja nehomogene linearne jednadžbe $L[y]=b(t)$, njihova razlika $y_1(t)-y_2(t)$ je:",
     ["Rješenje homogene jednadžbe $L[y]=0$", "Rješenje nehomogene jednadžbe $L[y]=2b(t)$",
      "Uvijek jednako nula", "Nije rješenje niti jedne jednadžbe"], 0),
    ("Dimenzija prostora rješenja homogene linearne diferencijalne jednadžbe 4. reda jest:",
     ["1", "2", "4", "Beskonačno"], 2),
    ("Ako su rješenja homogene linearne jednadžbe 2. reda $y_1=e^t$ i $y_2=e^{-t}$, njihov Vronskijan $W(t)$ iznosi:",
     ["0", "-2", "$2e^t$", "$e^{2t}$"], 1),
    ("Koje je opće rješenje jednadžbe $y''+4y=0$?",
     ["$y(t)=C_1 e^{2t}+C_2 e^{-2t}$", "$y(t)=C_1\\cos(2t)+C_2\\sin(2t)$",
      "$y(t)=(C_1+C_2 t)e^{2t}$", "$y(t)=C_1\\cos(4t)+C_2\\sin(4t)$"], 1),
    ("Karakteristični polinom jednadžbe $y''-6y'+9y=0$ ima:",
     ["Dva različita realna korijena $\\lambda=3,-3$", "Dvostruki realni korijen $\\lambda=3$",
      "Kompleksno konjugirane korijene $3\\pm 3i$", "Jedan korijen $\\lambda=9$"], 1),
    ("Opće rješenje jednadžbe $y''-6y'+9y=0$ glasi:",
     ["$y(t)=C_1e^{3t}+C_2e^{-3t}$", "$y(t)=C_1e^{3t}+C_2te^{3t}$",
      "$y(t)=C_1\\cos(3t)+C_2\\sin(3t)$", "$y(t)=(C_1+C_2t^2)e^{3t}$"], 1),
    ("Ako je $A$ dijagonalna matrica $\\text{diag}(2,-3)$, tada je matrična funkcija $e^{tA}$ jednaka:",
     ["$\\text{diag}(e^{2t}, e^{-3t})$", "$\\text{diag}(2t,-3t)$", "$\\text{diag}(e^2,e^{-3})$", "Matrici sa svim elementima jednakim $e^{-t}$"], 0),
    ("Za $2\\times2$ matricu $A$ s $\\text{tr}(A)=-4$ i $\\det(A)=3$, svojstvene vrijednosti su:",
     ["$-1$ i $-3$", "$1$ i $3$", "$-2$ i $-2$", "$2$ i $-6$"], 0),
    ("Sustav $y'=Ay$ s matricom $A$ koja ima svojstvene vrijednosti $\\lambda_1=-1$ i $\\lambda_2=-3$ u ishodištu ima ravnotežnu točku koja je:",
     ["Nestabilni čvor", "Asimptotski stabilni čvor", "Sedlo", "Centar"], 1),
    ("Ako su svojstvene vrijednosti matrice $A$ jednake $\\lambda = \\pm 2i$ (čisto imaginarne), ishodište je:",
     ["Asimptotski stabilan fokus", "Nestabilan fokus", "Centar (stabilan po Ljapunovu, ali ne i asimptotski)", "Sedlo"], 2),
    ("Ako matrica $A$ ima svojstvene vrijednosti $\\lambda_1=2$ i $\\lambda_2=-5$, ishodište za sustav $y'=Ay$ je:",
     ["Asimptotski stabilan čvor", "Sedlo (nestabilno)", "Fokus", "Stabilan centar"], 1),
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