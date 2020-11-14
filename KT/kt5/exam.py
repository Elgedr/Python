"""KT5."""


def take_partial(text: str, leave_count: int, take_count: int) -> str:
    """
    Take only part of the string.

    Ignore first leave_count symbols, then use next take_count symbols.
    Repeat the process until the end of the string.

    The following conditions are met (you don't have to check those):
    leave_count >= 0
    take_count >= 0
    leave_count + take_count > 0

    take_partial("abcdef", 2, 3) => "cde"
    take_partial("abcdef", 0, 1) => "abcdef"
    take_partial("abcdef", 1, 0) => ""
    """
    pass


def divisible_numbers(nums: list):
    """
    Given a list of integers.

    Return a dictionary where the keys are all the positive numbers
    that are can divide at least one number in the list
    and value are all the numbers in the given list that are divisible by that number.

    The given list will not have any 0-s.

    print(divisible_numbers([1, 2, 3]))  # {1: [1, 2, 3], 2: [2], 3: [3]}
    print(divisible_numbers([1, 2, 4, 8, 16]))  # {1: [1, 2, 4, 8, 16], 2: [2, 4, 6, 8, 16], 4: [4], 8: [8], 16: [16]}

    :param nums:
    :return:
    """
    res = {}
    for num in nums:
        res[num] = []
        for i in range(len(nums)):
            if nums[i] % num == 0:
                res[num].append(nums[i])
    return res


def min_max_diff(nums):
    """
    Find the diff between the smallest and the biggest diff between two integer numbers in the list.

    The list will have at least 2 elements.

    min_diff([1, 2, 3]) => 1 & 2 => 1
    min_diff([1, 9, 19]) => 8 & 18 => 10
    min_diff([100, 90]) => 10 & 10 => 0
    min_diff([1, 100, 1000, 1]) => 0 & 999 => 999

    :param nums: list of ints, at least 2 elements.
    :return: diff between biggest and smallest diff.
    """
    minimum = min(nums)
    maximum = max(nums)
    return maximum - minimum


class Movie:
    """Movie object, do not change."""

    def __init__(self, name: str, year: int, genres: list):
        """Constructor."""
        self.name = name
        self.year = year
        self.genres = genres


def create_movie(name_with_year: str, genre1: str, genre2: str):
    """
    Create a new movie from name and 2 genres.

    Name is in format "name some thing (2019)".
    Year is inside parenthesis and always 4 digits.
    Everything before parenthesis is a name.
    Return None, if:
    - year is below 1900 and above 2020 ("blah (1200)", "blah (3000)")
    - name is empty ("(1933)")
    Otherwise create a new movie and return it.

    Year has to be int.
    Remove trailing space from name.
    "film (1999)" => should give "film" 1999
    """
    if len(name_with_year) <= 6:
        return None
    name = name_with_year.split(' (')[0]
    year = name_with_year.split(' (')[1]
    yearr = int(year[:-1])
    if 2020 < yearr < 1900:
        return None
    else:
        film = Movie(name, yearr, [genre1, genre2])
    return film



def get_ordered_movies(movies: list) -> list:
    """
    Return sorted movies by year (desc, newer first) and count of genres (asc).

    If both year and count of genres are the same, keep the original order.
    """
    res = sorted(movies, key=lambda x: (-x.year, x.genres))
    return res


def add_genres(movies: list, genres: list) -> None:
    """
    Modify the movies in the list by adding genres.

    A genre is added if it does not already exist.
    """
    for i in movies:
        for genre in genres:
            if genre not in i.genres:
                i.genres.append(genre)


def remove_movies_by_genre(movies: list, genre: str) -> list:
    """
    Return a new list where all the movies with the given genre are removed.

    The order of movies should remain the same.
    The original movies list should remain unchanged.
    """
    new = movies
    for movie in new:
        if genre in movie.genres:
            new.remove(movie)
    return new


class Disease:
    """Disease."""

    def __init__(self, name):
        """Constructor."""
        pass

    def get_name(self):
        """Return name."""
        pass


class Patient:
    """Patient."""

    def __init__(self, name):
        """Constructor."""
        pass

    def get_diseases(self):
        """Return diseases list."""
        pass

    def get_name(self):
        """Return patient name."""
        pass

    def add_disease(self, disease: Disease) -> bool:
        """
        Add a disease to the patient.

        If the patient already has the disease with the same name, return False.
        Otherwise add the disease to the patient and return True.
        """
        pass


class Hospital:
    """Hospital."""

    def __init__(self, max_patients):
        """
        Constructor.

        max_patients indicates how many active patients
        the hospital can hold.
        This value is guaranteed to be non-negative.
        """
        pass

    def add_patient(self, patient: Patient) -> bool:
        """
        Add a patient to the hospital.

        Check the conditions in the following order:
        If the given patient has no diseases, he/she will be
        counted into cured patients (see method below), return False.
        The previous condition is checked even if the hospital is full.

        If there is no more room for the patient, return False.

        If the given patient is already in hospital (in active patients list),
        return False.

        Otherwise return True.

        For simplicity the patient who has been cured will not return to the hospital.
        """
        pass

    def get_active_patients(self):
        """Return the list of active patients in the order of adding."""
        pass

    def cure(self, disease: Disease, amount: int, cost: int):
        """
        Cure certain patients.

        You have certain amount of cure for the given disease.
        You have to treat the patients who have a disease with the same name
        as the given disease.
        First, you have to cure the patients who have more diseases.
        So, a patient with 3 diseases should be cured before a patient
        with 2 diseases and so on.
        If the patients have the same amount of diseases, take one
        who was added before.
        In case of curing, remove the disease from the patient.
        If the patient has no diseases, he/she will be put into cured patients
        (see method below) and removed from active patients list.

        Treating a patient costs a certain amount.
        This cost has to be summed up for the patient.

        Return how many patients got treatment.
        If there are 10 patients with the given disease and "amount" is 3, return 3.
        If there are 10 patients with the given disease and "amount" is 20, return 10.
        """
        pass

    def get_patients_by_diseases(self) -> dict:
        """
        Return diseases and all the patients for each disease.

        The order of elements (key-value pairs) in dict is not important.
        The order of elements in values should be the same
        as in active patients list (the order patients were added).
        This means if the patients list is: [patient1, patient2, patient3]
        then the result should be:

        {"covid": [patient1, patient2],
        "astma": [patient1, patient3]}

        The list of patients is in the same order.
        """
        pass

    def get_cured_patients(self) -> list:
        """
        Return a list of cured (have no diseases) patients.

        There is no limit how many patients can be in this list.
        """
        pass

    def get_cost_by_patient(self) -> dict:
        """
        Get treatment cost by person.

        Return dict where key is the name of the patient and
        the value is the cost for the given person.
        You can assume there are no duplicate names in patients.
        You have to count both active and cured patients.
        For example if there is a patient named "Ago"
        and he is not cured yet, the method returns:
        {"Ago": 0}

        The order of elements in dictionary is not important.
        """
        pass

    def get_total_cost(self):
        """Return total cost of treatments."""
        pass


if __name__ == '__main__':
    print(min_max_diff([1, 9, 19]))
    print(divisible_numbers([1, 2, 4, 8, 16]))