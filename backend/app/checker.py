"""Provjera korisnikovog odgovora na zadatak.

Prvo pokusa numericku/simbolicku usporedbu preko SymPy (npr. "3+2x" == "2x+3",
"x^2" == "x**2", "sin(x)^2+cos(x)^2" == "1"), s tolerancijom za decimalne
priblizne odgovore. Ako parsiranje ne uspije (npr. odgovor je matrica u
obliku [[1,0],[0,1]]), pada natrag na usporedbu normaliziranog teksta.
"""

import re
from sympy import sympify, simplify, trigsimp, Matrix, N
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

_TRANSFORMS = standard_transformations + (implicit_multiplication_application, convert_xor)
_NUMERIC_TOLERANCE = 1e-4


def _normalize_text(s: str) -> str:
    return re.sub(r"\s+", "", s.strip().lower())


def _try_matrix(s: str):
    """Pokusaj parsirati string oblika [[1,0],[0,1]] kao SymPy Matrix."""
    s = s.strip()
    if not (s.startswith("[[") and s.endswith("]]")):
        return None
    try:
        rows = []
        for row_str in re.findall(r"\[([^\[\]]*)\]", s):
            rows.append([sympify(x.strip()) for x in row_str.split(",") if x.strip() != ""])
        if not rows:
            return None
        return Matrix(rows)
    except Exception:
        return None


def check_answer(user_answer: str, correct_answer: str) -> bool:
    if not user_answer or not correct_answer:
        return False

    # 1) pokusaj kao matricu
    m_user = _try_matrix(user_answer)
    m_correct = _try_matrix(correct_answer)
    if m_user is not None and m_correct is not None:
        try:
            return (m_user - m_correct).is_zero_matrix
        except Exception:
            pass

    # 2) pokusaj kao simbolicki/brojcani izraz
    try:
        expr_user = parse_expr(user_answer, transformations=_TRANSFORMS)
        expr_correct = parse_expr(correct_answer, transformations=_TRANSFORMS)
        diff = simplify(trigsimp(expr_user - expr_correct))

        if diff == 0:
            return True

        # numericka tolerancija za priblizne decimalne odgovore (npr. 0.3333 vs 1/3)
        try:
            numeric_diff = complex(N(diff))
            if abs(numeric_diff) < _NUMERIC_TOLERANCE:
                return True
        except (TypeError, ValueError):
            pass
    except Exception:
        pass

    # 3) fallback: normalizirani tekst (razmaci, velika/mala slova)
    return _normalize_text(user_answer) == _normalize_text(correct_answer)