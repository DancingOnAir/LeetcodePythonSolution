from typing import List


class Solution:
    def soupServings(self, N: int) -> float:
        dp = [0.0] * N
        dp[0] = 0.25 * (0.5 + 0.5 + 0.5 + 0.5)
        dp[1] = 0.25 * (1 + 0.5 + 0.5 + 0.5)
        dp[25] = 0.25 * (1 + 0 + 0.5 + 0.5)
        dp[50] = 0.25 * (1 + 1 + 0.5 + 0)
        dp[75] = 0.25 * (1 + 1 + 0 + 0)
        dp[100] = 0.25 * (1 + 0 + 0 + 0)
        dp[101] = 0.25 * (0 + 0 + 0 + 0)

        for i in range(1, N):
            if i // 25 == (i - 1) // 25:
                dp[i] = dp[i - 1]
            else:

        return dp[-1]


def test_soup_servings():
    solution = Solution()

    assert solution.soupServings(50) == 0.625, 'wrong result'


if __name__ == '__main__':
    test_soup_servings()
