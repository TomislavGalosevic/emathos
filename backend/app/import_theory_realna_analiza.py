"""Jednokratni uvoz teorije za kolegij 'Realna analiza'."""

from .database import SessionLocal
from . import models

COURSE_NAME = "Realna analiza"

# ---------------------------------------------------------------------------
# Tocno / Netocno (50)
# ---------------------------------------------------------------------------
TRUEFALSE = [
    ("Realan vektorski prostor $\\mathbb{R}^n$ s euklidskim skalarnim produktom čini unitaran prostor.", True),
    ("Svaki unitaran prostor ujedno je i normiran prostor s normom induciranom skalarnim produktom.", True),
    ("Za $p$-normu na $\\mathbb{R}^n$ s $p=2$ dobivamo standardnu euklidsku normu.", True),
    ("Dvije norme na vektorskom prostoru $X$ su ekvivalentne ako postoje $m,M>0$ takvi da je $m\\|x\\| \\le \\|x\\|' \\le M\\|x\\|$ za svaki $x\\in X$.", True),
    ("Relacija ekvivalencije normi zadovoljava refleksivnost, simetričnost i tranzitivnost.", True),
    ("Ekvivalentne norme na vektorskom prostoru induciraju ekvivalentne metrike.", True),
    ("Metrika $d(x,y)=\\|x-y\\|$ naziva se metrika inducirana normom.", True),
    ("Preslikavanje $f$ između metričkih prostora koje čuva udaljenost naziva se izometrija ako je bijekcija.", True),
    ("Svaki podskup omeđenog skupa u metričkom prostoru ujedno je i omeđen skup.", True),
    ("Unija konačno mnogo omeđenih skupova u metričkom prostoru je omeđen skup.", True),
    ("Presjek konačno mnogo omeđenih skupova u metričkom prostoru je omeđen skup.", True),
    ("Prazan skup i cijeli prostor $X$ uvijek su otvoreni skupovi u bilo kojoj topologiji na $X$.", True),
    ("Proizvoljna unija otvorenih skupova u topološkom prostoru je otvoren skup.", True),
    ("Konačan presjek otvorenih skupova u topološkom prostoru je otvoren skup.", True),
    ("Relativna topologija $T_Y$ na podskupu $Y$ topološkog prostora $(X,T)$ definirana je kao familija skupova $U\\cap Y$ za sve $U\\in T$.", True),
    ("Za bilo koji podskup $A$ topološkog prostora vrijedi $\\text{Int}\\,A \\subseteq A$.", True),
    ("Skup $A$ je otvoren ako i samo ako je jednak svom interioru, tj. $A=\\text{Int}\\,A$.", True),
    ("Za bilo koje podskupove $A$ i $B$ vrijedi $\\text{Int}(A\\cap B) = \\text{Int}\\,A \\cap \\text{Int}\\,B$.", True),
    ("Za bilo koji podskup $A$ topološkog prostora vrijedi $A \\subseteq \\text{Cl}\\,A$.", True),
    ("Skup $A$ je zatvoren ako i samo ako je jednak svom zatvaraču, tj. $A=\\text{Cl}\\,A$.", True),
    ("Za bilo koje podskupove $A$ i $B$ vrijedi $\\text{Cl}(A\\cup B) = \\text{Cl}\\,A \\cup \\text{Cl}\\,B$.", True),
    ("Svaki konvergentan niz u metričkom prostoru je Cauchyjev niz.", True),
    ("Svaki Cauchyjev niz u metričkom prostoru je omeđen.", True),
    ("Uniformno neprekidno preslikavanje između metričkih prostora preslikava Cauchyjeve nizove u Cauchyjeve nizove.", True),
    ("Kompaktan skup u metričkom prostoru $(X,d)$ je omeđen i zatvoren.", True),
    ("Bilo koji presjek beskonačno mnogo otvorenih skupova u topološkom prostoru uvijek je otvoren skup.", False),
    ("Bilo koja unija beskonačno mnogo zatvorenih skupova u topološkom prostoru uvijek je zatvoren skup.", False),
    ("Pravac $\\mathbb{R}$ uz standardnu euklidsku metriku je kompaktan skup.", False),
    ("Svaki Cauchyjev niz u bilo kojem metričkom prostoru je konvergentan.", False),
    ("Limes niza u bilo kojem općem topološkom prostoru mora biti jedinstven.", False),
    ("Za bilo koja dva podskupa $A$ i $B$ topološkog prostora vrijedi $\\text{Int}(A\\cup B) = \\text{Int}\\,A \\cup \\text{Int}\\,B$.", False),
    ("Za bilo koja dva podskupa $A$ i $B$ topološkog prostora vrijedi $\\text{Cl}(A\\cap B) = \\text{Cl}\\,A \\cap \\text{Cl}\\,B$.", False),
    ("Svako neprekidno preslikavanje između metričkih prostora preslikava Cauchyjeve nizove u Cauchyjeve nizove.", False),
    ("Diskretan metrički prostor ima samo trivijalne otvorene skupove.", False),
    ("Skup $A$ je otvoren ako i samo ako je jednak svom zatvaraču $A=\\text{Cl}\\,A$.", False),
    ("Ako je skup $A$ omeđen u metričkom prostoru, onda je njegov zatvarač $\\text{Cl}\\,A$ neomeđen.", False),
    ("Svaki omeđen niz u proizvoljnom metričkom prostoru ima konvergentan podniz.", False),
    ("Ako je preslikavanje $f:X\\to Y$ Lipschitzovo, ono ne mora biti uniformno neprekidno.", False),
    ("Ako je $f:X\\to Y$ homeomorfizam, onda $f$ ne mora biti bijekcija.", False),
    ("Otvorena kugla $K(x_0,r)$ u metričkom prostoru je uvijek zatvoren skup.", False),
    ("Topološki prostor $X$ je povezan ako se može prikazati kao unija dva neprazna disjunktna otvorena skupa.", False),
    ("Proizvoljan presjek zatvorenih skupova ne mora biti zatvoren skup.", False),
    ("Kriterij homogenosti skalarnog produkta dopušta negativne skalare bez izvlačenja modula.", True),
    ("Ako je $d$ pseudometrika, tada iz $d(x,y)=0$ nužno slijedi $x=y$.", False),
    ("Skup $A$ je gust u $X$ ako je njegov interior jednak cijelom prostoru $X$, tj. $\\text{Int}\\,A=X$.", False),
    ("Za svaki podskup $A$ topološkog prostora vrijedi $\\text{Cl}(\\text{Cl}\\,A) \\ne \\text{Cl}\\,A$.", False),
    ("Za svaki podskup $A$ topološkog prostora vrijedi $\\text{Int}(\\text{Int}\\,A) \\ne \\text{Int}\\,A$.", False),
    ("Ako je preslikavanje neprekidno, slika svakog otvorenog skupa je nužno otvoren skup.", False),
    ("Prostor je separabilan ako sadrži neprebrojiv gust podskup.", False),
    ("Gomilište $x_0$ skupa $A$ u topološkom prostoru mora pripadati skupu $A$.", False),
]

