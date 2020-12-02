from typing import List


class Solution:
    # dp[i] = dp[i-1] if s[i-1] == s[i-2]
    def strangePrinter(self, s: str) -> int:
        n = len(s)

        pass


def test_strange_printer():
    solution = Solution()

    assert solution.strangePrinter('aaabbb') == 2, 'wrong result'
    assert solution.strangePrinter('aba') == 2, 'wrong result'


if __name__ == '__main__':
    test_strange_printer()
