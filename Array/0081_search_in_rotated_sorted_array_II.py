from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in set(nums)

    def search1(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[right]:
                right -= 1
            # left side is sorted
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # right side is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


def test_search():
    solution = Solution()

    nums1 = [2, 5, 6, 0, 0, 1, 2]
    target1 = 0
    print(solution.search(nums1, target1))

    nums2 = [2, 5, 6, 0, 0, 1, 2]
    target2 = 3
    print(solution.search(nums2, target2))

    nums3 = [1, 3, 1, 1, 1]
    target3 = 3
    print(solution.search(nums3, target3))


if __name__ == '__main__':
    test_search()
