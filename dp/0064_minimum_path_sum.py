from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = (min(dp[j - 1], dp[j]) or dp[j - 1]) + grid[i][j]
        return dp[-1]

    # 2d dp
    def minPathSum1(self, grid: List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0

        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not i and not j:
                    dp[i][j] = grid[i][j]
                elif not i:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif not j:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]


def test_min_path_sum():
    solution = Solution()

    grid1 = [[1, 3, 1],
             [1, 5, 1],
             [4, 2, 1]]
    print(solution.minPathSum(grid1))


if __name__ == '__main__':
    test_min_path_sum()
