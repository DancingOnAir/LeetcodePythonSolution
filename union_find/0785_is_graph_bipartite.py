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
                return

            if self.sz[rp] < self.sz[rq]:
                self.parent[rp] = rq
                self.sz[rq] += self.sz[rp]
            else:
                self.parent[rq] = rp
                self.sz[rp] += self.sz[rq]

    def isBipartite(self, graph: List[List[int]]) -> bool:
        uf = Solution.UF(len(graph))
        for i, vertex in enumerate(graph):
            for j in range(len(vertex)):
                if uf.find(i) == uf.find(vertex[j]):
                    return False
                uf.unite(vertex[0], vertex[j])
        return True


def test_is_bipartite():
    solution = Solution()

    assert not solution.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]), 'wrong result'
    assert solution.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]), 'wrong result'


if __name__ == '__main__':
    test_is_bipartite()
