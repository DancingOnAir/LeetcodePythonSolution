from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(len(nums) - bisect_right(nums, 0), bisect_left(nums, 0))


def test_maximum_count():
    solution = Solution()
    assert solution.maximumCount([-2, -1, -1, 1, 2, 3]) == 3, 'wrong result'
    assert solution.maximumCount([-3, -2, -1, 0, 0, 1, 2]) == 3, 'wrong result'
    assert solution.maximumCount([5, 20, 66, 1314]) == 4, 'wrong result'


if __name__ == '__main__':
    test_maximum_count()
