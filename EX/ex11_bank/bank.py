"""Bank."""
import datetime
import random
import string


class PersonError(Exception):
    """Person error."""
    pass


class TransactionError(Exception):
    """Transaction error."""
    pass


class Person:
    """Person class."""

    def __init__(self, first_name: str, last_name: str, age: int):
        """
        Person constructor.

        :param first_name: first name
        :param last_name: last name
        :param age: age, must be greater than 0
        """
        self.first_name = first_name
        self.last_name = last_name
        self._age = age
        self._bank_account = None

    @property
    def full_name(self) -> str:
        """Get person's full name. Combination of first and last name."""
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self) -> int:
        """Get person's age."""
        return self._age

    @age.setter
    def age(self, value: int):
        """Set person's age. Must be greater than 0."""
        if value <= 0:
            raise PersonError
        else:
            self._age = value

    def __repr__(self) -> str:
        """
        Person representation.

        :return: person's full name
        """
        return self.full_name


class Bank:
    """Bank class."""

    def __init__(self, name: str):
        """
        Bank constructor.

        :param name: name of the bank
        """
        self._name = name
        self._customers = []
        self._transactions = []

    def add_customer(self, person: Person) -> bool:
        """
        Add customer to bank.

        :param person: person object
        :return: was customer successfully added
        """
        if person not in self._customers:
            self._customers.append(person)
            return True
        return False
    # todo  fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

    def remove_customer(self, person: Person) -> bool:
        """
        Remove customer from bank.

        :param person: person object
        :return: was customer successfully removed
        """
        if person in self._customers:
            self._customers.remove(person)
            person._bank_account = None
            return True
        return False

    def __repr__(self) -> str:
        """
        Bank representation.

        :return: name of the bank
        """
        return self._name


class Transaction:
    """Transaction class."""

    def __init__(self, amount: float, date: datetime.date, sender_account: 'Account', receiver_account: 'Account',
                 is_from_atm: bool):
        """
        Transaction constructor.

        :param amount: value
        :param date: date of the transaction
        :param sender_account: sender's object
        :param receiver_account: receiver's object
        :param is_from_atm: is transaction from atm
        """
        self._amount = amount
        self._date = date
        self._sender_account = sender_account
        self._receiver_account = receiver_account
        self._is_from_atm = is_from_atm

    def __repr__(self) -> str:
        """
        Transaction representation.

        :rtype: object's values displayed in a nice format
        """
        if self._is_from_atm is True:
            return f"([{self._amount}] €) ATM"
        else:
            return f"([{self._amount}] €) [{self._sender_account._person.full_name}] -> [{self._receiver_account._person.full_name}]"


class Account:
    """Account class."""

    def __init__(self, balance: float, person: Person, bank: 'Bank'):
        """
        Account constructor.

        :param balance: initial account balance
        :param person: person object
        :param bank: bank object
        """
        # self.balance = balance
        self._person = person
        self._bank = bank
        self._transactions = []

    @property
    def balance(self) -> float:
        """Get account's balance."""
        return

    def deposit(self, amount: float, is_from_atm: bool = True):
        """Deposit money to account."""
        pass

    def withdraw(self, amount: float, is_from_atm: bool = True):
        """Withdraw money from account."""
        pass

    def transfer(self, amount: float, receiver_account: 'Account'):
        """Transfer money from one account to another."""
        pass

    def account_statement(self, from_date: datetime.date, to_date: datetime.date) -> list:
        """All transactions in given period."""
        pass

    def get_debit_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get total income in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: debit turnover number
        """
        pass

    def get_credit_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get total expenditure in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: credit turnover number
        """
        pass

    def get_net_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get net turnover (income - costs) in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: net turnover number
        """
        pass

    def __repr__(self) -> str:
        """
        Account representation.

        :return: account number
        """
        pass
