from typing import List
from collections import defaultdict


class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.weight = [1] * n

    def find(self, p):
        if p != self.parent[p]:
            p = self.find(self.parent[p])

        return p

    def union(self, p, q):
        r1 = self.find(p)
        r2 = self.find(q)

        if r1 != r2:
            if self.weight[r1] < self.weight[r2]:
                r1, r2 = r2, r1
            self.parent[r2] = r1
            self.weight[r1] += self.weight[r2]
            return True

        return False


class Solution:
    class UF(object):
        def __init__(self, n):
            self.parent = list(range(n))
            self.weight = [1] * n

        def find(self, p):
            if p != self.parent[p]:
                p = self.find(self.parent[p])
            return p

        def unite(self, p, q):
            r1 = self.find(p)
            r2 = self.find(q)

            if r1 != r2:
                if self.weight[r1] < self.weight[r2]:
                    r1, r2 = r2, r1
                self.parent[r2] = r1
                self.weight[r1] += self.weight[r2]

    def containsCycle(self, grid: List[List[str]]) -> bool:
        row = len(grid)
        col = len(grid[0])
        uf = Solution.UF(row * col)

        for i in range(row):
            for j in range(col):
                roots = set()
                for di, dj in [[0, -1], [-1, 0]]:
                    ni = i + di
                    nj = j + dj

                    if ni < 0 or nj < 0 or grid[i][j] != grid[ni][nj]:
                        continue

                    root = uf.find(ni * col + nj)
                    if root in roots:
                        return True
                    roots.add(root)

                for r in roots:
                    uf.unite(r, i * col + j)

        return False

    def containsCycle1(self, grid: List[List[str]]) -> bool:
        row = len(grid)
        col = len(grid[0])
        uf = UnionFind(row * col)

        for i in range(row):
            for j in range(col):

                idx = i * col + j
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    if not uf.union(idx, idx - col):
                        return True
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    if not uf.union(idx, idx - 1):
                        return True
        return False


def test_contains_cycle():
    solution = Solution()

    assert solution.containsCycle([["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]), 'wrong result'
    assert solution.containsCycle([["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]), 'wrong result'
    assert not solution.containsCycle([["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]), 'wrong result'


if __name__ == '__main__':
    test_contains_cycle()
