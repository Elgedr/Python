"""Board games."""
import random
import string


class Statistics:
    """Statistics class."""

    def __init__(self, filename: str):
        """Statistics constructor."""
        self.games = {}
        self.players = {}
        self.filename = filename
        self.read_from_file(filename)

    def get(self, path: str):
        """Get a path."""
        tokens = path[1:].split("/")  # our path = /game/{name}/amount we will get ["game", "{name}", "amount"]
        func = getattr(self, 'get_' + tokens[0])  # get_game
        return func(tokens[0])

    def read_from_file(self, filename: str):
        with open(filename, encoding='utf-8') as f:
            for line in f:
                splitted = line.split(";")
                game_name = splitted[0]
                name_for_gameplay_class = splitted[0]
                name_for_game_class = splitted[0]
                result_type = splitted[2]
                players = splitted[1].split(",")  # ['ago', 'emi', 'el']
                points = splitted[3].split(",")  # ['6', '30', '12']

                name_for_gameplay_class = Gameplay(game_name, result_type, points, players)

                if name_for_game_class in self.games.keys():
                    second_object_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
                    new = second_object_name
                    new = Game(result_type)
                    new.add_game_to_list(name_for_gameplay_class)
                    self.games[name_for_game_class].append(new)
                else:
                    self.games[name_for_game_class] = []
                    game_name = Game(result_type)
                    game_name.add_game_to_list(name_for_gameplay_class)
                    self.games[name_for_game_class].append(game_name)

                for name in players:
                    if name in self.players.keys():
                        second_object_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
                        new = second_object_name
                        new = Player(result_type)
                        new.add_player_games(name_for_gameplay_class)
                        new.add_player_games(name_for_gameplay_class)
                        self.players[name].append(new)
                    else:
                        key_indict = name
                        self.players[key_indict] = []
                        name = Player(name)
                        name.add_player_games(name_for_gameplay_class)
                        name.add_player_games(name_for_gameplay_class)
                        self.players[key_indict].append(name)

                # self.games[name_for_game_class].append(game_name)

    # def get_games(self):
    #     return self.games
    #
    # def get_players(self):
    #     return self.players

    def get_games(self):
        res = []
        for key in self.players:
            res.append(key)
        return res

    def get_players(self, x):
        res = []
        for key in self.players:
            res.append(key)
        return res

    def get_total(self):
        pass


class Gameplay:
    """One game class."""

    def __init__(self, game_name: str, game_type: str, points_per_game: list, players: list):
        """Gameplay constructor."""
        self.game_name = game_name
        self.times_of_playing = 0
        self.winner_or_not = bool
        self.game_type = game_type
        self.points_per_game = points_per_game
        self.amount_of_players = 0
        self.players = players


class Player:
    """Player class."""

    def __init__(self, name: str):
        """Player constructor."""
        self.player_name = name
        self.player_games = []
        self.player_points = []

    def add_player_games(self, game: Gameplay):
        self.player_games.append(game)

    def add_player_points(self, point: int):
        self.player_points.append(point)


class Game:
    """Game class."""

    def __init__(self, result_type: str):
        """Game constructor."""
        self.game_list = []
        self.players_names = []
        self.result_type = result_type
        # self.results = ""

    def add_players_names(self, player: Player):
        self.players_names.append(player)

    def add_game_to_list(self, game: Gameplay):
        self.game_list.append(game)


if __name__ == '__main__':
    statistics = Statistics("ex13_test_file.txt")
    # print(statistics.get_games())
    # print(statistics.get_players())
    print(statistics.get("/players"))
