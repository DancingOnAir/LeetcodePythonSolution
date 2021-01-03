from typing import List


class Solution:
    def numTilings(self, N: int) -> int:
        if N == 1:
            return 1
        MOD = 10 ** 9 + 7
        # dp[i][j] means at the i-th position, the status is j
        dp = [[0] * 3 for _ in range(N)]
        dp[0][0] = 1
        dp[1][0] = 2
        dp[1][1] = 1
        dp[1][2] = 1

        for i in range(2, N):
            dp[i][0] = (dp[i - 1][0] + dp[i - 2][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD
            dp[i][1] = (dp[i - 2][0] + dp[i - 1][2]) % MOD
            dp[i][2] = (dp[i - 2][0] + dp[i - 1][1]) % MOD
        return dp[N - 1][0]


def test_num_tilings():
    solution = Solution()
    assert solution.numTilings(3) == 5, 'wrong result'


if __name__ == '__main__':
    test_num_tilings()
