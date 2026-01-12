from typing import List
from collections import Counter


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]
        for k in range(m + n):
            min_j = max(n - k, 0)
            max_j = min(m + n - 1 - k, n - 1)
            # top left
            s = set()
            for j in range(min_j, max_j):
                i = k + j - n
                s.add(grid[i][j])
                res[i + 1][j + 1] = len(s)
            # bottom right
            s.clear()
            for j in range(max_j, min_j, -1):
                i = k + j - n
                s.add(grid[i][j])
                res[i - 1][j - 1] = abs(res[i - 1][j - 1] - len(s))
        return res


def test_difference_of_distinct_values():
    solution = Solution()
    assert solution.differenceOfDistinctValues([[1, 2, 3], [3, 1, 5], [3, 2, 1]]) == [[1, 1, 0], [1, 0, 1],
                                                                                      [0, 1, 1]], 'wrong result'


if __name__ == '__main__':
    test_difference_of_distinct_values()