# ---------------------------------------------------------------------------
# Nadopuni recenicu (50) - odgovor je OBICAN TEKST (usporeduje se doslovno)
# ---------------------------------------------------------------------------
FILLIN = [
    ("Funkcija $\\|\\cdot\\|:X\\to\\mathbb{R}$ na vektorskom prostoru $X$ naziva se norma ako za sve $x,y\\in X$ i $\\lambda\\in\\mathbb{R}$ zadovoljava aksiome: nenegativnost, strogost, homogenost $\\|\\lambda x\\|=|\\lambda|\\|x\\|$ i nejednakost ___.", "trokuta"),
    ("Euklidska norma na $\\mathbb{R}^n$ inducirana je standardnim euklidskim ___ produktom.", "skalarnim"),
    ("Dvije norme $\\|\\cdot\\|$ i $\\|\\cdot\\|'$ na vektorskom prostoru $X$ su ekvivalentne ako postoje $m,M>0$ takvi da vrijedi $m\\|x\\| \\le \\|x\\|' \\le$ ___ za svaki $x\\in X$.", "M||x||"),
    ("Ekvivalencija normi na vektorskom prostoru je relacija ___.", "ekvivalencije"),
    ("Ekvivalentne norme na vektorskom prostoru induciraju ___ metrike.", "ekvivalentne"),
    ("Ako metrička funkcija $d$ zadovoljava $d(x,y)=0$ samo u jednom smjeru ($x=y \\Rightarrow d(x,y)=0$), tada $d$ nazivamo ___.", "pseudometrika"),
    ("Metrika $d$ na $X$ definirana s $d(x,y)=0$ ako je $x=y$, te $d(x,y)=1$ ako je $x\\ne y$ naziva se ___ metrika.", "diskretna"),
    ("Preslikavanje $f:X\\to Y$ između metričkih prostora koje zadovoljava $d_Y(f(x),f(y))=d_X(x,y)$ i bijekcija je naziva se ___.", "izometrija"),
    ("Nenegativan broj $\\text{diam}\\,A = \\sup\\{d(x,y):x,y\\in A\\}$ naziva se ___ skupa $A$.", "dijametar"),
    ("Skup $A$ u metričkom prostoru je omeđen ako mu je dijametar ___.", "konacan"),
    ("Svaki podskup omeđenog skupa je ___ skup.", "omedjen"),
    ("Unija konačno mnogo omeđenih skupova je ___ skup.", "omedjen"),
    ("Presjek konačno mnogo omeđenih skupova je ___ skup.", "omedjen"),
    ("Familija $\\mathcal{U}$ otvorenih skupova na $X$ čini topologiju na $X$ ako sadrži prazan skup i $X$, te je zatvorena na proizvoljne unije i ___ presjeke.", "konacne"),
    ("Ako je $(X,T)$ topološki prostor i $Y\\subseteq X$, familija $T_Y = \\{U\\cap Y : U\\in T\\}$ naziva se ___ topologija na $Y$.", "relativna"),
    ("Najveći otvoren skup sadržan u skupu $A$ naziva se ___ skupa $A$.", "interior"),
    ("Za svaki podskup $A$ topološkog prostora vrijedi $\\text{Int}\\,A \\subseteq$ ___.", "A"),
    ("Operacija interiora zadovoljava svojstvo idempotentnosti, tj. $\\text{Int}(\\text{Int}\\,A) =$ ___.", "Int A"),
    ("Skup $A$ je otvoren ako i samo ako vrijedi $A =$ ___.", "Int A"),
    ("Za proizvoljne podskupove $A$ i $B$ vrijedi $\\text{Int}(A\\cap B) = \\text{Int}\\,A \\cap$ ___.", "Int B"),
    ("Najmanji zatvoreni skup koji sadrži skup $A$ naziva se ___ skupa $A$.", "zatvarac"),
    ("Za svaki podskup $A$ topološkog prostora vrijedi $A \\subseteq$ ___.", "Cl A"),
    ("Operacija zatvarača je idempotentna, odnosno $\\text{Cl}(\\text{Cl}\\,A) =$ ___.", "Cl A"),
    ("Skup $A$ je zatvoren ako i samo ako vrijedi $A =$ ___.", "Cl A"),
    ("Za proizvoljne podskupove $A$ i $B$ vrijedi $\\text{Cl}(A\\cup B) = \\text{Cl}\\,A \\cup$ ___.", "Cl B"),
    ("Za skup $A$ kažemo da je gust u $X$ ako je njegov zatvarač jednak ___.", "X"),
    ("Topološki prostor u kojem se svake dvije različite točke mogu separirati disjunktnim otvorenim okolinama naziva se ___ (ili $T_2$) prostor.", "Hausdorffov"),
    ("Limes konvergentnog niza u metričkom prostoru je ___.", "jedinstven"),
    ("Svaki konvergentan niz u metričkom prostoru je ___.", "Cauchyjev"),
    ("Svaki Cauchyjev niz u metričkom prostoru je ___.", "omedjen"),
    ("Metrički prostor u kojem svaki Cauchyjev niz konvergira naziva se ___ metrički prostor.", "potpun"),
    ("Bolzano-Weierstrassov teorem za nizove tvrdi da svaki omeđen niz u $\\mathbb{R}^n$ ima ___ podniz.", "konvergentan"),
    ("Preslikavanje $f:X\\to Y$ je neprekidno u $x_0$ u metričkom prostoru ako za svaki $\\varepsilon>0$ postoji $\\delta>0$ takav da iz $d_X(x,x_0)<\\delta$ slijedi $d_Y(f(x),f(x_0))<$ ___.", "epsilon"),
    ("Heineova karakterizacija neprekidnosti tvrdi da je $f$ neprekidno u $x_0$ akko za svaki niz $(x_n)$ koji konvergira prema $x_0$ pripadni niz $f(x_n)$ konvergira prema ___.", "f(x0)"),
    ("Preslikavanje $f:X\\to Y$ je Lipschitzovo ako postoji $\\lambda \\ge 0$ takav da za sve $x,y\\in X$ vrijedi $d_Y(f(x),f(y)) \\le$ ___.", "lambda*d_X(x,y)"),
    ("Preslikavanje $f:X\\to Y$ kod kojeg je slika svakog otvorenog skupa otvoren skup naziva se ___ preslikavanje.", "otvoreno"),
    ("Preslikavanje $f:X\\to Y$ kod kojeg je slika svakog zatvorenog skupa zatvoren skup naziva se ___ preslikavanje.", "zatvoreno"),
    ("Uniformno neprekidno preslikavanje preslikava Cauchyjeve nizove u ___ nizove.", "Cauchyjeve"),
    ("Za skup $K$ u topološkom prostoru kažemo da je kompaktan ako se svaki njegov otvoreni pokrivač može reducirati na ___ potpokrivač.", "konacan"),
    ("U metričkom prostoru skup $K$ je kompaktan ako i samo ako svaki niz u $K$ ima konvergentan podniz s limesom u ___.", "K"),
    ("Borel-Lebesgueov teorem tvrdi da je podskup $K$ u $\\mathbb{R}^n$ kompaktan ako i samo ako je omeđen i ___.", "zatvoren"),
    ("Kompaktan skup $K$ u metričkom prostoru $(X,d)$ je omeđen i ___.", "zatvoren"),
    ("Pravac $\\mathbb{R}$ uz standardnu euklidsku metriku ___ kompaktan skup.", "nije"),
    ("Topološki prostor $X$ je povezan ako se ne može prikazati kao unija dva neprazna disjunktna ___ skupa.", "otvorena"),
    ("Topološki prostor je povezan akko je svako neprekidno preslikavanje $f:X\\to\\{0,1\\}$ (gdje $\\{0,1\\}$ ima diskretnu metriku) ___.", "konstantno"),
    ("Prostor $X$ naziva se separabilan ako sadrži ___ gust podskup.", "prebrojiv"),
    ("Za familiju podskupova kažemo da ima svojstvo konačnih presjeka ako je svaki ___ presjek elemenata te familije neprazan.", "konacan"),
    ("Lema o cijevi promatra kompaktan prostor $Y$ i tvrdi da svaka otvorena okolina cijevi sadrži traku oblika ___ gdje je $V$ otvorena okolina u $X$.", "V x Y"),
    ("Ako je $A\\subseteq X$ gust skup i $Y$ potpun metrički prostor, svako uniformno neprekidno preslikavanje $f:A\\to Y$ može se na jedinstven način ___ do uniformno neprekidnog preslikavanja $g:X\\to Y$.", "prosiriti"),
    ("Pseudometrika $d$ na $X$ razlikuje se od metrike po tome što iz $d(x,y)=0$ ne mora slijediti ___.", "x=y"),
]

