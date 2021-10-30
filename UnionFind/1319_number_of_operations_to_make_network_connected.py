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

        def union(self, p, q):
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

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        m = len(connections)
        if m < n - 1:
            return -1

        uf = Solution.UF(n)
        for i in range(m):
            uf.union(connections[i][0], connections[i][1])

        group = set()
        for i in range(n):
            group.add(uf.find(uf.parent[i]))
        return len(group) - 1


def test_make_connected():
    solution = Solution()

    assert solution.makeConnected(4, [[0, 1], [0, 2], [1, 2]]) == 1, 'wrong result'
    assert solution.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]) == 2, 'wrong result'
    assert solution.makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]) == -1, 'wrong result'
    assert solution.makeConnected(5, [[0, 1], [0, 2], [3, 4], [2, 3]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_make_connected()
