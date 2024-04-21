from typing import List
from heapq import heappop, heappush
from collections import defaultdict


class Solution:
    # Dijkstra's algorithm
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = defaultdict(dict)
        for u, v, w in edges:
            g[u][v] = min(g[u].get(v, float('inf')), w)
            g[v][u] = min(g[v].get(u, float('inf')), w)

        res = [float('inf')] * n
        hp = [(0, 0)]
        while hp:
            time, u = heappop(hp)
            if res[u] > time:
                res[u] = time
                if u in g:
                    for v, w in g.pop(u).items():
                        if time + w < disappear[v]:
                            heappush(hp, (time + w, v))
        return [x if x < float('inf') else -1 for x in res]


def test_minimum_time():
    solution = Solution()
    assert solution.minimumTime(3, [[2, 0, 9], [1, 0, 5], [2, 2, 4], [0, 1, 10], [1, 1, 10], [1, 1, 10], [2, 2, 10],
                                    [1, 1, 10]], [4, 13, 19]) == [0, 5, 9], 'wrong result'
    assert solution.minimumTime(3, [[0, 1, 2], [1, 2, 1], [0, 2, 4]], [1, 1, 5]) == [0, -1, 4], 'wrong result'
    assert solution.minimumTime(3, [[0, 1, 2], [1, 2, 1], [0, 2, 4]], [1, 3, 5]) == [0, 2, 3], 'wrong result'
    assert solution.minimumTime(2, [[0, 1, 1]], [1, 1]) == [0, -1], 'wrong result'


if __name__ == '__main__':
    test_minimum_time()
