"""Train."""


class Train:
    """Class."""

    def __init__(self, passengers: list, carriages: int, seats_in_carriage: int):
        """Constructor."""
        self._carriages = carriages  # vagunite arv
        self._seats_in_carriage = seats_in_carriage  # istmete arv ühes vagunis
        self._passengers = self.f_passengers(passengers)  # reisijate nimekiri. можем вызывать тут это функцию, потому что она вбирает в себя переменную.

    def f_passengers(self, passengers):
        """List of passengers."""
        res = []
        for i in passengers:
            if int(i.seat.split("-")[0]) <= self._carriages and int(i.seat.split("-")[1]) <= self._seats_in_carriage:
                res.append(i)
            else:
                pass
        return res

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
        return len(self._passengers)

    def get_passengers_in_carriages(self) -> dict:
        """Tagastab sõnastiku vagunite ja reisijate andmetega."""
        result = {}
        for i in range(1, self.carriages + 1):
            result[str(i)] = []
        for passen in self._passengers:
            result[passen.seat.split("-")[0]].append({'id': passen.passenger_id, 'seat': passen.seat.split("-")[1]})
        return result

    @passengers.setter
    def passengers(self, value_list: list):
        self._passengers = value_list

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
        return {'id': self.passenger_id, 'seat': self.seat}


if __name__ == '__main__':
    p_1 = Passenger('123', '1-9')
    p_2 = Passenger('321', '2-11')
    p_3 = Passenger('456', '4-5')
    t = Train([p_1, p_2, p_3], 3, 10)
    print(t.passengers)
    print(t.get_passengers_in_carriages())
