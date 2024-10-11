class Bitset:
    def __init__(self, size: int):
        self.n = size
        self.ones = 0
        self.num = 0

    def fix(self, idx: int) -> None:
        if self.num & (1 << idx) == 0:
            self.num |= (1 << idx)
            self.ones += 1

    def unfix(self, idx: int) -> None:
        if self.num & (1 << idx):
            self.num ^= (1 << idx)
            self.ones -= 1

    def flip(self) -> None:
        self.num ^= (1 << self.n) - 1
        self.ones = self.n - self.ones

    def all(self) -> bool:
        return self.ones == self.n

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return bin(self.num)[2:].zfill(self.n)[::-1]


def test_bitset():
    obj = Bitset(5)
    obj.fix(3)
    obj.fix(1)
    obj.flip()
    assert not obj.all(), 'wrong result'
    obj.unfix(0)
    obj.flip()
    assert obj.one(), 'wrong result'
    obj.unfix(0)
    assert obj.count() == 2, 'wrong result'
    assert obj.toString() == "01010", 'wrong result'


if __name__ == '__main__':
    test_bitset()
