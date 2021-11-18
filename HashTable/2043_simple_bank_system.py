from typing import List


class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.withdraw(account1, money):
            if self.deposit(account2, money):
                return True
            self.deposit(account1, money)
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= self.n:
            self.balance[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= self.n and self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        return False


class Bank1:
    def __init__(self, balance: List[int]):
        self.balance = {i + 1: v for i, v in enumerate(balance)}

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 not in self.balance or account2 not in self.balance or self.balance[account1] < money:
            return False

        self.balance[account1] -= money
        self.balance[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account not in self.balance:
            return False

        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account not in self.balance or self.balance[account] < money:
            return False

        self.balance[account] -= money
        return True


def test_bank():
    bank = Bank([10, 100, 20, 50, 30])
    assert bank.withdraw(3, 10), 'wrong result'
    assert bank.transfer(5, 1, 20), 'wrong result'
    assert bank.deposit(5, 20), 'wrong result'
    assert not bank.transfer(3, 4, 15), 'wrong result'
    assert not bank.withdraw(10, 50), 'wrong result'


if __name__ == '__main__':
    test_bank()
