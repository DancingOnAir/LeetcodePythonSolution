from typing import List
from math import comb


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] % 10

        res = 0
        for i, x in enumerate(nums):
            res += comb(n - 1, i) * x

        return res % 10


def test_triangular_sum():
    solution = Solution()
    assert solution.triangularSum([1, 2, 3, 4, 5]) == 8, 'wrong result'
    assert solution.triangularSum([5]) == 5, 'wrong result'


if __name__ == '__main__':
    test_triangular_sum()
