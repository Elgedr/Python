"""Order names by popularity."""


def read_from_file() -> list:
    """Read names from file."""
    names = []
    with open("popular_names.txt", encoding='utf-8') as file:
        for line in file:
            names.append(line.strip())
    return names


def to_dictionary(names: list) -> dict:
    """To dictioary."""
    new_dict = {}
    for name in names:
        if name not in new_dict:
            new_dict[name] = names.count(name)
        else:
            pass
    return new_dict


def to_sex_dicts(names_dict: dict) -> tuple:
    """Divide the names by sex to 2 different dictionaries."""
    female_names = {}
    male_names = {}
    for keys in names_dict:
        if 'F' in keys:
            female_names[keys[:-2:]] = names_dict[keys]
        elif 'M' in keys:
            male_names[keys[:-2:]] = names_dict[keys]
    return female_names, male_names

if __name__ == '__main__':
    print(to_sex_dicts({'Kati:F': 1000, 'Mati:M': 800, 'Mari:F': 600, 'Tõnu:M': 400}))

def most_popular(names_dict: dict) -> str:
    """Find the most popular name in the dictionary."""
    if len(names_dict) == 0:
        return "Empty dictionary."
    else:
        result = max(names_dict, key=names_dict.get)
    return result


def number_of_people(names_dict: dict) -> int:
    """Calculate the number of people in the dictionary."""
    result = sum(names_dict.values())
    return result
# zzz

def names_by_popularity(names_dict: dict) -> str:
    """Create a string used to print the names by popularity."""
    if len(names_dict) == 0:
        return ""
