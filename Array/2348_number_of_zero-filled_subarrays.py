from typing import List
from itertools import groupby


class Solution:
    # two pointers
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = j = 0
        for i, val in enumerate(nums):
            if val != 0:
                j = i + 1
            res += i - j + 1
        return res

    # itertools.groupby
    def zeroFilledSubarray1(self, nums: List[int]) -> int:
        res = 0
        for k, g in groupby(nums):
            if k == 0:
                n = len(list(g))
                res += (1 + n) * n // 2
        return res


def test_zero_filled_subarray():
    solution = Solution()
    assert solution.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6, 'wrong result'
    assert solution.zeroFilledSubarray([0, 0, 0, 2, 0, 0]) == 9, 'wrong result'


if __name__ == '__main__':
    test_zero_filled_subarray()
