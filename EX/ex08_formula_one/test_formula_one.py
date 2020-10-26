"""Tester."""

import pytest

from formula_one import Driver, Race, FormulaOne

filename = "ex08_example_data.txt"


class TestDriver:
    """Class."""
    driver = Driver("Mika Hakkinen", "Mclaren-Mercedes")  # пишем данные одного из водителей из нашего документа

    def test_get_results(self):
        """Test."""
        assert self.driver.get_results() == {}

    def test_get_points(self):
        """Test."""
        assert self.driver.get_points() == 0

    def test_set_points(self):
        """Test."""
        assert self.driver.set_points() == None

    def test_add_result(self):
        """Test."""
        assert self.driver.add_result(1, 10) == None


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
