from typing import List
from math import inf
from functools import lru_cache


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-inf] * 2 for _ in range(k + 2)] for _ in range(n + 1)]
        for j in range(1, k + 2):
            dp[0][j][0] = 0

        for i in range(n):
            for j in range(k + 1):
                dp[i + 1][j + 1][0] = max(dp[i][j + 1][0], dp[i][j + 1][1] + prices[i])
                dp[i + 1][j + 1][1] = max(dp[i][j + 1][1], dp[i][j][0] - prices[i])
        return dp[n][k + 1][0]

    def maxProfit1(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dfs(i, j, hold):
            if j < 0:
                return -inf
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])
            return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i])

        return dfs(n - 1, k, False)


def test_max_profit():
    solution = Solution()
    assert solution.maxProfit(2, [2, 4, 1]) == 2, 'wrong result'
    assert solution.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7, 'wrong result'


if __name__ == '__main__':
    test_max_profit()
