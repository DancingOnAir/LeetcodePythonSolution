from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
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
                    dp[i][i + d] = max(pre_sum[i + 1][i + d] - dp[i + 1][i + d], pre_sum[i][i + d - 1] - dp[i][i + d - 1])
        return dp[0][-1]


def test_stone_game_vii():
    solution = Solution()
    assert solution.stoneGameVII([5,3,1,4,2]) == 6, 'wrong result'


if __name__ == '__main__':
    test_stone_game_vii()
