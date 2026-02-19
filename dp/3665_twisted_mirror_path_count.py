from typing import List
from functools import cache


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        # dp[0][j] == dp[i][0] == 0，等价于 dfs(-1, j) == dfs(i, -1) == 0
        dp = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        # dp[1][1] == 1, 等价于 dfs(0, 0) == 1
        dp[0][1] = [1, 1]
        for i, r in enumerate(grid):
            for j, x in enumerate(r):
                if x == 0:
                    dp[i + 1][j + 1][0] = (dp[i + 1][j][0] + dp[i][j + 1][1]) % MOD
                    dp[i + 1][j + 1][1] = dp[i + 1][j + 1][0]
                else:
                    dp[i + 1][j + 1][0] = dp[i][j + 1][1]
                    dp[i + 1][j + 1][1] = dp[i + 1][j][0]

        return dp[m][n][0]

    # dfs
    def uniquePaths1(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 1_000_000_007

        @cache
        def dfs(i, j, k):
            if i < 0 or j < 0:
                return 0

            if i == 0 and j == 0:
                return 1

            # k == 0 -> 从方向右边来到(i, j), 1 -> 下面来到(i, j)
            if grid[i][j] == 0:
                return (dfs(i - 1, j, 1) + dfs(i, j - 1, 0)) % MOD
            if k == 0:
                return dfs(i - 1, j, 1)
            return dfs(i, j - 1, 0)

        return dfs(m - 1, n - 1, 0)


def test_unique_paths():
    solution = Solution()
    assert solution.uniquePaths([[0, 1, 0], [0, 0, 1], [1, 0, 0]]) == 5, 'wrong result'
    assert solution.uniquePaths([[0, 0], [0, 0]]) == 2, 'wrong result'
    assert solution.uniquePaths([[0, 1, 1], [1, 1, 0]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_unique_paths()
