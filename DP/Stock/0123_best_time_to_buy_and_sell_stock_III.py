from typing import List
from functools import lru_cache


class Solution:
    # dfs
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dfs(i, j, hold):
            if j < 0:
                return float('-inf')
            if i < 0:
                return float('-inf') if hold else 0
            if hold:
                return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])
            return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i])
        return dfs(n - 1, 2, False)


def test_max_profit():
    solution = Solution()
    assert solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6, 'wrong result'
    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4, 'wrong result'
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_profit()
