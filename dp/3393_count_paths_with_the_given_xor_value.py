from typing import List
from functools import cache


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dfs(i, j, x):
            if i < 0 or j < 0:
                return 0
            val = grid[i][j]
            if i == 0 and j == 0:
                return 1 if x == val else 0
            return (dfs(i - 1, j, x ^ val) + dfs(i, j - 1, x ^ val)) % MOD

        return dfs(len(grid) - 1, len(grid[0]) - 1, k)


def test_count_path_with_xor_value():
    solution = Solution()
    assert solution.countPathsWithXorValue([[2, 1, 5], [7, 10, 0], [12, 6, 4]], 11) == 3, 'wrong result'
    assert solution.countPathsWithXorValue([[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], 2) == 5, 'wrong result'
    assert solution.countPathsWithXorValue([[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], 10) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_path_with_xor_value()
