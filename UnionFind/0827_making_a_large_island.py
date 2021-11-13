from typing import List
from collections import defaultdict


class Solution:
    class UF(object):
        def __init__(self, n):
            self.parent = list(range(n))
            self.sz = [1] * n
            self.cnt = n

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

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = Solution.UF(n * n)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            uf.unite(i * n + j, x * n + y)

        idx_to_area = defaultdict(int)
        idx_to_neighbor = defaultdict(set)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    p = uf.find(i * n + j)

                    idx_to_area[p] += 1
                    for x, y in (i, j - 2), (i, j + 2), (i - 2, j), (i + 2, j), (i + 1, j + 1), (i + 1, j - 1), (
                    i - 1, j + 1), (i - 1, j - 1):
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            q = uf.find(x * n + y)
                            if p != q:
                                idx_to_neighbor[p].add(q)

        if not idx_to_neighbor:
            return min((max(idx_to_area.values()) if idx_to_area else 0) + 1, n * n)

        res = 0
        for p, qs in idx_to_neighbor.items():
            for q in qs:
                res = max(res, idx_to_area[p] + idx_to_area[q] + 1)
        return res


def test_largest_island():
    solution = Solution()

    assert solution.largestIsland([[0, 0], [0, 0]]) == 1, 'wrong result'
    assert solution.largestIsland([[1, 0], [0, 1]]) == 3, 'wrong result'
    assert solution.largestIsland([[1, 1], [1, 0]]) == 4, 'wrong result'
    assert solution.largestIsland([[1, 1], [1, 1]]) == 4, 'wrong result'


if __name__ == '__main__':
    test_largest_island()
