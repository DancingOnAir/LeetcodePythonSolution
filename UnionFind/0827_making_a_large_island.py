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

    def largestIsland(self, grid: List[List[int]]) -> int:

        pass


def test_largest_island():
    solution = Solution()

    assert solution.largestIsland([[1, 0], [0, 1]]) == 3, 'wrong result'
    assert solution.largestIsland([[1, 1], [1, 0]]) == 4, 'wrong result'
    assert solution.largestIsland([[1, 1], [1, 1]]) == 4, 'wrong result'


if __name__ == '__main__':
    test_largest_island()

