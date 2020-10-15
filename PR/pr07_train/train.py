"""Train."""


class Train:
    """Class."""

    def __init__(self, passengers: list, carriages: int, seats_in_carriage: int):
        """Constructor."""
        self.carriages = carriages  # vagunite arv
        self.seats_in_carriage = seats_in_carriage  # istmete arv ühes vagunis
        self.passengers = passengers  # reisijate nimekiri


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
        seats_count = self._carriages * self._seats_in_carriage
        return seats_count

    def get_number_of_passengers(self) -> int:
        """Tagastab rongi sisse tulevate reisijate arvu."""
        return len(self._passengers)

    def get_passengers_in_carriages(self) -> dict:
        """Tagastab sõnastiku vagunite ja reisijate andmetega."""
        result = {}
        for i in range(self._carriages):
            result[str(i + 1)] = []
        for i in self._passengers:
            result[i.seat.split("-")[0]].append(i.__dict__())
        return result

    @passengers.setter
    def passengers(self, value_list: list):
        print("op")
        set_list = []
        for i in value_list:
            seat_value = [i.seat.split("-")[0], i.seat.split("-")[1]]
            if int(seat_value[0]) > 0 and int(seat_value[0]) <= self._carriages and int(i.seat.split("-")[1]) <= self._seats_in_carriage:
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




if __name__ == '__main__':
    p_1 = Passenger('123', '1-9')
    p_2 = Passenger('123', '1-9')
    p_3 = Passenger('123', '1-9')


    # p_2 = Passenger('321', '2-11')
    # p_3 = Passenger('456', '4-5')
    t = Train([p_1, p_2, p_3], 3, 10)
    print(t.passengers)
    print(t.get_passengers_in_carriages())
    passengers = [
        Passenger('test', '1-2'),
        Passenger('test2', '2-3'),
        Passenger('test3', '4-2'),
    ]
    t = Train(passengers, 3, 2)
    result = t.get_passengers_in_carriages()
    print(result)  # {'1': [{'id': 'test', 'seat': '2'}], '2': [], '3': []}
    assert len(result.keys()) == 3
    assert len(result['1']) == 1
    assert len(result['2']) == 0
    assert len(result['3']) == 0
    assert len(passengers) == 3