from typing import List
from functools import lru_cache


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(i, j, target):
            if j - i < 2:
                return i + 1 == j and nums[i] + nums[j] == target

            return max(1 + helper(i + 2, j, target) if nums[i] + nums[i + 1] == target else 0,
                       1 + helper(i, j - 2, target) if nums[j - 1] + nums[j] == target else 0,
                       1 + helper(i + 1, j - 1, target) if nums[i] + nums[j] == target else 0)

        n = len(nums)
        return 1 + max(helper(2, n - 1, nums[0] + nums[1]),
                       helper(0, n - 3, nums[-2] + nums[-1]),
                       helper(1, n - 2, nums[0] + nums[-1]))


def test_max_operations():
    solution = Solution()
    assert solution.maxOperations([3, 2, 1, 2, 3, 4]) == 3, 'wrong result'
    assert solution.maxOperations([3, 2, 6, 1, 4]) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_operations()
