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
        seats_count = int(self._carriages) * int(self._seats_in_carriage)
        return seats_count

    def get_number_of_passengers(self) -> int:
        """Tagastab rongi sisse tulevate reisijate arvu."""
        passengers = self._passengers
        res = []
        car = int(self._carriages)
        sit = int(self._seats_in_carriage)
        for passenger in passengers:
            if int(passenger._seat.split("-")[0]) > car or int(passenger._seat.split("-")[1]) > sit:
                passengers.remove(passenger)
            else:
                res.append(passenger)
        return len(res)

    def get_passengers_in_carriages(self) -> dict:
        """Tagastab sõnastiku vagunite ja reisijate andmetega."""
        res = []
        car = int(self._carriages)
        sit = int(self._seats_in_carriage)
        for passenger in self.passengers:
            if int(passenger._seat.split("-")[0]) > car or int(passenger._seat.split("-")[1]) > sit:
                self.passengers.remove(passenger)




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
        self._passenger_id = passenger_id  # reisija unikaalne identifikaator (id)
        self._seat = seat  # istekoha number.  vaguni_nr-istekoha_nr 2-14

    def __dict__(self):
        """Magic method."""
        return {'id': self._passenger_id, 'seat': self._seat}


if __name__ == '__main__':
    p_1 = Passenger('123', '1-9')
    p_2 = Passenger('321', '2-11')
    p_3 = Passenger('456', '4-5')
    t = Train([p_1, p_2, p_3], 3, 10)
    print(t.passengers)
    print(t.get_passengers_in_carriages())
