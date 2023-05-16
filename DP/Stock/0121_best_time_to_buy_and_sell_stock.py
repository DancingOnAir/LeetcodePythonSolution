from typing import List
from functools import lru_cache
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-inf] * 2 for _ in range(3)] for _ in range(n + 1)]
        dp[0][1][0] = 0

        for i, p in enumerate(prices):
            for j in range(2):
                dp[i + 1][j + 1][0] = max(dp[i][j + 1][0], dp[i][j + 1][1] + p)
                dp[i + 1][j + 1][1] = max(dp[i][j + 1][1], dp[i][j][0] - p)
        # 没有profit可以不交易
        return max(dp[n][2][0], 0)

    # 看待成恰好交易一次的股票交易问题
    # dfs(i, -1, 0) = -inf 任何情况下 j不能为负
    # dfs(-1, j, 0) = 0 第0天开始未持有股票
    # dfs(-1, j, 0) = -inf 第0天开始不可能持有股票
    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dfs(i, j, hold):
            if j < 0:
                return -inf
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, j, True), dfs(i - 1, j, False) - prices[i])
            return max(dfs(i - 1, j, False), dfs(i - 1, j - 1, True) + prices[i])
        return dfs(n - 1, 1, False)


def test_max_profit():
    solution = Solution()
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5, 'wrong result'
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_profit()
