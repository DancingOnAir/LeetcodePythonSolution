from typing import List


class Solution:
    # f(n, k) = sum(f(n - 1, i)), where max(k - n + 1, 0) <= i <= k
    # f(0, k) = 0
    # f(n, 0) = 1
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        MOD = 10 ** 9 + 7
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = 1
            for j in range(1, k + 1):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD
                if j - i >= 0:
                    dp[i][j] = (dp[i][j] - dp[i - 1][j - i] + MOD) % MOD

        return dp[n][k]


def test_k_inverse_pairs():
    solution = Solution()

    assert solution.kInversePairs(3, 0) == 1, "wrong result"
    assert solution.kInversePairs(3, 1) == 2, "wrong result"
    assert solution.kInversePairs(3, 3) == 1, "wrong result"


if __name__ == '__main__':
    test_k_inverse_pairs()
