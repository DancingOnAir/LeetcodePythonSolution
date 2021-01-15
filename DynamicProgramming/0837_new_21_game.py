from typing import List


class Solution:
    # dp[i] represents possibility to achieve total points equal or less than i
    # dp[i] = 1/w * (dp[i+1] + dp[i+2] + ... + dp[i+w])
    # K <= i <= K + W - 1
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0.0] * (K + W)
        for i in range(K + W - 1, -1, -1):
            if K <= i < K+W:
                if i <= N:
                    dp[i] = 1.0
            else:
                for j in range(1, W + 1):
                    dp[i] += dp[i + j]
                dp[i] /= W
        return dp[0]


def test_new_21_game():
    solution = Solution()
    # assert solution.new21Game(10, 1, 10) == 1.00000, 'wrong result'
    # assert solution.new21Game(6, 1, 10) == 0.60000, 'wrong result'
    assert solution.new21Game(21, 17, 10) == 0.73278, 'wrong result'


if __name__ == '__main__':
    test_new_21_game()
