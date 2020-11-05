"""KT4."""
from typing import Optional


def odd_sums_of_consecutive_elements(nums: list) -> list:
    """
    Return list of odd sums of consecutive elements.

    Consider all consecutive elements in the input list. Return a list of all the odd sums of consecutive elements.

    odd_sums_of_consecutive_elements([1, 2, 3, 5]) => [3, 5]
    odd_sums_of_consecutive_elements([8, 10]) => []
    odd_sums_of_consecutive_elements([9]) => []
    odd_sums_of_consecutive_elements([11, 8]) => [19]

    :param nums:
    :return:
    """
    res = []
    for i in range(0, len(nums) - 1):
        summa = nums[i] + nums[i + 1]
        if summa % 2 != 0:
            res.append(summa)
    return res


def list_move(initial_list: list, amount: int, factor: int) -> list:
    """
    Create amount lists where elements are shifted right by factor.

    This function creates a list with amount of lists inside it.
    In each sublist, elements are shifted right by factor elements.
    factor >= 0

    list_move(["a", "b", "c"], 3, 0) => [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
    list_move(["a", "b", "c"], 3, 1) => [['a', 'b', 'c'], ['c', 'a', 'b'], ['b', 'c', 'a']]
    list_move([1, 2, 3], 3, 2) => [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    list_move([1, 2, 3], 4, 1) => [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 2, 3]]
    list_move([], 3, 4) => [[], [], []]
    """
    pass


def fizzbuzz_series_up(nr: int) -> list:
    """
    Create a list of fizzbuzz series.

    Create a list with the pattern

    [1,   1, 2,   1, 2, 3,   ... 1, 2, 3, 4, 5, 6, 7 .., 14, 15, 16 , .., n],

    where additionally all numbers divisible by 3 are replaced with string "fizz",
    and all numbers divisible by 5 are replaced with string "buzz"
    if number is divisible by 3 and 5, it should be replaced with "fizzbuzz:

    [1,   1, 2,   1, 2, "fizz",   ... 1, 2, "fizz", 4, "buzz", "fizz, 7 .., 14, "fizzbuzz, 16 , .., n]].

    (spaces added to show the grouping).

    If n is not positive, return empty list.

    series_up(3) → [1, 1, 2, 1, 2, "fizz"]

    series_up(2) → [1, 1, 2]

    series_up(4) → [1, 1, 2, 1, 2, "fizz", 1, 2, "fizz", 4]

    series_up(7) → [
                        1,
                        1, 2,
                        1, 2, "fizz",
                        1, 2, "fizz", 4,
                        1, 2, "fizz", 4, "buzz",
                        1, 2, "fizz", 4, "buzz", "fizz",
                        1, 2, "fizz", 4, "buzz", "fizz", 7
                    ]

    series_up(0) → []
    """
    pass


class Student:
    """Student class."""

    def __init__(self, name: str, average_grade: float, credit_points: int):
        """Constructor."""
        self.credit_points = credit_points
        self.average_grade = average_grade
        self.name = name


def create_student(name: str, grades: list, credit_points: int) -> Student:
    """
    Create a new student where average grade is the average of the grades in the list.

    Round the average grade up to three decimal places.
    If the list of grades is empty, the average grade will be 0.
    """
    if not grades:
        average = 0
        return Student(name, average, credit_points)
    else:
        average = round(sum(grades) / len(grades), 3)
        student1 = Student(name, average, credit_points)
    return student1


def get_top_student_with_credit_points(students: list, min_credit_points: int):
    """
    Return the student with the highest average grade who has enough credit points.

    If there are no students with enough credit points, return None.
    If several students have the same average score, return the first.
    """
    studentss = []
    for student in students:
        if student.credit_points > min_credit_points:
            studentss.append(student)
        res = sorted(studentss, key=lambda x: -x.average_grade)
        if not res:
            return None
        return res[0]


