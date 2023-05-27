from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
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
