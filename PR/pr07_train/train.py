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
        count = 0
        while len(self._passengers) > 0:
            count += 1
        return count

    def get_passengers_in_carriages(self) -> dict:
        """Tagastab sõnastiku vagunite ja reisijate andmetega."""


    @passengers.setter
    def passengers(self, value_list: list):
        for passenger in value_list:
           pas_carriage = passenger._seat.split("-")[0]
           pas_seat = passenger._seat.split("-")[1]
           if pas_carriage > int(self._carriages) or pas_seat > int(self._seats_in_carriage):
               value_list.remove(passenger)
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