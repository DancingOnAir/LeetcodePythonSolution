from typing import List
from itertools import accumulate


class Solution:
    # TLE
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        l = 0
        res = 0
        pre_sum = list(accumulate(runningCosts, initial=0))
        for r in range(n):
            while max(chargeTimes[l: r + 1], default=0) + (pre_sum[r+1] - pre_sum[l]) * (r - l + 1) > budget:
                l += 1
            res = max(res, r - l + 1)
        return res


def test_maximum_robots():
    solution = Solution()
    assert solution.maximumRobots([3, 6, 1, 3, 4], [2, 1, 3, 4, 5], 25) == 3, 'wrong result'
    assert solution.maximumRobots([11, 12, 19], [10, 8, 7], 19) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximum_robots()
