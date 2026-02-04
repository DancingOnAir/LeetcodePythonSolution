from typing import List


class Solution:
    class UF(object):
        def __init__(self, n, m):
            self.parent = list(range(n))
            self.sz = [1] * n
            self.cnt = m

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
            if self.sz[rp] < self.sz[rq]:
                self.parent[rp] = rq
                self.sz[rq] += self.sz[rp]
            else:
                self.parent[rq] = rp
                self.sz[rp] += self.sz[rq]
            self.cnt -= 1

    def closedIsland1(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = sum(1 for i in range(row) for j in range(col) if grid[i][j] == 0)
        uf = Solution.UF(row * col, res)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    continue

                idx = i * col + j
                if i > 0 and grid[i - 1][j] == 0:
                    uf.unite(idx - col, idx)
                if j > 0 and grid[i][j - 1] == 0:
                    uf.unite(idx - 1, idx)

        opened_island = set()
        for i in range(row):
            if grid[i][0] == 0:
                opened_island.add(uf.find(i * col))
            if grid[i][col - 1] == 0:
                opened_island.add(uf.find(i * col + col - 1))

        for j in range(col):
            if grid[0][j] == 0:
                opened_island.add(uf.find(j))
            if grid[row - 1][j] == 0:
                opened_island.add(uf.find((row - 1) * col + j))
        return uf.cnt - len(opened_island)

    class UF2(object):
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

    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = Solution.UF2(m, n)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if not grid[i][j]:
                    for r, c in (i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j):
                        if not grid[r][c]:
                            uf.unite(i * n + j, r * n + c)
        return sum(not grid[i][j] and uf.parent[i * n + j] == i * n + j for i in range(1, m - 1) for j in range(1, n - 1))


def test_closed_island():
    solution = Solution()

    assert solution.closedIsland(
        [[0, 1, 1, 1, 0], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]]) == 1, 'wrong result'
    assert solution.closedIsland(
        [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 0]]) == 2, 'wrong result'
    assert solution.closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]) == 1, 'wrong result'
    assert solution.closedIsland([[1, 1, 1, 1, 1, 1, 1],
                                  [1, 0, 0, 0, 0, 0, 1],
                                  [1, 0, 1, 1, 1, 0, 1],
                                  [1, 0, 1, 0, 1, 0, 1],
                                  [1, 0, 1, 1, 1, 0, 1],
                                  [1, 0, 0, 0, 0, 0, 1],
                                  [1, 1, 1, 1, 1, 1, 1]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_closed_island()
