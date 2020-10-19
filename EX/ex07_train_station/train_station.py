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
        if p_id == self._train_id and p_wagon <= self._carriages and p_seat <= self._seats_in_carriage:
            for passen in self._passengers_filtred:
                if passenger.seat == passen.seat:
                    return None
            self._passengers_filtred.append(passenger)
        return passenger

    @train_id.setter
    def train_id(self, value: str):
        """Setter."""
        self._train_id = value

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
            pass_id = pas.seat.split('_')[0]
            for tr in self._trains:
                if tr.train_id == pass_id:
                    if not tr.add_passenger(pas):
                        passangers_in_train.remove(pas)
                    else:
                        tr.add_passenger(pas)

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
