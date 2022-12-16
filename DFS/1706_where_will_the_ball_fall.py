from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if c < 0 or c >= n:
                return -1
            if r == m:
                return c

            if c + 1 < n and grid[r][c] == grid[r][c + 1] == 1:
                return dfs(r + 1, c + 1)
            elif c - 1 >= 0 and grid[r][c] == grid[r][c - 1] == -1:
                return dfs(r + 1, c - 1)
            return -1

        res = list()
        for i in range(n):
            res.append(dfs(0, i))
        return res


def test_find_ball():
    solution = Solution()
    assert solution.findBall([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]) == [1, -1, -1, -1, -1], 'wrong result'
    assert solution.findBall([[-1]]) == [-1], 'wrong result'
    assert solution.findBall([[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]) == [0, 1, 2, 3, 4, -1], 'wrong result'


if __name__ == '__main__':
    test_find_ball()
