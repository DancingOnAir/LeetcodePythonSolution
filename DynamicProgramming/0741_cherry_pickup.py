from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n < 1:
            return 0

        m = (n << 1) - 1
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for k in range(1, m):
            for i in range(n - 1, -1, -1):
                for p in range(n - 1, -1, -1):
                    j, q = k - i, k - p

                    if j < 0 or j >= n or q < 0 or q >= n or grid[i][j] == -1 or grid[p][q] == -1:
                        dp[i][p] = -1
                        continue

                    if i > 0:
                        dp[i][p] = max(dp[i][p], dp[i - 1][p])
                    if p > 0:
                        dp[i][p] = max(dp[i][p], dp[i][p - 1])
                    if i > 0 and p > 0:
                        dp[i][p] = max(dp[i][p], dp[i - 1][p - 1])
                    if dp[i][p] >= 0:
                        dp[i][p] += grid[i][j]
                        if p != i:
                            dp[i][p] += grid[p][q]

        return max(0, dp[-1][-1])

    # bottom-up dp
    def cherryPickup2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = grid[0][0]

        for i in range(n):
            for j in range(n):
                for k in range(min(i + j + 1, n)):
                    if not i and not j and not k:
                        continue
                    if i + j - k < 0 or i + j - k >= n or grid[i][j] == -1 or grid[k][i + j - k] == -1:
                        continue

                    a = dp[i - 1][j][k] if i > 0 else -1
                    b = dp[i - 1][j][k - 1] if i > 0 else -1
                    c = dp[i][j - 1][k] if j > 0 else -1
                    d = dp[i][j - 1][k - 1] if j > 0 else -1

                    dp[i][j][k] = max(a, b, c, d)
                    if dp[i][j][k] != -1:
                        if i == k:
                            dp[i][j][k] += grid[i][j]
                        else:
                            dp[i][j][k] += grid[i][j] + grid[k][i + j - k]
        return 0 if dp[-1][-1][-1] == -1 else dp[-1][-1][-1]

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

    # 错误解法，第一次遍历最大值+第二次被影响过的最大值 != 最优解
    def cherryPickup1(self, grid: List[List[int]]) -> int:
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
