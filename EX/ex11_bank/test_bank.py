"""Tester."""

import pytest
import datetime

from bank import PersonError, TransactionError, Person, Bank, Transaction, Account


def test_person():
    """Test person class."""
    person1 = Person("Ellina", "Gedrojets", 18)
    person2 = Person("Robert", "Soidla", 19)
    assert person2.age == 19
    assert person2.__repr__() == person2.full_name
    assert person1.bank_account is None
    with pytest.raises(PersonError):
        assert Person("Ellina", "Mailna", -20)


def test_bank():
    """Test bank class."""
    person2 = Person("Robert", "Soidla", 19)
    person1 = Person("Ellina", "Gedrojets", 18)
    bank1 = Bank("Swed")
    assert bank1.add_customer(person2) is True
    assert person2 in bank1.customers
    assert bank1.add_customer(person2) is False
    assert bank1.remove_customer(person2) is True
    assert bank1.remove_customer(person1) is False
    assert bank1.__repr__() == bank1.name


def test_transaction():
    """Test transaction class."""
    person1 = Person("Ellina", "Gedrojets", 18)
    person2 = Person("Robert", "Soidla", 19)
    bank1 = Bank("Swed")
    bank2 = Bank("LHV")
    acc1 = Account(20, person1, bank1)
    acc2 = Account(100, person2, bank2)
    tr1 = Transaction(10, datetime.date.today(), acc1, acc2, False)
    tr2 = Transaction(20, datetime.date.today(), acc1, acc1, True)
    assert tr1.__repr__() == "(10 €) Ellina Gedrojets -> Robert Soidla"
    assert tr2.__repr__() == "(20 €) ATM"


def test_account():
    """Test account class."""
    person1 = Person("Ellina", "Gedrojets", 18)
    person2 = Person("Robert", "Soidla", 19)
    bank1 = Bank("Swed")
    bank2 = Bank("LHV")
    acc1 = Account(20, person1, bank1)
    acc2 = Account(100, person2, bank2)
    assert len(acc1.number) == 20
    assert acc2._balance == 100


def test_deposit():
    """Test deposit."""
    person1 = Person("Ellina", "Gedrojets", 18)
    person2 = Person("Robert", "Soidla", 19)
    bank1 = Bank("Swed")
    bank2 = Bank("LHV")
    acc1 = Account(20, person1, bank1)
    acc2 = Account(100, person2, bank2)
    with pytest.raises(TransactionError):
        assert acc1.deposit(-10)

    acc2.deposit(2, True)
    tr1 = Transaction(2, datetime.date.today(), acc2, acc2, True)
    assert str(acc2.transactions[0]) == str(tr1)

    acc1.deposit(10, False)
    assert acc1.balance == 30


def test_withdraw():
    """Test function withdraw."""
    person1 = Person("Ellina", "Gedrojets", 18)
    person2 = Person("Robert", "Soidla", 19)
    bank1 = Bank("Swed")
    bank2 = Bank("LHV")
    acc1 = Account(20, person1, bank1)
    acc2 = Account(100, person2, bank2)
    with pytest.raises(TransactionError):
        assert acc1.withdraw(-10)
    with pytest.raises(TransactionError):
        assert acc1.withdraw(acc1.balance + 1)

    acc2.withdraw(10, False)
    assert acc2.balance == 90

    acc2.withdraw(10)
    tr = Transaction(-10, datetime.date.today(), acc2, acc2, True)
    assert str(acc2.transactions[0]) == str(tr)


def test_transfer():
    """Test transfer function."""
    person1 = Person("Ellina", "Gedrojets", 18)
    person2 = Person("Robert", "Soidla", 19)
    person3 = Person("Mari", "Mets", 80)
    person4 = Person("Lilian", "Valge", 40)
    bank1 = Bank("Swed")
    bank2 = Bank("LHV")
    bank3 = Bank("Luminor")
    acc1 = Account(20, person1, bank1)
    acc2 = Account(100, person2, bank2)
    acc3 = Account(250, person3, bank3)
    acc4 = Account(0, person4, bank3)
    with pytest.raises(TransactionError):
        assert acc1.transfer(10000, acc2)

    """different banks transfer."""
    acc1.transfer(10, acc2)
    assert acc1.transactions == acc2.transactions == bank1.transactions == bank2.transactions

    """Same banks transfer."""
    acc3.transfer(7, acc4)
    assert acc3.transactions == acc4.transactions == bank3.transactions


def test_acc_statement():
    """Test."""
    person1 = Person("Ellina", "Gedrojets", 18)
    bank1 = Bank("Swed")
    acc1 = Account(20, person1, bank1)
    old_transaction = Transaction(150, datetime.date.today() - datetime.timedelta(days=19), acc1, acc1, True)
    acc1.transactions.append(old_transaction)
    new_transaction = Transaction(50, datetime.date.today() - datetime.timedelta(days=5), acc1, acc1, True)
    acc1.transactions.append(new_transaction)
    result_is_new_trans = acc1.account_statement(datetime.date.today() - datetime.timedelta(days=7), datetime.date.today())

    assert result_is_new_trans == [new_transaction]


def test_get_debit_turnover():
    """Test."""
    person1 = Person("Ellina", "Gedrojets", 18)
    bank1 = Bank("Swed")
    acc1 = Account(20, person1, bank1)
    acc1.deposit(300)
    acc1.deposit(10)
    acc1.withdraw(50)
    assert acc1.get_debit_turnover(datetime.date.today(), datetime.date.today()) == 310

def test_get_credit_turnover():
    """Test."""
    person1 = Person("Ellina", "Gedrojets", 18)
    bank1 = Bank("Swed")
    acc1 = Account(2000, person1, bank1)
    acc1.deposit(10)
    acc1.deposit(10)
    acc1.withdraw(50)
    acc1.withdraw(20)
    assert acc1.get_credit_turnover(datetime.date.today(), datetime.date.today()) == -70


def test_get_net_turnover():
    """Test."""
    person1 = Person("Ellina", "Gedrojets", 18)
    bank1 = Bank("Swed")
    acc1 = Account(200, person1, bank1)
    acc1.deposit(10)
    acc1.withdraw(50)
    assert acc1.get_net_turnover(datetime.date.today(), datetime.date.today()) == -40
