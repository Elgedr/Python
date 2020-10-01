"""Test 1 (K14)."""


def workday_count(days):
    """Given number of days."""
    res = 0
    if days > 7:
        week = days // 7
        days -= week * 7
        res = (week * 5)
    if days == 7 or days == 6:
        res = res + 5
    if days < 6:
        res = res + days
    return res


def caught_speeding(speed, is_birthday: bool):
    """Return which category speeding ticket you would get."""
    if speed <= 60 and is_birthday is False:
        return 0
    elif 61 <= speed <= 80 and is_birthday is False:
        return 1
    elif speed >= 81 and is_birthday is False:
        return 2
    elif is_birthday is True and speed <= 65:
        return 0
    elif is_birthday is True and 66 < speed <= 85:
        return 1
    elif is_birthday is True and speed >= 86:
        return 2


def first_half(text):
    """Return the first half of an string."""
    amount = int(len(text) / 2)
    result = text[:amount:]
    return result


def last_indices_elements_sum(nums):
    """Return sum of elements at indices of last two elements."""
    last = nums[-1]
    lastt = nums[-2]
    if nums[-1] > len(nums) - 1 and nums[-2] > len(nums) - 1:
        result = 0 + 0
        return result
    if nums[-1] > len(nums) - 1:
        result = 0 + nums[lastt]
    elif nums[-2] > len(nums) - 1:
        result = 0 + nums[last]
    else:
        result = nums[last] + nums[lastt]
    return result


if __name__ == '__main__':
    print(last_indices_elements_sum([0, 1, 7, 2]))


def max_duplicate(nums):
    """Return the largest element which has at least one duplicate."""
    numbers = []
    for number in nums:
        if nums.count(number) > 1:
            numbers.append(number)
        else:
            pass
    if len(numbers) == 0:
        return None
    numbers = set(numbers)
    return max(numbers)