def add_result_to_student(student: Student, grades_count: int, new_grade: int, credit_points) -> Student:
    """
    Update student average grade and credit points by adding a new grade (result).

    As the student object does not have grades count information, it is provided in this function.
    average grade = sum of grades / count of grades

    With the formula above, we can deduct:
    sum of grades = average grade * count of grades

    The student has the average grade, function parameters give the count of grades.
    If the sum of grades is known, a new grade can be added and a new average can be calculated.
    The new average grade must be rounded to three decimal places.
    Given credits points should be added to old credit points.

    Example1:
        current average (from student object) = 4
        grades_count (from parameter) = 2
        so, the sum is 2 * 4 = 8
        new grade (from parameter) = 5
        new average = (8 + 5) / 3 = 4.333
        The student object has to be updated with the new average

    Example2:
        current average = 0
        grades_count = 0
        calculated sum = 0 * 0 = 0
        new grade = 4
        new average = 4 / 1 = 4

    Return the modified student object.
    """
    average = student.average_grade * grades_count
    newawerage = (average + new_grade) / (grades_count + 1)
    student.average_grade = round(newawerage, 3)
    student.credit_points = student.credit_points + credit_points
    return student


def get_ordered_students(students: list) -> list:
    """
    Return a new sorted list of students by (down).

    credit points (higher first), average_grade (higher first), name (a to z).
    """
    res = sorted(students, key=lambda x: (-x.credit_points, -x.average_grade, x.name))
    return res


class Room:
    """Room."""

    def __init__(self, number: int, price: int):
        """Constructor."""
        pass

    def add_feature(self, feature: str) -> bool:
        """
        Add a feature to the room.

        Do not add the feature and return False if:
        - the room already has that feature
        - the room is booked.
        Otherwise, add the feature to the room and return True
        """
        pass

    def get_features(self) -> list:
        """Return all the features of the room."""
        pass

    def get_price(self) -> int:
        """Return the price."""
        pass

    def get_number(self) -> int:
        """Return the room number."""
        pass


class Hotel:
    """Hotel."""

    def __init__(self):
        """Constructor."""
        pass

    def add_room(self, room: Room) -> bool:
        """
        Add room to hotel.

        If a room with the given number already exists, do not add a room and return False.
        Otherwise add the room to hotel and return True.
        """
        pass

    def book_room(self, required_features: list) -> Optional[Room]:
        """
        Book an available room which has the most matching features.

        Find a room which has most of the required features.
        If there are several with the same amount of matching features, return the one with the smallest room number.
        If there is no available rooms, return None
        """
        pass

    def get_available_rooms(self) -> list:
        """Return a list of available (not booked) rooms."""
        pass

    def get_rooms(self) -> list:
        """Return all the rooms (both booked and available)."""
        pass

    def get_booked_rooms(self) -> list:
        """Return all the booked rooms."""
        pass

    def get_feature_profits(self) -> dict:
        """
        Return a dict where key is a feature and value is the total price for the booked rooms which have the feature.

        Example:
            room1, price=100, features=a, b, c
            room2, price=200, features=b, c, d
            room3, price=400, features=a, c

        all the rooms are booked
        result:
        {
        'a': 500,
        'b': 300,
        'c': 700,
        'd': 200
        }
        """
        pass

    def get_most_profitable_feature(self) -> Optional[str]:
        """
        Return the feature which profits the most.

        Use get_feature_profits() method to get the total price for every feature.
        Return the feature which has the highest value (profit).
        If there are several with the same max value, return the feature which is alphabetically lower (a < z)
        If there are no features booked, return None.
        """
        pass


if __name__ == '__main__':
    hotel = Hotel()
    room1 = Room(1, 100)
    room1.add_feature("tv")
    room1.add_feature("bed")
    room2 = Room(2, 200)
    room2.add_feature("tv")
    room2.add_feature("sauna")
    hotel.add_room(room1)
    hotel.add_room(room2)
    # TODO: try to add room with existing number, try to add existing feature to room
    assert hotel.get_rooms() == [room1, room2]
    assert hotel.get_booked_rooms() == []

    assert hotel.book_room(["tv", "president"]) == room1
    assert hotel.get_available_rooms() == [room2]
    assert hotel.get_booked_rooms() == [room1]

    assert hotel.book_room([]) == room2
    assert hotel.get_available_rooms() == []

    assert hotel.get_feature_profits() == {
        'tv': 300,
        'bed': 100,
        'sauna': 200
    }
    assert hotel.get_most_profitable_feature() == 'tv'

    # TODO: try to add a room so that two or more features have the same profit
