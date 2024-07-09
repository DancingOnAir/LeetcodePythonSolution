from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        X = [[0] * (n + 1) for _ in range(m + 1)]
        Y = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(m):
            for j in range(n):
                X[i][j] = X[i - 1][j] + X[i][j - 1] - X[i - 1][j - 1] + (grid[i][j] == 'X')
                Y[i][j] = Y[i - 1][j] + Y[i][j - 1] - Y[i - 1][j - 1] + (grid[i][j] == 'Y')

                if X[i][j] > 0 and X[i][j] == Y[i][j]:
                    res += 1
        return res

    def numberOfSubmatrices1(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            if i > 0:
                dp[i][0][0] = dp[i - 1][0][0]
                dp[i][0][1] = dp[i - 1][0][1]
            dp[i][0][0] += grid[i][0] == 'X'
            dp[i][0][1] += grid[i][0] == 'Y'

            if dp[i][0][0] > 0 and dp[i][0][0] == dp[i][0][1]:
                res += 1

        for j in range(1, n):
            dp[0][j][0] = dp[0][j - 1][0]
            dp[0][j][1] = dp[0][j - 1][1]

            dp[0][j][0] += grid[0][j] == 'X'
            dp[0][j][1] += grid[0][j] == 'Y'

            if dp[0][j][0] > 0 and dp[0][j][0] == dp[0][j][1]:
                res += 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j][0] = dp[i - 1][j][0] + dp[i][j - 1][0] - dp[i - 1][j - 1][0] + (grid[i][j] == 'X')
                dp[i][j][1] = dp[i - 1][j][1] + dp[i][j - 1][1] - dp[i - 1][j - 1][1] + (grid[i][j] == 'Y')

                if dp[i][j][0] > 0 and dp[i][j][0] == dp[i][j][1]:
                    res += 1
        return res


def test_number_of_submatrices():
    solution = Solution()
    assert solution.numberOfSubmatrices([["X", "Y", "."], ["Y", ".", "."]]) == 3, 'wrong result'
    assert solution.numberOfSubmatrices([["X", "X"], ["X", "Y"]]) == 0, 'wrong result'
    assert solution.numberOfSubmatrices([[".", "."], [".", "."]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_number_of_submatrices()
