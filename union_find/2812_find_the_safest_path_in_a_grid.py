from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # 统计所有的thief点
        q = []
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dist[i][j] = 0
        # 计算曼哈顿距离，每次循环把距离一样的归类
        groups = [q]
        direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            tmp = q
            q = []
            for x, y in tmp:
                for dx, dy in direct:
                    if 0 <= x + dx < n and 0 <= y + dy < n and dist[x + dx][y + dy] < 0:
                        q.append((x + dx, y + dy))
                        dist[x + dx][y + dy] = len(groups)
            groups.append(q)
        # union-find pattern
        pa = list(range(n * n))

        def find(p):
            if pa[p] != p:
                pa[p] = find(pa[p])
            return pa[p]

        for d in range(len(groups) - 2, 0, -1):
            for x, y in groups[d]:
                for dx, dy in direct:
                    if 0 <= x + dx < n and 0 <= y + dy < n and dist[x + dx][y + dy] >= dist[x][y]:
                        pa[find((x + dx) * n + y + dy)] = find(x * n + y)
            if find(0) == find(n * n - 1):
                return d
        return 0


def test_maximum_safeness_factor():
    solution = Solution()
    assert solution.maximumSafenessFactor([[1, 0, 0], [0, 0, 0], [0, 0, 1]]) == 0, 'wrong result'
    assert solution.maximumSafenessFactor([[0, 0, 1], [0, 0, 0], [0, 0, 0]]) == 2, 'wrong result'
    assert solution.maximumSafenessFactor([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_maximum_safeness_factor()
