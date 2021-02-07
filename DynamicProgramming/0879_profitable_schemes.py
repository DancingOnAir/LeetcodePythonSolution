from typing import List


class Solution:
    # dp[i][j] means the count of schemes with i profit and j members.
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (n + 1) for _ in range(minProfit + 1)]
        dp[0][0] = 1

        for g, p in zip(group, profit):
            for i in range(minProfit, -1, -1):
                for j in range(n - g, -1, -1):
                    dp[min(i + p, minProfit)][j + g] += dp[i][j]

        return sum(dp[-1]) % MOD

    # dp[i][j][k] represents the total schemes of 0-i-1 crimes, j memebers and at least k profit.
    def profitableSchemes1(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        l = len(group)

        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(l + 1)]
        for i in range(l + 1):
            for j in range(n + 1):
                dp[i][j][0] = 1

        for i in range(1, l + 1):
            for j in range(1, n + 1):
                for k in range(minProfit + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= group[i - 1]:
                        dp[i][j][k] += dp[i - 1][j - group[i - 1]][max(k - profit[i - 1], 0)]

                    dp[i][j][k] %= MOD
        return dp[l][n][minProfit]


def test_profitable_schemes():
    solution = Solution()
    assert solution.profitableSchemes(5, 3, [2, 2], [2, 3]) == 2, 'wrong result'
    assert solution.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]) == 7, 'wrong result'


if __name__ == '__main__':
    test_profitable_schemes()
