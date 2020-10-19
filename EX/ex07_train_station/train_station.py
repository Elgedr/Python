"""Train Station."""


class Passenger:
    """Class."""

    def __init__(self, passenger_id: str, seat: str):
        """Constructor."""
        self._passenger_id = passenger_id  # reisija unikaalne identifikaator (id)
        self._seat = seat  # istekoha number (rongi_id-vaguni_nr-istekoha_nr)

    @property
    def id(self) -> str:
        """Decorator."""
        return self._passenger_id

    @property
    def seat(self) -> str:
        """Decorator."""
        return self._seat


class Train:
    """Class."""

    def __init__(self, train_id: str, carriages: int, seats_in_carriage: int):
        """Constructor."""
        self._train_id = train_id  # rongi unikaalne id
        self._carriages = carriages  # vagunite arv
        self._seats_in_carriage = seats_in_carriage  # ühes vagunis olevate istmete arv
        self._passengers_filtred = []

    def __dict__(self):
        """Magic metod."""
        seats = f"{self.get_number_of_passengers()} / {self.get_seats_in_train()}"
        return {"train id": self._train_id, "carriages": self._carriages, "seats": seats}

    @property
    def passengers_filtred(self) -> list:
        """Decorator."""
        return self._passengers_filtred

    @property
    def carriages(self) -> int:
        """Decorator."""
        return self._carriages

    @property
    def train_id(self) -> str:
        """Decorator."""
        return self._train_id

    @property
    def seats_in_carriage(self) -> int:
        """Decorator."""
        return self._seats_in_carriage

    def get_seats_in_train(self) -> int:
        """Meetod, mis tagastab istmete koguarvu terve rongi peale."""
        res = self._carriages * self._seats_in_carriage
        return res

    def get_number_of_passengers(self) -> int:
        """Meetod, mis tagastab rongi reisijate arvu."""
        res = len(self._passengers_filtred)
        return res

    def get_passengers_in_carriages(self) -> dict:
        """Meetod, mis tagastab sõnastiku vagunite ja reisijate andmetega."""
        res = {}
        for wagon_num in range(1, self._carriages + 1):
            res[str(wagon_num)] = []
        for passanger in self._passengers_filtred:
            res[passanger.seat.split("-")[1]].append(passanger)
        return res

    def add_passenger(self, passenger: Passenger):
        """Meetod, mis lisab reisija rongi peale rongijaamast."""
        p_id = passenger.seat.split('-')[0]
        p_seat = int(passenger.seat.split('-')[2])
        p_wagon = int(passenger.seat.split('-')[1])
        if p_id == self._train_id and 0 < p_wagon <= self._carriages and 0 < p_seat <= self._seats_in_carriage:
            for passen in self._passengers_filtred:
                if passenger.seat == passen.seat:
                    return None
            self._passengers_filtred.append(passenger)
            return passenger

    @train_id.setter
    def train_id(self, value: str):
        """Setter."""
        self._train_id = value

    @carriages.setter
    def carriages(self, value: int):
        self._carriages = value

    @seats_in_carriage.setter
    def seats_in_carriage(self, value: int):
        """Setter."""
        self._seats_in_carriage = value


