from typing import List


class Solution:
    # f(n, k) = sum(f(n - 1, i)), where max(k - n + 1, 0) <= i <= k
    # f(0, k) = 0
    # f(n, 0) = 1
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0] * (k + 1)] * (n + 1)
        MOD = 10 ** 9 + 7

        for i in range(1, n + 1):
            for j in range(0, k + 1):
                if j > i * (i - 1) // 2:
                    break

                if j == 0:
                    dp[i][j] = 1
                else:
                    val = (dp[i - 1][j] + MOD - (dp[i - 1][j - i] if (j - i) >= 0 else 0)) % MOD
                    dp[i][j] = (dp[i][j - 1] + val) % MOD

        return dp[n][k]


def test_k_inverse_pairs():
    solution = Solution()

    assert solution.kInversePairs(3, 0) == 1, "wrong result"
    assert solution.kInversePairs(3, 1) == 2, "wrong result"


if __name__ == '__main__':
    test_k_inverse_pairs()
