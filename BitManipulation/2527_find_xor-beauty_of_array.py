from typing import List
from functools import reduce
from operator import xor


class Solution:
    # https://leetcode.com/problems/find-xor-beauty-of-array/solutions/3015014/why-just-xor-of-all-numbers-works/
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(xor, nums)


def test_xor_beauty():
    solution = Solution()
    assert solution.xorBeauty([1, 4]) == 5, 'wrong result'
    assert solution.xorBeauty([15, 45, 20, 2, 34, 35, 5, 44, 32, 30]) == 34, 'wrong result'


if __name__ == '__main__':
    test_xor_beauty()
