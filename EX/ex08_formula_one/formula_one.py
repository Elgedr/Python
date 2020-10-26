"""Formula One."""

import re
import csv
import os.path


class Driver:
    """Driver class."""

    def __init__(self, name: str, team: str):
        """
        Driver constructor.

        Here you should save driver's results as dictionary,
        where key is race number and value is points from that race.
        You must also save driver's points into a variable "points".
        """
        self.name = name  # Driver name
        self.team = team  # Driver team
        self.points = 0  # Driver's points
        self.driver_result = {}  # key-etapi number (int) ; value-sellelt etapilt saadud punktid (int)

    def get_results(self) -> dict:
        """Get all driver's results."""
        return self.driver_result

    def get_points(self) -> int:
        """Return calculated driver points."""
        return self.points

    def set_points(self):
        """Set points for driver."""
        self.points = 0
        for points in self.driver_result.values():
            self.points += points

    def add_result(self, race_number: int, points: int):
        """Add new result to dictionary of results."""
        self.driver_result[race_number] = points


class Race:
    """Race class."""

    def __init__(self, file):
        """Race constructor."""
        self._file = file  # File with race data
        self._opend_file = []
        self.read_file_to_list()  # пишем метод сюда, чтобы он сработал автоматом
        self._amount_of_race = self._opend_file.pop(0)  # поп удаляет элемент по указанному индексу и возвращает его. теперь в нашем открытом файле нет 3ойки

    def read_file_to_list(self):
        """Read file data to list in constructor."""
        if os.path.isfile(self._file):  # проверяем существует ли файл
            with open(self._file) as f:
                # next(f) пропускает 1ую строку
                for line in f:
                    data = line.rstrip()  # ['Mika Häkkinen', 'McLaren-Mercedes', '42069'] если 2 или больше
                    # пробела разделяет. rstrip удаляет все элементы справа если это /n, /r, /t. так что в скобках можно ничего не указывать
                    # drivers_str = " ".join(data)  # 'Mika Häkkinen McLaren-Mercedes 42069 2' вернет строку составленную
                    # из элементов списка
                    self._opend_file.append(data)
        else:
            raise FileNotFoundError("No file found!")  # raise работает как return. после него код не работает

    @staticmethod
    def extract_info(line: str) -> dict:
        """Helper method for read_file_to_list."""
        res = re.split(r"\s\s+", line)  # r пишем так как у нас регулярное выражение. \s значит
        result = {'Name': res[0], 'Team': res[1], 'Time': int(res[2]), 'Diff': '', 'Race': int(res[3])}
        return result

    def filter_data_by_race(self, race_number: int) -> list:
        """
        Filter data by race number.

        :param race_number: Race number
        :return: Filtered race data
        """
        res = []
        for info_of_person in self._opend_file:
            if int(self.extract_info(info_of_person)['Race']) == race_number:
                res.append(self.extract_info(info_of_person))
        return res

    @staticmethod
    def format_time(time: str) -> str:
        """
        Format time from milliseconds to M:SS.SSS.

        format_time('12') -> 0:00.012
        format_time('1234') -> 0:01.234
        format_time('123456') -> 2:03.456

        :param time: Time in milliseconds
        :return: Time as M:SS.SSS string.
        """
        milliseconds = int(time)
        minutes = milliseconds // 60000  # получим целую часть. узнаем минуты
        milliseconds -= minutes * 60000  # отнимем полученный результат от миллисекунд
        seconds = milliseconds // 1000
        milliseconds -= seconds * 1000
        milliseconds = str(milliseconds)
        seconds = str(seconds)
        return f"{minutes}:{seconds.zfill(2)}.{milliseconds.zfill(3)}"  # zfill(нужная длина) добавляет 0 к началу
        # строки пока она не станет нужной длины, которую мы указали

    @staticmethod
    def calculate_time_difference(first_time: int, second_time: int) -> str:
        """
        Calculate difference between two times.

        First time is always smaller than second time. Both times are in milliseconds.
        You have to return difference in format +M:SS.SSS

        calculate_time_difference(4201, 57411) -> +0:53.210

        :rtype: object
        :param first_time: First time in milliseconds
        :param second_time: Second time in milliseconds
        :return: Time difference as +M:SS.SSS string.
        """
        difference = (second_time - first_time)
        difference = str(difference)
        res = f"+{Race.format_time(difference)}"  # чтобы позвать статик метод в другом статик методе используем "название класса."
        return res  # возвращает разницу во времени в нужном формате

    @staticmethod
    def sort_data_by_time(results: list) -> list:
        """
        Sort results data list of dictionaries by 'Time'.

        :param results: List of dictionaries
        :return: Sorted list of dictionaries
        """
        res = sorted(results, key=lambda dictionary: dictionary['Time'])
        return res

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
        final_list = []
        points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
        place = 1
        filtered = self.filter_data_by_race(race_number)  # сортируем список из файла по номеру гонки.
        # получаем лист из словарей, относящихся к определенной гонке
        sorted_by_time = self.sort_data_by_time(filtered)  # сортируем прошлый список по времени
        first = [dictionary['Time'] for dictionary in sorted_by_time][0]  # получаем значение ключа из словаря того,
        # чье время меньше всего
        for dictionary in sorted_by_time:
            last = dictionary.get('Time')  # получить значение ключа в словаре
            dictionary["Diff"] = self.calculate_time_difference(first, last)  # добавляем в словарь difference в правильном формате
            time = self.format_time(dictionary["Time"])
            dictionary["Time"] = time
            dictionary["Place"] = place
            if place <= 10:
                point = points[place - 1]
                dictionary["Points"] = point
            if dictionary['Place'] == 1:
                dictionary['Diff'] = ''
            place += 1
            final_list.append(dictionary)
        return final_list


