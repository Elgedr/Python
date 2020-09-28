"""Hobbies."""
import csv


def create_list_from_file(file):
    """Read names from file."""
    with open(file, encoding='utf-8') as f:
        return f.read().splitlines()


def create_dictionary(file) -> dict:
    """Create dictionary about given peoples' hobbies as Name: [hobby_1, hobby_2]."""
    new_dict = {}
    for key in create_list_from_file(file):
        name = key.split(":")[0]
        hobby = key.split(":")[1]
        if name not in new_dict:
            new_dict[name] = [hobby]
        else:
            if hobby not in new_dict[name]:
                new_dict[name].append(hobby)
    return new_dict


def find_person_with_most_hobbies(file) -> list:
    """Find the person (or people) who have more hobbies than others."""
    people_hobbies_dict = create_dictionary(file)
    people = []
    amount = 0
    for key in people_hobbies_dict:
        if len(people_hobbies_dict[key]) > amount:
            amount = len(people_hobbies_dict[key])
            people.clear()
            people.append(key)
        elif len(people_hobbies_dict[key]) == amount:
            people.append(key)
    return people


def find_person_with_least_hobbies(file) -> list:
    """Find the person (or people) who have less hobbies than others."""
    people = []
    people_hobbies_dict = create_dictionary(file)
    amount = len(people_hobbies_dict)
    for key in people_hobbies_dict:
        if amount > len(people_hobbies_dict[key]):
            amount = len(people_hobbies_dict[key])
            people.clear()
            people.append(key)
        elif len(people_hobbies_dict[key]) == amount:
            people.append(key)
    return people


def find_most_popular_hobby(file) -> list:
    """Find the most popular hobby."""
    dictionary_from_names_and_hobbies = create_dictionary(file)  # словарь  в виде {"Mari": ["gym", "eating", "run"]}
    dictionary_with_values = {}  # словарь где {ключ = кол-во этих хобби: значение = само хобби}
    list_from_values = []
    for value in dictionary_from_names_and_hobbies.values():  # рассматриваем сразу значения из словаря по отдельности
        list_from_values = list_from_values + value  # добавляем все хобби в список
    for hobby in set(list_from_values):  # set используем для того, чтобы все элементы были разные
        dictionary_with_values.setdefault(list_from_values.count(hobby), []).append(hobby)  # вернет {key =
        # кол-во хобби : value = хобби }
    return dictionary_with_values[max(dictionary_with_values)]  # возвращаем значение с самым наибольшем ключем


def find_least_popular_hobby(file):
    """Find the least popular hobby."""
    dictionary_from_names_and_hobbies = create_dictionary(file)
    dictionary_with_values = {}
    list_from_values = []
    for value in dictionary_from_names_and_hobbies.values():
        list_from_values = list_from_values + value
    for hobby in set(list_from_values):
        dictionary_with_values.setdefault(list_from_values.count(hobby), []).append(hobby)
    return dictionary_with_values[min(dictionary_with_values)]


def write_corrected_database(file, file_to_write):
    """Write .csv file in a proper way. Use collected and structured data."""
    with open(file_to_write, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        name = "Name"
        hobbies = "Hobbies"
        writer.writerow([name, hobbies])
        dictt = create_dictionary(file)
        for i in dictt:
            dictt[i] = sorted(dictt[i])
        dictt = sorted(dictt.items())
        for key, value in dictt:
            name = key
            hobbies = "-".join(value)
            writer.writerow([name, hobbies])
    return file_to_write
