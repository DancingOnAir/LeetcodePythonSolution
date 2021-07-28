import string
from functools import lru_cache


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def helper(lo, hi):
            if lo >= hi:
                return int(lo == hi)
            if w[lo] == w[hi]:
                return 2 + helper(lo+1, hi - 1)
            return max(helper(lo + 1, hi), helper(lo, hi - 1))

        res = 0
        w = word1 + word2
        for c in string.ascii_lowercase:
            i = word1.find(c)
            j = word2.rfind(c)
            if i != - 1 and j != -1:
                res = max(res, helper(i, j + len(word1)))
        return res

    def longestPalindrome1(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        w = word1 + word2
        n = n1 + n2
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        res = 0
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if w[i] == w[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if i < n1 <= j:
                        res = max(res, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return res


def test_longest_palindrome():
    solution = Solution()
    assert solution.longestPalindrome('cacb', 'cbba') == 5, 'wrong result'
    assert solution.longestPalindrome('ab', 'ab') == 3, 'wrong result'
    assert solution.longestPalindrome('aa', 'bb') == 0, 'wrong result'


if __name__ == '__main__':
    test_longest_palindrome()
