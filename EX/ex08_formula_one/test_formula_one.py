"""Tester."""

import pytest

from formula_one import Driver, Race, FormulaOne

filename = "ex08_example_data.txt"


class TestDriver:
    driver = Driver("Mika Hakkinen", "Mclaren-Mercedes")  # пишем данные одного из водителей из нашего документа

    def test_get_results(self):
        assert self.driver.get_results() == {}

    def test_get_points(self):
        assert self.driver.get_points() == 0

    def test_set_points(self):
        assert self.driver.set_points() == None

    def test_add_result(self):
        assert self.driver.add_result(1, 10) == None


class TestRace:
    race = Race(filename)

    def test_get_results_by_race(self):
        assert len(self.race.get_results_by_race(1)) == 7


class TestFormulaOne:
    formula = FormulaOne(filename)