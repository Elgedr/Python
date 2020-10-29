"""Tester."""

import pytest

from formula_one import Driver, Race, FormulaOne

filename = "ex08_example_data.txt"


class TestDriver:
    """Class."""

    driver = Driver("Mika Hakkinen", "Mclaren-Mercedes")  # пишем данные одного из водителей из нашего документа
    driver.add_result(1, 15)
    driver.add_result(2, 10)

    def test_get_results(self):
        """Test."""
        assert self.driver.get_results() == {1: 15, 2: 10}

    def test_get_points(self):
        """Test."""
        assert self.driver.get_points() == 25


class TestRace:
    """Class."""

    race = Race(filename)

    def test_get_results_by_race(self):
        """Test."""
        assert len(self.race.get_results_by_race(1)) == 7

    def test_extract_info(self):
        """Test."""
        assert self.race.extract_info("Mika Hakkinen  Mclaren-Mercedes   79694  1") == {'Name': 'Mika Hakkinen', 'Team': 'Mclaren-Mercedes', 'Time': 79694, 'Diff': '', 'Race': 1}

    def test_filter_data_by_race(self):
        """Test."""
        assert len(self.race.filter_data_by_race(1)) == 7

    def test_format_time(self):
        """Test."""
        assert self.race.format_time('6000') == '0:06.000'

    def test_calculate_time_difference(self):
        """Test."""
        assert self.race.calculate_time_difference(4201, 57411) == "+0:53.210"


class TestFormulaOne:
    """Class."""

    formula = FormulaOne(filename)

    def test_write_race_results_to_file(self):
        """Test."""
        self.formula.write_race_results_to_file(1)
        with open('results_for_race_1.txt', 'r') as f:
            listt = f.readlines()
        assert listt[2] == "1         Jenson Button            Williams-BMW             1:17.606                      25    \n"

    def test_write_race_results_to_csv(self):
        """Test."""
        self.formula.write_race_results_to_csv(1)
        with open('race_1_results.csv') as f:
            res = f.readlines()
        assert res[2] == '2,Heinz-Harald Frentzen,Jordan-Mugen-Honda,1:17.690,+0:00.084,18,1\n'

    def test_write_championship_to_file(self):
        """Test."""
        self.formula.write_championship_to_file()
        with open('championship_results.txt') as f:
            res = f.readlines()
        assert res[2] == '1         Jenson Button            Williams-BMW             50    \n'
