from typing import List
from itertools import product


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        row_cnt = list(map(sum, grid))
        col_cnt = list(map(sum, zip(*grid)))

        res = 0
        for i, j in product(range(len(grid)), range(len(grid[0]))):
            res += grid[i][j] * (row_cnt[i] - 1) * (col_cnt[j] - 1)
        return res

    def numberOfRightTriangles1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_sum, col_sum = [0] * m, []
        for r in range(m):
            row_sum[r] = sum(grid[r])
        for c in zip(*grid):
            col_sum.append(sum(c))

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res += (row_sum[r] - 1) * (col_sum[c] - 1)
        return res


def test_number_of_right_triangles():
    solution = Solution()
    assert solution.numberOfRightTriangles([[0, 1, 0], [0, 1, 1], [0, 1, 0]]) == 2, 'wrong result'
    assert solution.numberOfRightTriangles([[1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]) == 0, 'wrong result'
    assert solution.numberOfRightTriangles([[1, 0, 1], [1, 0, 0], [1, 0, 0]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_number_of_right_triangles()
