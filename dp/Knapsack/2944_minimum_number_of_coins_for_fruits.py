from typing import List
from functools import lru_cache


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dfs(i):
            if i * 2 >= n:
                return prices[i - 1]
            return min(dfs(j) for j in range(i + 1, i * 2 + 2)) + prices[i - 1]
        return dfs(1)


def test_minimum_coins():
    solution = Solution()
    assert solution.minimumCoins([3, 1, 2]) == 4, 'wrong result'
    assert solution.minimumCoins([1, 10, 1, 1]) == 2, 'wrong result'


if __name__ == '__main__':
    test_minimum_coins()
