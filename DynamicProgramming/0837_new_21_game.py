from typing import List


class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        pass


def test_new_21_game():
    solution = Solution()
    assert solution.new21Game(10, 1, 10) == 1.00000, 'wrong result'
    assert solution.new21Game(6, 1, 10) == 0.60000, 'wrong result'
    assert solution.new21Game(21, 17, 10) == 0.73278, 'wrong result'


if __name__ == '__main__':
    test_new_21_game()
