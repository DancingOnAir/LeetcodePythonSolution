from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        # 从0，n-2个元素做二分，这里取[0, n-1)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


def test_find_min():
    solution = Solution()
    assert solution.findMin([2, 3, 4, 5, 1]) == 1, 'wrong result'
    assert solution.findMin([3, 4, 5, 1, 2]) == 1, 'wrong result'
    assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0, 'wrong result'
    assert solution.findMin([11, 13, 15, 17]) == 11, 'wrong result'


if __name__ == '__main__':
    test_find_min()
