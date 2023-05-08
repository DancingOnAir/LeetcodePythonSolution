from typing import List
from math import inf


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [0x3f3f3f] * amount
        for x in coins:
            for c in range(x, amount + 1):
                dp[c] = min(dp[c], dp[c - x] + 1)

        res = dp[amount]
        return res if res < 0x3f3f3f else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # dp前i个coins组成amount为c的时候需要最少的数量
        dp = [[inf] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i, x in enumerate(coins):
            for c in range(amount + 1):
                if c < x:
                    dp[i + 1][c] = dp[i][c]
                else:
                    dp[i + 1][c] = min(dp[i][c], dp[i + 1][c - x] + 1)

        res = dp[n][amount]
        return res if res < inf else -1

    def coinChange1(self, coins: List[int], amount: int) -> int:
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
