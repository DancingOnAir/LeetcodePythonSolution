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
            return True

    # unicode union find
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        tree = ''.join(map(chr, range(1001)))
        for u, v in edges:
            if tree[u] == tree[v]:
                return [u, v]
            tree = tree.replace(tree[u], tree[v])

    # union find
    def findRedundantConnection1(self, edges: List[List[int]]) -> List[int]:
        uf = Solution.UF(len(edges) + 1)
        for i, j in edges:
            if not uf.unite(i, j):
                return [i, j]


def test_find_redundant_connection():
    solution = Solution()

    assert solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3], 'wrong result'
    assert solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4], 'wrong result'


if __name__ == '__main__':
    test_find_redundant_connection()
