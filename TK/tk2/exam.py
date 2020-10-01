"""Test 2 (R10)."""


def format_time(minutes):
    """Funktsioon."""
    hours = minutes // 60
    mins = minutes % 60
    if hours == 0:
        return f"{mins}min"
    elif hours != 0 and mins > 0:
        return f"{hours}h {mins}min"
    else:
        return f"{hours}h"


def sorta_sum(a: int, b: int) -> int:
    """Given 2 ints, a and b, return their sum."""
    result = a + b
    if 10 <= result <= 19:
        return 20
    else:
        return result


def combo_string(s1: str, s2: str) -> str:
    """Return a new string of the form short + long + short."""
    if len(s1) > len(s2):
        return s2 + s1 + s2
    elif len(s2) > len(s1):
        return s1 + s2 + s1
    elif len(s1) == 0 and len(s2) == 0:
        return ""


def num_as_index(nums: list) -> int:
    """Return element which index is the value of the smaller of the first and the last element."""
    minimum = min([nums[0], nums[-1]])
    if minimum > len(nums):
        return minimum
    return nums[minimum]


def count_clumps(nums: list) -> int:
    """Return the number of clumps in the given list."""
    listt = []
    for numbers in nums:
        if nums.count(numbers) > 1:
            listt.append(numbers)
    result = len(listt)
    return result
