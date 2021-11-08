from typing import List


class Solution:
    class UF(object):
        def __init__(self, n):
            self.parent = list(range(n))
            self.weight = [1.0] * n

        def find(self, p):
            if p != self.parent[p]:
                origin = self.parent[p]
                self.parent[p] = self.find(self.parent[p])
                self.weight[p] *= self.weight[origin]
            return self.parent[p]

            # while p != self.parent[p]:
            #     self.weight[p] *= self.weight[self.parent[p]]
            #     self.parent[p] = self.parent[self.parent[p]]
            #     p = self.parent[p]
            #
            # return p

        def unite(self, p, q, v):
            rp = self.find(p)
            rq = self.find(q)

            if rp == rq:
                return

            self.parent[rp] = rq
            self.weight[rp] = self.weight[q] * v / self.weight[p]

        def connected(self, p, q):
            rp = self.find(p)
            rq = self.find(q)

            if rp == rq:
                return self.weight[p] / self.weight[q]
            return -1.0

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        uf = Solution.UF(n * 2)

        m = dict()
        idx = 0
        for i, (x, y) in enumerate(equations):
            if x not in m:
                m[x] = idx
                idx += 1
            if y not in m:
                m[y] = idx
                idx += 1
            uf.unite(m[x], m[y], values[i])

        res = [-1.0] * len(queries)
        for i, (x, y) in enumerate(queries):
            if x in m and y in m:
                res[i] = uf.connected(m[x], m[y])
        return res


def test_calc_equation():
    solution = Solution()

    assert solution.calcEquation([["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]], [3.0, 4.0, 5.0, 6.0], [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]) == [360.00000, 0.00833, 20.00000, 1.00000, -1.00000, -1.00000], 'wrong result'
    assert solution.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                                 [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]) == [6.00000, 0.50000,
                                                                                                   -1.00000, 1.00000,
                                                                                                   -1.00000]
    assert solution.calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0],
                                 [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]) == [3.75000, 0.40000, 5.00000,
                                                                                           0.20000]
    assert solution.calcEquation([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]) == [0.50000,
                                                                                                            2.00000,
                                                                                                            -1.00000,
                                                                                                            -1.00000]


if __name__ == '__main__':
    test_calc_equation()
