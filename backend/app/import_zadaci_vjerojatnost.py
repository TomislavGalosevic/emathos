"""
Import zadataka za modul "Vjerojatnost"
unutar kolegija "Primijenjena matematika za racunalnu znanost".
Pokretanje: python -m app.import_zadaci_vjerojatnost
"""

import json
from .database import Base, engine, SessionLocal
from . import models

COURSE_NAME = "Primijenjena matematika za racunalnu znanost"
MODULE_NAME = "Vjerojatnost"

def multi(fields):
    return json.dumps(fields, ensure_ascii=False)

def choice(answer, options):
    return json.dumps({"answer": answer, "options": options}, ensure_ascii=False)

ZADACI = [
    {
        "tekst": r"Iz intervala $[0,3]$ na slučajan način biramo dva broja $x$ i $y$. "
                 r"Kolika je vjerojatnost da je zadovoljena nejednakost $x^2+y^2\le 1$?",
        "tip": "auto",
        "tocan_odgovor": "pi/36",
        "rjesenje": r"$P=\dfrac{\pi}{36}$",
        "hints": [
            r"Ukupno geometrijsko područje je kvadrat $[0,3]\times[0,3]$ s površinom $9$.",
            r"Povoljno područje je četvrtina kruga radijusa $1$, površine $\pi/4$. Dakle $P=\frac{\pi/4}{9}$."
        ]
    },
    {
        "tekst": r"U prvoj kutiji je $10$ plavih, $5$ crvenih i $1$ zelena kuglica; "
                 r"u drugoj $5$ plavih, $7$ crvenih i $6$ zelenih. "
                 r"Biramo kutiju na slučaj i izvlačimo jednu kuglicu. "
                 r"(a) Kolika je vjerojatnost da je izvučena plava kuglica? "
                 r"(b) Ako je izvučena plava, kolika je vjerojatnost da je to bila druga kutija?",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "P(Plava) =", "answer": "65/144"},
            {"label": "P(Kutija 2 | Plava) =", "answer": "4/13"}
        ]),
        "rjesenje": r"$P(\text{Plava})=\dfrac{65}{144}$, $\quad P(K_2\mid\text{Plava})=\dfrac{4}{13}$",
        "hints": [
            r"Formula potpune vjerojatnosti: $P(P)=\tfrac{1}{2}\cdot\tfrac{10}{16}+\tfrac{1}{2}\cdot\tfrac{5}{18}$.",
            r"Bayesova formula: $P(K_2\mid P)=\frac{\frac{1}{2}\cdot\frac{5}{18}}{P(P)}$."
        ]
    },
    {
        "tekst": r"Bacamo simetričan novčić $3$ puta. Neka je $X$ broj pojavljivanja pisma. "
                 r"(a) Odredite tablicu distribucije i $P(X\ge 2)$. "
                 r"(b) Neka je $Y=X-2$. Odredite $E[Y]$ i $\mathrm{Var}(Y)$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "P(X >= 2) =", "answer": "1/2"},
            {"label": "E[Y] =", "answer": "-1/2"},
            {"label": "Var(Y) =", "answer": "3/4"}
        ]),
        "rjesenje": r"$P(X\ge 2)=\tfrac{1}{2}$, $\quad E[Y]=-\tfrac{1}{2}$, $\quad\mathrm{Var}(Y)=\tfrac{3}{4}$",
        "hints": [
            r"$X\sim B(3,\tfrac{1}{2})$: $P(X=k)=\binom{3}{k}\tfrac{1}{8}$.",
            r"$E[Y]=E[X]-2=\tfrac{3}{2}-2=-\tfrac{1}{2}$. $\mathrm{Var}(Y)=\mathrm{Var}(X)=\tfrac{3}{4}$."
        ]
    },
    {
        "tekst": r"Slučajna varijabla $X$ zadana je funkcijom gustoće "
                 r"$f(x)=k\,e^{-2x}$ za $x\ge 0$, inače $0$. "
                 r"(i) Odredite $k$. "
                 r"(ii) Odredite funkciju distribucije $F(x)$. "
                 r"(iii) Izračunajte $P(X\ge 2)$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "k =", "answer": "2"},
            {"label": "F(x) za x >= 0:", "answer": "1 - exp(-2*x)"},
            {"label": "P(X >= 2) =", "answer": "exp(-4)"}
        ]),
        "rjesenje": r"$k=2$, $\;F(x)=1-e^{-2x}$ ($x\ge 0$), $\;P(X\ge 2)=e^{-4}$",
        "hints": [
            r"(i) $\int_0^\infty k\,e^{-2x}\,\mathrm{d}x=\frac{k}{2}=1\Rightarrow k=2$.",
            r"(ii) $F(x)=\int_0^x 2e^{-2t}\,\mathrm{d}t=1-e^{-2x}$. (iii) $P(X\ge 2)=1-F(2)=e^{-4}$."
        ]
    },
    {
        "tekst": r"U jednoj kutiji je $40$ crvenih i $10$ plavih kuglica, "
                 r"u drugoj $42$ crvene i $8$ plavih. Slučajno se otvori jedna kutija i izvuče kuglica. "
                 r"(a) Kolika je vjerojatnost da je crvena? "
                 r"(b) Ako je crvena, kolika je vjerojatnost da je to kutija s $40$ crvenih?",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "P(Crvena) =", "answer": "41/50"},
            {"label": "P(K1 | Crvena) =", "answer": "20/41"}
        ]),
        "rjesenje": r"$P(C)=\dfrac{41}{50}$, $\quad P(K_1\mid C)=\dfrac{20}{41}$",
        "hints": [
            r"$P(C)=\tfrac{1}{2}\cdot\tfrac{40}{50}+\tfrac{1}{2}\cdot\tfrac{42}{50}=\tfrac{82}{100}=\tfrac{41}{50}$.",
            r"Bayes: $P(K_1\mid C)=\frac{\frac{1}{2}\cdot\frac{40}{50}}{\frac{41}{50}}=\frac{20}{41}$."
        ]
    },
    {
        "tekst": r"Dva prijatelja su se dogovorila naći između $20$h i $21$h. "
                 r"Tko prvi dođe čeka najviše $10$ minuta. "
                 r"Izračunajte vjerojatnost da se sretnu.",
        "tip": "auto",
        "tocan_odgovor": "11/36",
        "rjesenje": r"$P=\dfrac{11}{36}$",
        "hints": [
            r"Modelirajte dolaske s $x,y\in[0,1]$ (u satima). Uvjet susreta: $|x-y|\le\tfrac{1}{6}$.",
            r"$P=1-2\cdot\tfrac{1}{2}\cdot\left(\tfrac{5}{6}\right)^2=1-\tfrac{25}{36}=\tfrac{11}{36}$."
        ]
    },
    {
        "tekst": r"Četiri strijelca gađaju metu nezavisno, svaki s vjerojatnošću pogotka $0{,}7$. "
                 r"Sljedeći strijelac gađa samo ako prethodni promaši. "
                 r"Neka je $X$ broj promašaja. "
                 r"(a) Odredite tablicu distribucije $X$. "
                 r"(b) Izračunajte $P(X>2)$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "P(X=0) =", "answer": "0.7"},
            {"label": "P(X=1) =", "answer": "0.21"},
            {"label": "P(X=2) =", "answer": "0.063"},
            {"label": "P(X=3) =", "answer": "0.0189"},
            {"label": "P(X=4) =", "answer": "0.0081"},
            {"label": "P(X > 2) =", "answer": "27/1000"}
        ]),
        "rjesenje": r"$P(X\!>\!2)=0{,}027=\dfrac{27}{1000}$",
        "hints": [
            r"$P(X=0)=0{,}7$; $P(X=k)=0{,}3^k\cdot 0{,}7$ za $k=1,2,3$; $P(X=4)=0{,}3^4$.",
            r"$P(X>2)=P(X=3)+P(X=4)=0{,}3^3\cdot 0{,}7+0{,}3^4=0{,}027$."
        ]
    },
    {
        "tekst": r"Tablica distribucije diskretne s.v. $X$ zadana je s "
                 r"$X\sim\bigl((-1,0,1),\,(a/2,\,ab,\,b/2)\bigr)$ i $E[X]=\tfrac{1}{3}$. "
                 r"Odredite $a$, $b$ i $\mathrm{Var}(X)$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "a =", "answer": "1/3"},
            {"label": "b =", "answer": "1"},
            {"label": "Var(X) =", "answer": "5/9"}
        ]),
        "rjesenje": r"$a=\tfrac{1}{3}$, $\;b=1$, $\;\mathrm{Var}(X)=\tfrac{5}{9}$",
        "hints": [
            r"Sustav: $\tfrac{a}{2}+ab+\tfrac{b}{2}=1$ i $-\tfrac{a}{2}+\tfrac{b}{2}=\tfrac{1}{3}$.",
            r"$\mathrm{Var}(X)=E[X^2]-(E[X])^2=\tfrac{a}{2}\cdot1+\tfrac{b}{2}\cdot1-\tfrac{1}{9}$."
        ]
    },
    {
        "tekst": r"Dana je funkcija $f(x)=a(1+x)^2$ za $x\in\langle 0,1\rangle$, inače $0$. "
                 r"(a) Odredite $a$ tako da $f$ bude funkcija gustoće. "
                 r"(b) Odredite $E[X]$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "a =", "answer": "3/7"},
            {"label": "E[X] =", "answer": "17/28"}
        ]),
        "rjesenje": r"$a=\dfrac{3}{7}$, $\quad E[X]=\dfrac{17}{28}$",
        "hints": [
            r"(a) $\int_0^1 a(1+x)^2\,\mathrm{d}x=a\cdot\tfrac{7}{3}=1\Rightarrow a=\tfrac{3}{7}$.",
            r"(b) $E[X]=\int_0^1 x\cdot\tfrac{3}{7}(1+x)^2\,\mathrm{d}x=\tfrac{3}{7}\cdot\tfrac{17}{12}=\tfrac{17}{28}$."
        ]
    },
    {
        "tekst": r"Neka je $X$ neprekidna s.v. s gustoćom $f_X$ i distribucijom $F_X$. "
                 r"Odredite $F_Y$ i $f_Y$ za $Y=e^{-3X}$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "F_Y(y) za y > 0 =", "answer": "1 - F_X(-log(y)/3)"},
            {"label": "f_Y(y) za y > 0 =", "answer": "f_X(-log(y)/3) / (3*y)"}
        ]),
        "rjesenje": r"$F_Y(y)=1-F_X\!\left(-\tfrac{\ln y}{3}\right)$, $\quad f_Y(y)=\dfrac{1}{3y}f_X\!\left(-\tfrac{\ln y}{3}\right)$ za $y>0$",
        "hints": [
            r"$F_Y(y)=P(e^{-3X}\le y)=P\!\left(X\ge-\tfrac{\ln y}{3}\right)=1-F_X\!\left(-\tfrac{\ln y}{3}\right)$.",
            r"Derivirajte po $y$: $f_Y(y)=\frac{1}{3y}f_X\!\left(-\tfrac{\ln y}{3}\right)$."
        ]
    },
    {
        "tekst": r"U tri kutije su: K1: $2$ crvene, $3$ plave; K2: $3$ crvene, $2$ plave; K3: $2$ crvene, $2$ plave. "
                 r"Iz svake kutije izvlačimo $2$ kuglice i stavljamo u 4. kutiju ($6$ kuglica ukupno). "
                 r"Iz 4. kutije izvlačimo $2$. "
                 r"(a) Kolika je vjerojatnost da su obje plave? "
                 r"(b) Ako su obje plave, kolika je vjerojatnost da potječu iz K2?",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "P(obje plave) =", "answer": "529/2250"},
            {"label": "P(iz K2 | obje plave) =", "answer": "1/7"}
        ]),
        "rjesenje": r"$P(\text{obje plave})=\dfrac{529}{2250}$, $\quad P(K_2\mid\text{obje plave})=\dfrac{1}{7}$",
        "hints": [
            r"Izračunajte očekivani raspored plavih u 4. kutiji pomoću hipergeometrijske distribucije.",
            r"Primijenite formulu potpune vjerojatnosti i Bayesovu formulu na sve moguće sastave 4. kutije."
        ]
    },
    {
        "tekst": r"Dva vlaka dolaze svako jutro između $7$:$00$ i $7$:$20$. "
                 r"Svaki stoji $5$ minuta. Kolika je vjerojatnost da se sretnu na stanici?",
        "tip": "auto",
        "tocan_odgovor": "7/16",
        "rjesenje": r"$P=\dfrac{7}{16}$",
        "hints": [
            r"Modelirajte dolaske s $x,y\in[0,20]$. Uvjet susreta: $|x-y|\le 5$.",
            r"$P=1-\left(\tfrac{15}{20}\right)^2=1-\tfrac{9}{16}=\tfrac{7}{16}$."
        ]
    },
    {
        "tekst": r"Tablica distribucije s.v. $X$ je $X\sim\bigl((-2,0,2),\,(a^2,\,a,\,\tfrac{1}{4})\bigr)$. "
                 r"(a) Odredite $a$. "
                 r"(b) Za $Y=X^2+1$ odredite $E[Y]$ i $\mathrm{Var}(Y)$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "a =", "answer": "1/2"},
            {"label": "E[Y] =", "answer": "3"},
            {"label": "Var(Y) =", "answer": "4"}
        ]),
        "rjesenje": r"$a=\tfrac{1}{2}$, $\quad E[Y]=3$, $\quad\mathrm{Var}(Y)=4$",
        "hints": [
            r"$a^2+a+\tfrac{1}{4}=1\Rightarrow\left(a+\tfrac{1}{2}\right)^2=1\Rightarrow a=\tfrac{1}{2}$.",
            r"$Y=X^2+1$ poprima vrijednosti: $X=-2\Rightarrow Y=5$, $X=0\Rightarrow Y=1$, $X=2\Rightarrow Y=5$."
        ]
    },
    {
        "tekst": r"Odredite $k$ tako da $f(x)=k(x^3+2)$ za $x\in\langle 0,2\rangle$, inače $0$, "
                 r"bude funkcija gustoće s.v. $X$. Izračunajte drugi moment $E[X^2]$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "k =", "answer": "1/8"},
            {"label": "E[X^2] =", "answer": "2"}
        ]),
        "rjesenje": r"$k=\dfrac{1}{8}$, $\quad E[X^2]=2$",
        "hints": [
            r"$\int_0^2 k(x^3+2)\,\mathrm{d}x=k\cdot 8=1\Rightarrow k=\tfrac{1}{8}$.",
            r"$E[X^2]=\int_0^2 x^2\cdot\tfrac{1}{8}(x^3+2)\,\mathrm{d}x=\tfrac{1}{8}\cdot 16=2$."
        ]
    },
    {
        "tekst": r"Neka je $X$ neprekidna s.v. s gustoćom $f_X$ i distribucijom $F_X$. "
                 r"Odredite $F_Y$ i $f_Y$ za $Y=3e^X$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "F_Y(y) za y > 0 =", "answer": "F_X(log(y/3))"},
            {"label": "f_Y(y) za y > 0 =", "answer": "f_X(log(y/3)) / y"}
        ]),
        "rjesenje": r"$F_Y(y)=F_X\!\left(\ln\tfrac{y}{3}\right)$, $\quad f_Y(y)=\dfrac{1}{y}f_X\!\left(\ln\tfrac{y}{3}\right)$ za $y>0$",
        "hints": [
            r"$F_Y(y)=P(3e^X\le y)=P\!\left(X\le\ln\tfrac{y}{3}\right)=F_X\!\left(\ln\tfrac{y}{3}\right)$.",
            r"Derivirajte po $y$: $f_Y(y)=\tfrac{1}{y}\,f_X\!\left(\ln\tfrac{y}{3}\right)$."
        ]
    },
    {
        "tekst": r"Biramo $x\in[-2,2]$ i $y\in[0,2]$ na slučajan način. "
                 r"Kolika je vjerojatnost da je $y\ge 1-x^2$?",
        "tip": "auto",
        "tocan_odgovor": "5/6",
        "rjesenje": r"$P=\dfrac{5}{6}$",
        "hints": [
            r"Ukupna površina pravokutnika $[-2,2]\times[0,2]$ je $8$.",
            r"Nepovoljno područje: $0\le y<1-x^2$ za $x\in[-1,1]$. Površina: $\int_{-1}^{1}(1-x^2)\,\mathrm{d}x=\tfrac{4}{3}$. $P=1-\tfrac{4/3}{8}=\tfrac{5}{6}$."
        ]
    },
    {
        "tekst": r"Pred Lukom je kutija s $6$ kuverti: $2$ prazne i $4$ s po $1000$ kuna. "
                 r"Luka izvlači jednu po jednu bez vraćanja dok ne izvuče praznu. "
                 r"(a) Kolika je vjerojatnost da izvuče svih $4000$ kn? "
                 r"(b) Odredite $E[X]$ i $\mathrm{Var}(X)$ iznosa dobivenih novaca.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "P(4000 kn) =", "answer": "1/15"},
            {"label": "E[X] =", "answer": "4000/3"},
            {"label": "Var(X) =", "answer": "14000000/9"}
        ]),
        "rjesenje": r"$P(4000)=\tfrac{1}{15}$, $\quad E[X]=\tfrac{4000}{3}$, $\quad\mathrm{Var}(X)=\tfrac{14000000}{9}$",
        "hints": [
            r"$P(X=1000k)$ = vjerojatnost da prvih $k$ kuverti budu novčane, a $(k+1)$-a prazna.",
            r"$P(X=0)=\tfrac{2}{6}=\tfrac{1}{3}$; $P(X=1000)=\tfrac{4}{6}\cdot\tfrac{2}{5}=\tfrac{4}{15}$; itd."
        ]
    },
    {
        "tekst": r"S.v. $X$ zadana je gustoćom $f(x)=4ax^{-5}$ za $x\ge 2$, inače $0$. "
                 r"(a) Odredite $a$. "
                 r"(b) Odredite $F(x)$. "
                 r"(c) Izračunajte $E[X]$. "
                 r"(d) Izračunajte $P(2<X<4)$. "
                 r"(e) Kolika je $P(X=7)$?",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "a =", "answer": "16"},
            {"label": "F(x) za x >= 2 =", "answer": "1 - 16/x**4"},
            {"label": "E[X] =", "answer": "8/3"},
            {"label": "P(2 < X < 4) =", "answer": "15/16"},
            {"label": "P(X = 7) =", "answer": "0"}
        ]),
        "rjesenje": r"$a=16$, $\;F(x)=1-\dfrac{16}{x^4}$, $\;E[X]=\dfrac{8}{3}$, $\;P(2\!<\!X\!<\!4)=\dfrac{15}{16}$, $\;P(X=7)=0$",
        "hints": [
            r"(a) $\int_2^\infty 4a x^{-5}\,\mathrm{d}x=\tfrac{4a}{4\cdot 2^4}=\tfrac{a}{16}=1\Rightarrow a=16$.",
            r"(d) $F(4)-F(2)=(1-\tfrac{16}{256})-(1-1)=\tfrac{15}{16}$. (e) Neprekidna s.v.: $P(X=c)=0$."
        ]
    },
    {
        "tekst": r"Neka je $X$ neprekidna s.v. s gustoćom $f_X$ i distribucijom $F_X$. "
                 r"Odredite $F_Y$ i $f_Y$ za $Y=e^{6X+1}$.",
        "tip": "multi",
        "tocan_odgovor": multi([
            {"label": "F_Y(y) za y > 0 =", "answer": "F_X((log(y)-1)/6)"},
            {"label": "f_Y(y) za y > 0 =", "answer": "f_X((log(y)-1)/6) / (6*y)"}
        ]),
        "rjesenje": r"$F_Y(y)=F_X\!\left(\tfrac{\ln y-1}{6}\right)$, $\quad f_Y(y)=\dfrac{1}{6y}f_X\!\left(\tfrac{\ln y-1}{6}\right)$ za $y>0$",
        "hints": [
            r"$F_Y(y)=P(e^{6X+1}\le y)=P\!\left(X\le\tfrac{\ln y-1}{6}\right)=F_X\!\left(\tfrac{\ln y-1}{6}\right)$.",
            r"Derivirajte: $f_Y(y)=\tfrac{1}{6y}f_X\!\left(\tfrac{\ln y-1}{6}\right)$."
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