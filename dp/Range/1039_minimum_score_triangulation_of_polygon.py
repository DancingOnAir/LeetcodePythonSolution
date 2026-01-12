from typing import List
from functools import lru_cache
from math import inf


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                res = inf
                for k in range(i + 1, j):
                    res = min(res, dp[i][k] + dp[k][j] + values[i] * values[j] * values[k])
                dp[i][j] = res
        return dp[0][n - 1]

    def minScoreTriangulation1(self, values: List[int]) -> int:
        n = len(values)

        @lru_cache(None)
        def dfs(i, j):
            if i + 1 == j:
                return 0

            return min(dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k] for k in range(i + 1, j))
        return dfs(0, n - 1)


def test_min_score_triangulation():
    solution = Solution()
    assert solution.minScoreTriangulation([1, 2, 3]) == 6, 'wrong result'
    assert solution.minScoreTriangulation([3, 7, 4, 5]) == 144, 'wrong result'


if __name__ == '__main__':
    test_min_score_triangulation()
