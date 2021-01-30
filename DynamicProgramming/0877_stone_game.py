from typing import List


class Solution:
    # 2d dp
    def stoneGame(self, piles: List[int]) -> bool:
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
