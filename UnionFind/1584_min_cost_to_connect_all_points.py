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

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def cal_manhattan_distance(pt1, pt2):
            return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

        n = len(points)
        edges = list()
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((i, j, cal_manhattan_distance(points[i], points[j])))
        edges.sort(key=lambda x: x[2])

        uf = Solution.UF(n)
        res = 0
        for i, j, v in edges:
            uf.unite(i, j)

            if uf.cnt < n:
                n -= 1
                res += v

            if uf.cnt == 1:
                break
        return res


def test_min_cost_connect_points():
    solution = Solution()

    assert solution.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20, 'wrong result'
    assert solution.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18, 'wrong result'
    assert solution.minCostConnectPoints([[0, 0], [1, 1], [1, 0], [-1, 1]]) == 4, 'wrong result'
    assert solution.minCostConnectPoints([[-1000000, -1000000], [1000000, 1000000]]) == 4000000, 'wrong result'
    assert solution.minCostConnectPoints([[0, 0]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_cost_connect_points()
