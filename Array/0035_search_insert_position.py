from typing import List
import bisect


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return left

    def searchInsert1(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


def test_search_insert():
    solution = Solution()

    # nums1 = [1, 3, 5, 6]
    # target1 = 5
    # print(solution.searchInsert(nums1, target1))

    nums2 = [1, 3, 5, 6]
    target2 = 2
    print(solution.searchInsert(nums2, target2))

    nums3 = [1, 3, 5, 6]
    target3 = 7
    print(solution.searchInsert(nums3, target3))

    nums4 = [1, 3, 5, 6]
    target4 = 0
    print(solution.searchInsert(nums4, target4))


if __name__ == '__main__':
    test_search_insert()
