from typing import List
from functools import lru_cache


class Solution:
    # 递推
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        # 表示递归里<0的边界情况，所以+1
        dp = [0] * (n + 1)
        dictionary = set(dictionary)

        for i in range(n):
            # 不选
            dp[i + 1] = dp[i] + 1
            # 选
            for j in range(i + 1):
                if s[j: i + 1] in dictionary:
                    dp[i + 1] = min(dp[i + 1], dp[j])
        return dp[n]

    # 递归
    def minExtraChar1(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)

        @lru_cache(None)
        def dfs(i):
            if i < 0:
                return 0
            # 不选
            res = dfs(i - 1) + 1
            for j in range(i + 1):
                if s[j: i + 1] in dictionary:
                    res = min(res, dfs(j - 1))
            return res
        return dfs(len(s) - 1)


def test_min_extra_char():
    solution = Solution()
    assert solution.minExtraChar("leetscode", ["leet", "code", "leetcode"]) == 1, 'wrong result'
    assert solution.minExtraChar("sayhelloworld", ["hello", "world"]) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_extra_char()
