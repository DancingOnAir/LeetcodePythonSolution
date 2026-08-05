class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        return True


def test_stone_game():
    solution = Solution()
    assert solution.stoneGame([5,3,4,5]), 'wrong result'
    assert solution.stoneGame([3,7,2,3]), 'wrong result'


if __name__ == '__main__':
    test_stone_game()

