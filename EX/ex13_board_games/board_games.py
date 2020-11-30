"""Board games."""


class Statistics:
    """Statistics class."""

    def __init__(self, filename: str):
        """Statistics constructor."""
        self.games = {}
        self.players = {}
        self.filename = filename

    def __get__(self, path: str):
        """Get a path."""
        tokens = path[1::].split("/")  # our path = /game/{name}/amount we will get ["game", "{name}", "amount"]
        func = getattr(self,  "get_" + tokens[0])  # get_game
        return func(tokens)

    def make_dict_of_players(self, filename: str):
        with open(filename, encoding='utf-8') as f:
            res = f.read().splitlines()
        return res


    def get_games(self, x):
        game_name = x[0]
        game = self.games

    def get_players(self, x):
        player_name = x[0]



class Player:
    """Player class."""

    def __init__(self):
        """Player constructor."""


class Game:
    """Game class."""

    def __init__(self, file: str):
        """Game constructor."""


if __name__ == '__main__':
    statistics = Statistics("ex13_test_file.txt")
    print()
