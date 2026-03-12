from typing import List


class UF:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sz = [1] * n

    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p

    def unite(self, p, q):
        rp = self.find(p)
        rq = self.find(q)

        if rp == rq:
            return

        if self.sz[rp] < self.sz[rq]:
            self.parents[rp] = rq
            self.sz[rq] += self.sz[rp]
        else:
            self.parents[rq] = rp
            self.sz[rp] += self.sz[rq]


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        if n < 2:
            return 0

        s = list(map(set, properties))
        uf = UF(n)
        for i in range(n - 1):
            s_i = s[i]
            len_i = len(s_i)
            if len_i < k:
                continue
            for j in range(i + 1, n):
                s_j = s[j]
                len_j = len(s_j)
                if len(s_i & s_j) >= k:
                    uf.unite(i, j)

        res = set()
        for i in range(n):
            res.add(uf.find(i))
        return len(res)


def test_number_of_components():
    solution = Solution()
    assert solution.numberOfComponents([[1, 2], [1, 1], [3, 4], [4, 5], [5, 6], [7, 7]], 1) == 3, 'wrong result'
    assert solution.numberOfComponents([[1, 2, 3], [2, 3, 4], [4, 3, 5]], 2) == 1, 'wrong result'
    assert solution.numberOfComponents([[1, 1], [1, 1]], 2) == 2, 'wrong result'


if __name__ == '__main__':
    test_number_of_components()
