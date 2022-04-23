from operator import add, mul
from functools import partial


class Fancy:
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
            return self.arr[idx]  % (10 ** 9 + 7)
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
