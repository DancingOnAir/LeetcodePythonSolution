from typing import List


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        g = [[] for _ in range(n + 1)]
        # 添加1个无效的0到根节点，方便后续的计算节点的儿子个数:len(g(u)) - 1
        g[1] = [0]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u, pa, left_t):
            if left_t == 0:
                return u == target
            # 如果刚好为target 判断是否为叶子节点，否则青蛙会继续跳跃
            if u == target:
                return len(g[u]) == 1

            for v in g[u]:
                if v != pa:
                    prod = dfs(v, u, left_t - 1)
                    if prod:
                        return prod * (len(g[u]) - 1)
            return 0
        prod = dfs(1, -1, t)
        return 1 / prod if prod else 0


def test_frog_position():
    solution = Solution()
    assert abs(solution.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 2,
                                     4) - 0.16666666666666666) < 1e-5, 'wrong result'
    assert abs(solution.frogPosition(7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 1,
                                     7) - 0.3333333333333333) < 1e-5, 'wrong result'


if __name__ == '__main__':
    test_frog_position()