# ---------------------------------------------------------------------------
# Flash kartice (25)
# ---------------------------------------------------------------------------
FLASHCARD = [
    ("Iskaži teorem o ekvivalenciji normi.",
     "Relacija ekvivalencije normi na vektorskom prostoru $X$ zadovoljava refleksivnost ($\\|\\cdot\\| \\sim \\|\\cdot\\|$), simetričnost ($\\|\\cdot\\| \\sim \\|\\cdot\\|' \\Rightarrow \\|\\cdot\\|' \\sim \\|\\cdot\\|$) i tranzitivnost ($\\|\\cdot\\| \\sim \\|\\cdot\\|'$ i $\\|\\cdot\\|' \\sim \\|\\cdot\\|'' \\Rightarrow \\|\\cdot\\| \\sim \\|\\cdot\\|''$)."),
    ("Iskaži teorem o ekvivalentnim normama i metrikama.",
     "Ako su $\\|\\cdot\\|$ i $\\|\\cdot\\|'$ ekvivalentne norme na $X$ (postoje $m,M>0$ t.d. $m\\|x\\| \\le \\|x\\|' \\le M\\|x\\|$), tada su pripadne inducirane metrike $d$ i $d'$ ekvivalentne ($m\\,d(x,y) \\le d'(x,y) \\le M\\,d(x,y)$)."),
    ("Iskaži tvrdnje korolara o omeđenosti skupova u metričkom prostoru.",
     "Neka je $(X,d)$ metrički prostor. Vrijedi: a) Svaki podskup omeđenog skupa je omeđen. b) Presjek konačno mnogo omeđenih skupova je omeđen. c) Unija konačno mnogo omeđenih skupova je omeđen."),
    ("Iskaži teorem o relativnoj topologiji na podskupu $Y$.",
     "Neka je $(X,T)$ topološki prostor i $Y\\subseteq X$. Tada je familija $T_Y = \\{U\\cap Y : U\\in T\\}$ topologija na $Y$."),
    ("Iskaži teorem o svojstvima interiora skupa.",
     "Neka je $(X,T)$ topološki prostor i $A,B\\subseteq X$. Vrijedi: 1) $\\text{Int}\\,A \\subseteq A$ 2) $\\text{Int}(\\text{Int}\\,A) = \\text{Int}\\,A$ 3) $A\\subseteq B \\Rightarrow \\text{Int}\\,A \\subseteq \\text{Int}\\,B$ 4) $\\text{Int}\\,X=X$ 5) $A$ otvoren $\\Leftrightarrow A=\\text{Int}\\,A$ 6) $\\text{Int}(A\\cap B)=\\text{Int}\\,A\\cap\\text{Int}\\,B$."),
    ("Iskaži teorem o svojstvima zatvarača skupa.",
     "Neka je $(X,T)$ topološki prostor i $A,B\\subseteq X$. Vrijedi: 1) $A\\subseteq\\text{Cl}\\,A$ 2) $\\text{Cl}(\\text{Cl}\\,A)=\\text{Cl}\\,A$ 3) $A\\subseteq B \\Rightarrow \\text{Cl}\\,A\\subseteq\\text{Cl}\\,B$ 4) $\\text{Cl}\\,\\emptyset=\\emptyset$ 5) $A$ zatvoren $\\Leftrightarrow A=\\text{Cl}\\,A$ 6) $\\text{Cl}(A\\cup B)=\\text{Cl}\\,A\\cup\\text{Cl}\\,B$."),
    ("Iskaži teorem o važnim svojstvima Cauchyjeva niza.",
     "U metričkom prostoru $(X,d)$ vrijedi: a) Svaki konvergentan niz je Cauchyjev niz. b) Svaki Cauchyjev niz je omeđen."),
    ("Iskaži teorem o uniformno neprekidnom preslikavanju i Cauchyjevim nizovima.",
     "Ako je $f:(X,d_X)\\to(Y,d_Y)$ uniformno neprekidno i $(x_n)$ Cauchyjev niz u $X$, tada je $(f(x_n))$ Cauchyjev niz u $Y$."),
    ("Iskaži tvrdnju i skicu dokaza da pravac $\\mathbb{R}$ nije kompaktan skup.",
     "Pravac $\\mathbb{R}$ nije kompaktan. Otvoreni pokrivač $\\{\\langle a,b\\rangle : a,b\\in\\mathbb{R}, a<b\\}$ ne može se reducirati na konačan potpokrivač jer za $r=\\max\\{b_1,\\dots,b_k\\}$ vrijedi da $r$ nije pokriven, pa potpokrivač ne prekriva cijeli $\\mathbb{R}$."),
    ("Iskaži teorem/korolar o kompaktnom skupu u metričkom prostoru.",
     "Kompaktan skup $K$ u metričkom prostoru $(X,d)$ je omeđen i zatvoren."),
    ("Iskaži teorem o ekvivalentnim uvjetima za povezanost topološkog prostora.",
     "Neka je $X$ topološki prostor. Ekvivalentno je: a) $X$ je povezan. b) $X$ se ne može prikazati kao unija dva neprazna disjunktna zatvorena skupa. c) Svako neprekidno preslikavanje $f:X\\to\\{0,1\\}$ je konstantno."),
    ("Što je to unitaran prostor?",
     "Uređeni par $(X,\\langle\\cdot,\\cdot\\rangle)$ koji se sastoji od realnog vektorskog prostora $X$ i skalarnog produkta $\\langle\\cdot,\\cdot\\rangle$ definiranog na $X$."),
    ("Koja četiri aksioma definiraju metriku na skupu $X$?",
     "M1) $d(x,y)\\ge 0$ (nenegativnost) M2) $d(x,y)=0 \\Leftrightarrow x=y$ (strogost) M3) $d(x,y)=d(y,x)$ (simetričnost) M4) $d(x,y) \\le d(x,z)+d(y,z)$ (nejednakost trokuta)."),
    ("Što je to otvoren skup u metričkom prostoru $(X,d)$?",
     "Skup $U\\subseteq X$ je otvoren ako za svaku točku $x_0\\in U$ postoji $r>0$ takav da je otvorena kugla $K(x_0,r)$ u potpunosti sadržana u $U$."),
    ("Koja tri aksioma definiraju topološki prostor $(X,\\mathcal{U})$?",
     "T1) $\\emptyset$ i $X$ pripadaju $\\mathcal{U}$. T2) Unija proizvoljne familije članova iz $\\mathcal{U}$ je član iz $\\mathcal{U}$. T3) Presjek konačno mnogo članova iz $\\mathcal{U}$ je član iz $\\mathcal{U}$."),
    ("Koja je definicija baze topologije?",
     "Familija $\\mathcal{B}$ je baza topologije $T$ ako se svaki element topologije $T$ može prikazati kao unija elemenata iz $\\mathcal{B}$."),
    ("Što je to Hausdorffov ($T_2$) prostor?",
     "Topološki prostor u kojem se za svake dvije različite točke $x$ i $y$ mogu pronaći disjunktne otvorene okoline $U_x$ i $U_y$ takve da je $U_x\\cap U_y=\\emptyset$."),
    ("Što je to potpun metrički prostor?",
     "Metrički prostor u kojem svaki Cauchyjev niz konvergira prema nekoj točki tog prostora."),
    ("Iskaži Bolzano-Weierstrassov teorem za nizove.",
     "Svaki omeđen niz u euklidskom prostoru $\\mathbb{R}^n$ ima konvergentan podniz."),
    ("Iskaži Heineovu karakterizaciju neprekidnosti preslikavanja.",
     "Preslikavanje $f:X\\to Y$ između metričkih prostora je neprekidno u $x_0$ ako i samo ako za svaki niz $(x_n)$ koji konvergira prema $x_0$ pripadni niz $(f(x_n))$ konvergira prema $f(x_0)$."),
    ("Koja je definicija Lipschitzovog preslikavanja?",
     "Preslikavanje $f:X\\to Y$ je Lipschitzovo ako postoji konstanta $\\lambda \\ge 0$ takva da za sve $x,y\\in X$ vrijedi $d_Y(f(x),f(y)) \\le \\lambda\\, d_X(x,y)$."),
    ("Što je to homeomorfizam?",
     "Neprekidna bijekcija $f:X\\to Y$ između topoloških prostora čiji je inverz $f^{-1}:Y\\to X$ također neprekidno preslikavanje."),
    ("Iskaži Borel-Lebesgueov teorem za skupove u $\\mathbb{R}^n$.",
     "Podskup $K$ u $\\mathbb{R}^n$ je kompaktan ako i samo ako je omeđen i zatvoren."),
    ("Što znači da skup $A$ ima svojstvo konačnih presjeka?",
     "Familija podskupova ima svojstvo konačnih presjeka ako je presjek bilo koje njezine konačne podfamilije neprazan."),
    ("Što je to separabilan topološki prostor?",
     "Topološki prostor $X$ je separabilan ako sadrži prebrojiv gust podskup."),
]

