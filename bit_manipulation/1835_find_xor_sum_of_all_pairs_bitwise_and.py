from typing import List
from functools import reduce


class Solution:
    # (a ^ b) & (c ^ d) = (a & c) ^ (a & d) ^ (b & c) ^ (b & d)
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, arr1) & reduce(lambda a, b: a ^ b, arr2)


def test_get_xor_sum():
    solution = Solution()
    assert solution.getXORSum([1, 2, 3], [6, 5]) == 0, 'wrong result'
    assert solution.getXORSum([12], [4]) == 4, 'wrong result'


if __name__ == '__main__':
    test_get_xor_sum()
