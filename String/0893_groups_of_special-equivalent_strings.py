from typing import List
from collections import defaultdict


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        words = [''.join(sorted(w[0::2]) + sorted(w[1::2])) for w in words]
        return len(set(words))


def test_num_special_equiv_groups():
    solution = Solution()
    assert solution.numSpecialEquivGroups(["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]) == 3, 'wrong result'
    assert solution.numSpecialEquivGroups(["abc", "acb", "bac", "bca", "cab", "cba"]) == 3, 'wrong result'


if __name__ == '__main__':
    test_num_special_equiv_groups()
