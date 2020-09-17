"""Pancakes."""


def make_dough(ingredients: list):
    """Make dough."""
    egg = ingredients.count("egg") // 1
    flour = ingredients.count("flour") // 4
    milk = ingredients.count("milk") // 5
    butter = ingredients.count("butter") // 1
    sugar = ingredients.count("sugar") // 2
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
    after_cooking = taina_kogus - for_one_pancake
    result = round(after_cooking, 2)
    return result


def make_n_pancakes(n: int, ingredients: list):
    """Make n pancakes."""
    dough_amount = make_dough(ingredients)  # например 7
    done_pancakes = 0
    if can_make_pancake(dough_amount) is False:
        return done_pancakes
    else:
        while can_make_pancake(dough_amount) is True:
            dough_amount = make_a_pancake(dough_amount)
            done_pancakes = done_pancakes + 1
    if done_pancakes > n:
        return n
    return done_pancakes


if __name__ == '__main__':
    ingredients = ["egg"] + ["milk"] * 5 + ["flour"] * 4 \
                  + ["butter"] + ["sugar"]
    print(make_dough(ingredients))  # 0 -> not enough sugar.
    ingredients2 = ["egg"] * 4 + ["milk"] * 9 + ["flour"] * 14 \
                        + ["butter"] * 3 + ["sugar"] * 7
    print(make_dough(ingredients2))  # 7 -> can make 7dl dough not 7.x dl.
    ingredients3 = ["egg" for _ in range(3)] + ["milk" for _ in range(15)] + ["flour" for _ in range(7)] \
                  + ["butter" for _ in range(3)] + ["sugar" for _ in range(2)]
    print(make_n_pancakes(8, ingredients3))  # 8
    ingredients4 = ["egg" for _ in range(21)] + ["milk" for _ in range(45)] + ["flour" for _ in range(4)] \
                  + ["butter" for _ in range(14)] + ["sugar" for _ in range(12)]
    print(make_n_pancakes(4, ingredients4))  # 4 -> 7dl dough, 0.8dl per pancake -> could make 8 pancakes, we want 4