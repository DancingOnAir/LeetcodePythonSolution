from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_wise = 0
        for i in range(m):
            left, right = 0, n - 1
            while left <= right:
                if grid[i][left] != grid[i][right]:
                    row_wise += 1
                left += 1
                right -= 1

        col_wise = 0
        for j in range(n):
            left, right = 0, m - 1
            while left <= right:
                if grid[left][j] != grid[right][j]:
                    col_wise += 1
                left += 1
                right -= 1

        return min(row_wise, col_wise)


def test_min_flips():
    solution = Solution()
    assert solution.minFlips([[1, 0, 0], [0, 0, 0], [0, 0, 1]]) == 2, 'wrong result'
    assert solution.minFlips([[0, 1], [0, 1], [0, 0]]) == 1, 'wrong result'
    assert solution.minFlips([[1], [0]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_flips()
