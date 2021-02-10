from typing import List
from collections import Counter


class Solution:
    # dp[i][j] = max weight from first i stones, capacity is j,
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        if 1 == n:
            return stones[0]

        total = sum(stones)
        capacity = total >> 1
        dp = [[0] * (capacity + 1) for _ in range(n)]
        for i in range(n):
            for j in range(capacity + 1):
                if j < stones[i]:
                    if i == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if i == 0:
                        dp[i][j] = stones[i]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i]] + stones[i])
        return total - 2 * dp[n - 1][capacity]


def test_last_stone_weight_ii():
    solution = Solution()
    assert solution.lastStoneWeightII([2, 7, 4, 1, 8, 1]) == 1, 'wrong result'
    assert solution.lastStoneWeightII([100, 1, 10]) == 89, 'wrong result'


if __name__ == '__main__':
    test_last_stone_weight_ii()
