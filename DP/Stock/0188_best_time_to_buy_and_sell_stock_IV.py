from typing import List
from math import inf
from functools import lru_cache


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dfs(i, j, hold):
            if j < 0:
                return -inf
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])
            return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i])

        return dfs(n - 1, k, False)


def test_max_profit():
    solution = Solution()
    assert solution.maxProfit(2, [2, 4, 1]) == 2, 'wrong result'
    assert solution.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7, 'wrong result'


if __name__ == '__main__':
    test_max_profit()
