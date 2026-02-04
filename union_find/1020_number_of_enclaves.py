from typing import List


class Solution:
    class UF(object):
        def __init__(self, r, c):
            self.row = r
            self.col = c
            self.parent = list(range(r * c))

        def find(self, p):
            while p != self.parent[p]:
                self.parent[p] = self.parent[self.parent[p]]
                p = self.parent[p]
            return p

        def unite(self, p, q):
            rp = self.find(p)
            rq = self.find(q)
            if rp == rq:
                return

            if self.is_boundary(rq):
                self.parent[rp] = rq
            else:
                self.parent[rq] = rp

        def is_boundary(self, p):
            return p // self.col in (0, self.row - 1) or p % self.col in (0, self.col - 1)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        uf = Solution.UF(r, c)

        for i in range(1, r - 1):
            for j in range(1, c - 1):
                if grid[i][j]:
                    for x, y in (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                        if grid[x][y]:
                            uf.unite(i * c + j, x * c + y)
        return sum(grid[i][j] and not uf.is_boundary(uf.find(i * c + j)) for i in range(1, r - 1) for j in range(1, c - 1))


def test_num_enclaves():
    solution = Solution()

    assert solution.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) == 3, 'wrong result'
    assert solution.numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_num_enclaves()
