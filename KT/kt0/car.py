"""Car operations."""


class Car:
    """Car object."""

    def __init__(self, model, year, price):
        """Car constructor."""
        self.year = year
        self.model = model
        self.price = price


def create_car(model: str, price: int) -> 'Car':
    """Create a new car object with the current year if price is above 0."""
    if price > 0:
        car3 = Car(model, 2020, price)
    else:
        return None
    return car3


def get_most_expensive_car_below_price(cars: list, max_price: int) -> 'Car':
    """
    Return the most expensive car with the price lower than max_price.

    If several cars have the same price, return the first.
    If there are no cars with which have the price lower than max_price, return None.
    """
    res = []
    cars_list = []
    for car in cars:
        if car.price < max_price:
            res.append(car)
        if not res:
            return None
    res = sorted(res, key=lambda x: x.price, reverse=True)
    maximum = max(res)
    for carr in res:
        if carr.price == maximum.price:
            cars_list.append(carr)
    return cars_list[0]


def update_prices(cars: list, discount_per_year: int) -> None:
    """
    Update each car price so that for every year of their age they get discount_per_year lower price.

    If the car year is 2018 and currently it's 2020, then the discount is applied twice.
    The car price can never go below 0.

    Example:
        Currently it's 2020

        Car year is 2015
        Car price is 100
        discount_per_year = 5
        The new price for the car is 75

        Car year is 2000, price is 100, discount_per_year = 7
        The new price for the car is 0.
    """
    our_year = 2020
    for car in cars:
        price = car.price - ((our_year - car.year) * discount_per_year)
        if price < 0:
            car.price = 0
        else:
            car.price = price


def get_cars_with_model(cars: list, model: str) -> list:
    """Return list of cars with the given model."""
    res = []
    for car in cars:
        if car.model == model:
            res.append(car)
    return res


def get_ordered_cars(cars: list) -> list:
    """Return a new sorted list of cars by: year (newer first), price (cheaper first), model (from a to z)."""
    ret = [] + cars
    res = sorted(ret, key=lambda x: (-x.year, x.price, x.model))
    return res


if __name__ == '__main__':
    car1 = Car("BMW", 2020, 500)
    car2 = Car("Audi", 2000, 15000)
    listt = [car1, car2]
    print(get_most_expensive_car_below_price(listt, 10000))
