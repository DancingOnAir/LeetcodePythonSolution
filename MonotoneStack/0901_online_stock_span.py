from typing import List, Tuple


class StockSpanner:
    def __init__(self):
        self.stock: List[Tuple[int, int]] = list()

    def next(self, price: int) -> int:
        res = 1
        while self.stock and self.stock[-1][0] <= price:
            res += self.stock.pop()[1]

        self.stock.append((price, res))
        return res


def test_stock_spanner():
    obj = StockSpanner()
    assert obj.next(100) == 1, 'wrong result'
    assert obj.next(80) == 1, 'wrong result'
    assert obj.next(60) == 1, 'wrong result'
    assert obj.next(70) == 2, 'wrong result'
    assert obj.next(60) == 1, 'wrong result'
    assert obj.next(75) == 4, 'wrong result'
    assert obj.next(85) == 6, 'wrong result'


if __name__ == '__main__':
    test_stock_spanner()
