from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [0x3f3f3f3f] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != 0x3f3f3f3f else -1


def test_coin_change():
    solution = Solution()
    assert solution.coinChange([1, 2, 5], 11) == 3, 'wrong result'
    assert solution.coinChange([2], 3) == -1, 'wrong result'
    assert solution.coinChange([1], 0) == 0, 'wrong result'
    assert solution.coinChange([1], 1) == 1, 'wrong result'
    assert solution.coinChange([1], 2) == 2, 'wrong result'


if __name__ == '__main__':
    test_coin_change()
