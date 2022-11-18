from typing import List


class Solution:
    # https://leetcode.com/problems/domino-and-tromino-tiling/discuss/116581/Detail-and-explanation-of-O(n)-solution-why-dpn2*dn-1%2Bdpn-3
    def numTilings(self, N: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * 1001
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        if N < 3:
            return dp[N]

        for i in range(3, N+1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[N]


    def numTilings1(self, N: int) -> int:
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
