from typing import List
from collections import defaultdict


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        restricted = set(restricted)
        valid_nodes = [0]
        seen = {0}
        res = 0
        while valid_nodes:
            res += len(valid_nodes)
            cur = list()
            for node in valid_nodes:
                for child in graph[node]:
                    if child not in restricted and child not in seen:
                        cur.append(child)
                        seen.add(child)
            valid_nodes = cur
        return res


def test_reachable_nodes():
    solution = Solution()
    assert solution.reachableNodes(7, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5]) == 4, 'wrong result'
    assert solution.reachableNodes(7, [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]], [4, 2, 1]) == 3, 'wrong result'


if __name__ == '__main__':
    test_reachable_nodes()

