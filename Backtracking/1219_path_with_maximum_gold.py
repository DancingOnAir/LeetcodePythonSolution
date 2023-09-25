from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        nodes = []
        m, n = len(grid), len(grid[0])
        res = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0:
                    nodes.append([r, c])

        def dfs(i, j, tot):
            nonlocal res
            res = max(res, tot)

            for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] != 0 and ([x, y] not in path):
                    path.append([x, y])
                    dfs(x, y, tot + grid[x][y])
                    path.pop()

        for i, j in nodes:
            path = [[i, j]]
            dfs(i, j, grid[i][j])
        return res


def test_get_maximum_gold():
    solution = Solution()
    assert solution.getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]) == 24, 'wrong result'
    assert solution.getMaximumGold([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]) == 28, 'wrong result'


if __name__ == '__main__':
    test_get_maximum_gold()
