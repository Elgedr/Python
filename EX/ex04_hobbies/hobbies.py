"""Hobbies"""
import csv


def create_list_from_file(file):
    """Read names from file."""
    hobbies = []
    with open("hobbies_database.txt", encoding='utf-8') as file:
        for line in file:
            hobbies.append(line.strip())
    return hobbies


def create_dictionary(file):
    """Create dictionary about given peoples' hobbies as Name: [hobby_1, hobby_2]."""
    new_dict = {}
    for name in create_list_from_file(file):
        deleted_part = name.find(":")
        if name not in new_dict:
            new_dict[name[:deleted_part:]] = [name[deleted_part::]]
            # new_dict[name[:deleted_part:]].append(name[deleted_part::])
        if name and new_dict[name] in new_dict:
            pass
        elif name in new_dict and new_dict[name] not in new_dict:
            new_dict[name].append(name[deleted_part::])
    return new_dict


if __name__ == '__main__':
    dic = create_dictionary("hobbies_database.txt")
    print(len(create_list_from_file("hobbies_database.txt")))
    print(create_dictionary([]))