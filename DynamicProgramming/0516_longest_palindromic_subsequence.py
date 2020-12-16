from typing import List


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        dp = [[0] * n for _ in range(n)]
        for i in range(n)[::-1]:
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]


def test_longest_palindrome_subseq():
    solution = Solution()

    assert solution.longestPalindromeSubseq("aa") == 2, 'wrong result'
    assert solution.longestPalindromeSubseq("bbbab") == 4, 'wrong result'
    assert solution.longestPalindromeSubseq("cbbd") == 2, 'wrong result'


if __name__ == '__main__':
    test_longest_palindrome_subseq()
