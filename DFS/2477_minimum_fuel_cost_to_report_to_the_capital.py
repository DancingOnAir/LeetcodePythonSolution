from typing import List


class Solution:
    # 以0为根，子树node的大小为sz，那么它到父节点这条边的流量为sz，那么就至少需要ceil(sz / seats)辆车
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        g = [[] for _ in range(n)]
        for u, v in roads:
            g[u].append(v)
            g[v].append(u)

        res = 0

        def dfs(u, pa):
            sz = 1
            for v in g[u]:
                if v != pa:
                    sz += dfs(v, u)
            if u:
                nonlocal res
                # 求上确界
                res += (sz + seats - 1) // seats
            return sz
        dfs(0, -1)
        return res


def test_minimum_fuel_cost():
    solution = Solution()
    assert solution.minimumFuelCost([[0, 1], [0, 2], [0, 3]], 5) == 3, 'wrong result'
    assert solution.minimumFuelCost([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2) == 7, 'wrong result'
    assert solution.minimumFuelCost([], 1) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_fuel_cost()
