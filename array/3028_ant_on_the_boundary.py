from typing import List
from itertools import accumulate


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        return list(accumulate(nums)).count(0)


def test_return_to_boundary_count():
    solution = Solution()
    assert solution.returnToBoundaryCount([2, 3, -5]) == 1, 'wrong result'
    assert solution.returnToBoundaryCount([3, 2, -3, -4]) == 0, 'wrong result'


if __name__ == '__main__':
    test_return_to_boundary_count()
