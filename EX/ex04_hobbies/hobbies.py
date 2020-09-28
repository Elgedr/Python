"""Hobbies"""
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
    """ Find the person (or people) who have less hobbies than others."""
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
    people_hobbies_dict = create_dictionary(file)
    all_hobbies = list(people_hobbies_dict.values())
    the_most_popular_hobby = []
    hobby_amount = {}
    for hobby in all_hobbies:
        hobby_amount[hobby] = all_hobbies.count(hobby)
    for hobby in hobby_amount:
        if hobby_amount[hobby] == hobby_amount[max(hobby_amount, key=hobby_amount.get)]:
            the_most_popular_hobby.append(hobby)
    return the_most_popular_hobby


def find_least_popular_hobby(file):
    """Find the least popular hobby."""


def write_corrected_database(file, file_to_write):
    """Write .csv file in a proper way. Use collected and structured data."""
    with open(file_to_write, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        name = "Name"
        hobbies = "Hobbies"
        writer.writerow([name, hobbies])
