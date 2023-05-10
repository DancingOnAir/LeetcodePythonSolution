from functools import lru_cache


class Solution:
    # 2d dp
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i, x in enumerate(text1):
            for j, y in enumerate(text2):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[l1][l2]

    # dfs + cache
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))
        return dfs(len(text1) - 1, len(text2) - 1)


def test_longest_common_subsequence():
    solution = Solution()
    assert solution.longestCommonSubsequence("abcde", 'ace') == 3, 'wrong result'
    assert solution.longestCommonSubsequence("abc", 'abc') == 3, 'wrong result'
    assert solution.longestCommonSubsequence("abc", 'def') == 0, 'wrong result'


if __name__ == '__main__':
    test_longest_common_subsequence()
