from typing import List
from functools import lru_cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        @lru_cache(None)
        def dfs(i, arr):
            if i < 0:
                return 0

            return max(dfs(i - 1, arr), dfs(i - 2, arr) + arr[i])
        return max(dfs(n - 2, tuple(nums[1:])), dfs(n - 2, tuple(nums[:-1])))


def test_rob():
    solution = Solution()
    assert solution.rob([2, 3, 2]) == 3, 'wrong result'
    assert solution.rob([1, 2, 3, 1]) == 4, 'wrong result'
    assert solution.rob([1, 2, 3]) == 3, 'wrong result'


if __name__ == '__main__':
    test_rob()
