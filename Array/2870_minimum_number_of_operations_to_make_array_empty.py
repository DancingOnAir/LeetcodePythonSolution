from typing import List
from collections import Counter
from math import ceil


class Solution:
    # concise & pythonic
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for v in Counter(nums).values():
            if v == 1:
                return -1
            res += ceil(v / 3)
        return res

    # original
    def minOperations1(self, nums: List[int]) -> int:
        values = Counter(nums).values()
        res = 0
        for v in values:
            if v == 1:
                return -1

            r, m = divmod(v, 3)
            if m == 0:
                res += r
            else:
                res += r + 1
        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]) == 4, 'wrong result'
    assert solution.minOperations([2, 1, 2, 2, 3, 3]) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
