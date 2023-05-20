from typing import List
from functools import lru_cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if n == 1 or (total & 1):
            return False
        target = total // 2

        @lru_cache(None)
        def dfs(i, c):
            if c == 0:
                return True

            if i < 0:
                return False
            if c < nums[i]:
                return dfs(i - 1, c)
            return dfs(i - 1, c) or dfs(i - 1, c - nums[i])
        return dfs(n - 1, target)


def test_can_partition():
    solution = Solution()
    assert solution.canPartition([1, 5, 11, 5]), 'wrong result'
    assert not solution.canPartition([1, 2, 3, 5]), 'wrong result'


if __name__ == '__main__':
    test_can_partition()
