from typing import List
from collections import deque, defaultdict
from functools import lru_cache


class Solution:
    # dp
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v in relations:
            graph[v].append(u)

        @lru_cache(None)
        def dp(node):
            return time[node - 1] + max([dp(child) for child in graph[node]] + [0])
        return max(dp(i) for i in range(1, n + 1))

    # topological sort
    def minimumTime1(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        for u, v in relations:
            graph[u - 1].append(v - 1)
            in_degree[v - 1] += 1

        distance = [0] * n
        dq = deque([])
        for i, val in enumerate(in_degree):
            if val == 0:
                dq.append(i)
                distance[i] = time[i]

        while dq:
            u = dq.popleft()
            for v in graph[u]:
                distance[v] = max(distance[v], distance[u] + time[v])
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    dq.append(v)

        return max(distance)


def test_minimum_time():
    solution = Solution()
    assert solution.minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5]) == 8, 'wrong result'
    assert solution.minimumTime(5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]) == 12, 'wrong result'


if __name__ == '__main__':
    test_minimum_time()

