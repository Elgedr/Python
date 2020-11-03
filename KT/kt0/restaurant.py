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
        elif menu.compare_to(menu) is True:
            return False
        for dish in menu.dishes:
            if dish not in self.dishes:
                return False
        else:
            self.menu.append(menu)
            return True

    def get_menus(self) -> list:
        """Return all the menus in the restaurant."""
        menues = self.menu
        return menues

    def get_dishes_available_in_menu(self) -> list:
        """Return unique dishes which are in one of the menues."""
        dishes = []
        for dish in self.get_dishes():
            for menu in self.get_menus():
                if dish in menu:
                    dishes.append(dish)
                    break
        return dishes

    def get_menus_ordered_by_price(self) -> list:
        """A new list of menus ordered by total price (highest first), then by dish count (lower first)."""
        ret = [] + self.menu
        prices = {}
        for menue in self.menu:
            for dish in menue:
                prices[menue] = sum()


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
        self.dishes = []  # dishes from Dish class

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
        if len(menu.dishes) != len(self.dishes):
            return False
        menu_dict = {}
        for food in menu.get_dishes():
            menu_dict[food.name] = food.price
        for items in self.dishes:
            if items.name in menu_dict and items.price == menu_dict[items.price]:
                return True
        return False


if __name__ == '__main__':
    dish1 = Dish('Kartul', 20)
    dish2 = Dish('soup', 30)
    dish3 = Dish("puree", 15)
    dishes = [dish1, dish2, dish3]
    rest1 = Restaurant('macdonalds')
