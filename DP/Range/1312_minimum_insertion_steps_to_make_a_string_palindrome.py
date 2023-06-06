from functools import lru_cache


class Solution:
    # dp
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][n - 1]

    # dfs + cache
    def minInsertions1(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            return min(dfs(i + 1, j), dfs(i, j - 1)) + 1
        return dfs(0, n - 1)


def test_min_insertions():
    solution = Solution()
    assert solution.minInsertions("zzazz") == 0, 'wrong result'
    assert solution.minInsertions("mbadm") == 2, 'wrong result'
    assert solution.minInsertions("leetcode") == 5, 'wrong result'


if __name__ == '__main__':
    test_min_insertions()