class FormulaOne:
    """FormulaOne class."""

    def __init__(self, file):
        """
        FormulaOne constructor.

        It is reasonable to create Race instance here to collect all data from file.
        """
        self._file = file  # File with race data
        self._race = Race(file)

    def write_race_results_to_file(self, race_number: int):
        """
        Write one race results to a file.

        File name is 'results_for_race_{race_number}.txt'.
        Exact specifications are described in the text.

        :param race_number: Race to write to file
        """
        filename = f'results_for_race_{race_number}.txt'
        filtered_file = self._race.get_results_by_race(race_number)
        with open(filename, 'w') as file:
            file.write(f'PLACE{5 * " "}NAME{21 * " "}TEAM{21 * " "}TIME{11 * " "}DIFF{11 * " "}POINTS{0 * " "}\n'
                       f'{96 * "-"}\n')
            for dictionaries in filtered_file:
                file.write(f'{dictionaries["Place"]}{(10 - len(str(dictionaries["Place"]))) * " "}'  # write записывает 1 строку в файл
                           f'{dictionaries["Name"]}{(25 - len(dictionaries["Name"])) * " "}'
                           f'{dictionaries["Team"]}{(25 - len(str(dictionaries["Team"]))) * " "}'
                           f'{dictionaries["Time"]}{(15 - len(str(dictionaries["Time"]))) * " "}'
                           f'{dictionaries["Diff"]}{(15 - len(dictionaries["Diff"])) * " "}'
                           f'{dictionaries["Points"]}{(6 - len(str(dictionaries["Points"]))) * " "}\n')

    def write_race_results_to_csv(self, race_number: int):
        """
        Write one race results to a csv file.

        File name is 'race_{race_number}_results.csv'.
        Exact specifications are described in the text.

        :param race_number: Race to write to file
        """
        file_name = f'race_{race_number}_results.csv'
        with open(file_name, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['Place', 'Name', 'Team', 'Time', 'Diff', 'Points', 'Race'])
            for dictionary in self._race.get_results_by_race(race_number):
                writer.writerow([dictionary["Place"], dictionary["Name"], dictionary["Team"],dictionary["Time"], dictionary["Diff"], dictionary["Points"], race_number])

    def write_championship_to_file(self):
        """
        Write championship results to file.

        It is reasonable to create Driver class instance for each unique driver name and collect their points
        using methods from Driver class.
        Exact specifications are described in the text.
        """
        pass


if __name__ == '__main__':
    f1 = FormulaOne("ex08_example_data.txt")
    print(Race.format_time('6000'))
    f1.write_race_results_to_file(1)
    f1.write_race_results_to_csv(2)
    f1.write_race_results_to_csv(1)
    f1.write_championship_to_file()
    print(Race.calculate_time_difference(4201, 57411))
    print(Race.extract_info("Mika Hakkinen  Mclaren-Mercedes   79694  1"))
    print([{'Name': "ellina", 'Time': 200, 'Race': 2}, {'Name': "robi", 'Time': 100, 'Race': 10}, {'Name': "milja", 'Time': 900, 'Race': 7}])
    r1 = Race('ex08_example_data.txt')
    print(r1.filter_data_by_race(1))
    print(r1.get_results_by_race(2))
