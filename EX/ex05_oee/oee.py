"""EX05 - OEE."""
import csv


def read_production_data(filename: str) -> dict:
    """Read a csv file and make a dictionary."""
    productivity_dictionary = {}
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] in productivity_dictionary:
                pass
            else:
                productivity_dictionary[row[0]] = row[1::]
        return productivity_dictionary



def calculate_quality(production_data: dict) -> dict:
    """Quality."""
    quality_dict = {}
    for k, v in production_data.items():
        try:
            result = float(int(v[3]) / int(v[2]))
            resultt = round(result, 3) * 100
        except ZeroDivisionError:
            resultt = 0.0
        quality_dict[k] = resultt
    return quality_dict


def calculate_availability(production_data: dict) -> dict:
    """Availabilty."""
    production_dict = {}
    for k, v in production_data.items():
        try:
            result = float(int(v[0]) / 420)
            resultt = round(result, 3) * 100
        except ZeroDivisionError:
            resultt = 0.0
        production_dict[k] = resultt
    return production_dict


def calculate_performance(production_data: dict) -> dict:
    """Performance."""


def calculate_oee(production_data: dict) -> dict:
    """oee."""


def write_results_to_file(production_data: dict, filename: str):
    """Results to fole."""


if __name__ == '__main__':
    prod_data = read_production_data("reedene_vahetus.csv")
    print('\n- Production data -')
    print('[Run Time (minutes), Ideal Run Rate (pcs/min), Total Count (pcs), Good Count (pcs)]')
    for key, value in prod_data.items():
        print(f"{key}: {value}")

    # Sildistaja: [358, 57, 18602, 18388]
    # Hapukurgipurgitaja: [415, 12, 4800, 2013]
    # Autoklaav: [450, 10, 4500, 4500]
    # Supivillija: [402, 36, 14230, 14214]
    # Makaronikeetja: [410, 25, 10230, 10230]
    # Kartulikoorija: [420, 111, 46620, 44123]
    # Mahlapress: [0, 0, 0, 0]

    quality_dict = calculate_quality(prod_data)
    print('\n- Quality calculation results -')
    for key, value in quality_dict.items():
        print(f"{key}: {value}")

    # Sildistaja: 98.8
    # Hapukurgipurgitaja: 41.9
    # Autoklaav: 100.0
    # Supivillija: 99.9
    # Makaronikeetja: 100.0
    # Kartulikoorija: 94.6
    # Mahlapress: 0.0

    availability_dict = calculate_availability(prod_data)
    print('\n- Availability calculation results -')
    for key, value in availability_dict.items():
        print(f"{key}: {value}")

    # Sildistaja: 85.2
    # Hapukurgipurgitaja: 98.8
    # Autoklaav: 107.1
    # Supivillija: 95.7
    # Makaronikeetja: 97.6
    # Kartulikoorija: 100.0
    # Mahlapress: 0.0