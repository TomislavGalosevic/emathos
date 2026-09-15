"""
Import zadataka za kolegij "Primjena diferencijalnog i integralnog racuna".
Pokretanje: python -m app.import_zadaci_pdir
"""

import json
from .database import Base, engine, SessionLocal
from . import models

COURSE_NAME = "Primjena diferencijalnog i integralnog racuna"

def multi(fields):
    return json.dumps(fields, ensure_ascii=False)

ZADACI = [
    {
        "tekst": r"Visina trokuta povećava se brzinom $1$ cm/min, dok se površina povećava brzinom $2$ cm²/min. "
                 r"Kojom brzinom se mijenja baza trokuta kada je visina $10$ cm, a površina $100$ cm²?",
        "tip": "auto",
        "tocan_odgovor": "-8/5",
        "rjesenje": r"$\dfrac{\mathrm{d}b}{\mathrm{d}t}=-\dfrac{8}{5}=-1{,}6$ cm/min (baza se smanjuje)",
        "hints": [
            r"$P=\frac{bv}{2}\Rightarrow\frac{\mathrm{d}P}{\mathrm{d}t}=\frac{1}{2}\!\left(\frac{\mathrm{d}b}{\mathrm{d}t}\cdot v+b\cdot\frac{\mathrm{d}v}{\mathrm{d}t}\right)$.",
            r"Iz $P=100$ i $v=10$: $b=20$. Uvrstite $\frac{\mathrm{d}P}{\mathrm{d}t}=2$, $\frac{\mathrm{d}v}{\mathrm{d}t}=1$."
        ]
    },
    {
        "tekst": r"Iz spremnika oblika obrnutog stošca (visina $6$ m, promjer baze $4$ m) curi voda brzinom "
                 r"$10000$ cm³/min. Istovremeno se ulijeva voda. Ako se nivo vode povećava brzinom "
                 r"$20$ cm/min pri visini $2$ m, odredite brzinu ulijevanja $V_{\mathrm{in}}$ (u cm³/min).",
        "tip": "auto",
        "tocan_odgovor": "800000*pi/9 + 10000",
        "rjesenje": r"$V_{\mathrm{in}}=\dfrac{800000\pi}{9}+10000\approx 289\,252{,}7$ cm³/min",
        "hints": [
            r"$r/h=1/3$, pa $V(h)=\frac{\pi}{27}h^3$. Deriviranjem: $\frac{\mathrm{d}V}{\mathrm{d}t}=\frac{\pi}{9}h^2\frac{\mathrm{d}h}{\mathrm{d}t}$.",
            r"Pri $h=200$ cm i $\frac{\mathrm{d}h}{\mathrm{d}t}=20$: $\frac{\mathrm{d}V}{\mathrm{d}t}=\frac{800000\pi}{9}$. Tada $V_{\mathrm{in}}=\frac{\mathrm{d}V}{\mathrm{d}t}+10000$."
        ]
    },
    {
        "tekst": r"Odredite točke $P$ i $Q$ na paraboli $y=1-x^2$ takve da trokut koji čine $x$-os, "
                 r"tangenta u $P$ i tangenta u $Q$ bude jednakostraničan.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Koordinata x točke P:", "answer": "-sqrt(3)/2"},
            {"label": "Koordinata y točke P:", "answer": "1/4"},
            {"label": "Koordinata x točke Q:", "answer": "sqrt(3)/2"},
            {"label": "Koordinata y točke Q:", "answer": "1/4"}
        ]),
        "rjesenje": r"$P\!\left(-\frac{\sqrt{3}}{2},\,\frac{1}{4}\right)$, $Q\!\left(\frac{\sqrt{3}}{2},\,\frac{1}{4}\right)$",
        "hints": [
            r"Tangente moraju zatvarati kutove $60°$ i $120°$ s $x$-osi, pa je $y'(x)=-2x=\pm\sqrt{3}$.",
            r"$x=\pm\frac{\sqrt{3}}{2}$, $y=1-\frac{3}{4}=\frac{1}{4}$."
        ]
    },
    {
        "tekst": r"Odredite zakrivljenost krivulje zadane parametrizacijom $\mathbf{r}(t)=(t,\;3\cos t,\;3\sin t)$, $t\in\mathbb{R}$.",
        "tip": "auto",
        "tocan_odgovor": "3/10",
        "rjesenje": r"$\kappa=\dfrac{3}{10}$",
        "hints": [
            r"$\mathbf{r}'=(1,-3\sin t,3\cos t)$, $\mathbf{r}''=(0,-3\cos t,-3\sin t)$.",
            r"$\|\mathbf{r}'\|^3=10\sqrt{10}$, $\|\mathbf{r}'\times\mathbf{r}''\|=3\sqrt{10}$. Dakle $\kappa=\frac{3\sqrt{10}}{10\sqrt{10}}=\frac{3}{10}$."
        ]
    },
    {
        "tekst": r"Izračunajte volumen tijela koje nastaje rotacijom područja omeđenog krivuljama "
                 r"$y=\sin\!\left(\frac{x}{2}+\frac{\pi}{4}\right)\!\cos\!\left(\frac{x}{2}+\frac{\pi}{4}\right)$, "
                 r"$y=0$, $x=\frac{3\pi}{2}$ i $x=\frac{5\pi}{2}$ oko osi $x=\pi$.",
        "tip": "auto",
        "tocan_odgovor": "2*pi**2",
        "rjesenje": r"$V=2\pi^2$",
        "hints": [
            r"Pojednostavite: $y=\frac{1}{2}\cos x$.",
            r"Formula cilindričnih ljuski: $V=2\pi\int_{3\pi/2}^{5\pi/2}(x-\pi)\cdot|y(x)|\,\mathrm{d}x$."
        ]
    },
    {
        "tekst": r"Koristeći rotaciju, izvedite formulu za volumen stošca radijusa $r$ i visine $h$.",
        "tip": "auto",
        "tocan_odgovor": "pi*r**2*h/3",
        "rjesenje": r"$V=\dfrac{1}{3}\pi r^2 h$",
        "hints": [
            r"Rotirajte pravac $y=\frac{r}{h}x$ na intervalu $[0,h]$ oko $x$-osi.",
            r"$V=\pi\int_0^h\left(\frac{r}{h}x\right)^2\mathrm{d}x=\frac{\pi r^2}{h^2}\cdot\frac{h^3}{3}=\frac{\pi r^2 h}{3}$."
        ]
    },
    {
        "tekst": r"U desnu pretklijetku srca ubrizgano je $2$ mg boje. Koncentracija boje je modelirana funkcijom "
                 r"$c(x)=\sqrt{169-x^2}$, $x\in[0,13]$ (min). Odredite ukupni volumen krvi.",
        "tip": "auto",
        "tocan_odgovor": "8/(169*pi)",
        "rjesenje": r"$V=\dfrac{8}{169\pi}$",
        "hints": [
            r"$V=\dfrac{A}{\int_0^{13}c(x)\,\mathrm{d}x}$, $A=2$ mg.",
            r"$\int_0^{13}\sqrt{169-x^2}\,\mathrm{d}x=\frac{169\pi}{4}$ (četvrtina kruga polumjera $13$). Dakle $V=\frac{2}{169\pi/4}=\frac{8}{169\pi}$."
        ]
    },
    {
        "tekst": r"Posuda oblika stošca s vrhom prema dolje (visina $16$ cm, polumjer $5$ cm) je dijelom ispunjena vodom "
                 r"koja istječe proporcionalno omočenoj površini. Sipamo vodu brzinom $2$ cm³/min, "
                 r"a visina se smanjuje brzinom $0{,}3$ cm/min pri $h=10$ cm. "
                 r"Kojom brzinom trebamo ulijevati vodu da visina bude konstantnih $10$ cm?",
        "tip": "auto",
        "tocan_odgovor": "375*pi/128 + 2",
        "rjesenje": r"$V_{\mathrm{in}}=\dfrac{375\pi}{128}+2\approx 11{,}20$ cm³/min",
        "hints": [
            r"$r/h=5/16$, $V(h)=\frac{25\pi}{768}h^3$. Iz $\frac{\mathrm{d}V}{\mathrm{d}t}=V_{\mathrm{in}}-k\cdot P$ pri $h=10$, $\frac{\mathrm{d}h}{\mathrm{d}t}=-0{,}3$ nađite $k$.",
            r"Za $\frac{\mathrm{d}h}{\mathrm{d}t}=0$: $V_{\mathrm{in}}=k\cdot P_{10}$."
        ]
    },
    {
        "tekst": r"Tijelo nađeno u $1$:$15$ h ima temperaturu $32{,}3°$C; temperatura prostorije je $22°$C. "
                 r"Nakon sat vremena temperatura tijela pala je na $30{,}3°$C. Normalna temperatura tijela je $37°$C. "
                 r"Odredite vrijeme zločina (u obliku $HH$:$MM$).",
        "tip": "auto",
        "tocan_odgovor": "23:31",
        "rjesenje": r"Zločin se dogodio u $23$:$31$ h",
        "hints": [
            r"Newtonov zakon: $T(t)=22+(T_0-22)e^{-kt}$. Iz $T(0)=32{,}3$ i $T(1)=30{,}3$ nađite $k$.",
            r"Nađite $t$ za koji je $T(t)=37°$ s $T_0=32{,}3$ — to je proteklo vrijeme od zločina do nalaska."
        ]
    },
    {
        "tekst": r"U desnu pretklijetku srca ubrizgano je $1{,}3$ mg boje. Koncentracija: "
                 r"$c(x)=\sqrt{225-x^2}$, $x\in[0,15]$ (min). Odredite ukupni volumen krvi.",
        "tip": "auto",
        "tocan_odgovor": "26/(1125*pi)",
        "rjesenje": r"$V=\dfrac{5{,}2}{225\pi}=\dfrac{26}{1125\pi}$",
        "hints": [
            r"$\int_0^{15}\sqrt{225-x^2}\,\mathrm{d}x=\frac{225\pi}{4}$ (četvrtina kruga polumjera $15$).",
            r"$V=\frac{1{,}3}{225\pi/4}=\frac{5{,}2}{225\pi}$."
        ]
    },
    {
        "tekst": r"Prirodna duljina opruge je $60$ cm. Za rastezanje na $67$ cm potrebna je sila $50$ N. "
                 r"Odredite rad potreban za rastezanje opruge do $72$ cm.",
        "tip": "auto",
        "tocan_odgovor": "36/7",
        "rjesenje": r"$W=\dfrac{36}{7}\approx 5{,}14$ J",
        "hints": [
            r"Hookeov zakon: $k=\frac{50}{0{,}07}=\frac{5000}{7}$ N/m.",
            r"$W=\frac{1}{2}k x^2\Big|_0^{0{,}12}=\frac{1}{2}\cdot\frac{5000}{7}\cdot(0{,}12)^2=\frac{36}{7}$ J."
        ]
    },
    {
        "tekst": r"U desnu pretklijetku srca ubrizgano je $3{,}2$ mg boje. Koncentracija: "
                 r"$c(x)=\sqrt{256-x^2}$, $x\in[0,16]$ (min). Odredite ukupni volumen krvi.",
        "tip": "auto",
        "tocan_odgovor": "1/(20*pi)",
        "rjesenje": r"$V=\dfrac{1}{20\pi}$",
        "hints": [
            r"$\int_0^{16}\sqrt{256-x^2}\,\mathrm{d}x=64\pi$ (četvrtina kruga polumjera $16$).",
            r"$V=\frac{3{,}2}{64\pi}=\frac{1}{20\pi}$."
        ]
    },
    {
        "tekst": r"Koliko je trake potrebno da se napravi model mosta oblika cikloide "
                 r"$x(t)=t-\sin t$, $y(t)=1-\cos t$, $t\in[0,2\pi]$?",
        "tip": "auto",
        "tocan_odgovor": "8",
        "rjesenje": r"$s=8$",
        "hints": [
            r"$s=\int_0^{2\pi}\sqrt{(x'(t))^2+(y'(t))^2}\,\mathrm{d}t=\int_0^{2\pi}\sqrt{2-2\cos t}\,\mathrm{d}t$.",
            r"$\sqrt{2-2\cos t}=2\left|\sin\frac{t}{2}\right|$, pa $s=2\int_0^{2\pi}\sin\frac{t}{2}\,\mathrm{d}t=8$."
        ]
    },
    {
        "tekst": r"Odredite koordinate težišta područja omeđenog krivuljama $y=x^2$ i $y=\sqrt{x}$.",
        "tip": "point",
        "tocan_odgovor": "(9/20, 9/20)",
        "rjesenje": r"$T\!\left(\dfrac{9}{20},\,\dfrac{9}{20}\right)$",
        "hints": [
            r"Površina: $P=\int_0^1(\sqrt{x}-x^2)\,\mathrm{d}x=\frac{1}{3}$.",
            r"$x_T=\frac{1}{P}\int_0^1 x(\sqrt{x}-x^2)\,\mathrm{d}x$, $y_T=\frac{1}{2P}\int_0^1(x-(x^2)^2)\,\mathrm{d}x$."
        ]
    },
    {
        "tekst": r"U trokutu $ABC$ kut pri vrhu $A$ iznosi $\pi/6$, a zbroj duljina stranica koje zatvaraju taj kut je $100$ cm. "
                 r"Kolika mora biti duljina stranice $AB$ da bi površina trokuta $ABC$ bila maksimalna?",
        "tip": "auto",
        "tocan_odgovor": "50",
        "rjesenje": r"$|AB|=50$ cm",
        "hints": [
            r"$P(c)=\frac{1}{2}\cdot b\cdot c\cdot\sin\frac{\pi}{6}=\frac{c(100-c)}{4}$ gdje $c=|AB|$.",
            r"Maksimum kvadratne funkcije: $c=50$ cm."
        ]
    },
    {
        "tekst": r"Trošak proizvodnje $C(x)=6+2\sqrt{x+1}$ milijuna eura za $x$ zrakoplova godišnje. "
                 r"Procijenite marginalnim troškom trošak $16.$ zrakoplova i usporedite sa stvarnim.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "Procjena C'(15) (mil. €):", "answer": "1/4"},
            {"label": "Stvarni trošak C(16)-C(15) (aproks. mil. €):", "answer": "2*sqrt(17) - 8"}
        ]),
        "rjesenje": r"Procjena: $C'(15)=\frac{1}{4}=0{,}25$ M€; Stvarni: $C(16)-C(15)=2\sqrt{17}-8\approx0{,}246$ M€",
        "hints": [
            r"$C'(x)=\frac{1}{\sqrt{x+1}}$. Za $x=15$: $C'(15)=\frac{1}{\sqrt{16}}=\frac{1}{4}$.",
            r"$C(16)-C(15)=2\sqrt{17}-2\sqrt{16}=2\sqrt{17}-8$."
        ]
    },
    {
        "tekst": r"Marko napravi limunadu sobne temperature $30°$C i stavi je u hladnjak ($6°$C). "
                 r"Nakon $20$ min limunada se ohladila na $25°$C. "
                 r"Nakon koliko minuta (od trenutka stavljanja) će biti željene temperature $15°$C?",
        "tip": "auto",
        "tocan_odgovor": "20*log(Rational(3,8))/log(Rational(19,24))",
        "rjesenje": r"$t\approx 83{,}97$ min",
        "hints": [
            r"$T(t)=6+24e^{-kt}$. Iz $T(20)=25$: $e^{-20k}=\frac{19}{24}$.",
            r"Iz $T(t)=15$: $e^{-kt}=\frac{9}{24}=\frac{3}{8}$. Dakle $t=\frac{20\ln(3/8)}{\ln(19/24)}$."
        ]
    },
    {
        "tekst": r"Dokažite da krivulja $r=a\sin\varphi+b\cos\varphi$ (gdje $ab\neq 0$) predstavlja kružnicu "
                 r"u kartezijevim koordinatama. Odredite središte i polumjer.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "x-koordinata središta:", "answer": "b/2"},
            {"label": "y-koordinata središta:", "answer": "a/2"},
            {"label": "Polumjer R:", "answer": "sqrt(a**2+b**2)/2"}
        ]),
        "rjesenje": r"Središte $S\!\left(\dfrac{b}{2},\dfrac{a}{2}\right)$, polumjer $R=\dfrac{\sqrt{a^2+b^2}}{2}$",
        "hints": [
            r"Pomnožite s $r$: $r^2=ar\sin\varphi+br\cos\varphi$, tj. $x^2+y^2=ay+bx$.",
            r"Dopunite do punih kvadrata: $\left(x-\frac{b}{2}\right)^2+\left(y-\frac{a}{2}\right)^2=\frac{a^2+b^2}{4}$."
        ]
    },
    {
        "tekst": r"Automobil $A$ putuje prema jugu brzinom $60$ km/h, a automobil $B$ prema zapadu brzinom "
                 r"$25$ km/h. Oba kreću s istog mjesta. Odredite brzinu promjene udaljenosti između njih "
                 r"nakon $2$ sata.",
        "tip": "auto",
        "tocan_odgovor": "65",
        "rjesenje": r"$\dfrac{\mathrm{d}s}{\mathrm{d}t}=65$ km/h",
        "hints": [
            r"$s^2=y^2+x^2$, $y=60t$, $x=25t$. Deriviranjem: $s\cdot\frac{\mathrm{d}s}{\mathrm{d}t}=y\frac{\mathrm{d}y}{\mathrm{d}t}+x\frac{\mathrm{d}x}{\mathrm{d}t}$.",
            r"Pri $t=2$: $y=120$, $x=50$, $s=130$. $\frac{\mathrm{d}s}{\mathrm{d}t}=\frac{120\cdot60+50\cdot25}{130}=65$."
        ]
    },
    {
        "tekst": r"Izračunajte zakrivljenost krivulje u ravnini zadane u polarnim koordinatama izrazom $r=2\cos\varphi$.",
        "tip": "auto",
        "tocan_odgovor": "1",
        "rjesenje": r"$\kappa=1$",
        "hints": [
            r"Prevedite u parametarsku formu: $\mathbf{r}(\varphi)=(2\cos^2\varphi,\,2\cos\varphi\sin\varphi,\,0)=(1+\cos 2\varphi,\,\sin 2\varphi,\,0)$.",
            r"$\|\mathbf{r}'\|=2$, $\|\mathbf{r}'\times\mathbf{r}''\|=4$. $\kappa=4/8=1/2$... čekajte, krivulja je kružnica polumjera $1$, pa $\kappa=1$."
        ]
    },
    {
        "tekst": r"Izračunajte volumen tijela koje nastaje rotacijom područja omeđenog krivuljama "
                 r"$y=\sin(x-\pi)+2$, $y=2$, $x=\pi$ i $x=2\pi$ oko pravca $x=\pi$.",
        "tip": "auto",
        "tocan_odgovor": "2*pi**2",
        "rjesenje": r"$V=2\pi^2$",
        "hints": [
            r"Cilindrične ljuske: $V=2\pi\int_\pi^{2\pi}(x-\pi)\cdot(\sin(x-\pi)+2-2)\,\mathrm{d}x$.",
            r"Supstitucija $u=x-\pi$: $V=2\pi\int_0^\pi u\sin u\,\mathrm{d}u$. Parcijalna integracija daje $2\pi^2$."
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
        tips = {}
        for z in ZADACI:
            tips[z["tip"]] = tips.get(z["tip"], 0) + 1
        for t, c in sorted(tips.items()):
            print(f"  {t}: {c}")
    except Exception:
        import traceback; traceback.print_exc()
    finally:
        db.close()


if __name__ == "__main__":
    run()