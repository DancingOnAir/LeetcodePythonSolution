from typing import List
from collections import defaultdict


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        n = len(graph)
        roots = [k for k, v in graph.items() if len(v) == n - 1]
        if not roots:
            return 0
        elif len(roots) > 1:
            return 2

        pairs = {tuple(p) for p in pairs}
        for root in roots:
            nodes = graph[root]
            for i in range(len(nodes)):
                for j in range(i+1, len(nodes)):
                    if (nodes[i], nodes[j]) in pairs and (nodes[j], nodes[i]) in pairs:
                        return 2
        return 1


def test_check_ways():
    solution = Solution()
    assert solution.checkWays([[3, 5], [4, 5], [2, 5], [1, 5], [1, 4], [2, 4]]) == 1, 'wrong result'
    assert solution.checkWays([[1, 2], [2, 3]]) == 1, 'wrong result'
    assert solution.checkWays([[1, 2], [2, 3], [1, 3]]) == 2, 'wrong result'
    assert solution.checkWays([[1, 2], [2, 3], [2, 4], [1, 5]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_check_ways()
