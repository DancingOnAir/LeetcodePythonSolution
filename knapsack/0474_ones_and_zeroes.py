from typing import List
from collections import Counter


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter = [(c['0'], c['1']) for c in map(Counter, strs)]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for c0, c1 in counter:
            for i in range(m, c0 - 1, -1):
                for j in range(n, c1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - c0][j - c1] + 1)

        return dp[m][n]

    # dp[i][j] = max length of the subset which is composed with i 0s and j 1s
    def findMaxForm1(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            num_digit_one = s.count('1')
            num_digit_zero = len(s) - num_digit_one

            for i in range(m, num_digit_zero - 1, -1):
                for j in range(n, num_digit_one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - num_digit_zero][j - num_digit_one] + 1)
        return dp[m][n]


def test_find_max_form():
    solution = Solution()
    assert solution.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4, 'wrong result'
    assert solution.findMaxForm(["10", "0", "1"], 1, 1) == 2, 'wrong result'


if __name__ == '__main__':
    test_find_max_form()
