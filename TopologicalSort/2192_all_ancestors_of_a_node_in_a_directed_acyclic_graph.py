from typing import List
from collections import deque


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        ancestors = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
            ancestors[v].add(u)

        dq = deque(i for i, val in enumerate(in_degree) if val == 0)
        res = [set() for _ in range(n)]
        while dq:
            u = dq.popleft()
            for v in graph[u]:
                ancestors[v] |= ancestors[u]
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    dq.append(v)
        return [sorted(a) for a in ancestors]


def test_get_ancestors():
    solution = Solution()
    assert solution.getAncestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]) == [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]], 'wrong result'
    assert solution.getAncestors(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]) == [[],[0],[0,1],[0,1,2],[0,1,2,3]], 'wrong result'


if __name__ == '__main__':
    test_get_ancestors()
