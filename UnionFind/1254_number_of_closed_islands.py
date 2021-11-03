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

    def closedIsland(self, grid: List[List[int]]) -> int:
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


def test_closed_island():
    solution = Solution()

    assert solution.closedIsland(
        [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]) == 2, 'wrong result'
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
