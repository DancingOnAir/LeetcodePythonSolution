from typing import List
from functools import lru_cache


class Solution:
    # 2-d dp
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n + 1)]
        for i, x in enumerate(nums):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] - x)
            dp[i + 1][1] = max(dp[i][1], dp[i][0] + x)
        return dp[n][1]

    # dfs + cache
    def maxAlternatingSum1(self, nums: List[int]) -> int:
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
