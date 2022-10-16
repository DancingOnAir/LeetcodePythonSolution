from typing import List
from itertools import accumulate
from functools import reduce
from operator import xor


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]
        cur = 0
        for i in range(1, len(pref)):
            cur ^= res[-1]
            res.append(cur ^ pref[i])
        return res


def test_find_array():
    solution = Solution()
    assert solution.findArray([5, 2, 0, 3, 1]) == [5, 7, 2, 3, 2], 'wrong result'
    assert solution.findArray([13]) == [13], 'wrong result'


if __name__ == '__main__':
    test_find_array()
