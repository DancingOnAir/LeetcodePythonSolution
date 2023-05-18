from typing import List
from functools import lru_cache


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i, even):
            if i < 0:
                return 0
            if even:
                return max(dfs(i - 1, True), dfs(i - 1, False) + nums[i])
            return max(dfs(i - 1, False), dfs(i - 1, True) - nums[i])
        return dfs(n - 1, True)


def test_max_alternating_sum():
    solution = Solution()
    assert solution.maxAlternatingSum([4, 2, 5, 3]) == 7, 'wrong result'
    assert solution.maxAlternatingSum([5, 6, 7, 8]) == 8, 'wrong result'
    assert solution.maxAlternatingSum([6, 2, 1, 2, 4, 5]) == 10, 'wrong result'


if __name__ == '__main__':
    test_max_alternating_sum()
