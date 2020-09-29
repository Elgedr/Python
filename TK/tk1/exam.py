"""Test 1 (K14)."""


def workday_count(days):
    """Given number of days."""
    amount_of_days = days
    if amount_of_days <= 5:
        return amount_of_days
    elif amount_of_days == 6:
        result = amount_of_days - 1
        return result
    elif amount_of_days == 7:
        result = amount_of_days - 2
        return result


if __name__ == '__main__':
    print(workday_count(9))