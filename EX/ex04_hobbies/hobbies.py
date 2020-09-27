"""Hobbies"""
import csv


def create_list_from_file(file):
    """Read names from file."""
    with open(file, encoding='utf-8') as f:
        return f.read().splitlines()


def create_dictionary(file):
    """Create dictionary about given peoples' hobbies as Name: [hobby_1, hobby_2]."""
    new_dict = {}
    for i in create_list_from_file(file):
        name = i.split(":")[0]
        hobby = i.split(":")[1]
        if name not in new_dict:
            new_dict[name] = [hobby]
        else:
            if hobby not in new_dict[name]:
                new_dict[name].append(hobby)
    return new_dict


def find_person_with_most_hobbies(file):
    """Find the person (or people) who have more hobbies than others."""
    people_hobbies_dict = create_dictionary(file)
    people = []
    amount = 0
    for i in people_hobbies_dict:
        if len(people_hobbies_dict[i]) > amount:
            amount = len(people_hobbies_dict[i])
            people.clear()
            people.append(i)
        elif len(people_hobbies_dict[i]) == amount:
            people.append(i)
    return people


def find_person_with_least_hobbies(file):
    """ Find the person (or people) who have less hobbies than others."""
    person = []


if __name__ == '__main__':
    file = "hobbies_database.txt"
    dic = create_dictionary(file)
    print(len(create_list_from_file(file)))
    print(find_person_with_most_hobbies(file))