from typing import List
import bisect


class Solution:
    def extreme_insertion_index(self, nums, target, is_left):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] > target or (is_left and nums[mid] == target):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left_index = self.extreme_insertion_index(nums, target, True)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        return [left_index, self.extreme_insertion_index(nums, target, False) - 1]

    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        start_position = bisect.bisect_left(nums, target)
        end_position = bisect.bisect_right(nums, target)

        return [start_position, end_position - 1] if nums[start_position] == target else [-1, -1]


def test_search_range():
    solution = Solution()

    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    print(solution.searchRange(nums1, target1))

    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    print(solution.searchRange(nums2, target2))


if __name__ == '__main__':
    test_search_range()
