from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        left, right, up, down = n, 0, m, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    left = min(left, i)
                    right = max(right, i)
                    up = min(up, j)
                    down = max(down, j)
        return (right - left + 1) * (down - up + 1)


def test_minimum_area():
    solution = Solution()
    assert solution.minimumArea([[0, 1, 0], [1, 0, 1]]) == 6, 'wrong result'
    assert solution.minimumArea([[1, 0], [0, 0]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_minimum_area()
