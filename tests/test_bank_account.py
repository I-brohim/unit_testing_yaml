import pytest
from bank_account.bank_account import BankAccount


@pytest.fixture
def start_account():
    return BankAccount(100)


#initialization
def test_minimum():
    with pytest.raises(ValueError, match="negative"):
        return BankAccount(-1)

#deposit
def test_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150

def test_neg_deposit(start_account):
    with pytest.raises(ValueError, match="positive"):
        start_account.deposit(-10)


#withdraw
def test_withdraw(start_account):
    start_account.withdraw(50)
    assert start_account.balance == 50


def test_neg_withdraw(start_account):
    with pytest.raises(ValueError, match="positive"):
        start_account.withdraw(-10)

def test_insufficient_withdraw(start_account):
    with pytest.raises(ValueError, match="funds"):
        start_account.withdraw(150)


#transfer

def test_transfer():
    acc1 = BankAccount(100)
    acc2 = BankAccount(50)

    acc1.transfer_to(acc2, 50)
    assert acc2.balance == 100

def test_transfer_error(start_account):
    with pytest.raises(ValueError, match="must be"):
        start_account.transfer_to("string", 50)
