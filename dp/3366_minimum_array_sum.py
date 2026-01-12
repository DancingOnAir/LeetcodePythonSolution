from typing import List
from functools import lru_cache
from math import ceil


class Solution:
    # dp concise version
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i, x, y):
            if i == n:
                return 0
            val = nums[i]
            res = dfs(i + 1, x, y) + nums[i]
            if x:
                res = min(res, dfs(i + 1, x - 1, y) + (val + 1) // 2)
            if y and val >= k:
                res = min(res, dfs(i + 1, x, y - 1) + val - k)
                if x:
                    tmp = (val + 1) // 2 - k if (val + 1) // 2 >= k else (val - k + 1) // 2
                    res = min(res, dfs(i + 1, x - 1, y - 1) + tmp)
            return res

        return dfs(0, op1, op2)

    # dp
    def minArraySum1(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i, x, y):
            if i == n:
                return 0

            if x == 0 and y == 0:
                return dfs(i + 1, x, y) + nums[i]
            else:
                res = dfs(i + 1, x, y) + nums[i]
                if x > 0:
                    res = min(res, dfs(i+1, x-1, y) + ceil(nums[i]/2))
                if y > 0 and nums[i] >= k:
                    res = min(res, dfs(i+1, x, y-1) + (nums[i] - k))
                if x > 0 and y > 0:
                    if nums[i] >= k:
                        res = min(res, dfs(i+1, x-1, y-1) + ceil((nums[i] - k)/2))
                    if ceil(nums[i]/2) >= k:
                        res = min(res, dfs(i+1, x-1, y-1) + (ceil(nums[i]/2) - k))
                return res

        return dfs(0, op1, op2)


def test_min_array_sum():
    solution = Solution()
    assert solution.minArraySum([3], k=6, op1=0, op2=1) == 3, 'wrong result'
    assert solution.minArraySum([2, 8, 3, 19, 3], k=3, op1=1, op2=1) == 23, 'wrong result'
    assert solution.minArraySum([2, 4, 3], k=3, op1=2, op2=1) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_array_sum()

