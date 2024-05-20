from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i < m - 1 and grid[i][j] != grid[i + 1][j]) or (j < n - 1 and grid[i][j] == grid[i][j + 1]):
                    return False
        return True


def test_satisfies_conditions():
    solution = Solution()
    assert solution.satisfiesConditions([[1, 0, 2], [1, 0, 2]]), 'wrong result'
    assert not solution.satisfiesConditions([[1, 1, 1], [0, 0, 0]]), 'wrong result'
    assert not solution.satisfiesConditions([[1], [2], [3]]), 'wrong result'


if __name__ == '__main__':
    test_satisfies_conditions()
