from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


def test_search():
    solution = Solution()
    assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4, 'wrong result'
    assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1, 'wrong result'


if __name__ == '__main__':
    test_search()
