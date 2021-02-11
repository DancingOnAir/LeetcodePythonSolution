from typing import List
from collections import Counter


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        pass

    # dp, loop for all possible sum
    def lastStoneWeightII3(self, stones: List[int]) -> int:
        dp = {0}
        total = sum(stones)
        for s in stones:
            dp |= {s + x for x in dp}
        return min(abs(total - x * 2) for x in dp)

    # 0-1 knapsack problem dp[i] = max weight when capacity is i
    def lastStoneWeightII2(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        capacity = total >> 1

        dp = [0] * (capacity + 1)
        for i in range(n):
            for j in range(capacity, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return total - 2 * dp[-1]

    # 0-1 knapsack problem, dp[i][j] = max weight from first i stones, capacity is j,
    def lastStoneWeightII1(self, stones: List[int]) -> int:
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
