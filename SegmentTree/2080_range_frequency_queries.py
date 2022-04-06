from typing import List
from bisect import bisect_left, bisect_right
from collections import defaultdict


# binary search + default dict
class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.occurrence = defaultdict(list)
        for i, val in enumerate(arr):
            self.occurrence[val].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        return bisect_right(self.occurrence[value], right) - bisect_left(self.occurrence[value], left)


def test_range_freq_query():
    obj = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
    assert obj.query(1, 2, 4) == 1, 'wrong result'
    assert obj.query(0, 11, 33) == 2, 'wrong result'


if __name__ == '__main__':
    test_range_freq_query()
