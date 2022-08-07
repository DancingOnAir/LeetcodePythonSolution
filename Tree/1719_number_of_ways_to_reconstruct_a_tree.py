from typing import List
from collections import defaultdict


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        def helper(nodes):
            d = defaultdict(list)
            m = len(nodes) - 1
            for node in nodes:
                d[len(graph[node])].append(node)

            if len(d[m]) == 0:
                return 0
            root = d[m][0]

            for node in graph[root]:
                graph[node].remove(root)

            comps, seen, i = defaultdict(set), set(), 0
            def dfs(node, i):
                comps[i].add(node)
                seen.add(node)
                for nei in graph[node]:
                    if nei not in seen:
                        dfs(nei, i)

            for node in nodes:
                if node != root and node not in seen:
                    dfs(node, i)
                    i += 1

            candidates = [helper(val) for val in comps.values()]
            if 0 in candidates:
                return 0
            if 2 in candidates:
                return 2
            if len(d[m]) >= 2:
                return 2
            return 1

        return helper(set(graph.keys()))


def test_check_ways():
    solution = Solution()
    assert solution.checkWays([[3, 5], [4, 5], [2, 5], [1, 5], [1, 4], [2, 4]]) == 1, 'wrong result'
    assert solution.checkWays([[1, 2], [2, 3]]) == 1, 'wrong result'
    assert solution.checkWays([[1, 2], [2, 3], [1, 3]]) == 2, 'wrong result'
    assert solution.checkWays([[1, 2], [2, 3], [2, 4], [1, 5]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_check_ways()
