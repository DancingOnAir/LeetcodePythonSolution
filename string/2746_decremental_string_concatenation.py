from typing import List
from functools import lru_cache


class Solution:
    # https://leetcode.com/problems/decremental-string-concatenation/solutions/3682035/python-3-6-lines-dp-t-m-96-67/
    # 放置前，或放置后
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        @lru_cache(None)
        def dp(i, first, last):
            if i == len(words):
                return 0
            cur_first = words[i][0]
            cur_last = words[i][-1]
            return max((first == cur_last) + dp(i + 1, cur_first, last), (last == cur_first) + dp(i + 1, first, cur_last))

        return sum(map(len, words)) - dp(1, words[0][0], words[0][-1])


def test_minimize_concatenated_length():
    solution = Solution()
    assert solution.minimizeConcatenatedLength(["aa", "ab", "bc"]) == 4, 'wrong result'
    assert solution.minimizeConcatenatedLength(["ab", "b"]) == 2, 'wrong result'
    assert solution.minimizeConcatenatedLength(["aaa", "c", "aba"]) == 6, 'wrong result'


if __name__ == '__main__':
    test_minimize_concatenated_length()
