"""KT1."""


def positive_or_not(nums: list, pos: bool) -> list:
    """
    Given a list of integers and a boolean pos.

    If pos is True, return a new list containing only positive numbers of the first list.
    Otherwise return a new list containing all the other numbers but positive of the given list.

    print(positive_or_not([9, 5, 0, 6, -5, -1], True))  => [9, 5, 6]
    print(positive_or_not([3, 4, -2, 1, -78, 0], False))  => [-2, -78, 0]

    :param nums:
    :return:
    """
    positive = []
    negative = []
    for num in nums:
        if num <= 0:
            negative.append(num)
        elif num > 0:
            positive.append(num)
    if pos is True:
        return positive
    elif pos is False:
        return negative


def sum_half_evens(nums: list) -> int:
    """
    Return the sum of first half of even ints in the given array.

    If there are odd number of even numbers, then include the middle number.

    sum_half_evens([2, 1, 2, 3, 4]) => 4
    sum_half_evens([2, 2, 0, 4]) => 4
    sum_half_evens([1, 3, 5, 8]) => 8
    sum_half_evens([2, 3, 5, 7, 8, 9, 10, 11]) => 10
    """
    num = []
    numss = []
    for i in nums:
        if i % 2 == 0:
            num.append(i)
        else:
            pass
    length = len(num)
    if length % 2 == 0:
        bb = len(num) / 2
        for i in range(bb + 1):
            numss.append(i)
    elif length % 2 != 0:
        rangee = len(num)
        for i in range((rangee + 1) / 2):
            numss.append(i)
    return sum(nums)
    # if len(nums) % 2 == 0:
    #    rangee = len(nums) / 2
    #    for i in range(rangee):
    #
    # elif len(nums) % 2 != 0:
    #     renge = len(nums) + 1 / 2
    #     for i in range(renge):



def max_block(s: str) -> int:
    """
    Given a string, return the length of the largest "block" in the string.

    A block is a run of adjacent chars that are the same.

    max_block("hoopla") => 2
    max_block("abbCCCddBBBxx") => 3
    max_block("") => 0
    """
    pass


if __name__ == '__main__':
    # print(positive_or_not([3, 4, -2, 1, -78, 0], False))
    print(sum_half_evens([2, 1, 2, 3, 4]))
