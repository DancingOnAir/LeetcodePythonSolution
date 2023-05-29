from functools import lru_cache


class Solution:
    # dp
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        def cal(s):
            return sum(ord(c) for c in s)

        l1, l2 = len(s1), len(s2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        for i, x in enumerate(s1):
            for j, y in enumerate(s2):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j] + ord(x)
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return cal(s1) + cal(s2) - 2 * dp[l1][l2]

    # dfs
    def minimumDeleteSum1(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)

        @lru_cache(None)
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if s1[i] == s2[j]:
                return dfs(i - 1, j - 1) + ord(s1[i])
            return max(dfs(i - 1, j), dfs(i, j - 1))

        def cal(s):
            return sum(ord(c) for c in s)

        return cal(s1) + cal(s2) - 2 * dfs(l1 - 1, l2 - 1)


def test_minimum_delete_sum():
    solution = Solution()
    assert solution.minimumDeleteSum("sea", "eat") == 231, 'wrong result'
    assert solution.minimumDeleteSum("delete", "leet") == 403, 'wrong result'


if __name__ == '__main__':
    test_minimum_delete_sum()
