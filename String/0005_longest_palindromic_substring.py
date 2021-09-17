class Solution:
    # dp solution
    # dp[i][j] = 1 represents the substring [i: j] of s is palindrome else 0
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if 0 == n or 1 == n:
            return s

        dp = [[0] * n for _ in range(n)]
        max_start = max_end = 0
        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                max_start = i
                max_end = i + 1

        for l in range(3, n+1):
            for i in range(n - l + 1):
                j = i + l - 1
                if dp[i + 1][j - 1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    max_start = i
                    max_end = j
        return s[max_start: max_end+1]


def test_longest_palindrome():
    solution = Solution()

    # assert solution.longestPalindrome("babad") == "bab", 'wrong result'
    assert solution.longestPalindrome("cbbd") == "bb", 'wrong result'
    assert solution.longestPalindrome("a") == "a", 'wrong result'
    assert solution.longestPalindrome("ac") == "a", 'wrong result'


if __name__ == '__main__':
    test_longest_palindrome()
