"""Test 1 (K14)."""


def workday_count(days):
    """Given number of days."""
    amount_of_days = days
    if amount_of_days <= 5:
        return amount_of_days
    elif amount_of_days > 5:
        result = amount_of_days - 1
        return result
    elif amount_of_days == 7:
        result = amount_of_days - 2
        return result


if __name__ == '__main__':
    print(workday_count(9))


def caught_speeding(speed, is_birthday: bool):
    """Return which category speeding ticket you would get."""
    if speed <= 60 and is_birthday == False:
        return 0
    elif 61 < speed <= 80 and is_birthday == False:
        return 1
    elif speed >= 81 and is_birthday == False:
        return 2
    elif is_birthday == True and speed <= 65:
        return 0
    elif is_birthday == True and 66 < speed <= 85:
        return 1
    elif is_birthday == True and speed >= 86:
        return 2


if __name__ == '__main__':
    print(caught_speeding(50, False))