from functools import cache


class Solution:
    # dp
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n < m:
            return 0
        dp = [1] + [0] * m
        for i, x in enumerate(s):
            for j in range(min(i, m - 1), max(0, m - n + i) - 1, -1):
                if x == t[j]:
                    dp[j + 1] += dp[j]
        return dp[m]

    # dp
    def numDistinct2(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        if n < m:
            return 0
        # 表示s[0..i]中t[0..j]出现的个数
        dp = [([1] + [0] * m) for _ in range(n + 1)]
        for i, x in enumerate(s):
            # t的长度最小值满足m - j <= n - i，最大值不可能超过i
            for j in range(max(0, m - n + i), min(i + 1, m)):
                dp[i + 1][j + 1] = dp[i][j + 1]
                if x == t[j]:
                    dp[i + 1][j + 1] += dp[i][j]
        return dp[n][m]

    # dfs
    def numDistinct1(self, s: str, t: str) -> int:
        @cache
        def dfs(i, j):
            if i < j:
                return 0
            if j < 0:
                return 1
            res = dfs(i - 1, j)
            if s[i] == t[j]:
                res += dfs(i - 1, j - 1)
            return res
        return dfs(len(s) - 1, len(t) - 1)


def test_num_distinct():
    solution = Solution()
    assert solution.numDistinct("rabbbit", "rabbit") == 3, 'wrong result'
    assert solution.numDistinct("babgbag", "bag") == 5, 'wrong result'


if __name__ == '__main__':
    test_num_distinct()
