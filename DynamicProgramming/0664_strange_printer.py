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
                    temp = min(dp[i][i+l-1], dp[i+1][i+l])
                    if s[i] != s[i+l]:
                        temp += 1
                    dp[i][i+l] = min(dp[i][i+l-1] + (s[i+l-1] != s[i+l]), dp[i+1][i+l] + (s[i] != s[i+1]), temp)

        return dp[0][n-1]


def test_strange_printer():
    solution = Solution()

    assert solution.strangePrinter('aaabbb') == 2, 'wrong result'
    assert solution.strangePrinter('aba') == 2, 'wrong result'
    assert solution.strangePrinter("ccdcadbddbaddcbccdcdabcbcddbccdcbad") == 17, 'wrong result'


if __name__ == '__main__':
    test_strange_printer()
