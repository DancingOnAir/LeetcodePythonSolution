from functools import lru_cache


class Solution:
    # bottom-up, space optimized
    def minDistance(self, word1: str, word2: str) -> int:
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