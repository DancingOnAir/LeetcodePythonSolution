from typing import List
from functools import lru_cache
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-inf] * 2 for _ in range(4)] for _ in range(n + 1)]
        for j in range(1, 4):
            dp[0][j][0] = 0

        for i, p in enumerate(prices):
            for j in range(3):
                dp[i + 1][j + 1][0] = max(dp[i][j + 1][0], dp[i][j][1] + p)
                dp[i + 1][j + 1][1] = max(dp[i][j + 1][1], dp[i][j + 1][0] - p)

        return dp[n][3][0]

    # dfs
    def maxProfit1(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dfs(i, j, hold):
            if j < 0:
                return float('-inf')
            if i < 0:
                return float('-inf') if hold else 0
            if hold:
                return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])
            return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i])
        return dfs(n - 1, 2, False)


def test_max_profit():
    solution = Solution()
    assert solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6, 'wrong result'
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4, 'wrong result'
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_profit()
