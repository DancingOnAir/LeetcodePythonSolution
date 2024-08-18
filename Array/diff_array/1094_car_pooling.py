from typing import List
from itertools import accumulate
from collections import Counter


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = Counter()
        for p, f, t in trips:
            d[f] += p
            d[t] -= p

        sum_d = 0
        for k in sorted(d):
            sum_d += d[k]
            if sum_d > capacity:
                return False
        return True

    def carPooling1(self, trips: List[List[int]], capacity: int) -> bool:
        d = [0] * 1001
        for p, f, t in trips:
            d[f] += p
            d[t] -= p
        return all(s <= capacity for s in accumulate(d))


def test_car_pooling():
    solution = Solution()
    assert not solution.carPooling([[2, 1, 5], [3, 3, 7]], 4), 'wrong result'
    assert solution.carPooling([[2, 1, 5], [3, 3, 7]], 5), 'wrong result'


if __name__ == '__main__':
    test_car_pooling()
