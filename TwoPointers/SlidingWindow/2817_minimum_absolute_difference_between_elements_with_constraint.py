from typing import List
from sortedcontainers import SortedList


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        res, n = float('inf'), len(nums)
        sl = SortedList([float('-inf'), float('inf')])

        for x, y in zip(nums, nums[x:]):
            sl.add(x)
            j = sl.bisect_left(y)
            res = min(res, sl[j] - y, y - sl[j - 1])
        return res


def test_min_absolute_difference():
    solution = Solution()
    assert solution.minAbsoluteDifference([4, 3, 2, 4], 2) == 0, 'wrong result'
    assert solution.minAbsoluteDifference([5, 3, 2, 10, 15], 1) == 1, 'wrong result'
    assert solution.minAbsoluteDifference([1, 2, 3, 4], 3) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_absolute_difference()
