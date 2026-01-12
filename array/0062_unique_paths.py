from typing import List
import math


class Solution:
    # math solution
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m + n - 2) // math.factorial(m - 1) // math.factorial(n - 1)

    # 1d dp
    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [1] * m
        for _ in range(1, n):
            for j in range(1, m):
                dp[j] += dp[j - 1]

        return dp[m - 1]

    # 2d dp
    def uniquePaths1(self, m: int, n: int) -> int:
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if 1 == i or 1 == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n][m]


def test_unique_paths():
    solution = Solution()

    m1, n1 = 3, 2
    print(solution.uniquePaths(m1, n1))

    m2, n2 = 7, 3
    print(solution.uniquePaths(m2, n2))


if __name__ == '__main__':
    test_unique_paths()
