from typing import List
from math import inf
from functools import lru_cache


class Solution:
    # dfs + cache
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]

        @lru_cache(None)
        def dfs(i, j):
            if i + 1 == j:
                return 0
            res = inf
            for k in range(i, j + 1):
                res = min(res, dfs(i, k - 1) + dfs(k + 1, j) + cuts[j + 1] - cuts[i - 1])
            return res
        return dfs(1, len(cuts) - 1)


def test_min_cost():
    solution = Solution()
    assert solution.minCost(7, [1, 3, 4, 5]) == 16, 'wrong result'
    assert solution.minCost(9, [5, 6, 1, 4, 2]) == 22, 'wrong result'


if __name__ == '__main__':
    test_min_cost()
