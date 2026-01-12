from typing import List
from math import inf
from functools import lru_cache


class Solution:
    # dp
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        m = len(cuts)

        dp = [[0] * m for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(i + 2, m):
                dp[i][j] = inf
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])
        return dp[0][m - 1]

    # dfs + cache
    def minCost1(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        m = len(cuts)

        @lru_cache(None)
        def dfs(i, j):
            if i + 1 == j:
                return 0
            res = inf
            for k in range(i + 1, j):
                res = min(res, dfs(i, k) + dfs(k, j) + cuts[j] - cuts[i])
            return res
        return dfs(0, m - 1)


def test_min_cost():
    solution = Solution()
    assert solution.minCost(7, [1, 3, 4, 5]) == 16, 'wrong result'
    assert solution.minCost(9, [5, 6, 1, 4, 2]) == 22, 'wrong result'


if __name__ == '__main__':
    test_min_cost()
