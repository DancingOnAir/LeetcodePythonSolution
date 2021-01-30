from typing import List


class Solution:
    # https://leetcode.com/problems/stone-game/discuss/154610/DP-or-Just-return-true
    # Alex is first to pick pile.
    # piles.length is even, and this lead to an interesting fact:
    # Alex can always pick odd piles or always pick even piles!
    def stoneGame(self, piles: List[int]) -> bool:
        return True


def test_stone_game():
    solution = Solution()
    assert solution.stoneGame([5, 3, 4, 5]), 'wrong result'


if __name__ == '__main__':
    test_stone_game()
