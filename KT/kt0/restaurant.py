"""Restaurant system."""


class Restaurant:
    """Restaurant."""

    def __init__(self, name: str):
        """Restaurant constructor."""
        pass

    def add_dish(self, dish: 'Dish') -> bool:
        """Add a dish if not already in restaurant."""
        pass

    def get_dishes(self) -> list:
        """Return all the dishes in the restaurant."""
        pass

    def add_menu(self, menu: 'Menu') -> bool:
        """
        Add a menu to the restaurant if all the dishes are available.

        Menu cannot be added if:
        - it has no dishes
        - the menu with the same dishes (in any order) already exists
        """
        pass

    def get_menus(self) -> list:
        """Return all the menus in the restaurant."""
        pass

    def get_dishes_available_in_menu(self) -> list:
        """Return unique dishes which are in one of the menues."""
        pass

    def get_menus_ordered_by_price(self) -> list:
        """A new list of menus ordered by total price (highest first), then by dish count (lower first)."""
        pass


class Dish:
    """Dish (food)."""

    def __init__(self, name: str, price: int):
        """Dish constructor."""
        pass

    def get_name(self) -> str:
        """Return the name of the dish."""
        pass

    def get_price(self) -> int:
        """Return the price of the dish."""
        pass


class Menu:
    """Menu which holds different dishes."""

    def __init__(self):
        """Menu constructor."""
        pass

    def add_dish(self, dish: Dish) -> bool:
        """Add dish to menu if it does not exist already."""
        pass

    def get_dishes(self) -> list:
        """Return all the dishes in menu."""
        pass

    def compare_to(self, menu: 'Menu') -> bool:
        """
        Compare the current menu with the given menu.

        Menus are the same if:
        - they have the same dishes (instances)
        - they have the same dishes (name-price are the same)
        - the order is not important (menu A,B is the same as B,A)
        If the menus are the same, return True. Oterhwise False.
        """
        pass