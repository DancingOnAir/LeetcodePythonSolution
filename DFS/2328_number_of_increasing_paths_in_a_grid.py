from typing import List


class Solution:
    # dp[i][j] means the number of paths ending at A[i][j].
    # We initial all dp[i][j] = 1.
    # Because we want strictly increasing paths, there is no cycle of path.
    # We iterative all A[i][j] in increasing order,
    # d[i][j] += dp[x][y] from smaller neighbours.
    # Finally return the sum of dp.
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n, mod = len(grid), len(grid[0]), 10 ** 9 + 7
        dp = [[1] * n for _ in range(m)]
        for v, i, j in sorted([grid[i][j], i, j] for i in range(m) for j in range(n)):
            for x, y in ([i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]):
                if 0 <= x < m and 0 <= y < n and grid[x][y] < grid[i][j]:
                    dp[i][j] += dp[x][y] % mod
        return sum(map(sum, dp)) % mod


def test_count_paths():
    solution = Solution()
    assert solution.countPaths([[1, 1], [3, 4]]) == 8, 'wrong result'
    assert solution.countPaths([[1], [2]]) == 3, 'wrong result'


if __name__ == '__main__':
    test_count_paths()
