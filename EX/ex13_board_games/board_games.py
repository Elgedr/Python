"""Board games."""
import os
import os.path


class Statistics:
    """Statistics class."""

    def __init__(self, filename: str):
        """Statistics constructor."""
        self.filename = filename

    def __get__(self, path: str):
        """Get a path."""
        pass


class Player:
    """Player class."""

    def __init__(self):
        """Player constructor."""


class Game:
    """Game class."""

    def __init__(self):
        """Game constructor."""


if __name__ == '__main__':
    statistics = Statistics("ex13_test_file.txt")
