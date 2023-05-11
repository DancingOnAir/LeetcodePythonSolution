from functools import lru_cache


class Solution:
    # 2d dp
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        dp[0] = list(range(l2 + 1))
        for i, x in enumerate(word1):
            dp[i + 1][0] = i + 1
            for j, y in enumerate(word2):
                if x == y:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
        return dp[l1][l2]

    # https://www.bilibili.com/video/BV1TM4y1o7ug/?spm_id_from=333.788&vd_source=e6f3bca3cb4f75b9e8b036e0e78f1541
    # dfs
    def minDistance4(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)

        @lru_cache(None)
        def dfs(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if word1[i] == word2[j]:
                return dfs(i - 1, j - 1)
            return min(dfs(i, j - 1), dfs(i - 1, j), dfs(i - 1, j - 1)) + 1
        return dfs(l1 - 1, l2 - 1)

    # bottom-up, space optimized
    def minDistance3(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        cur, pre = [0] * (l2+1), [0] * (l2+1)

        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i == 0:
                    cur[j] = j
                elif j == 0:
                    cur[j] = i
                elif word1[i - 1] == word2[j - 1]:
                    cur[j] = pre[j - 1]
                else:
                    cur[j] = min(pre[j - 1], pre[j], cur[j - 1]) + 1
            cur, pre = pre, cur
        return pre[l2]

    # top-down
    def minDistance2(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return j
            if j == 0:
                return i
            if word1[i - 1] == word2[j - 1]:
                return dp(i - 1, j - 1)
            return min(dp(i - 1, j - 1), dp(i - 1, j), dp(i, j - 1)) + 1

        return dp(len(word1), len(word2))

    # bottom-up
    def minDistance1(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        if not l1:
            return l2

        if not l2:
            return l1

        dp = [[0] * (l2+1) for _ in range(l1+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[l1][l2]


def test_min_distance():
    solution = Solution()

    assert solution.minDistance('horse', 'ros') == 3, 'wrong result'
    assert solution.minDistance('intention', 'execution') == 5, 'wrong result'


if __name__ == '__main__':
    test_min_distance()
