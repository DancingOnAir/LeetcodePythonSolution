from typing import List
from itertools import accumulate


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                res = max(res, grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1])
        return res

    def maxSum1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pre_sum = [[] for _ in range(m)]
        for i in range(m):
            pre_sum[i] = [0] + list(accumulate(grid[i]))

        res = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                res = max(res, pre_sum[i - 1][j + 2] - pre_sum[i - 1][j - 1] + grid[i][j] + pre_sum[i + 1][j + 2] - pre_sum[i + 1][j - 1])
        return res


def test_max_sum():
    solution = Solution()
    assert solution.maxSum([[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]) == 30, 'wrong result'
    assert solution.maxSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 35, 'wrong result'


if __name__ == '__main__':
    test_max_sum()