class TrainStation:
    """Class."""

    def __init__(self, trains: list, passengers: list):
        """Constructor."""
        self._trains = trains  # rongijaama sisse tulevate rongide nimekiri
        self._passengers = passengers  # rongijaama sisse tulevate reisijate nimekiri
        self.passangers_in_trains()  # если не добавить название метода сюда, то он не будет видимым в классе

    def get_station_overview(self) -> list:
        """Meetod, mis tagastab hetke seisundi aruande kõikiest rongijaamas olevatest rongidest listi kujul ning rongi info on sõnastiku kujul."""
        res = []
        for t in self.trains:
            res.append(t.__dict__)
        return res

    def get_number_of_passengers(self):
        """Meetod, mis tagastab rongijaama (rongidesse paigutatud) reisijate koguarvu."""
        return len(self._passengers)

    def passangers_in_trains(self):
        """Filter passengers."""
        passangers_in_train = []
        passangers_in_train.extend(self._passengers)
        for pas in self._passengers:
            pass_id = pas.seat.split('-')[0]
            for tr in self._trains:
                if tr.train_id == pass_id:
                    if not tr.add_passenger(pas):
                        passangers_in_train.remove(pas)

        self._passengers = passangers_in_train

    @property
    def passengers(self):
        """Decorator."""
        return self._passengers

    @passengers.setter
    def passengers(self, value_list: list):
        """Setter."""
        self._passengers = value_list

    @property
    def trains(self):
        """Decorator."""
        return self._trains

    @trains.setter
    def trains(self, value_list: list):
        """Setter."""
        self._trains = value_list


if __name__ == "__main__":
    # passengers
    p1 = Passenger("10", "AA-1-0")
    p2 = Passenger("11", "AA-1-1")
    p3 = Passenger("12", "AA-1-1")
    p4 = Passenger("13", "AA-1-2")
    p5 = Passenger("14", "AA-2-5")
    p6 = Passenger("15", "AB-2-4")
    p7 = Passenger("16", "AB-10-4")
    p8 = Passenger("17", "AB-0-0")
    passengers = [p1, p2, p3, p4, p5, p6, p7, p8]

    # trains for station
    t1 = Train("AA", 5, 5)
    t2 = Train("AB", 2, 4)
    trains = [t1, t2]
    # train for additional tests
    t3 = Train("AA", 5, 5)
    # stations
    s1 = TrainStation(trains, passengers)
    stations = [s1]


    # TEST FUNCTION
    def basic_test(testname, output, expected):
        """Compare output with expected result."""
        if output == expected:
            print(f"{testname}: PASSED")
        else:
            print(f"{testname}: FAIL\n {output} - your output \n {expected} - expected")


    # TESTS
    print("INIT TESTS")
    basic_test("init_passengers", [p._passenger_id for p in passengers],
               ['10', '11', '12', '13', '14', '15', '16', '17'])
    basic_test("init_trains", [t.train_id for t in trains], ['AA', 'AB'])
    basic_test("init_station", s1.trains, trains)

    ## ARE YOU USING ADD_PASSENGER CORRECTLY?
    print("\nADD_PASSENGER TESTS")
    add_passenger_correct = [False, True, False, True, True, False, False, False] or [None, p2, None, p4, p5, None,
                                                                                      None, None]
    basic_test("add_passengers_to_train3_without_station", [t3.add_passenger(p) for p in passengers],
               add_passenger_correct)
    basic_test("check_for_valid_passengers_train3", [p._passenger_id for p in t3._passengers_filtred], ['11', '13', '14'])

    print("\nTRAINS AT THE STATION")
    basic_test("get_seats_in_train", [t.get_seats_in_train() for t in trains], [25, 8])
    basic_test("get_number_of_passengers", [t.get_number_of_passengers() for t in trains], [3, 1])
    basic_test("check_for_valid_passengers_station", [p._passenger_id for p in s1._passengers], ['11', '13', '14', '15'])
    get_passengers_in_carriages_correct = [{'1': [p2, p4], '2': [p5], '3': [], '4': [], '5': []}, {'1': [], '2': [p6]}]
    basic_test("get_passengers_in_carriages", [t.get_passengers_in_carriages() for t in trains],
               get_passengers_in_carriages_correct)
    get_station_overview_correct = [{'train_id': 'AA', 'carriages': 5, 'seats': '3/25'},
                                    {'train_id': 'AB', 'carriages': 2, 'seats': '1/8'}]
    basic_test("get_station_overview", s1.get_station_overview(), get_station_overview_correct)
    basic_test("get_number_of_passengers", s1.get_number_of_passengers(), 4)
