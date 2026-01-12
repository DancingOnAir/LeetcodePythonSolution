from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        for i, x in enumerate(word1):
            for j, y in enumerate(word2):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return l1 + l2 - 2 * dp[l1][l2]

    # dfs
    def minDistance2(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)

        @lru_cache(None)
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if word1[i] == word2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))
        return l1 + l2 - 2 * dfs(l1 - 1, l2 - 1)

    def minDistance1(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(l1):
            for j in range(l2):
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], dp[i][j] + (word1[i] == word2[j]))
        return l1 + l2 - 2 * dp[l1][l2]


def test_min_distance():
    solution = Solution()

    assert solution.minDistance('sea', 'eat') == 2, "wrong result"
    assert solution.minDistance('mart', 'karma') == 5, "wrong result"


if __name__ == '__main__':
    test_min_distance()
