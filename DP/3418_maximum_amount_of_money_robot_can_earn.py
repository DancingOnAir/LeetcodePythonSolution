from typing import List
from heapq import heappop, heappush
from functools import lru_cache


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i, j, k):
            if i < 0 or j < 0:
                return float('-inf')

            val = coins[i][j]
            if i == 0 and j == 0:
                return max(val, 0) if k else val
            # 选
            res = max(dfs(i - 1, j, k), dfs(i, j - 1, k)) + val
            # 不选
            if k and val < 0:
                res = max(res, dfs(i - 1, j, k - 1), dfs(i, j - 1, k - 1))
            return res

        return dfs(len(coins) - 1, len(coins[0]) - 1, 2)


def test_maximum_amount():
    solution = Solution()
    assert solution.maximumAmount([[0, 1, -1], [1, -2, 3], [2, -3, 4]]) == 8, 'wrong result'
    assert solution.maximumAmount([[10, 10, 10], [10, 10, 10]]) == 40, 'wrong result'


if __name__ == '__main__':
    test_maximum_amount()
