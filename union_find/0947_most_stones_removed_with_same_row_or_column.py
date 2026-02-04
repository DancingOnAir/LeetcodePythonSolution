from collections import defaultdict
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
                self.sz[rq] += self.sz[rp]
            self.cnt -= 1

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = Solution.UF(n)

        xd = defaultdict(list)
        yd = defaultdict(list)
        for i, (x, y) in enumerate(stones):
            if x not in xd:
                xd[x].append(i)
            else:
                uf.unite(xd[x][0], i)

            if y not in yd:
                yd[y].append(i)
            else:
                uf.unite(yd[y][0], i)

        return n - uf.cnt


def test_remove_stones():
    solution = Solution()

    assert solution.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]) == 5, 'wrong result'
    assert solution.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]) == 3, 'wrong result'


if __name__ == '__main__':
    test_remove_stones()
