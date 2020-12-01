"""Board games."""
import random
import string


class Statistics:
    """Statistic class."""

    def __init__(self, filename: str):
        """Statistic constructor."""
        self.games = {}
        self.players = {}
        self.filename = filename
        self.read_from_file(filename)

    def get(self, path: str):
        """Get a path."""
        if path == "/total/places" or path == "/total/points" or path == "/total/winner":
            tokens = path[1:].split("/")[1]
            return self.get_total_result_type(tokens)
        elif len(path[1:].split("/")) == 3 and path[1:].split("/")[2] == "amount" and path[1:].split("/")[0] == "player":
            token = path[1:].split("/")
            func = getattr(self, "get_" + token[0] + "_amount")
            return func(token[1])
        elif len(path[1:].split("/")) == 3 and path[1:].split("/")[2] == "favourite":
            token = path[1::].split("/")
            func = getattr(self, "get_" + token[2] + "_amount")
            return func(token[1])
        elif len(path[1:].split("/")) == 3 and path[1:].split("/")[0] == "game" and path[1:].split("/")[2] == "amount":
            token = path[1::].split("/")
            func = getattr(self, "get_" + token[0] + "_playing")
            return func(token[1])
        elif len(path[1:].split("/")) == 3 and path[1:].split("/")[0] == "game" and path[1:].split("/")[2] == "player-amount":
            token = path[1::].split("/")
            func = getattr(self, "get_" + token[0] + "_playeramount")
            return func(token[1])
        else:
            tokens = path[1:].split("/")  # our path = /game/{name}/amount we will get ["game", "{name}", "amount"]
            func = getattr(self, 'get_' + tokens[0])  # get_game
            return func(tokens[0])

    def read_from_file(self, filename: str):
        """Read from file."""
        with open(filename, encoding='utf-8') as f:
            for line in f:
                linee = line.rstrip("\n")
                splitted = linee.split(";")
                game_name = splitted[0]
                name_for_gameplay_class = splitted[0]
                name_for_game_class = splitted[0]
                result_type = splitted[2]
                players = splitted[1].split(",")  # ['ago', 'emi', 'el']
                points = splitted[3].split(",")  # ['6', '30', '12']

                name_for_gameplay_class = Gameplay(game_name, result_type, points, players, None)

                for name in players:
                    if name in self.players.keys():
                        second_object_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
                        new = second_object_name
                        new = Player(result_type)
                        if result_type == "winner" and name in points or result_type == "places" and name == points[0] or result_type == "points" and points[players.index(name)] == max(points):
                            name_for_gameplay_class = Gameplay(game_name, result_type, points, players, True)
                        else:
                            name_for_gameplay_class = Gameplay(game_name, result_type, points, players, False)
                        new.add_player_games(name_for_gameplay_class)
                        self.players[name].append(new)
                    else:
                        key_indict = name
                        self.players[key_indict] = []
                        name = Player(name)
                        if result_type == "winner" and name in points or result_type == "places" and name == points[0] or result_type == "points" and points[players.index(key_indict)] == max(points):
                            name_for_gameplay_class = Gameplay(game_name, result_type, points, players, True)
                        else:
                            name_for_gameplay_class = Gameplay(game_name, result_type, points, players, False)
                        name.add_player_games(name_for_gameplay_class)
                        self.players[key_indict].append(name)

                if name_for_game_class in self.games.keys():
                    second_object_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
                    new = second_object_name
                    new = Game(result_type)
                    new.add_game_to_list(name_for_gameplay_class)
                    for i in players:
                        new.add_players_names(i)
                    self.games[name_for_game_class].append(new)
                else:
                    self.games[name_for_game_class] = []
                    game_name = Game(result_type)
                    game_name.add_game_to_list(name_for_gameplay_class)
                    for i in players:
                        game_name.add_players_names(i)
                    self.games[name_for_game_class].append(game_name)

    def get_games(self, x):
        """."""
        res = []
        for key in self.games:
            res.append(key)
        return res

    def get_players(self, x):
        """."""
        res = []
        for key in self.players:
            res.append(key)
        return res

    def get_total(self, x):
        """."""
        res = []
        for value in self.games.values():
            for game in value:
                res.append(game)
        return len(res)

    def get_total_result_type(self, typ):
        """."""
        counter = 0
        for values in self.games.values():
            for game in values:
                if game.result_type == typ:
                    counter += 1
        return counter

    def get_player_amount(self, x):
        """."""
        res = self.players.get(x)
        return len(res)

    def get_favourite_amount(self, x):
        """."""
        final = []
        listt = self.players.get(x)
        for plajerobyect in listt:
            for games in plajerobyect.player_games:
                final.append(games)
        res = max(final, key=final.count)
        return res

    def get_game_playing(self, x):
        """."""
        return len(self.games.get(x))

    def get_game_playeramount(self, x):
        """."""
        res = []
        # for listt in self.players.values():
        #     for item in listt:
        #         for objects in item.player_games:
        #             if objects == x:
        #                 res[x] = len(objects.players)
        # return res
        listt = self.games.get(x)
        for gameobject in listt:
            res.append(len(gameobject.players_names))
        return max(res, key=res.count)


class Gameplay:
    """One game class."""

    def __init__(self, game_name: str, game_type: str, points_per_game: list, players: list, winner_or_not):
        """Gameplay constructor."""
        self.game_name = game_name
        self.times_of_playing = 0
        self.winner_or_not = winner_or_not
        self.game_type = game_type
        self.points_per_game = points_per_game
        self.amount_of_players = 0
        self.players = players

    def __repr__(self):
        """."""
        return self.game_name

    def __eq__(self, other):
        """."""
        if self.game_name == other:
            return True


class Player:
    """Player class."""

    def __init__(self, name: str):
        """Player constructor."""
        self.player_name = name
        self.player_games = []
        self.player_points = []

    def add_player_games(self, game: Gameplay):
        """."""
        self.player_games.append(game)

    def add_player_points(self, point: int):
        """."""
        self.player_points.append(point)


class Game:
    """Game class."""

    def __init__(self, result_type: str):
        """Game constructor."""
        self.game_list = []
        self.players_names = []
        self.result_type = result_type
        # self.results = ""

    def add_players_names(self, player):
        """."""
        self.players_names.append(player)

    def add_game_to_list(self, game: Gameplay):
        """."""
        self.game_list.append(game)


if __name__ == '__main__':
    statistics = Statistics("ex13_test_file.txt")
    # print(statistics.get_games())
    # print(statistics.get_players())
    print(statistics.get("/players"))
    print(statistics.get("/games"))
    print(statistics.get("/total"))
    print(statistics.get("/total/points"))
    print(statistics.get("/player/joosep/amount"))
    print(statistics.get("/player/joosep/favourite"))
    print(statistics.get("/game/terraforming mars/amount"))
    print(statistics.get("/game/terraforming mars/player-amount"))
