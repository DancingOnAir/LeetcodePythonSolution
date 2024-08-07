from typing import List
from collections import deque


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs():
            dq = deque([0])
            seen = {0}
            dist = 0
            while dq:
                for _ in range(len(dq)):
                    u = dq.popleft()
                    if u == n - 1:
                        return dist
                    for v in graph[u]:
                        if v not in seen:
                            seen.add(v)
                            dq.append(v)
                dist += 1

        graph = [[] * n for _ in range(n)]
        for i in range(n - 1):
            graph[i].append(i + 1)

        res = []
        for u, v in queries:
            graph[u].append(v)
            res.append(bfs())
        return res


def test_shortest_distance_after_queries():
    solution = Solution()
    assert solution.shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]]) == [3, 2, 1], 'wrong result'
    assert solution.shortestDistanceAfterQueries(4, [[0, 3], [0, 2]]) == [1, 1], 'wrong result'


if __name__ == '__main__':
    test_shortest_distance_after_queries()
