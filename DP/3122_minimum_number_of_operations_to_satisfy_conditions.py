from typing import List
from collections import defaultdict


class Solution:
    # https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/solutions/5052486/dp-top-down-bottom-up-and-monster-style/
    def minimumOperations(self, grid: List[List[int]]) -> int:
        def dfs(i, pre):
            if i == n:
                return 0
            if dp[i][pre] == 0:
                for v in range(10):
                    if i == 0 or v != pre:
                        dp[i][pre] = max(dp[i][pre], cnt[i][v] + dfs(i + 1, v))
            return dp[i][pre]

        cnt, dp = [[0] * 10 for _ in range(1000)], [[0] * 10 for _ in range(1000)]

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                cnt[j][grid[i][j]] += 1
        return m * n - dfs(0, 0)


def test_minimum_operations():
    solution = Solution()
    assert solution.minimumOperations([[1, 0, 2], [1, 0, 2]]) == 0, 'wrong result'
    assert solution.minimumOperations([[1, 1, 1], [0, 0, 0]]) == 3, 'wrong result'
    assert solution.minimumOperations([[1], [2], [3]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_minimum_operations()
