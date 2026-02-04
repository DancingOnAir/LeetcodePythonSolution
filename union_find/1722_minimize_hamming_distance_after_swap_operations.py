from typing import List
from collections import defaultdict, Counter


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

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = Solution.UF(n)

        for x, y in allowedSwaps:
            uf.unite(x, y)

        match = defaultdict(set)
        for i in range(n):
            match[uf.find(i)].add(i)

        res = 0
        for v in match.values():
            A = [source[i] for i in v]
            B = [target[i] for i in v]
            res += sum((Counter(A) - Counter(B)).values())
        return res


def test_minimum_hamming_distance():
    solution = Solution()

    assert solution.minimumHammingDistance([1, 2, 3, 4], [2, 1, 4, 5], [[0, 1], [2, 3]]) == 1, 'wrong result'
    assert solution.minimumHammingDistance([1, 2, 3, 4], [1, 3, 2, 4], []) == 2, 'wrong result'
    assert solution.minimumHammingDistance([5, 1, 2, 4, 3], [1, 5, 4, 2, 3],
                                           [[0, 4], [4, 2], [1, 3], [1, 4]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_hamming_distance()
