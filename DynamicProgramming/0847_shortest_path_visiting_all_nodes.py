from typing import List
from collections import deque, defaultdict


class Solution:
    # bfs
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = deque((1 << x, x) for x in range(n))
        dist = defaultdict(lambda: n*n)

        for x in range(n):
            dist[1 << x, x] = 0

        while q:
            cover, head = q.popleft()
            d = dist[cover, head]
            if cover == 2 ** n - 1:
                return d

            for child in graph[head]:
                cover2 = cover | (1 << child)
                if d + 1 < dist[cover2, child]:
                    dist[cover2, child] = d + 1
                    q.append((cover2, child))


def test_shortest_path_length():
    solution = Solution()

    assert solution.shortestPathLength([[1, 2, 3], [0], [0], [0]]) == 4, 'wrong result'
    assert solution.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]) == 4, 'wrong result'


if __name__ == '__main__':
    test_shortest_path_length()
