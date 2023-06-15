from typing import List
from functools import lru_cache


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        cost = [[0] * n for _ in range(n)]

        def dfs(u, pa):
            for v in g[u]:
                if v != pa:
                    cost[i][v] = cost[i][u] + price[v]
                    dfs(v, u)

        for i in range(n):
            dfs(i, -1)

        return max(cost[u][v] for u in range(n) for v in range(n) if u != v)


def test_max_output():
    solution = Solution()
    assert solution.maxOutput(4, [[2, 0], [0, 1], [1, 3]], [2, 3, 1, 1]) == 6, 'wrong result'
    assert solution.maxOutput(6, [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5]], [9, 8, 7, 6, 10, 5]) == 24, 'wrong result'
    assert solution.maxOutput(3, [[0, 1], [1, 2]], [1, 1, 1]) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_output()
