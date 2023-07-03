from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def low_bound(nums, target, left_bound):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if left_bound:
                        right -= 1
                    else:
                        left += 1
                elif nums[mid] < target:
                    left += 1
                else:
                    right -= 1

            if left_bound:
                if left >= len(nums):
                    return -1
            else:
                if right < 0:
                    return -1
            if left_bound:
                return left if nums[left] == target else -1
            return right if nums[right] == target else -1

        return [low_bound(nums, target, True), low_bound(nums, target, False)]


def test_search_range():
    solution = Solution()
    assert solution.searchRange([5,7,7,8,8,10], 8) == [3, 4], 'wrong result'
    assert solution.searchRange([5,7,7,8,8,10], 6) == [-1, -1], 'wrong result'
    assert solution.searchRange([], 0) == [-1, -1], 'wrong result'


if __name__ == '__main__':
    test_search_range()