# ---------------------------------------------------------------------------
# Visestruki odabir (20) - pozicije tocnih odgovora ravnomjerno izmijesane
# ---------------------------------------------------------------------------
MCQ = [
    ("Koji od navedenih uvjeta definira nejednakost trokuta za normu na vektorskom prostoru?",
     ["$\\|x+y\\| \\ge \\|x\\|+\\|y\\|$", "$\\|\\lambda x\\|=|\\lambda|\\|x\\|$",
      "$\\|x+y\\| \\le \\|x\\|+\\|y\\|$", "$\\|x\\|=0 \\Leftrightarrow x=0$"], 2),
    ("Ako su $\\|\\cdot\\|$ i $\\|\\cdot\\|'$ ekvivalentne norme na $X$, tada inducirane metrike $d$ i $d'$ zadovoljavaju:",
     ["$d(x,y)=d'(x,y)$ za sve $x,y$", "$m\\,d(x,y) \\le d'(x,y) \\le M\\,d(x,y)$ za neke $m,M>0$",
      "$d(x,y)+d'(x,y)=1$", "$d'(x,y) \\le d(x,y)/2$"], 1),
    ("Koji od navedenih iskaza NIJE točan za omeđene skupove u metričkom prostoru?",
     ["Svaki podskup omeđenog skupa je omeđen.", "Unija konačno mnogo omeđenih skupova je omeđena.",
      "Presjek konačno mnogo omeđenih skupova je omeđen.", "Unija proizvoljne beskonačne familije omeđenih skupova uvijek je omeđena."], 3),
    ("Za podskup $Y$ topološkog prostora $(X,T)$, relativna topologija $T_Y$ sastoji se od skupova oblika:",
     ["$U\\cup Y$ gdje je $U\\in T$", "$U\\cap Y$ gdje je $U\\in T$", "$U\\setminus Y$ gdje je $U\\in T$", "$Y\\setminus U$ gdje je $U\\in T$"], 1),
    ("Za interior bilo kojih podskupova $A$ i $B$ topološkog prostora uvijek vrijedi jednakost:",
     ["$\\text{Int}(A\\cup B)=\\text{Int}\\,A\\cup\\text{Int}\\,B$", "$\\text{Int}(A\\setminus B)=\\text{Int}\\,A\\setminus\\text{Int}\\,B$",
      "$\\text{Int}\\,A=\\text{Cl}\\,A$", "$\\text{Int}(A\\cap B)=\\text{Int}\\,A\\cap\\text{Int}\\,B$"], 3),
    ("Za zatvarač bilo kojih podskupova $A$ i $B$ topološkog prostora uvijek vrijedi jednakost:",
     ["$\\text{Cl}(A\\cup B)=\\text{Cl}\\,A\\cup\\text{Cl}\\,B$", "$\\text{Cl}(A\\cap B)=\\text{Cl}\\,A\\cap\\text{Cl}\\,B$",
      "$\\text{Cl}\\,A=\\text{Int}\\,A$", "$\\text{Cl}(A\\setminus B)=\\text{Cl}\\,A\\setminus\\text{Cl}\\,B$"], 0),
    ("Skup $A$ je zatvoren u topološkom prostoru ako i samo ako vrijedi:",
     ["$A=\\text{Int}\\,A$", "$\\text{Cl}\\,A=\\emptyset$", "$A=\\text{Cl}\\,A$", "$\\text{Int}\\,A=X$"], 2),
    ("Skup $A$ je otvoren u topološkom prostoru ako i samo ako vrijedi:",
     ["$A=\\text{Cl}\\,A$", "$\\text{Int}\\,A=\\emptyset$", "$\\text{Cl}\\,A=X$", "$A=\\text{Int}\\,A$"], 3),
    ("U metričkom prostoru $(X,d)$, za Cauchyjeve nizove vrijedi:",
     ["Svaki Cauchyjev niz je konvergentan i neomeđen.", "Svaki konvergentan niz je Cauchyjev i svaki Cauchyjev niz je omeđen.",
      "Niti jedan Cauchyjev niz nije omeđen.", "Svaki omeđen niz je ujedno i Cauchyjev."], 1),
    ("Uniformno neprekidno preslikavanje između metričkih prostora nužno čuva:",
     ["Cauchyjeve nizove", "Otvorenost svih skupova", "Izometriju prostora", "Neomeđenost skupova"], 0),
    ("Pravac $\\mathbb{R}$ uz standardnu euklidsku metriku NIJE kompaktan jer:",
     ["Nije zatvoren.", "Sadrži prebrojivo mnogo točaka.",
      "Nije omeđen (otvoreni pokrivač skupovima $\\langle a,b\\rangle$ ne može se reducirati na konačan potpokrivač).", "Nije povezan prostor."], 2),
    ("Svaki kompaktan skup u metričkom prostoru je nužno:",
     ["Otvoren i neomeđen", "Konvergentan i gust", "Diskretan i konačan", "Omeđen i zatvoren"], 3),
    ("Topološki prostor $X$ je povezan ako i samo ako je svako neprekidno preslikavanje $f:X\\to\\{0,1\\}$ (uz diskretnu metriku na $\\{0,1\\}$):",
     ["Konstantno", "Surjektivno", "Injektivno", "Neomeđeno"], 0),
    ("Za podskup $A$ u topološkom prostoru $X$ kažemo da je gust ako vrijedi:",
     ["$\\text{Int}\\,A=X$", "$\\text{Cl}\\,A=X$", "$A=\\emptyset$", "$\\text{Cl}\\,A=\\emptyset$"], 1),
    ("Prostor u kojem se svake dvije različite točke mogu separirati disjunktnim otvorenim okolinama naziva se:",
     ["Diskretan prostor", "Kompaktan prostor", "Hausdorffov ($T_2$) prostor", "Pseudometrički prostor"], 2),
    ("Metrički prostor u kojem svaki Cauchyjev niz konvergira naziva se:",
     ["Kompaktan prostor", "Homeomorfan prostor", "Diskretan prostor", "Potpun metrički prostor"], 3),
    ("Prema Borel-Lebesgueovom teoremu, podskup u $\\mathbb{R}^n$ je kompaktan akko je:",
     ["Omeđen i zatvoren", "Otvoren i omeđen", "Gust i prebrojiv", "Povezan i otvoren"], 0),
    ("Preslikavanje $f:X\\to Y$ je neprekidno u $x_0$ prema Heineovoj karakterizaciji ako za svaki niz $x_n\\to x_0$ vrijedi:",
     ["$f(x_n)\\to 0$", "$f(x_n)\\to f(x_0)$", "$f(x_n)$ je konstantan niz", "$d(f(x_n),x_0)\\to 0$"], 1),
    ("Topološki prostor je separabilan ako sadrži:",
     ["Neprebrojiv otvoren podskup", "Samo konačno mnogo točaka", "Prebrojiv gust podskup", "Diskretnu topologiju"], 2),
    ("Dijametar skupa $A$ u metričkom prostoru definiran je kao:",
     ["$\\sup\\{d(x,y):x,y\\in A\\}$", "$\\inf\\{d(x,y):x,y\\in A\\}$", "$\\max\\{\\|x\\|:x\\in A\\}$", "$\\min\\{d(x,x_0):x\\in A\\}$"], 0),
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