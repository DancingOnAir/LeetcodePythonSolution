import numpy as np


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise ValueError

        i_min, i_max, half_len = 0, m, (m + n + 1) // 2
        while i_min <= i_max:
            i = (i_min + i_max) // 2
            j = half_len - i
            # i is too small, increase i
            if i < m and nums2[j - 1] > nums1[i]:
                i_min = i + 1
            # i is too big, decrease i
            elif i > 0 and nums1[i - 1] > nums2[j]:
                i_max = i - 1
            else:
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) & 1:
                    return max_left

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) * 0.5

    def findMedianSortedArrays1(self, nums1: list, nums2: list) -> float:
        return np.median(sorted(nums1 + nums2))

    def findMedianSortedArrays2(self, nums1: list, nums2: list) -> float:
        nums = nums1 + nums2
        nums.sort()

        n = len(nums)
        i = n // 2
        if n & 1:
            return nums[i]
        return (nums[i - 1] + nums[i]) * 0.5


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
