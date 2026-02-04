from typing import List
from collections import defaultdict


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

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        m = defaultdict(list)
        for a, b in dislikes:
            m[a].append(b)
            m[b].append(a)

        uf = Solution.UF(n)
        for a, bs in m.items():
            for i in range(len(bs)):
                if uf.find(a - 1) == uf.find(bs[i] - 1):
                    return False
                uf.unite(bs[0] - 1, bs[i] - 1)
        return True


def test_possible_bipartition():
    solution = Solution()

    assert solution.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]]), 'wrong result'
    assert not solution.possibleBipartition(3, [[1, 2], [1, 3], [2, 3]]), 'wrong result'
    assert not solution.possibleBipartition(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]), 'wrong result'


if __name__ == '__main__':
    test_possible_bipartition()

