from typing import List
from collections import deque, defaultdict


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        new_g = [set() for _ in range(n)]
        for i in range(n):
            for j in graph[i]:
                new_g[i].add(j)
                new_g[j].add(i)
        graph = new_g

        dp = [[float('inf')] * n for _ in range(1 << n)]

        q = deque()
        for i in range(n):
            # dp[state][node], the distance between the ith node with itself equals 0
            dp[1 << i][i] = 0
            q.append((i, 1 << i))

        while q:
            node, state = q.popleft()
            for neighbour in graph[node]:
                new_state = state | (1 << neighbour)

                if dp[new_state][neighbour] == float('inf'):
                    dp[new_state][neighbour] = dp[state][node] + 1
                    q.append((neighbour, new_state))

        return min(dp[-1])

    # dp
    def shortestPathLength2(self, graph: List[List[int]]) -> int:
        n = len(graph)
        dist = [[float('inf')] * n for _ in range(1 << n)]
        for i in range(n):
            dist[1 << i][i] = 0

        for cover in range(1 << n):
            repeat = True

            while repeat:
                repeat = False
                for head, d in enumerate(dist[cover]):
                    for neighbor in graph[head]:
                        cover2 = cover | (1 << neighbor)
                        if d + 1 < dist[cover2][neighbor]:
                            dist[cover2][neighbor] = d + 1
                            if cover == cover2:
                                repeat = True
        return min(dist[2 ** n - 1])

    # bfs
    def shortestPathLength1(self, graph: List[List[int]]) -> int:
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
