from typing import List


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        res = [0] * n

        def dfs(u, pa):
            depths = list()

            for v in g[u]:
                if v != pa:
                    cur = dfs(v, u)
                    for x in cur:
                        depths.append(x + 1)

            for d in depths:
                res[d] += 1

            for i, d in enumerate(depths):
                for j in range(i + 1, len(depths)):
                    res[d + depths[j]] += 1
            return depths if depths else [0]

        dfs(1, -1)
        return res


def test_count_subgraphs_for_each_diameter():
    solution = Solution()
    assert solution.countSubgraphsForEachDiameter(4, [[1, 2], [2, 3], [2, 4]]) == [3, 4, 0], 'wrong result'
    assert solution.countSubgraphsForEachDiameter(2, [[1, 2]]) == [1], 'wrong result'
    assert solution.countSubgraphsForEachDiameter(3, [[1, 2], [2, 3]]) == [2, 1], 'wrong result'


if __name__ == '__main__':
    test_count_subgraphs_for_each_diameter()
