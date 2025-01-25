from typing import List
from itertools import pairwise


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(a - b) for a, b in pairwise(nums + [nums[0]]))


def test_max_adjacent_distance():
    solution = Solution()
    assert solution.maxAdjacentDistance([1, 2, 4]) == 3, 'wrong result'
    assert solution.maxAdjacentDistance([-5, -10, -5]) == 5, 'wrong result'


if __name__ == '__main__':
    test_max_adjacent_distance()
