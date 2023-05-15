from typing import List
from functools import lru_cache
from math import inf


class Solution:
    # 看待成恰好交易一次的股票交易问题
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dfs(i, j, hold):
            if j < 0:
                return -inf
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, j, True), dfs(i - 1, j, False) - prices[i])
            return max(dfs(i - 1, j, False), dfs(i - 1, j - 1, True) + prices[i])
        return dfs(n - 1, 1, False)


def test_max_profit():
    solution = Solution()
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5, 'wrong result'
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_profit()
