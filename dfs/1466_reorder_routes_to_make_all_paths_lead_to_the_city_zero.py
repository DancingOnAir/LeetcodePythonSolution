from typing import List


class Solution:
    # dfs思路：先构建无向图，然后从0开始dfs，从小到大标记层数，如果结点a的层数l1小于结点b的层数l2，说明a比b离0近，
    # 再考虑有向边，存在[a, b]的话,说明a指向b，不能从b到a，那么结果要加1
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        depths = [-1] * n

        def dfs(node, depth):
            depths[node] = depth
            for child in g[node]:
                if depths[child] < 0:
                    dfs(child, depth + 1)

        dfs(0, 0)
        res = 0
        for u, v in connections:
            if depths[u] < depths[v]:
               res += 1
        return res


def test_min_reorder():
    solution = Solution()
    assert solution.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3, 'wrong result'
    assert solution.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]) == 2, 'wrong result'
    assert solution.minReorder(3, [[1, 0], [2, 0]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_reorder()
