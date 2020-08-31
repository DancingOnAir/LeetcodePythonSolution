from typing import List


class Solution:
    # one pass solution
    def sortColors1(self, nums: List[int]) -> None:
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

    # count sort
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_red = count_white = count_blue = 0
        for i, val in enumerate(nums):
            if val == 0:
                count_red += 1
            elif val == 1:
                count_white += 1
            else:
                count_blue += 1

        nums[:count_red] = [0] * count_red
        nums[count_red:count_red + count_white] = [1] * count_white
        nums[count_red + count_white:] = [2] * count_blue


def test_sort_colors():
    solution = Solution()

    nums1 = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums1)
    print(nums1)

    nums2 = [0]
    solution.sortColors(nums2)
    print(nums2)


if __name__ == '__main__':
    test_sort_colors()
