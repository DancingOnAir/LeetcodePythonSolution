from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
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
