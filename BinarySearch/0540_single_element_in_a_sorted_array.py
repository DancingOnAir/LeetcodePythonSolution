from typing import List
from bisect import bisect_left, bisect_right
from functools import reduce


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = bisect_right(nums, nums[i])
            if i + 1 == j:
                return nums[i]
            i = j
        return -1

    def singleNonDuplicate1(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)


def test_single_non_duplicate():
    solution = Solution()
    assert solution.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2, 'wrong result'
    assert solution.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10, 'wrong result'


if __name__ == '__main__':
    test_single_non_duplicate()
