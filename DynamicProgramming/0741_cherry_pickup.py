from typing import List


class Solution:
    def __init__(self):
        self.path = list()

    def max_path_sum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == -1:
                    dp[i][j] = -1
                    break

                if not i and not j:
                    dp[i][j] = grid[0][0]
                    self.path.append([i, j])
                elif not i:
                    if dp[i][j - 1] == -1:
                        dp[i][j] = -1
                        break

                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                    # path.append([i, j])
                elif not j:
                    if dp[i - 1][j] == -1:
                        dp[i][j] = -1
                        break

                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                    # path.append([i, j])
                else:
                    if dp[i - 1][j] == -1 and dp[i][j - 1] == -1:
                        dp[i][j] = -1
                        break

                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                    if dp[i - 1][j] >= dp[i][j - 1]:
                        self.path.append([i - 1, j])
                    else:
                        self.path.append([i, j - 1])
        self.path.append([n - 1, n - 1])
        return dp[-1][-1]

    def cherryPickup(self, grid: List[List[int]]) -> int:
        first = self.max_path_sum(grid)
        if not first:
            return 0

        n = len(grid)
        for i in range(n):
            for j in range(n):
                if [i, j] in self.path:
                    grid[i][j] = 0
        second = self.max_path_sum(grid)
        return first + second


def test_cherry_pickup():
    solution = Solution()

    grid1 = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
    assert solution.cherryPickup(grid1) == 5, 'wrong result'

    grid2 = [[1, 1, -1], [1, -1, 1], [-1, 1, 1]]
    assert solution.cherryPickup(grid2) == 0, 'wrong result'


if __name__ == '__main__':
    test_cherry_pickup()
