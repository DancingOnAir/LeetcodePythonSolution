from typing import List
from functools import lru_cache


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[float('-inf')] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i, x in enumerate(nums):
            for c in range(target + 1):
                if c < x:
                    dp[i + 1][c] = dp[i][c]
                else:
                    dp[i + 1][c] = max(dp[i][c], dp[i][c - x] + 1)
        return dp[n][target] if dp[n][target] > float('-inf') else -1

    # MLE
    def lengthOfLongestSubsequence1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = -1

        @lru_cache(None)
        def dfs(i, cnt, total):
            if total == target:
                nonlocal res
                res = max(res, cnt)
            elif total > target:
                return

            if i >= n:
                return

            dfs(i + 1, cnt, total)
            dfs(i + 1, cnt + 1, total + nums[i])

        dfs(0, 0, 0)
        return res


def test_length_of_longest_subsequence():
    solution = Solution()
    assert solution.lengthOfLongestSubsequence([1, 1, 5, 4, 5], 3) == -1, 'wrong result'
    assert solution.lengthOfLongestSubsequence([1, 2, 3, 4, 5], 9) == 3, 'wrong result'
    assert solution.lengthOfLongestSubsequence([4, 1, 3, 2, 1, 5], 7) == 4, 'wrong result'


if __name__ == '__main__':
    test_length_of_longest_subsequence()
