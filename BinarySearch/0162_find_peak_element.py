from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-1] + nums + [-1]
        left, right = 1, len(nums) - 2
        while left <= right:
            mid = left + (right - left)
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                # 左位移1位，减去添加在头部的-1
                return mid - 1
            elif nums[mid - 1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


def test_find_peak_element():
    solution = Solution()
    assert solution.findPeakElement([1, 2, 3, 1]) in {2}, 'wrong result'
    assert solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in {1, 5}, 'wrong result'


if __name__ == '__main__':
    test_find_peak_element()
