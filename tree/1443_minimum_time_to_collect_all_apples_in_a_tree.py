from typing import List
from collections import defaultdict, deque


class Solution:
    # Kahn's algorithm
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        hasApple[0] = True
        degree = [0] * n

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        dq = deque(u for u in range(n) if degree[u] == 1)
        while dq:
            u = dq.popleft()
            if hasApple[u]:
                continue
            for v in graph[u]:
                if degree[u] > 0:
                    degree[v] -= 1
                    degree[u] -= 1
                    if degree[v] == 1:
                        dq.append(v)
        return sum(degree)

    # dfs
    def minTime2(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node, pre):
            for child in graph[node]:
                if child != pre and dfs(child, node):
                    hasApple[node] = True
            return hasApple[node]

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dfs(0, -1)
        return (sum(hasApple) - hasApple[0]) * 2

    # dfs
    def minTime1(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = [False for _ in range(n)]

        def dfs(node):
            if seen[node]:
                return 0
            seen[node] = True

            time = 0
            for child in graph[node]:
                time += dfs(child)
            if time > 0:
                return time + 2
            return 2 if hasApple[node] else 0
        return max(dfs(0) - 2, 0)


def test_min_time():
    solution = Solution()

    assert solution.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, True, False, True, True, False]) == 8, 'wrong result'
    assert solution.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, True, False, False, True, False]) == 6, 'wrong result'
    assert solution.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, False, False, False, False, False]) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_time()
