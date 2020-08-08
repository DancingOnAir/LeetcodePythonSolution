from typing import List


class Solution:
    def find_pivot(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        return left

    def search(self, nums: List[int], target: int) -> int:
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
