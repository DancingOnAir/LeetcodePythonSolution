from typing import List
from functools import lru_cache


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        # j = 0 不分割， 1分割
        @lru_cache(None)
        def dfs(i, j):
            if i == len(nums):
                return 0
            return max(dfs(i + 1, 1) + nums[i], dfs(i + 1, j ^ 1) + (-nums[i] if j else nums[i]))
        return dfs(0, 0)


def test_maximum_total_cost():
    solution = Solution()
    assert solution.maximumTotalCost([1, -2, 3, 4]) == 10, 'wrong result'
    assert solution.maximumTotalCost([1, -1, 1, -1]) == 4, 'wrong result'
    assert solution.maximumTotalCost([0]) == 0, 'wrong result'
    assert solution.maximumTotalCost([1, -1]) == 2, 'wrong result'


if __name__ == '__main__':
    test_maximum_total_cost()
