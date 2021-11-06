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
                return False

            if self.sz[rp] < self.sz[rq]:
                self.parent[rp] = rq
                self.sz[rq] += self.sz[rp]
            else:
                self.parent[rq] = rp
                self.sz[rp] += self.sz[rq]

            self.cnt -= 1
            return True

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = Solution.UF(n + 1)
        in_degree = [-1] * (n + 1)

        res = list()
        for i, (u, v) in enumerate(edges):
            if in_degree[v] == -1:
                in_degree[v] = i
            else:
                res.append(edges[in_degree[v]])
                res.append([u, v])
                edges[i][1] = 0

        for i, (u, v) in enumerate(edges):
            if not uf.unite(u, v):
                if not len(res):
                    return [u, v]
                return res[0]
        return res[1]

        # for u, v in edges:
        #     in_degree[v - 1] += 1
        #     if in_degree[v - 1] > 1:
        #         return [u, v]
        #     if not uf.unite(u - 1, v - 1):
        #         return [u, v]


def test_find_redundant_directed_connection():
    solution = Solution()

    assert solution.findRedundantDirectedConnection([[2, 1], [3, 1], [4, 2], [1, 4]]) == [2, 1], 'wrong result'
    assert solution.findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3], 'wrong result'
    assert solution.findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]) == [4, 1], 'wrong result'


if __name__ == '__main__':
    test_find_redundant_directed_connection()
