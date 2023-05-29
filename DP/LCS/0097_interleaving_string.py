from functools import lru_cache


class Solution:
    # 3-d dp
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False

        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
        dp[0][0] = True
        for i, x in enumerate(s1):
            if x == s3[i]:
                dp[i + 1][0] = True
            else:
                break

        for j, y in enumerate(s2):
            if y == s3[j]:
                dp[0][j + 1] = True
            else:
                break

        for i, x in enumerate(s1):
            for j, y in enumerate(s2):
                k = i + j + 1
                if x == s3[k]:
                    dp[i + 1][j + 1] |= dp[i][j + 1]
                if y == s3[k]:
                    dp[i + 1][j + 1] |= dp[i + 1][j]
        return dp[l1][l2]

    # dfs + cache
    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)

        @lru_cache(None)
        def dfs(i, j, k):
            if i == 0 and j == 0 and k == 0:
                return True

            a, b = False, False
            if i > 0 and k > 0 and s1[i - 1] == s3[k - 1]:
                a = dfs(i - 1, j, k - 1)
            if j > 0 and k > 0 and s2[j - 1] == s3[k - 1]:
                b = dfs(i, j - 1, k - 1)
            return a or b
        return dfs(l1, l2, l3)


def test_is_interleave():
    solution = Solution()
    assert solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"), 'wrong result'
    assert not solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"), 'wrong result'
    assert solution.isInterleave("", "", ""), 'wrong result'


if __name__ == '__main__':
    test_is_interleave()
