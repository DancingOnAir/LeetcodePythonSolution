from math import inf
from functools import lru_cache


class Solution:
    # dp
    def getMoneyAmount(self, n: int) -> int:
        dp = [[inf] * (n + 1) for _ in range(n + 1)]
        for i in range(n, 0, -1):
            dp[i][i] = 0
            dp[i - 1][i] = i - 1
            for j in range(i + 2, n + 1):
                dp[i][j] = min(max(dp[i][k - 1], dp[k + 1][j]) + k for k in range(i + 1, j))
        return dp[1][n]

    # dfs + cache
    def getMoneyAmount1(self, n: int) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return 0
            elif i + 1 == j:
                return i
            return min(max(dfs(i, k - 1), dfs(k + 1, j)) + k for k in range(i + 1, j))
        return dfs(1, n)


def test_get_money_amount():
    solution = Solution()
    assert solution.getMoneyAmount(10) == 16, 'wrong result'
    assert solution.getMoneyAmount(1) == 0, 'wrong result'
    assert solution.getMoneyAmount(2) == 1, 'wrong result'


if __name__ == '__main__':
    test_get_money_amount()

