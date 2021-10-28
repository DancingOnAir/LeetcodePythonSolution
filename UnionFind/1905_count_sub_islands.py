from typing import List


class Solution:
    class UnionFind(object):
        def __init__(self, n):
            self.parent = list(range(n))

        def find(self, p):
            if p != self.parent[p]:
                p = self.find(self.parent[p])
            return p

        def union(self, p, q):
            self.parent[self.find(p)] = self.find(q)

    # dfs
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j):
            if not (0 <= i < row and 0 <= j < col and grid2[i][j] == 1):
                return 1

            grid2[i][j] = 0
            res = grid1[i][j]
            for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                res &= dfs(i + di, j + dj)
            return res

        row = len(grid1)
        col = len(grid1[0])
        return sum(dfs(i, j) for i in range(row) for j in range(col) if grid2[i][j] == 1)

    # union find
    def countSubIslands2(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row = len(grid1)
        col = len(grid1[0])

        uf = Solution.UnionFind(row * col)
        for i in range(row):
            for j in range(col):
                idx = i * col + j
                if grid2[i][j] == 1:
                    if i > 0 and grid2[i - 1][j] == 1:
                        uf.union(idx - col, idx)
                    if j > 0 and grid2[i][j - 1] == 1:
                        uf.union(idx - 1, idx)
                else:
                    uf.parent[idx] = -1

        res = set()
        for p in uf.parent:
            if p != -1:
                res.add(uf.find(p))

        for i in range(row):
            for j in range(col):
                if uf.parent[i * col + j] >= 0 and grid1[i][j] == 0 and uf.find(uf.parent[i * col + j]) in res:
                    res.remove(uf.find(uf.parent[i * col + j]))
        return len(res)

    def countSubIslands1(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        parent = list(range(m * n + 1))

        def find(x):
            if x != parent[x]:
                x = find(parent[x])
            return x

        def union(x, y):
            p1 = find(x)
            p2 = find(y)

            if p1 != p2:
                parent[p2] = p1

        res = set()
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 0:
                    continue

                idx = i * n + j
                if i > 0 and grid2[i - 1][j] == 1:
                    union(idx - n, idx)
                if j > 0 and grid2[i][j - 1] == 1:
                    union(idx - 1, idx)

        res = set()
        abandon = set()
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    root = find(i * n + j)
                    res.add(root)
                    if (grid1[i][j] == 0 and root in res) or root in abandon:
                        res.remove(root)
                        abandon.add(root)

        return len(res)


def test_count_sub_islands():
    solution = Solution()

    grid11 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
    grid21 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
    assert solution.countSubIslands(grid11, grid21) == 3, 'wrong result'

    grid12 = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]
    grid22 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]
    assert solution.countSubIslands(grid12, grid22) == 2, 'wrong result'


if __name__ == '__main__':
    test_count_sub_islands()
