from typing import List


class Solution:
    class UF(object):
        def __init__(self, r, c):
            self.row = r
            self.col = c
            self.parent = list(range(r * c))
            self.sz = [1] * (r * c)
            self.left = [0] * r * c
            self.right = [0] * r * c
            for i in range(r):
                for j in range(c):
                    self.left[i * c + j] = j
                    self.right[i * c + j] = j

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
                rp, rq = rq, rp

            self.parent[rq] = rp
            self.sz[rp] += self.sz[rq]
            self.left[rp] = min(self.left[rp], self.left[rq])
            self.right[rp] = max(self.right[rp], self.right[rq])

            return True

        def isConnected(self, p, q):
            return self.find(p) == self.find(q)

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def neighbors(r, c):
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if row > r + dr >= 0 <= c + dc < col and (dr, dc) != (0, 0):
                        yield r + dr, c + dc

        uf = Solution.UF(row, col)
        # save water records
        seen = set()

        for i in range(len(cells)):
            x, y = cells[i][0] - 1, cells[i][1] - 1

            for r, c in neighbors(x, y):
                if (r, c) in seen:
                    uf.unite(x * col + y, r * col + c)
                    p = uf.find(r * col + c)
                    if uf.left[p] == 0 and uf.right[p] == col - 1:
                        return i

            seen.add((x, y))
        return row * col


def test_latest_day_to_cross():
    solution = Solution()

    assert solution.latestDayToCross(2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]) == 2, 'wrong result'
    assert solution.latestDayToCross(2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]]) == 1, 'wrong result'
    assert solution.latestDayToCross(3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]) == 3, 'wrong result'


if __name__ == '__main__':
    test_latest_day_to_cross()
