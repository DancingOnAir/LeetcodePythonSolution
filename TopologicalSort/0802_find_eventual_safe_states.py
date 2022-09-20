from typing import List
from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        in_graph = [[] for _ in range(n)]
        out_degrees = [0] * n
        dq = deque()
        for i, nodes in enumerate(graph):
            out_degrees[i] += len(nodes)
            if out_degrees[i] == 0:
                dq.append(i)
            for j in nodes:
                in_graph[j].append(i)

        res = list()
        while dq:
            terminal_node = dq.popleft()
            res.append(terminal_node)

            for node in in_graph[terminal_node]:
                out_degrees[node] -= 1
                if out_degrees[node] == 0:
                    dq.append(node)
        return sorted(res)


def test_eventual_safe_nodes():
    solution = Solution()
    assert solution.eventualSafeNodes([[], [0, 2, 3, 4], [3], [4], []]) == [0, 1, 2, 3, 4], 'wrong result'
    assert solution.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]) == [2, 4, 5, 6], 'wrong result'
    assert solution.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]) == [4], 'wrong result'


if __name__ == '__main__':
    test_eventual_safe_nodes()
