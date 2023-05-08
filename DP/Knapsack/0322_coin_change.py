from typing import List
from math import inf


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        def dfs(i, c):
            if i < 0:
                return 0 if c == 0 else inf

            if c < coins[i]:
                return dfs(i - 1, c)
            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)

        res = dfs(n - 1, amount)
        return res if res < inf else -1


def test_coin_change():
    solution = Solution()
    assert solution.coinChange([1,2,5], 11) == 3, 'wrong result'
    assert solution.coinChange([2], 3) == -1, 'wrong result'
    assert solution.coinChange([1], 0) == 0, 'wrong result'


if __name__ == '__main__':
    test_coin_change()
