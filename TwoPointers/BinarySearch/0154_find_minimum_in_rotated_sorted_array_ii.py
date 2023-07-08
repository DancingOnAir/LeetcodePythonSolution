from typing import List


class Solution:
    # https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/solution/zhi-yao-ni-hui-153-jiu-neng-kan-dong-pyt-qqc6/
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        # [0, n - 1)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]


def test_find_min():
    solution = Solution()
    assert solution.findMin([3, 3, 1, 3]) == 1, 'wrong result'
    assert solution.findMin([1, 3, 3]) == 1, 'wrong result'
    assert solution.findMin([1, 3, 5]) == 1, 'wrong result'
    assert solution.findMin([2, 2, 2, 0, 1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_find_min()
