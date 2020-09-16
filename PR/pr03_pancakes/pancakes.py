"""Pancakes."""


def make_dough(ingredients: list):
    """Make dough."""
    egg = ingredients.count("egg")
    flour = ingredients.count("flour")
    milk = ingredients.count("milk")
    butter = ingredients.count("butter")
    sugar = ingredients.count("butter")
    dough = 0
    ingredients_count = ["egg", "flour", "milk", "butter", "sugar"]
    for elements in range(len(ingredients_count)):
        if egg >= 1 and milk >= 5 and butter >= 1 and flour >= 4 and sugar >= 2:
            dough = dough + 7
    return dough


def can_make_pancake(dough: float) -> bool:
    """Can make pancake."""
    dough_amount_for_one_pancake = 0.8
    if dough / dough_amount_for_one_pancake >= 1:
        return True
    else:
        return False


if __name__ == '__main__':
    print(make_dough(ingredients=["egg"] * 10 + ["milk"] * 20 + ["flour"] * 29 + ["butter"] * 10 + ["sugar"] * 17))
