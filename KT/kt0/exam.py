"""KT0."""


def nr_of_common_characters(string1: str, string2: str) -> int:
    """
    Return a number of common characters of string1 and string2.

    Do not take into account repeated characters.

    common_characters("iva", "avis") -> 3 # 'a', 'i', 'v' are common
    common_characters("saali", "pall") -> 2  # 'a', 'l' are common
    common_characters("memm", "taat") -> 0
    common_characters("memm", "") -> 0

    """
    res = []
    if len(string2) == 0 or len(string1) == 0:
        return 0
    for letter in string1:
        if letter in string2:
            res.append(letter)
            string1.replace(letter, '')
    return len(set(res))


def nr_into_num_list(nr: int, num_list: list) -> list:
    """
    Return a list of numbers where the "nr" is added into the "num_list" so that the list keep going to be sorted.

    Built-in sort methods are not allowed.

    nr_into_num_list(5, []) -> [5]
    nr_into_num_list(5, [1,2,3,4]) -> [1,2,3,4,5]
    nr_into_num_list(5, [1,2,3,4,5,6]) -> [1,2,3,4,5,5,6]
    nr_into_num_list(0, [1,2,3,4,5]) -> [0,1,2,3,4,5,]

    """
    if not num_list:
        num_list.append(nr)
        return num_list
    for num in num_list:
        ind = num_list.index(num)
        if nr == num or num + 1 == nr:
            num_list.insert(ind + 1, nr)
            break
        elif num - 1 == nr:
            num_list.insert(ind, nr)
            break
    return num_list


if __name__ == '__main__':
    print(nr_of_common_characters("iva", "avis"))
    print(nr_of_common_characters("saali", "pall"))
    print(nr_of_common_characters("memm", "taat"))
    print(nr_of_common_characters("memm", ""))
    print(nr_into_num_list(5, [1, 2, 3, 4]))
    print(nr_into_num_list(0, [1, 2, 3, 4, 5]))
    print(nr_into_num_list(5, [1, 2, 3, 4, 6, 7, 8]))
    print(nr_into_num_list(777, []))
