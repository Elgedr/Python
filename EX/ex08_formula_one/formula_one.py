"""Formula One."""

import re
import csv


class Driver:
    """Driver class."""

    def __init__(self, name: str, team: str):
        """
        Driver constructor.
        Here you should save driver's results as dictionary,
        where key is race number and value is points from that race.
        You must also save driver's points into a variable "points".
        """
        self._name = name  # Driver name
        self._team = team  # Driver team
        self._points = 0  # Driver's points
        self._driver_result = {}  # key-etapi number (int) ; value-sellelt etapilt saadud punktid (int)

    def get_results(self) -> dict:
        """Get all driver's results."""
        return self._driver_result

    def get_points(self) -> int:
        """Return calculated driver points."""
        return self._points

    def set_points(self):
        """Set points for driver."""

    def add_result(self, race_number: int, points: int):
        """Add new result to dictionary of results."""
        self._driver_result[race_number] = points

    def count_points(self):
        """Count  driver's points"""


class Race:
    """Race class."""

    def __init__(self, file):
        """Race constructor."""
        self._file = file  # File with race data
        pass

    def read_file_to_list(self):
        """Read file data to list in constructor."""
        res = []
        try:
            with open(self._file) as f:
                next(f)  # пропускает 1ую строку
                for line in f:
                    data = re.split(r"  +", line)  # ['Mika Häkkinen', 'McLaren-Mercedes', '42069']
                    drivers_str = " ".join(data)  # 'Mika Häkkinen McLaren-Mercedes 42069' вернет строку составленную из элементов списка
                    res.append(drivers_str)
        except FileNotFoundError:
            return 'No file found!'
        raise

    @staticmethod
    def extract_info(line: str) -> dict:
        """ Helper method for read_file_to_list."""
        res = {}
        res['Name'] = line[0]
        res['Team'] = line[1]
        res['Time'] = int(line[2])
        res['Diff'] = ''
        res['Race'] = line[-1]
        return res

    def filter_data_by_race(self, race_number: int) -> list:
        """
        Filter data by race number.

        :param race_number: Race number
        :return: Filtered race data
        """
        file = self.read_file_to_list()
        copy_file = file
        res = []
        for info_of_person in copy_file:
            if info_of_person[-1] == race_number:
                res.append(info_of_person)
        return res

    @staticmethod
    def format_time(time: str) -> str:
        """
        Format time from milliseconds to M:SS.SSS

        format_time('12') -> 0:00.012
        format_time('1234') -> 0:01.234
        format_time('123456') -> 2:03.456

        :param time: Time in milliseconds
        :return: Time as M:SS.SSS string
        """
        return ""

    @staticmethod
    def calculate_time_difference(first_time: int, second_time: int) -> str:
        """
        Calculate difference between two times.

        First time is always smaller than second time. Both times are in milliseconds.
        You have to return difference in format +M:SS.SSS

        calculate_time_difference(4201, 57411) -> +0:53.210

        :param first_time: First time in milliseconds
        :param second_time: Second time in milliseconds
        :return: Time difference as +M:SS.SSS string
        """
        return ""

    @staticmethod
    def sort_data_by_time(results: list) -> list:
        """
        Sort results data list of dictionaries by 'Time'.

        :param results: List of dictionaries
        :return: Sorted list of dictionaries
        """
        return []

    def get_results_by_race(self, race_number: int) -> list:
        """
        Final results by race number.

        This method combines the rest of the methods.
        You have to filter data by race number and sort them by time.
        You must also fill 'Diff' as time difference with first position.
        You must add 'Place' and 'Points' key-value pairs for each dictionary.

        :param race_number: Race number for filtering
        :return: Final dictionary with complete data
        """
        return []


class FormulaOne:
    """FormulaOne class."""

    def __init__(self, file):
        """
        FormulaOne constructor.

        It is reasonable to create Race instance here to collect all data from file.
        """
        self._file = file  # File with race data
        pass

    def write_race_results_to_file(self, race_number: int):
        """
        Write one race results to a file.

        File name is 'results_for_race_{race_number}.txt'.
        Exact specifications are described in the text.

        :param race_number: Race to write to file
        """
        pass

    def write_race_results_to_csv(self, race_number: int):
        """
        Write one race results to a csv file.

        File name is 'race_{race_number}_results.csv'.
        Exact specifications are described in the text.

        :param race_number: Race to write to file
        """
        pass

    def write_championship_to_file(self):
        """
        Write championship results to file.

        It is reasonable to create Driver class instance for each unique driver name and collect their points
        using methods from Driver class.
        Exact specifications are described in the text.
        """
        pass


if __name__ == '__main__':
    f1 = FormulaOne("example.txt")
    f1.write_race_results_to_file(1)
    f1.write_race_results_to_csv(2)
    f1.write_championship_to_file()
