class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            tot = grid[i][j]
            grid[i][j] = 0
            return tot + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    cur = dfs(i, j)
                    if cur % k == 0:
                        res += 1
        return res


def test_calculate_islands():
    solution = Solution()
    assert solution.countIslands([[0, 2, 1, 0, 0], [0, 5, 0, 0, 5], [0, 0, 1, 0, 0], [0, 1, 4, 7, 0], [0, 2, 0, 0, 8]],
                                 5) == 2, 'wrong result'
    assert solution.countIslands([[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]], 3) == 6, 'wrong result'


if __name__ == '__main__':
    test_calculate_islands()
