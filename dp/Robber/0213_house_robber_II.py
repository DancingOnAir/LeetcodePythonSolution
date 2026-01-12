from typing import List
from functools import lru_cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            n = len(arr)

            dp = [0] * (n + 2)
            for i, x in enumerate(arr):
                dp[i + 2] = max(dp[i + 1], dp[i] + arr[i])
            return dp[n + 1]

        return max(nums[0] + helper(nums[2: -1]), helper(nums[1:]))

    # improved dfs
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i, arr):
            if i < 0:
                return 0
            return max(dfs(i - 1, arr), dfs(i - 2, arr) + arr[i])

        return max(nums[0] + dfs(n - 4, tuple(nums[2: -1])), dfs(n - 2, tuple(nums[1:])))

    # dfs
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        @lru_cache(None)
        def dfs(i, stop):
            if i < stop:
                return 0
            if i == stop:
                return nums[stop]

            return max(dfs(i - 1, stop), dfs(i - 2, stop) + nums[i])
        return max(dfs(n - 1, 1), dfs(n - 2, 0))


def test_rob():
    solution = Solution()
    assert solution.rob([2, 3, 2]) == 3, 'wrong result'
    assert solution.rob([1, 2, 3, 1]) == 4, 'wrong result'
    assert solution.rob([1, 2, 3]) == 3, 'wrong result'


if __name__ == '__main__':
    test_rob()
