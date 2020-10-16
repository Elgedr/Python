"""Train."""


class Train:
    """Class."""

    def __init__(self, passengers: list, carriages: int, seats_in_carriage: int):
        """Constructor."""
        self._passengers = passengers  # reisijate nimekiri
        self._carriages = carriages  # vagunite arv
        self._seats_in_carriage = seats_in_carriage  # istmete arv ühes vagunis

    @property
    def passengers(self) -> list:
        """Decorator."""
        return self._passengers

    @property
    def carriages(self) -> int:
        """Carriages."""
        return self._carriages

    @property
    def seats_in_carriage(self) -> int:
        """Seats."""
        return self._seats_in_carriage

    def get_seats_in_train(self) -> int:
        """Meetod, mis tagastab istmete koguarvu terve rongi peale."""
        seats_count = self.carriages * self.seats_in_carriage
        return seats_count

    def get_number_of_passengers(self) -> int:
        """Tagastab rongi sisse tulevate reisijate arvu."""
        self.passengers = self.passengers
        return len(self.passengers)

    def get_passengers_in_carriages(self) -> dict:
        """Tagastab sõnastiku vagunite ja reisijate andmetega."""
        result = {}
        self.passengers = self.passengers
        for i in range(1, self.carriages + 1):
            result[str(i)] = []
        for i in self.passengers:
            result[i.seat.split("-")[0]].append(i.__dict__())
        return result

    @passengers.setter
    def passengers(self, value_list: list):
        set_list = []
        for i in value_list:
            if int(i.seat.split("-")[0]) <= self._carriages and int(i.seat.split("-")[1]) <= self._seats_in_carriage:
                set_list.append(i)
        self._passengers = set_list

    @carriages.setter
    def carriages(self, value: int):
        self._carriages = value

    @seats_in_carriage.setter
    def seats_in_carriage(self, value: int):
        self._seats_in_carriage = value


class Passenger:
    """Class."""

    def __init__(self, passenger_id: str, seat: str):
        """Constructor."""
        self.passenger_id = passenger_id  # reisija unikaalne identifikaator (id)
        self.seat = seat  # istekoha number.  vaguni_nr-istekoha_nr 2-14

    def __dict__(self):
        """Magic method."""
        return {'id': self.passenger_id, 'seat': self.seat.split("-")[1]}
