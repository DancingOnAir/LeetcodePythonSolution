from typing import List
from functools import lru_cache


class Solution:
    # dp
    def longestSubsequence(self, nums: List[int]) -> int:
        mx = max(nums)
        max_diff = mx - min(nums)
        dp = [[0] * (max_diff + 2) for _ in range(len(nums))]
        last = [-1] * (mx + 1)

        for i, x in enumerate(nums):
            for j in range(max_diff, -1, -1):
                dp[i][j] = max(dp[i][j + 1], 1)
                if x - j >= 0 and last[x - j] >= 0:
                    dp[i][j] = max(dp[i][j], dp[last[x - j]][j] + 1)
                if x + j <= mx and last[x + j] >= 0:
                    dp[i][j] = max(dp[i][j], dp[last[x + j]][j] + 1)
            last[x] = i
        return max(map(max, dp))

    # dfs
    def longestSubsequence1(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i, pre, diff):
            if i == n:
                return 0

            res = dfs(i + 1, pre, diff)
            if abs(nums[i] - pre) <= diff:
                res = max(res, dfs(i + 1, nums[i], abs(nums[i] - pre)) + 1)
            return res
        return dfs(0, float('-inf'), float('inf'))


def test_longest_subsequence():
    solution = Solution()
    assert solution.longestSubsequence([16, 6, 3]) == 3, 'wrong result'
    assert solution.longestSubsequence([6, 5, 3, 4, 2, 1]) == 4, 'wrong result'
    assert solution.longestSubsequence([10, 20, 10, 19, 10, 20]) == 5, 'wrong result'


if __name__ == '__main__':
    test_longest_subsequence()
