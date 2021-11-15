from typing import List


class Solution:
    class UF(object):
        def __init__(self, r, c):
            self.row = r
            self.col = c
            self.parent = list(range(r * c))
            self.sz = [1] * (r * c)

        def find(self, p):
            while p != self.parent[p]:
                self.parent[p] = self.parent[self.parent[p]]
                p = self.parent[p]

            return p

        def unite(self, p, q):
            rp = self.find(p)
            rq = self.find(q)

            if rp == rq:
                return False

            if self.sz[rp] < self.sz[rq]:
                self.parent[rp] = rq
                self.sz[rq] += self.sz[rp]
            else:
                self.parent[rq] = rp
                self.sz[rp] += self.sz[rq]

            return True

        def isConnected(self, p, q):
            return self.find(p) == self.find(q)

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def neighours(r, c):
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if row > r + dr >= 0 <= c + dc < col and (dr, dc) != (0, 0):
                        yield r + dr, c + dc

        uf = Solution.UF(row, col)
        grid = [[0] * col for _ in range(row)]
        lefts = set()
        rights = set()

        for i in range(len(cells)):
            x, y = cells[i]
            x -= 1
            y -= 1

            grid[x][y] = 1
            if y == 0:
                lefts.add((x, y))
            elif y == col - 1:
                rights.add((x, y))

            for r, c in neighours(x, y):
                if grid[r][c] == 1:
                    uf.unite(x * col + y, r * col + c)

            for l in lefts:
                for r in rights:
                    if uf.isConnected(l[0] * col + l[1], r[0] * col + r[1]):
                        return i

        return len(cells)


def test_latest_day_to_cross():
    solution = Solution()

    assert solution.latestDayToCross(2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]) == 2, 'wrong result'
    assert solution.latestDayToCross(2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]]) == 1, 'wrong result'
    assert solution.latestDayToCross(3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]) == 3, 'wrong result'


if __name__ == '__main__':
    test_latest_day_to_cross()
