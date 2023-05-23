from typing import List
from functools import lru_cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        @lru_cache(None)
        def dfs(i, stop):
            if i < stop:
                return 0
            if i == stop:
                return nums[stop]

            return max(dfs(i - 1, stop), dfs(i - 2, stop) + nums[i])
        return max(dfs(n - 1, 1), dfs(n - 2, 0))


def test_rob():
    solution = Solution()
    assert solution.rob([2, 3, 2]) == 3, 'wrong result'
    assert solution.rob([1, 2, 3, 1]) == 4, 'wrong result'
    assert solution.rob([1, 2, 3]) == 3, 'wrong result'


if __name__ == '__main__':
    test_rob()
