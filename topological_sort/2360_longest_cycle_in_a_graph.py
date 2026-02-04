from typing import List
from collections import deque


class Solution:
    # topologic sort + floyd's algorithm
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        in_degree = [0] * n
        for u, v in enumerate(edges):
            if v != -1:
                in_degree[v] += 1

        candidates = set(range(n))
        dq = deque(i for i, val in enumerate(in_degree) if val == 0)
        while dq:
            u = dq.popleft()
            candidates.remove(u)
            if edges[u] != -1:
                in_degree[edges[u]] -= 1
            if edges[u] != -1 and in_degree[edges[u]] == 0:
                dq.append(edges[u])

        if not candidates:
            return -1

        res = 0
        seen = set()
        for node in candidates:
            if node in seen:
                continue
            u, v = edges[node], edges[edges[node]]
            sz = 1
            seen |= {node, u, v}
            while u != v:
                u = edges[u]
                v = edges[edges[v]]
                seen |= {u, v}
            # 环问题求环起点，当一个指针从起点node开始走，另一个指针从相遇点v开始走，当2者相遇时，就是环的起点。
            u = node
            while u != v:
                u = edges[u]
                v = edges[v]
            start = u

            v = edges[start]
            while v != start:
                v = edges[v]
                sz += 1
            res = max(res, sz)
        return res

    # dfs
    def longestCycle2(self, edges: List[int]) -> int:
        n = len(edges)
        seen = set()
        depths = [float('inf')] * n

        def dfs(i, depth):
            if i in seen or edges[i] == -1:
                return -1
            if depths[i] < depth:
                return depth - depths[i]
            depths[i] = depth
            res = dfs(edges[i], depth + 1)
            seen.add(i)
            return res

        return max(dfs(i, 0) for i in range(n))

    # topologic sort
    def longestCycle1(self, edges: List[int]) -> int:
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
