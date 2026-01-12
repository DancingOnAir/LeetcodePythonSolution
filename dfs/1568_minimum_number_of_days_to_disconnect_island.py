from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            grid[r][c] = 2
            for x, y in ((r, c - 1), (r, c + 1), (r + 1, c), (r - 1, c)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    dfs(x, y)

        def count():
            cnt = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        cnt += 1
                        dfs(i, j)
            # 还原，后续还要使用原始的grid
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        grid[i][j] = 1
            return cnt

        m, n = len(grid), len(grid[0])
        if count() != 1:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count() != 1:
                        return 1
                    grid[i][j] = 1
        return 2


def test_min_days():
    solution = Solution()
    assert solution.minDays([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) == 2, 'wrong result'
    assert solution.minDays([[1, 1]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_days()
