from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


def test_change():
    solution = Solution()
    assert solution.change(5, [1, 2, 5]) == 4, 'wrong result'
    assert solution.change(3, [2]) == 0, 'wrong result'
    assert solution.change(10, [10]) == 1, 'wrong result'


if __name__ == '__main__':
    test_change()
