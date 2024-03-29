from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = piles[:]
        for d in range(1, n):
            for i in range(n - d):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + d] - dp[i])
        return dp[0]

    # 2d dp
    # dp[i][j] means the biggest number of stones you can get more than opponent picking piles in piles[i] ~ piles[j].
    # You can first pick piles[i] or piles[j].
    # If you pick piles[i], your result will be piles[i] - dp[i + 1][j],
    # Notice: here is '-', not '+', coz the previous round is opponent, dp[i + 1][j] is the biggest number of the opponent can get more than you.
    # If you pick piles[j], your result will be piles[j] - dp[i][j - 1]
    def stoneGame2(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]

        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])

        return dp[0][-1] > 0

    # https://leetcode.com/problems/stone-game/discuss/154610/DP-or-Just-return-true
    # Alex is first to pick pile.
    # piles.length is even, and this lead to an interesting fact:
    # Alex can always pick odd piles or always pick even piles!
    def stoneGame1(self, piles: List[int]) -> bool:
        return True


def test_stone_game():
    solution = Solution()
    assert solution.stoneGame([5, 3, 4, 5]), 'wrong result'


if __name__ == '__main__':
    test_stone_game()
