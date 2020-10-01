"""Test 2 (R10)."""


def format_time(minutes):
    """Funktsioon"""
    hours = minutes // 60
    mins = minutes % 60
    if hours > 0:
        if minutes > 0:
            return f"{hours}h{mins}min"
        else:
            return f"{hours}h"
    else:
        return f"{mins}min"


def sorta_sum(a: int, b: int) -> int:
    """Given 2 ints, a and b, return their sum."""
    result = a + b
    if 10 <= result <= 19:
        return 20
    else:
        return result


def combo_string(s1: str, s2: str) -> str:
    """Return a new string of the form short + long + short."""
