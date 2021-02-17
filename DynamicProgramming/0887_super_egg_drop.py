class Solution:
    # dp[i][j] represents the minimum steps when floor is i, egg is j.
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0x3f3f3f3f] * (K + 1) for _ in range(N + 1)]
        for i in range(N + 1):
            dp[i][1] = i
        for i in range(K + 1):
            dp[0][i] = 0

        for i in range(1, K + 1):
            for j in range(1, N + 1):
                for k in range(1, j + 1):
                    dp[j][i] = min(dp[j][i], max(dp[k - 1][i - 1] + 1, dp[j - k][i] + 1))
        return dp[-1][-1]


def test_super_egg_drop():
    solution = Solution()
    assert solution.superEggDrop(1, 2) == 2, 'wrong result'
    assert solution.superEggDrop(2, 6) == 3, 'wrong result'
    assert solution.superEggDrop(3, 14) == 4, 'wrong result'


if __name__ == '__main__':
    test_super_egg_drop()
