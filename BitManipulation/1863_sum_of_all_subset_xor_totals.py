from typing import List
from itertools import combinations
from functools import reduce


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums) + 1):
            for comb in combinations(nums, i):
               res += reduce(lambda x, y: x ^ y, comb)
        return res


def test_subset_xor_sum():
    solution = Solution()
    assert solution.subsetXORSum([1, 3]) == 6, 'wrong result'
    assert solution.subsetXORSum([5, 1, 6]) == 28, 'wrong result'
    assert solution.subsetXORSum([3, 4, 5, 6, 7, 8]) == 480, 'wrong result'


if __name__ == '__main__':
    test_subset_xor_sum()
