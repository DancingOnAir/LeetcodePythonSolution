from typing import List


class Solution:
    class UF(object):
        def __init__(self, n):
            self.parent = list(range(n))
            self.sz = [1] * n

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

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = Solution.UF(len(edges) + 1)
        for i, j in edges:
            if uf.find(i) == uf.find(j):
                return [i, j]
            uf.unite(i, j)
        return [0, 0]


def test_find_redundant_connection():
    solution = Solution()

    assert solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3], 'wrong result'
    assert solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4], 'wrong result'


if __name__ == '__main__':
    test_find_redundant_connection()
