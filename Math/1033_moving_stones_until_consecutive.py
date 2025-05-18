from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        d1, d2 = b - a - 1, c - b - 1

        if d1 == 0 and d2 == 0:
            return [0, 0]
        if d1 < 2 or d2 < 2:
            return [1, d1 + d2]
        return [2, d1 + d2]


def test_num_move_stones():
    solution = Solution()
    assert solution.numMovesStones(1, 2, 5) == [1, 2], 'wrong result'
    assert solution.numMovesStones(4, 3, 2) == [0, 0], 'wrong result'
    assert solution.numMovesStones(3, 5, 1) == [1, 2], 'wrong result'


if __name__ == '__main__':
    test_num_move_stones()
