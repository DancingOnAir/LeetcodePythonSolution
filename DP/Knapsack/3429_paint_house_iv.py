from typing import List
from functools import lru_cache


class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i, pre_j, pre_k):
            if i < 0:
                return 0
            res = float('inf')
            for j, c1 in enumerate(cost[i]):
                if j == pre_j:
                    continue
                for k, c2 in enumerate(cost[n - 1 - i]):
                    if k == pre_k or k == j:
                        continue
                    res = min(res, dfs(i - 1, j, k) + c1 + c2)
            return res
        return dfs(n // 2 - 1, 3, 3)


def test_min_cost():
    solution = Solution()
    assert solution.minCost(4, [[3, 5, 7], [6, 2, 9], [4, 8, 1], [7, 3, 5]]) == 9, 'wrong result'
    assert solution.minCost(6, [[2, 4, 6], [5, 3, 8], [7, 1, 9], [4, 6, 2], [3, 5, 7], [8, 2, 4]]) == 18, 'wrong result'


if __name__ == '__main__':
    test_min_cost()
