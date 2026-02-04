from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        # 先dijkstra求出0到任意点时间的花费
        dist = [float('inf') for _ in range(n)]
        dist[0] = 0
        # 距离，点
        pq = [(0, 0)]
        # 表示到id的最短路径数
        count = [1] + [0] * (n - 1)
        while pq:
            min_time, u = heappop(pq)
            if u == n - 1:
                return count[u] % (10 ** 9 + 7)
            for v, t in graph[u]:
                cand_time = t + min_time
                # cand_time等于当前min_time则叠加，小于则覆盖更新
                if cand_time == dist[v]:
                    count[v] += count[u]
                elif cand_time < dist[v]:
                    dist[v] = cand_time
                    heappush(pq, (cand_time, v))
                    count[v] = count[u]


def test_count_paths():
    solution = Solution()
    assert solution.countPaths(7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]) == 4, 'wrong result'
    assert solution.countPaths(2, [[1, 0, 10]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_count_paths()

