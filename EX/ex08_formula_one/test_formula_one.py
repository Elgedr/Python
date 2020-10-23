"""Tester."""

import pytest

from formula_one import Driver, Race, FormulaOne

filename = "ex08_example_data.txt"


class TestDriver:
    driver = Driver("Name", "Team")

    def test_get_results(self):
        assert self.driver.get_results() == []

    def test_get_points(self):
        assert self.driver.get_results() == []

    def test_set_points(self):
        assert self.driver.get_results() == []

    def test_add_result(self):
        assert self.driver.get_results() == []

    def test_count_points(self):
        assert self.driver.get_results() == []


class TestRace:
    race = Race(filename)
    def test_read_file_to_list(self):
        assert False

    def test_extract_info(self):
        assert False

    def test_filter_data_by_race(self):
        assert False

    def test_format_time(self):
        assert False

    def test_calculate_time_difference(self):
        assert False

    def test_sort_data_by_time(self):
        assert False

    def test_get_results_by_race(self):
        assert False
