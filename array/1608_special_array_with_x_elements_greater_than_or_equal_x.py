from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2

            if mid < nums[mid]:
                left = mid + 1
            else:
                right = mid

        return -1 if left < len(nums) and left == nums[left] else left

    def specialArray1(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        nums.append(-1)
        for i in range(1, len(nums)):
            if nums[i - 1] >= i > nums[i]:
                return i
        return -1


def test_special_array():
    solution = Solution()

    nums1 = [3, 5]
    assert solution.specialArray(nums1) == 2, "wrong result"

    nums2 = [0, 0]
    assert solution.specialArray(nums2) == -1, "wrong result"

    nums3 = [0, 4, 3, 0, 4]
    assert solution.specialArray(nums3) == 3, "wrong result"

    nums4 = [3, 6, 7, 7, 0]
    assert solution.specialArray(nums4) == -1, "wrong result"


if __name__ == '__main__':
    test_special_array()
