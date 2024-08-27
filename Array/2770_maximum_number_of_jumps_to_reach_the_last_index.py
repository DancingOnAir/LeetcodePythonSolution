from typing import List
from functools import lru_cache


class Solution:
    def maximumJumps1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if abs(nums[j] - nums[i]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)
        return -1 if dp[-1] < 0 else dp[-1]

    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i):
            if i == n - 1:
                return 0
            res = float('-inf')
            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) <= target:
                    res = max(res, dfs(j) + 1)
            return res

        ans = dfs(0)
        return ans if ans >= 0 else -1


def test_maximum_jumps():
    solution = Solution()
    assert solution.maximumJumps([0, 1, 3, 2, 4], 1) == -1, 'wrong result'
    assert solution.maximumJumps([1, 3, 6, 4, 1, 2], 2) == 3, 'wrong result'
    assert solution.maximumJumps([1, 3, 6, 4, 1, 2], 3) == 5, 'wrong result'
    assert solution.maximumJumps([1, 3, 6, 4, 1, 2], 0) == -1, 'wrong result'


if __name__ == '__main__':
    test_maximum_jumps()
