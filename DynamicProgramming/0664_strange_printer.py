from typing import List
from functools import lru_cache
import re


class Solution:
    def strangePrinter(self, s: str) -> int:
        s = re.sub(r'(.)\1*', r'\1', s)
        memo = dict()

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            if (i, j) not in memo:
                ans = dp(i+1, j) + 1
                for k in range(i+1, j+1):
                    if s[k] == s[i]:
                        ans = min(ans, dp(i, k-1) + dp(k+1, j))
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, len(s) - 1)

    def strangePrinter1(self, s: str) -> int:
        if not s:
            return 0

        # s = ''.join(a for a, b in zip(s, '#'+s) if a != b)
        s = re.sub(r'(.)\1*', r'\1', s)
        n = len(s)

        dp = [[1] * n for _ in range(n)]
        for l in range(1, n):
            for i in range(n):
                if i + l < n:
                    dp[i][i+l] = min(dp[i][i+k] + dp[i+k+1][i+l] for k in range(0, l))
                    if s[i] == s[i+l]:
                        dp[i][i+l] -= 1

        return dp[0][n-1]


def test_strange_printer():
    solution = Solution()

    assert solution.strangePrinter('aaabbb') == 2, 'wrong result'
    assert solution.strangePrinter('aba') == 2, 'wrong result'
    assert solution.strangePrinter("ccdcadbddbaddcbccdcdabcbcddbccdcbad") == 17, 'wrong result'


if __name__ == '__main__':
    test_strange_printer()
