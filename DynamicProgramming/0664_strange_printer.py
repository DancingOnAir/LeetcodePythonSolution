from typing import List


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

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
