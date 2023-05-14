from typing import List
from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def dfs(i, hold):
            if i < 0:
                return -inf if hold else 0

            if hold:
                return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i])
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
        return dfs(n - 1, False)


def test_max_profit():
    solution = Solution()
    assert solution.maxProfit([1, 2, 3, 0, 2]) == 3, 'wrong result'
    assert solution.maxProfit([1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_profit()
