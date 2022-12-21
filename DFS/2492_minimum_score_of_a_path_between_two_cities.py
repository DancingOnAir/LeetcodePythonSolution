from typing import List
from collections import defaultdict


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v, d in roads:
            g[u].append([v, d])
            g[v].append([u, d])

        res = float('inf')
        seen = set()

        def dfs(u):
            for v, d in g[u]:
                nonlocal res
                res = min(res, d)

                if v not in seen:
                    seen.add(v)
                    dfs(v)

        dfs(1)
        return res


def test_min_score():
    solution = Solution()
    assert solution.minScore(3, [[3, 2, 1], [1, 3, 3]]) == 1, 'wrong result'
    assert solution.minScore(4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]) == 5, 'wrong result'
    assert solution.minScore(4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_score()
