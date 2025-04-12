from typing import List
from math import factorial


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        if not prices:
            return 0

        res = 0
        cur = 1
        for i in range(1, len(prices)):
            if prices[i - 1] == prices[i] + 1:
                cur += 1
            else:
                res += (cur + 1) * cur // 2
                cur = 1
        return res + (cur + 1) * cur // 2


def test_get_descent_periods():
    solution = Solution()
    assert solution.getDescentPeriods([3, 2, 1, 4]) == 7, 'wrong result'
    assert solution.getDescentPeriods([8, 6, 7, 7]) == 4, 'wrong result'
    assert solution.getDescentPeriods([1]) == 1, 'wrong result'


if __name__ == '__main__':
    test_get_descent_periods()
