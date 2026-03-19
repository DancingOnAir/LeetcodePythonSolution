from functools import cache


class Solution:


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
