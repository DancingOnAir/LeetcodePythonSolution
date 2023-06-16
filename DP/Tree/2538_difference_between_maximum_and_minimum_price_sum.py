from typing import List


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u, pa):
            nonlocal res
            mx1 = p = price[u]
            mx2 = 0
            for v in g[u]:
                if v != pa:
                    s1, s2 = dfs(v, u)
                    res = max(res, mx1 + s2, mx2 + s1)
                    # 这里都加p因为u肯定不是叶子，而v有可能是
                    mx1 = max(mx1, s1 + p)
                    mx2 = max(mx2, s2 + p)
            return mx1, mx2

        res = 0
        dfs(0, -1)
        return res

    # TLE
    def maxOutput1(self, n: int, edges: List[List[int]], price: List[int]) -> int:
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
