from typing import List
from sortedcontainers import SortedList


class UnionFind:
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


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c + 1)
        for p, q in connections:
            uf.unite(p, q)

        m = [SortedList() for _ in range(c + 1)]
        for i in range(1, c + 1):
            m[uf.find(i)].add(i)

        res = []
        for i, x in queries:
            root = uf.find(x)
            if i == 1:
                if x in m[root]:
                    res.append(x)
                elif len(m[root]):
                    res.append(m[root][0])
                else:
                    res.append(-1)
            else:
                m[root].discard(x)
        return res


def test_process_queries():
    solution = Solution()
    assert solution.processQueries(11, [[10,2],[10,8],[6,5],[1,5],[6,8],[6,4],[7,3],[7,9],[5,10],[3,2],[8,11]], [[2,9],[2,8],[1,8],[1,10],[2,9],[1,9]]) == [1,10,1], 'wrong result'
    assert solution.processQueries(5, [[1,2],[2,3],[3,4],[4,5]], [[1,3],[2,1],[1,1],[2,2],[1,2]]) == [3,2,3], 'wrong result'
    assert solution.processQueries(3, [], [[1,1],[2,1],[1,1]]) == [1,-1], 'wrong result'


if __name__ == '__main__':
    test_process_queries()
