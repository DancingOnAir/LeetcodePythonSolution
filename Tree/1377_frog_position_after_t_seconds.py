from typing import List
from collections import defaultdict


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False for _ in range(n)]
        nodes = [(1, 1)]
        while t + 1:
            tmp = list()
            for node, p in nodes:
                if not visited[node - 1]:
                    visited[node - 1] = True
                    next_p = sum(not visited[u - 1] for u in graph[node])
                    if node == target:
                        if next_p == 0 or t == 0:
                            return 1 / p
                        return 0
                    for u in graph[node]:
                        tmp.append((u, p * next_p))
            nodes = tmp
            t -= 1
        return 0


def test_frog_position():
    solution = Solution()
    assert abs(solution.frogPosition(3, [[2, 1], [3, 2]], 1, 2) - 1.0) < 10e-5, 'wrong result'
    assert abs(solution.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 2, 4) - 0.16666666666666666) < 10e-5, 'wrong result'
    assert abs(solution.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 1, 7) - 0.3333333333333333) < 10e-5, 'wrong result'


if __name__ == '__main__':
    test_frog_position()
