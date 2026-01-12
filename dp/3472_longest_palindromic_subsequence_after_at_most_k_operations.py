from functools import lru_cache, cache


class Solution:
    # dp
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        s = list(map(ord, s))
        n = len(s)
        cnt = 0
        for i in range(n // 2):
            d = abs(s[i] - s[-1 - i])
            cnt += min(d, 26 - d)
        if cnt <= k:
            return n

        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        for kk in range(k + 1):
            for i in range(n - 1, -1, -1):
                dp[kk][i][i] = 1
                for j in range(i + 1, n):
                    res = max(dp[kk][i + 1][j], dp[kk][i][j - 1])
                    d = abs(s[i] - s[j])
                    op = min(26 - d, d)
                    if op <= kk:
                        res = max(res, dp[kk - op][i + 1][j - 1] + 2)
                    dp[kk][i][j] = res
        return dp[k][0][-1]

    # dfs
    def longestPalindromicSubsequence1(self, s: str, k: int) -> int:
        s = list(map(ord, s))
        n = len(s)

        @cache
        def dfs(i, j, k):
            if i >= j:
                return j - i + 1
            res = max(dfs(i + 1, j, k), dfs(i, j - 1, k))
            d = abs(s[i] - s[j])
            op = min(26 - d, d)
            if op <= k:
                res = max(res, dfs(i + 1, j - 1, k - op) + 2)
            return res

        dfs.cache_clear()
        return dfs(0, n - 1, k)


def test_longest_palindromic_subsequence():
    solution = Solution()
    assert solution.longestPalindromicSubsequence("abced", 2) == 3, 'wrong result'
    assert solution.longestPalindromicSubsequence("aaazzz", 4) == 6, 'wrong result'


if __name__ == '__main__':
    test_longest_palindromic_subsequence()
