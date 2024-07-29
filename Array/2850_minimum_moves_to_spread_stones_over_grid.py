from typing import List
from itertools import product, permutations


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        dist = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        zeros, spares = [], []
        for i, j in product(range(3), range(3)):
            stones = grid[i][j]
            if stones == 0:
                zeros.append([i, j])
            elif stones > 1:
                spares.extend([[i, j]] * (stones - 1))

        return min(sum(map(dist, zeros, per)) for per in permutations(spares))


def test_minimum_moves():
    solution = Solution()
    assert solution.minimumMoves([[1, 1, 0], [1, 1, 1], [1, 2, 1]]) == 3, 'wrong result'
    assert solution.minimumMoves([[1, 3, 0], [1, 0, 0], [1, 0, 3]]) == 4, 'wrong result'


if __name__ == '__main__':
    test_minimum_moves()
