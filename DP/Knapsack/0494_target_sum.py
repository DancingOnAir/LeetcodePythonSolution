from typing import List
from functools import lru_cache


class Solution:
    # nums 原本所有的数之和为tot，需要添加正号的整数之和为p，那么 p - (tot - p) = target
    # 即p = (tot + target) // 2
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        target += sum(nums)
        if target < 0 or target % 2:
            return 0

        target //= 2

        @lru_cache(None)
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            if c < nums[i]:
                return dfs(i - 1, c)
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])
        return dfs(n - 1, target)


def test_find_target_sum_ways():
    solution = Solution()
    assert solution.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5, 'wrong result'
    assert solution.findTargetSumWays([1], 1) == 1, 'wrong result'


if __name__ == '__main__':
    test_find_target_sum_ways()
