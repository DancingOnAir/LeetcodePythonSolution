from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left <= right:
            mid = left + (right - left) // 2

            if sum((x - 1) // mid for x in nums) > maxOperations:
                left = mid + 1
            else:
                right = mid - 1
        return left


def test_minimum_size():
    solution = Solution()
    assert solution.minimumSize(
        [431, 922, 158, 60, 192, 14, 788, 146, 788, 775, 772, 792, 68, 143, 376, 375, 877, 516, 595, 82, 56, 704, 160,
         403, 713, 504, 67, 332, 26], 80) == 129, 'wrong result'
    assert solution.minimumSize([9], 2) == 3, 'wrong result'
    assert solution.minimumSize([2, 4, 8, 2], 4) == 2, 'wrong result'


if __name__ == '__main__':
    test_minimum_size()
