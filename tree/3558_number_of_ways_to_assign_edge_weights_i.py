from math import pow


class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        MOD = 1_000_000_007
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x, p):
            d = 0
            for y in g[x]:
                if y != p:
                    d = max(d, dfs(y, x) + 1)
            return d
        k = dfs(1, 0)
        return pow(2, k - 1) % MOD


def test_assign_edge_weights():
    solution = Solution()
    assert solution.assignEdgeWeights([[1, 2]]) == 1, 'wrong result'
    assert solution.assignEdgeWeights([[1, 2], [1, 3], [3, 4], [3, 5]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_assign_edge_weights()
