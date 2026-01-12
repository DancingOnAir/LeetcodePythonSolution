from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n == 0:
            return -1

        b = [0, n]
        while b[0] != b[1]:
            mid, left, right = (b[0] + b[1]) // 2, b[0], b[1]
            b = [mid, right] if nums[mid] > nums[left] else [left, mid]
        if nums[(left + 1) % n] < nums[left]:
            left = (left + 1) % n
        res = (bisect.bisect_left(nums[left: n] + nums[0: left], target) + left) % n

        return [-1, res][nums[res] == target]


    def search1(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def find_pivot(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        return left

    def search2(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[(mid + pivot) % n]:
                return (mid + pivot) % n
            elif target < nums[(mid + pivot) % n]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


def test_search():
    solution = Solution()

    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    print(solution.search(nums1, target1))

    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    print(solution.search(nums2, target2))


if __name__ == '__main__':
    test_search()
