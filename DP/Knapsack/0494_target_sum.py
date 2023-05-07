from typing import List
from functools import lru_cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0

        target //= 2
        n = len(nums)

        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i, x in enumerate(nums):
            for c in range(target + 1):
                if c < x:
                    dp[i + 1][c] = dp[i][c]
                else:
                    dp[i + 1][c] = dp[i][c] + dp[i][c - x]
        return dp[-1][-1]

    # nums 原本所有的数之和为tot，需要添加正号的整数之和为p，那么 p - (tot - p) = target
    # 即p = (tot + target) // 2
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        target += sum(nums)
        if target < 0 or target % 2:
            return 0

        target //= 2

        @lru_cache(None)
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if c < nums[i]:
                return dfs(i - 1, c)
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])
        return dfs(n - 1, target)


def test_find_target_sum_ways():
    solution = Solution()
    assert solution.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5, 'wrong result'
    assert solution.findTargetSumWays([1], 1) == 1, 'wrong result'


if __name__ == '__main__':
    test_find_target_sum_ways()
