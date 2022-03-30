from typing import List
from itertools import groupby
from functools import lru_cache


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        @lru_cache(None)
        def helper(ss):
            return max(len(list(g)) for _, g in groupby(ss))

        s = list(s)
        res = list()
        for i, val in enumerate(queryIndices):
            s[val] = queryCharacters[i]
            x = helper(''.join(s))
            res.append(x)
        return res


def test_longest_repeating():
    solution = Solution()
    assert solution.longestRepeating('babacc', 'bcb', [1, 3, 3]) == [3, 3, 4], 'wrong result'
    assert solution.longestRepeating('abyzz', 'aa', [2, 1]) == [2, 3], 'wrong result'


if __name__ == '__main__':
    test_longest_repeating()
