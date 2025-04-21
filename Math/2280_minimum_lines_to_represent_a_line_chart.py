from typing import List
from itertools import pairwise


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key=lambda x: x[0])
        res = 0
        pre_dx, pre_dy = 0, 1
        for (x1, y1), (x2, y2) in pairwise(stockPrices):
            dy, dx = y2 - y1, x2 - x1
            if pre_dy * dx != dy * pre_dx:
                res += 1
            pre_dy, pre_dx = dy, dx
        return res


def test_minimum_lines():
    solution = Solution()
    assert solution.minimumLines([[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]]) == 3, 'wrong result'
    assert solution.minimumLines([[3, 4], [1, 2], [7, 8], [2, 3]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_minimum_lines()
