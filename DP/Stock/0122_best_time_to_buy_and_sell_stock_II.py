from typing import List
from math import inf
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][1] = -inf
        for i, p in enumerate(prices):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + p)
            dp[i + 1][1] = max(dp[i][1], dp[i][0] - p)
        return dp[n][0]

    # https://www.bilibili.com/video/BV1ho4y1W7QK/?share_source=copy_web&vd_source=1fe6e1be7076869ed72407a8374a4eba
    def maxProfit1(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, hold):
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
        return dfs(len(prices) - 1, False)


def test_max_profit():
    solution = Solution()
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7, 'wrong result'
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4, 'wrong result'
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_profit()
