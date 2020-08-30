from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, cur, right = 0, 0, len(nums) - 1
        while cur <= right:
            if nums[cur] == 0:
                nums[cur], nums[left] = nums[left], nums[cur]
                cur += 1
                left += 1
            elif nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
            else:
                cur += 1

    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()


def test_sort_colors():
    solution = Solution()

    nums1 = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums1)
    print(nums1)


if __name__ == '__main__':
    test_sort_colors()
