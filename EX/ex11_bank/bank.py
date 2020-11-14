"""Bank."""
import datetime
import random


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
        self._age = self.age_control(age)
        self.bank_account = None

    def age_control(self, age):
        """Funct."""
        if age <= 0:
            raise PersonError
        return age

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
        if value > 0:
            self._age = value
        else:
            raise PersonError

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
        self.name = name
        self.customers = []
        self.transactions = []

    def add_customer(self, person: Person) -> bool:
        """
        Add customer to bank.

        :param person: person object
        :return: was customer successfully added
        """
        if person not in self.customers:
            account = Account(0, person, self)
            person.bank_account = account
            self.customers.append(person)
            return True
        return False

    def remove_customer(self, person: Person) -> bool:
        """
        Remove customer from bank.

        :param person: person object
        :return: was customer successfully removed
        """
        if person in self.customers:
            self.customers.remove(person)
            person.bank_account = None
            return True
        return False

    def __repr__(self) -> str:
        """
        Bank representation.

        :return: name of the bank
        """
        return self.name


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
        self.amount = amount
        self.date = date
        self.sender_account = sender_account
        self.receiver_account = receiver_account
        self.is_from_atm = is_from_atm

    def __repr__(self) -> str:
        """
        Transaction representation.

        :rtype: object's values displayed in a nice format
        """
        if self.is_from_atm is True:
            return f"({self.amount} €) ATM"
        else:
            return f"({self.amount} €) {self.sender_account.person.full_name} -> {self.receiver_account.person.full_name}"


class Account:
    """Account class."""

    def __init__(self, balance: float, person: Person, bank: 'Bank'):
        """
        Account constructor.

        :param balance: initial account balance
        :param person: person object
        :param bank: bank object
        """
        self._balance = balance
        self.person = person
        self.bank = bank
        self.transactions = []
        self.number = self.rando()

    @property
    def balance(self) -> float:
        """Get account's balance."""
        return self._balance

    def deposit(self, amount: float, is_from_atm: bool = True):
        """Deposit money to account."""
        if amount <= 0:
            raise TransactionError
        elif is_from_atm:
            self._balance += amount
            transaction1 = Transaction(amount, datetime.date.today(), self, self, True)
            self.transactions.append(transaction1)
            self.bank.transactions.append(transaction1)

    def withdraw(self, amount: float, is_from_atm: bool = True):
        """Withdraw money from account."""
        if amount <= 0:
            raise TransactionError
        elif amount > self._balance:
            raise TransactionError
        elif is_from_atm:
            transact2 = Transaction(-amount, datetime.date.today(), self, self, True)
            self.transactions.append(transact2)
            self.bank.transactions.append(transact2)
            self._balance -= amount

    def transfer(self, amount: float, receiver_account: 'Account'):
        """Transfer money from one account to another."""

        if receiver_account.bank != self.bank:
            if self._balance < 5 + amount or receiver_account == self:
                raise TransactionError
            elif amount > 0:
                self._balance -= 5
                self.withdraw(amount, False)
                receiver_account.deposit(amount, False)
                transact2 = Transaction(amount, datetime.date.today(), self, receiver_account, False)
                self.transactions.append(transact2)
                receiver_account.transactions.append(transact2)
                self.bank.transactions.append(transact2)
                receiver_account.bank.transactions.append(transact2)
        if receiver_account.bank == self.bank:
            if receiver_account == self or self._balance < amount:
                raise TransactionError
            elif amount > 0:
                receiver_account.deposit(amount, False)
                self.withdraw(amount, False)
                transact3 = Transaction(amount, datetime.date.today(), self, receiver_account, False)
                self.transactions.append(transact3)
                receiver_account.transactions.append(transact3)
                self.bank.transactions.append(transact3)

    def account_statement(self, from_date: datetime.date, to_date: datetime.date) -> list:
        """All transactions in given period."""
        res = []
        for transaction in self.transactions:
            if from_date <= transaction.date <= to_date:
                res.append(transaction)
        return res

    def get_debit_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get total income in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: debit turnover number
        """
        amount = 0
        for trans in self.transactions:
            if from_date <= trans.date <= to_date and trans.receiver_account == self:
                if trans.amount > 0:
                    amount += trans.amount
        return amount

    def get_credit_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get total expenditure in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: credit turnover number
        """
        amount = 0
        for trans in self.transactions:
            if from_date <= trans.date <= to_date and trans.receiver_account != self:
                if trans.amount < 0:
                    amount += abs(trans.amount)
        return -amount

    def get_net_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get net turnover (income - costs) in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: net turnover number
        """
        a = self.get_credit_turnover(from_date, to_date)
        b = self.get_debit_turnover(from_date, to_date)
        res = a + b
        return res

    def __repr__(self) -> str:
        """
        Account representation.

        :return: account number
        """
        return self.number

    def rando(self):
        """Generate bank number."""
        res = "EE"
        for i in range(18):
            res += str(random.randint(0, 9))
        return res


if __name__ == '__main__':
    person1 = Person("Ellina", "Gedrojets", 10)
    bank = Bank('Seb')
    account = Account(10, person1, bank)
    print(account.deposit(2))
    print(account.balance)
    print(account.withdraw(5))
    print(account.balance)
