from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        pass


def test_constrained_subset_sum():
    solution = Solution()
    assert solution.constrainedSubsetSum([-5266, 4019, 7336, -3681, -5767], 2) == 11355, 'wrong result'
    assert solution.constrainedSubsetSum([10, 2, -10, 5, 20], 2) == 37, 'wrong result'
    assert solution.constrainedSubsetSum([-1, -2, -3], 1) == -1, 'wrong result'
    assert solution.constrainedSubsetSum([10, -2, -10, -5, 20], 2) == 23, 'wrong result'


if __name__ == '__main__':
    test_constrained_subset_sum()
