class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (n // 2 * ((m + 1) // 2)) + ((n + 1) // 2 * (m // 2))


def test_flower_game():
    solution = Solution()
    assert solution.flowerGame(4, 4) == 8, 'wrong result'
    assert solution.flowerGame(3, 2) == 3, 'wrong result'
    assert solution.flowerGame(1, 1) == 0, 'wrong result'


if __name__ == '__main__':
    test_flower_game()
