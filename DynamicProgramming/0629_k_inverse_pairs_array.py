from typing import List


class Solution:
    # f(n, k) = sum(f(n - 1, i)), where max(k - n + 1, 0) <= i <= k
    # f(0, k) = 0
    # f(n, 0) = 1
    # 在纯and语句中，如果每一个表达式都不是假的话，那么返回最后一个，因为需要一直匹配直到最后一个。如果有一个是假，那么返回假
    # 在纯or语句中，只要有一个表达式不是假的话，那么就返回这个表达式的值。只有所有都是假，才返回假
    # 在or和and语句比较难表达，总而言之，碰到and就往后匹配，碰到or如果or左边的为真，那么就返回or左边的那个值，如果or左边为假，继续匹配or右边的参数。
    # 总结一句话就是：无论操作符是哪个，最后的结果一定是按照计算顺序能最快判断出结果的那个表达式决定的。
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [1] + [0] * k
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                dp[j] += dp[j - 1]
            for j in range(k, 0, -1):
                dp[j] -= j - i >= 0 and dp[j - i]
        return dp[k] % (10 ** 9 + 7)

    # dp[i][j] = dp[i - 1][j - i + 1] + dp[i - 1][j - i + 2] + ... + dp[i - 1][j]
    # dp[i][j - 1] = dp[i - 1][j - i] + dp[i - 1][j - i + 1] + ... + dp[i - 1][j - 1]
    # dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - (if j - i >= 0: dp[i-1][j-i] else: 0)
    def kInversePairs1(self, n: int, k: int) -> int:
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
