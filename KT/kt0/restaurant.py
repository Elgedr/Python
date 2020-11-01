"""Restaurant system."""


class Restaurant:
    """Restaurant."""

    def __init__(self, name: str):
        """Restaurant constructor."""
        self.name = name
        self.dishes = []
        self.menu = []

    def add_dish(self, dish: 'Dish') -> bool:
        """Add a dish if not already in restaurant."""
        if dish in self.dishes:
            return False
        else:
            self.dishes.append(dish)
            return True

    def get_dishes(self) -> list:
        """Return all the dishes in the restaurant."""
        dishes = self.dishes
        return dishes

    def add_menu(self, menu: 'Menu') -> bool:
        """
        Add a menu to the restaurant if all the dishes are available.

        Menu cannot be added if:
        - it has no dishes
        - the menu with the same dishes (in any order) already exists
        """
        if not menu.dishes:
            return False
        elif menu.compare_to() is True:
            #TODO   CJFNVKFDNOIFVNPLFDNJFNSBVNF[VJWIN
            return False
        for dish in menu.dishes:
            if dish not in self.dishes:
                return False
        else:
            self.menu.append(menu.dishes)
            return True

    def get_menus(self) -> list:
        """Return all the menus in the restaurant."""
        menues = self.menu
        return menues

    def get_dishes_available_in_menu(self) -> list:
        """Return unique dishes which are in one of the menues."""
        available_dishes = set(self.menu)
        return available_dishes

    def get_menus_ordered_by_price(self) -> list:
        """A new list of menus ordered by total price (highest first), then by dish count (lower first)."""
        prices = []
        for menu in self.menu:



class Dish:
    """Dish (food)."""

    def __init__(self, name: str, price: int):
        """Dish constructor."""
        self.name = name
        self.price = price

    def get_name(self) -> str:
        """Return the name of the dish."""
        name = self.name
        return name

    def get_price(self) -> int:
        """Return the price of the dish."""
        price = self.price
        return price


class Menu:
    """Menu which holds different dishes."""

    def __init__(self):
        """Menu constructor."""
        self.dishes = []  # dishes from Dich class

    def add_dish(self, dish: Dish) -> bool:
        """Add dish to menu if it does not exist already."""
        if dish in self.dishes:
            return False
        else:
            self.dishes.append(dish)
            return True

    def get_dishes(self) -> list:
        """Return all the dishes in menu."""
        dishes = self.dishes
        return dishes

    def compare_to(self, menu: 'Menu') -> bool:
        """
        Compare the current menu with the given menu.

        Menus are the same if:
        - they have the same dishes (instances)
        - they have the same dishes (name-price are the same)
        - the order is not important (menu A,B is the same as B,A)
        If the menus are the same, return True. Oterhwise False.
        """
        # for dishes in self.dishes:
        #     if dishes in menu.dishes:
        #         return True
        #     if
