from operator import add, mul
from functools import partial


# list operation
class Fancy1:
    def __init__(self):
        self.arr = list()

    def append(self, val: int) -> None:
        self.arr.append(val)

    def addAll(self, inc: int) -> None:
        self.arr = list(map(partial(add, inc), self.arr))

    def multAll(self, m: int) -> None:
        self.arr = list(map(partial(mul, m), self.arr))

    def getIndex(self, idx: int) -> int:
        if idx < len(self.arr):
            return self.arr[idx] % (10 ** 9 + 7)
        return -1


# math: Fermat's little theorem
class Fancy:
    def __init__(self):
        self.data = list()
        self.csum = [0]
        self.cmul = [1]
        self.mod = 10 ** 9 + 7

    def append(self, val: int) -> None:
        self.data.append(val)
        self.csum.append(self.csum[-1])
        self.cmul.append(self.cmul[-1])

    def addAll(self, inc: int) -> None:
        self.csum[-1] += inc

    def multAll(self, m: int) -> None:
        self.cmul[-1] *= m
        self.cmul[-1] %= self.mod

        self.csum[-1] *= m
        self.csum[-1] %= self.mod

    def getIndex(self, idx: int) -> int:
        if idx < len(self.data):
            # Fermat's little theorem states that if p is a prime number, then for any integer a,
            # the number a^p − a is an integer multiple of p, i.e. a^p = a (mod p).
            # In this application, we need a^(p-2) = a^-1 (mod p) where p is 1_000_000_007.
            # ratio = self.cmul[-1] * pow(self.cmul[idx], -1, self.mod)
            ratio = self.cmul[-1] * pow(self.cmul[idx], self.mod - 2, self.mod)
            return (self.csum[-1] + (self.data[idx] - self.csum[idx]) * ratio) % self.mod
        return -1


def test_fancy():
    obj = Fancy()

    obj.append(2)
    obj.addAll(3)
    obj.append(7)
    obj.multAll(2)
    assert obj.getIndex(0) == 10, 'wrong result'

    obj.addAll(3)
    obj.append(10)
    obj.multAll(2)
    assert obj.getIndex(0) == 26, 'wrong result'
    assert obj.getIndex(1) == 34, 'wrong result'
    assert obj.getIndex(2) == 20, 'wrong result'


if __name__ == '__main__':
    test_fancy()
