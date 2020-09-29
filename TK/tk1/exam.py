"""Test 1 (K14)."""


def workday_count(days):
    """Given number of days."""
    res = 0
    if days == 7 or days == 6:
        res = res + 5
    if days < 6:
        res = res + days
    if days > 7:
        week = days // 7
        days -= week * 7
        res = (week * 5)
    return res


def caught_speeding(speed, is_birthday: bool):
    """Return which category speeding ticket you would get."""
    if speed <= 60 and is_birthday == False:
        return 0
    elif 61 <= speed <= 80 and is_birthday == False:
        return 1
    elif speed >= 81 and is_birthday == False:
        return 2
    elif is_birthday == True and speed <= 65:
        return 0
    elif is_birthday == True and 66 < speed <= 85:
        return 1
    elif is_birthday == True and speed >= 86:
        return 2


def first_half(text):
    """Return the first half of an string."""
    amount = int(len(text) / 2)
    result = text[:amount:]
    return result

