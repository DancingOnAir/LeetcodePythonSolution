from typing import List
from collections import deque


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        for u, v in enumerate(edges):
            if v != -1:
                in_degree[v] += 1
                graph[u].append(v)

        dq = deque(i for i, val in enumerate(in_degree) if val == 0)
        seen = set()
        while dq:
            u = dq.popleft()
            seen.add(u)

            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    dq.append(v)

        if len(seen) == n:
            return -1
        res = -1
        while len(seen) < n:
            free = set(range(n)) - seen
            start = u = list(free)[0]
            cur = 0
            while start not in seen:
                u = graph[u][0]
                seen.add(u)
                cur += 1
            res = max(res, cur)
        return res


def test_longest_cycle():
    solution = Solution()
    assert solution.longestCycle([3, 3, 4, 2, 3]) == 3, 'wrong result'
    assert solution.longestCycle([2, -1, 3, 1]) == -1, 'wrong result'


if __name__ == '__main__':
    test_longest_cycle()
