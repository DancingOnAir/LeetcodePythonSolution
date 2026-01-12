from typing import List


class Solution:
    # https://leetcode.cn/problems/count-subtrees-with-max-distance-between-cities/solution/tu-jie-on3-mei-ju-zhi-jing-duan-dian-che-am2n/
    # dfs + multiply theory
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u - 1].append(v - 1)
            g[v - 1].append(u - 1)

        # 计算任意2个城市间的距离
        dist = [[0] * n for _ in range(n)]

        def dfs(u, pa):
            for v in g[u]:
                if v != pa:
                    dist[i][v] = dist[i][u] + 1
                    dfs(v, u)

        for i in range(n):
            # 计算i到其余城市的距离
            dfs(i, -1)

        def dfs2(u, pa):
            cnt = 1
            for v in g[u]:
                if v != pa and (di[v] < d or (di[v] == d and v > j)) and (dj[v] < d or (dj[v] == d and v > i)):
                    cnt *= dfs2(v, u)
            if di[u] + dj[u] > d:
                cnt += 1
            return cnt

        res = [0] * (n - 1)
        for i, di in enumerate(dist):
            for j in range(i + 1, n):
                dj = dist[j]
                d = di[j]
                res[d - 1] += dfs2(i, -1)
        return res

    # dfs + binary mask
    def countSubgraphsForEachDiameter1(self, n: int, edges: List[List[int]]) -> List[int]:
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
