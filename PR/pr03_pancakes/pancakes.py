"""Pancakes."""


def make_dough(ingredients: list):
    """Make dough."""
    egg = ingredients.count("egg") // 1
    flour = ingredients.count("flour") // 4
    milk = ingredients.count("milk") // 5
    butter = ingredients.count("butter") // 1
    sugar = ingredients.count("butter") // 2
    amount = [egg, flour, milk, butter, sugar]
    dough = min(amount) * 7
    return dough


def can_make_pancake(dough: float) -> bool:
    """Can make pancake."""
    dough_amount_for_one_pancake = 0.8
    if dough / dough_amount_for_one_pancake >= 1:
        return True
    return False


def make_a_pancake(dough: float):
    """Make a pancake."""
    taina_kogus = dough
    for_one_pancake = 0.8
    after_cooking = taina_kogus / for_one_pancake
    result = round(after_cooking, 2)
    return result


def make_n_pancakes(n: int, ingredients: list):
    """Make n pancakes."""
    dough_amount = make_dough(ingredients)
    done_pancakes = 0
    for i in range(0, n):
        if can_make_pancake(dough_amount):
            dough_amount = make_a_pancake(dough_amount)
            done_pancakes = done_pancakes + 1
    return done_pancakes



if __name__ == '__main__':

    print(make_dough(ingredients=["egg"] * 10 + ["milk"] * 20 + ["flour"] * 29 + ["butter"] * 10 + ["sugar"] * 17))
