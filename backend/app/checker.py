"""Provjera korisnikovog odgovora na zadatak."""

import re
from sympy import sympify, simplify, trigsimp, Matrix, N, E, pi, oo
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

_TRANSFORMS = standard_transformations + (implicit_multiplication_application, convert_xor)
_NUMERIC_TOLERANCE = 0.005 


def _parse_coord_pair(s: str):
    """Parsira par koordinata: T(a,b) ili (a,b) ili a,b → [str_a, str_b] ili None."""
    s = s.strip()
    s = re.sub(r'^[Tt]\s*', '', s)
    s = s.strip('()')
    parts = [p.strip() for p in s.split(',')]
    return parts if len(parts) == 2 else None

_LOCAL_NS = {"e": E, "pi": pi, "inf": oo, "infinity": oo}


def _preprocess(s: str) -> str:
    """Sitne normalizacije prije SymPy parsiranja."""
    s = s.strip()
    s = re.sub(r'\s*(min|cm|m|km|mm|kg|mg|g|N|J|kJ|rad|deg|°|h|s)\s*$', '', s, flags=re.IGNORECASE).strip()
    if '[' not in s:
        s = re.sub(r'(\d),(\d)', r'\1.\2', s)
    s = re.sub(r"\bln\s*\(", "log(", s)
    return s


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


def _preprocess_correct(s: str) -> str:
    """Minimalna normalizacija tocnog odgovora (samo ln→log, bez decimalne zareze)."""
    s = s.strip()
    s = re.sub(r"\bln\s*\(", "log(", s)
    return s


def check_answer(user_answer: str, correct_answer: str) -> bool:
    if not user_answer or not correct_answer:
        return False

    user_pp    = _preprocess(user_answer)
    correct_pp = _preprocess_correct(correct_answer)

    if correct_answer.strip().startswith("{"):
        import json as _json
        try:
            data = _json.loads(correct_answer)
            if "answer" in data:
                return _normalize_text(user_pp) == _normalize_text(data["answer"])
        except Exception:
            pass

    correct_coord = _parse_coord_pair(correct_answer)
    if correct_coord is not None:
        user_coord_raw = _parse_coord_pair(user_answer)
        if user_coord_raw is not None:
            return all(check_answer(u, c) for u, c in zip(user_coord_raw, correct_coord))
        user_coord_pp = _parse_coord_pair(user_pp)
        if user_coord_pp is not None:
            return all(check_answer(u, c) for u, c in zip(user_coord_pp, correct_coord))

    m_user    = _try_matrix(user_pp)
    m_correct = _try_matrix(correct_answer)
    if m_user is not None and m_correct is not None:
        try:
            return (m_user - m_correct).is_zero_matrix
        except Exception:
            pass

    try:
        expr_user    = parse_expr(user_pp,    transformations=_TRANSFORMS, local_dict=_LOCAL_NS)
        expr_correct = parse_expr(correct_pp, transformations=_TRANSFORMS, local_dict=_LOCAL_NS)
        diff = simplify(trigsimp(expr_user - expr_correct))

        if diff == 0:
            return True

        try:
            numeric_diff = complex(N(diff))
            if abs(numeric_diff) < _NUMERIC_TOLERANCE:
                return True
        except (TypeError, ValueError):
            pass
    except Exception:
        pass

    return _normalize_text(user_pp) == _normalize_text(correct_answer)