from sortedcontainers import SortedDict
from heapq import heappush, heappop


class StockPrice:
    def __init__(self):
        self.stock = dict()
        self.latest_timestamp = -1
        self.max_heap = list()
        self.min_heap = list()

    def update(self, timestamp: int, price: int) -> None:
        self.stock[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)

        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.stock[self.latest_timestamp]

    def maximum(self) -> int:
        p, t = heappop(self.max_heap)

        while self.stock[t] != -p:
            p, t = heappop(self.max_heap)
        heappush(self.max_heap, (p, t))
        return -p

    def minimum(self) -> int:
        p, t = heappop(self.min_heap)

        while self.stock[t] != p:
            p, t = heappop(self.min_heap)
        heappush(self.min_heap, (p, t))
        return p


def test_stock_price():
    obj = StockPrice()
    obj.update(1, 10)
    obj.update(2, 5)
    assert obj.current() == 5, 'wrong result'
    assert obj.maximum() == 10, 'wrong result'
    obj.update(1, 3)
    assert obj.maximum() == 5, 'wrong result'
    obj.update(4, 2)
    assert obj.minimum() == 2, 'wrong result'


if __name__ == '__main__':
    test_stock_price()
