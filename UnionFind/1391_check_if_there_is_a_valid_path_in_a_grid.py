from typing import List


class Solution:
    class UF(object):
        def __init__(self, n):
            self.parent = list(range(n))
            self.sz = [1] * n

        def find(self, p):
            while p != self.parent[p]:
                p = self.parent[p]

            return p

        def unite(self, p, q):
            rp = self.find(p)
            rq = self.find(q)

            if rp == rq:
                return

            if self.sz[rp] < self.sz[rq]:
                self.parent[rp] = rq
                self.sz[rq] += self.sz[rq]
            else:
                self.parent[rq] = rp
                self.sz[rp] += self.sz[rq]

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        match = {1: [{1, 3, 5}, {}], 2: [{}, {2, 5, 6}], 3: [{}, {2, 5, 6}], 4: [{1, 3, 5}, {2, 5, 6}], 5: [{}, {}], 6: [{1, 3, 5}, {}]}
        row = len(grid)
        col = len(grid[0])
        uf = Solution.UF(row * 2 * col * 2)
        top = {2, 5, 6}
        bottom = {2, 3, 4}
        left = {1, 3, 5}
        right = {1, 4, 6}

        for i in range(row):
            for j in range(col):
                idx = 2 * i * 2 * col + 2 * j
                if i > 0 and grid[i][j] in top:
                    uf.unite(idx, idx - 2 * col)
                if grid[i][j] in bottom:
                    uf.unite(idx, idx + 2 * col)
                if j > 0 and grid[i][j] in left:
                    uf.unite(idx, idx - 1)
                if grid[i][j] in right:
                    uf.unite(idx, idx + 1)

        return uf.find(0) == uf.find(2 * (row - 1) * col + 2 * (col - 1))


def test_has_valid_path():
    solution = Solution()

    assert solution.hasValidPath([[2, 4, 3], [6, 5, 2]]), 'wrong result'
    assert not solution.hasValidPath([[1, 2, 1], [1, 2, 1]]), 'wrong result'
    assert not solution.hasValidPath([[1, 1, 2]]), 'wrong result'
    assert solution.hasValidPath([[1, 1, 1, 1, 1, 1, 3]]), 'wrong result'
    assert solution.hasValidPath([[2], [2], [2], [2], [2], [2], [6]]), 'wrong result'


if __name__ == '__main__':
    test_has_valid_path()
