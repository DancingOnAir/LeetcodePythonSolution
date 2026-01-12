from typing import List
from bisect import bisect_left, bisect_right
from functools import reduce


class Solution:
    # concise binary search
    # https://leetcode.com/problems/single-element-in-a-sorted-array/solutions/1587257/c-easy-intuitive-solution-2-approaches-binary-search-tc-o-log-n-sc-o-1/
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 2
        while l <= r:
            mid = l + (r - l) // 2
            # 如果是左边部分
            # 这里等价于 ( mid%2==0 && nums[ mid ] == nums[ mid + 1 ] ) || ( mid%2 == 1 && nums[ mid ] == nums[ mid - 1 ] )
            if nums[mid] == nums[mid ^ 1]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]

    # binary search
    def singleNonDuplicate2(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = bisect_right(nums, nums[i])
            if i + 1 == j:
                return nums[i]
            i = j
        return -1

    # xor
    def singleNonDuplicate1(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)


def test_single_non_duplicate():
    solution = Solution()
    assert solution.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2, 'wrong result'
    assert solution.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10, 'wrong result'


if __name__ == '__main__':
    test_single_non_duplicate()
