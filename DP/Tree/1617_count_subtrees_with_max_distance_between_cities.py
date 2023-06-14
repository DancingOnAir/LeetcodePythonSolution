from typing import List


class Solution:

    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u - 1].append(v - 1)
            g[v - 1].append(u - 1)

        res = [0] * (n - 1)

        for mask in range(3, 1 << n):
            # 至少需要2个点
            if (mask & (mask - 1)) == 0:
                continue

            seen = diameter = 0

            def dfs(u):
                nonlocal seen, diameter
                # 标记x为访问过的城市
                seen |= 1 << u
                mx = 0
                for v in g[u]:
                    if ((seen >> v) & 1) == 0 and ((mask >> v) & 1):
                        depth = dfs(v) + 1
                        diameter = max(diameter, mx + depth)
                        mx = max(mx, depth)
                return mx

            dfs(mask.bit_length() - 1)
            # dfs保证是1个连通图，不是森林。这里保证经过的点一致，是同一个连通图
            if seen == mask:
                res[diameter - 1] += 1
        return res


def test_count_subgraphs_for_each_diameter():
    solution = Solution()
    assert solution.countSubgraphsForEachDiameter(4, [[1, 2], [2, 3], [2, 4]]) == [3, 4, 0], 'wrong result'
    assert solution.countSubgraphsForEachDiameter(2, [[1, 2]]) == [1], 'wrong result'
    assert solution.countSubgraphsForEachDiameter(3, [[1, 2], [2, 3]]) == [2, 1], 'wrong result'


if __name__ == '__main__':
    test_count_subgraphs_for_each_diameter()
