from typing import List
from functools import cache


class Solution:
    # dfs
    def uniquePaths(self, grid: List[List[int]]) -> int:
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
