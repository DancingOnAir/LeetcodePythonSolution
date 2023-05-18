from typing import List
from math import inf
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][1] = -inf
        for i, p in enumerate(prices):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + p - fee)
            dp[i + 1][1] = max(dp[i][1], dp[i][0] - p)
        return dp[n][0]

    def maxProfit1(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        @lru_cache(None)
        def dfs(i, hold):
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i] - fee)
        return dfs(n - 1, False)


def test_max_profit():
    solution = Solution()
    assert solution.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8, 'wrong result'
    assert solution.maxProfit([1, 3, 7, 5, 10, 3], 3) == 6, 'wrong result'


if __name__ == '__main__':
    test_max_profit()
