"""Tester."""

import pytest

from bank import PersonError, TransactionError, Person, Bank, Transaction, Account


class TestPerson:
    """Tester."""
    person1 = Person('Ellina', "Gedrojets", 100)

    def test_full_name(self):
        """Test1."""
        assert self.person1.full_name == "Ellina Gedrojets"

    # def test_age_control(self, age):
    #     """Test2."""
    #     assert self.person.age_control(age) == 100

    # def test_age(self):
    #     """Test3."""
    #     assert self.person.age() == 10


class TestBank:
    """Tester."""
    bank = Bank('SWED')
    person1 = Person('Ellina', "Gedrojets", 100)

    def test_add_customer(self, person: Person):
        """Test1."""
        assert self.bank.add_customer(person) == True

    def test_remove_customer(self, person: Person):
        """Test2."""
        assert self.bank.remove_customer(person) == True


class TestTransaction:
    """Tester."""
