from typing import List


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

        def connnected(self, p, q):
            rp = self.find(p)
            rq = self.find(q)
            return rp == rq

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        edges = list()
        for i in range(row):
            for j in range(col):
                idx = i * col + j
                if i > 0:
                    edges.append((idx - col, idx, abs(heights[i][j] - heights[i - 1][j])))
                if j > 0:
                    edges.append((idx - 1, idx, abs(heights[i][j] - heights[i][j - 1])))

        edges.sort(key=lambda x: x[2])

        uf = Solution.UF(row * col)
        res = 0
        for i, j, v in edges:
            uf.unite(i, j)
            if uf.connnected(0, row * col - 1):
                res = v
                break
        return res


def test_minimum_effort_path():
    solution = Solution()

    assert solution.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2, 'wrong result'
    assert solution.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1, 'wrong result'
    assert solution.minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_effort_path()
