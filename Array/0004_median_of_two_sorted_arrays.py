import numpy as np


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        return np.median(sorted(nums1 + nums2))

    def findMedianSortedArrays1(self, nums1: list, nums2: list) -> float:
        nums = nums1 + nums2
        nums.sort()

        n = len(nums)
        if n & 1:
            return nums[n // 2]
        return (nums[n // 2 - 1] + nums[n // 2]) * 0.5


def test_find_median_sorted_arrays():
    solution = Solution()

    nums11 = [1, 3]
    nums21 = [2]
    print(solution.findMedianSortedArrays(nums11, nums21))

    nums12 = [1, 2]
    nums22 = [3, 4]
    print(solution.findMedianSortedArrays(nums12, nums22))


if __name__ == '__main__':
    test_find_median_sorted_arrays()
