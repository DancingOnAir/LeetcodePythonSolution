from typing import List
from math import inf
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i][0] 表示卖出股票，dp[i][1] 表示持有股票，dp[i][2] 表示在冷却时间
        dp = [[0] * 2 for _ in range(n + 2)]
        dp[0][1] = -inf
        dp[1][1] = -inf
        for i, p in enumerate(prices):
            dp[i + 2][0] = max(dp[i + 1][0], dp[i + 1][1] + p)
            dp[i + 2][1] = max(dp[i + 1][1], dp[i][0] - p)
        return dp[n + 1][0]

    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dfs(i, hold):
            if i < 0:
                return -inf if hold else 0

            if hold:
                return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i])
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
        return dfs(n - 1, False)


def test_max_profit():
    solution = Solution()
    assert solution.maxProfit([1, 2, 3, 0, 2]) == 3, 'wrong result'
    assert solution.maxProfit([1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_profit()
