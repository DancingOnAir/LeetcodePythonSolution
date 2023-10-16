from typing import List
from functools import lru_cache


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
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
