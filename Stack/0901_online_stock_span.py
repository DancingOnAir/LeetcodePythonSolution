class StockSpanner:
    def __init__(self):
        self.stock = list()

    def next(self, price: int) -> int:
        res = 1
        while res <= len(self.stock) and self.stock[-res] <= price:
            res += 1

        self.stock.append(price)
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
