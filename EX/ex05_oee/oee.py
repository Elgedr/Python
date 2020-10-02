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
                print(productivity_dictionary)
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
