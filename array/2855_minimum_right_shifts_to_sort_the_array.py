from typing import List


class Solution:
    # 最多2段递增
    def minimumRightShifts(self, nums: List[int]) -> int:
        i, n = 1, len(nums)
        while i < n and nums[i - 1] < nums[i]:
            i += 1
        if i == n:
            return 0
        if nums[0] < nums[-1]:
            return -1
        mid = i
        i += 1
        while i < n and nums[i - 1] < nums[i]:
            i += 1
        if i < n:
            return -1
        return n - mid


def test_minimum_right_shifts():
    solution = Solution()
    # 7 - 4 n - i + (n - 1)
    # assert solution.minimumRightShifts([3, 4, 5, 1, 2]) == 2, 'wrong result'
    assert solution.minimumRightShifts([1, 3, 5]) == 0, 'wrong result'
    assert solution.minimumRightShifts([2, 1, 4]) == -1, 'wrong result'


if __name__ == '__main__':
    test_minimum_right_shifts()
