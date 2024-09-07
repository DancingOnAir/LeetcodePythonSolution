from typing import List
from collections import defaultdict


class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.n = len(grid)
        self.grid = grid
        self.g = defaultdict(list)
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                self.g[c] = [i, j]

    def adjacentSum(self, value: int) -> int:
        res = 0
        x, y = self.g[value]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x + dx < self.n and 0 <= y + dy < self.n:
                res += self.grid[x + dx][y + dy]
        return res

    def diagonalSum(self, value: int) -> int:
        res = 0
        x, y = self.g[value]
        for dx, dy in [(-1, 1), (-1, -1), (1, -1), (1, 1)]:
            if 0 <= x + dx < self.n and 0 <= y + dy < self.n:
                res += self.grid[x + dx][y + dy]
        return res

# Your NeighborSum object will be instantiated and called as such:
def test_neighbor_sum():
    obj = NeighborSum([[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]])
    assert obj.adjacentSum(15) == 23, 'wrong result'
    assert obj.diagonalSum(9) == 45, 'wrong result'


if __name__ == '__main__':
    test_neighbor_sum()
