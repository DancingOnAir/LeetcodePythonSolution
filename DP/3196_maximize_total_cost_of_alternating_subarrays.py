from typing import List
from functools import lru_cache


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] 表示nums数组下标[0, i]之间的数值构成的总成本最大值
        dp = [0] * (n + 1)
        for i, x in enumerate(nums):
            dp[i + 1] = max(dp[i] + x, dp[i - 1] + nums[i - 1] - x)
        return dp[-1]

    # dfs
    # 思路：把整个数组分割成长度为1或2的子数组
    def maximumTotalCost1(self, nums: List[int]) -> int:
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
