from functools import lru_cache


class Solution:
    # dp
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]

    # https://www.bilibili.com/video/BV1Gs4y1E7EU/?spm_id_from=333.788&vd_source=e6f3bca3cb4f75b9e8b036e0e78f1541
    # dfs
    def longestPalindromeSubseq3(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
            if s[i] == s[j]:
                return dfs(i + 1, j - 1) + 2
            return max(dfs(i + 1, j), dfs(i, j - 1))
        return dfs(0, n - 1)

    # 1d dp
    def longestPalindromeSubseq2(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        dp = [0] * (n - 1) + [1]
        for i in range(n)[::-1]:
            new_dp = dp[:]
            new_dp[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    new_dp[j] = dp[j - 1] + 2
                else:
                    new_dp[j] = max(dp[j], new_dp[j - 1])
            dp = new_dp
        return dp[-1]

    # 2d dp
    def longestPalindromeSubseq1(self, s: str) -> int:
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
