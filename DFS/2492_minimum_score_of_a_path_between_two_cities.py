from typing import List
from collections import defaultdict


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        def union(x, y, z):
            px = find(x)
            py = find(y)

            min_dist = min(dist[px], dist[py], z)
            parents[px] = py
            dist[px] = dist[py] = min_dist

        def find(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        parents = [i for i in range(n + 1)]
        dist = [float('inf') for _ in range(n + 1)]
        for u, v, d in roads:
            union(u, v, d)
        return dist[find(1)]

    def minScore1(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v, d in roads:
            g[u].append([v, d])
            g[v].append([u, d])

        res = float('inf')
        seen = set()

        def dfs(u):
            for v, d in g[u]:
                nonlocal res
                res = min(res, d)

                if v not in seen:
                    seen.add(v)
                    dfs(v)

        dfs(1)
        return res


def test_min_score():
    solution = Solution()
    assert solution.minScore(3, [[3, 2, 1], [1, 3, 3]]) == 1, 'wrong result'
    assert solution.minScore(4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]) == 5, 'wrong result'
    assert solution.minScore(4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_score()
