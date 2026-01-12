from typing import List
from itertools import accumulate


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return 0

        pre_sum = [0] + list(accumulate(stones))

        def dfs(i: int, j: int) -> int:
            if i == j:
                return 0
            if dp[i][j] == 0:
                total = pre_sum[j + 1] - pre_sum[i]
                dp[i][j] = max(total - stones[i] - dfs(i + 1, j), total - stones[j] - dfs(i, j - 1))
            return dp[i][j]

        dp = [[0] * n for _ in range(n)]
        return dfs(0, n - 1)

    def stoneGameVII1(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return 0

        pre_sum = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    pre_sum[i][j] = stones[i]
                else:
                    pre_sum[i][j] = stones[j] + pre_sum[i][j - 1]

        dp = [[0] * n for _ in range(n)]
        for d in range(1, n):
            for i in range(n - d):
                if d == 1:
                    dp[i][i + d] = max(stones[i], stones[i + d])
                else:
                    dp[i][i + d] = max(pre_sum[i + 1][i + d] - dp[i + 1][i + d],
                                       pre_sum[i][i + d - 1] - dp[i][i + d - 1])
        return dp[0][-1]


def test_stone_game_vii():
    solution = Solution()
    assert solution.stoneGameVII([5, 3, 1, 4, 2]) == 6, 'wrong result'


if __name__ == '__main__':
    test_stone_game_vii()
