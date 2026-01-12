from typing import List


class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        return 0


def test_max_balanced_subarray():
    solution = Solution()
    assert solution.maxBalancedSubarray([3, 1, 3, 2, 0]) == 4, "test1"
    assert solution.maxBalancedSubarray([3, 2, 8, 5, 4, 14, 9, 15]) == 8, "test2"
    assert solution.maxBalancedSubarray([0]) == 0, "test3"


if __name__ == '__main__':
    test_max_balanced_subarray()
