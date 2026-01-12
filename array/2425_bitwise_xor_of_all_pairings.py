import operator

from typing import List
from functools import reduce


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        res = 0
        if l1 & 1:
            res = res ^ reduce(operator.xor, nums2)
        if l2 & 1:
            res = res ^ reduce(lambda x, y: x ^ y, nums1)
        return res


def test_xor_all_nums():
    solution = Solution()
    assert solution.xorAllNums([2,1,3], [10,2,5,0]) == 13, 'wrong results'
    assert solution.xorAllNums([1,2], [3,4]) == 0, 'wrong results'


if __name__ == '__main__':
    test_xor_all_nums()
