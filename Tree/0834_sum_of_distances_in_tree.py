from typing import List
from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # root 当前节点, pre 当前节点的根节点
        def postorder(root, pre):
            for i in tree[root]:
                if i != pre:
                    postorder(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def preorder(root, pre):
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + n - count[i]
                    preorder(i, root)
            pass

        tree = defaultdict(set)
        count = [1] * n
        res = [0] * n

        for u, v in edges:
            tree[u].add(v)
            tree[v].add(u)

        postorder(0, -1)
        preorder(0, -1)
        return res

    def sumOfDistancesInTree1(self, n: int, edges: List[List[int]]) -> List[int]:
        # u: 当前节点, f: 当前节点的根节点
        def dfs1(u, f):
            dp[u] = 0
            sz[u] = 1

            for v in graph[u]:
                # 邻接点不允许为根节点
                if v == f:
                    continue
                dfs1(v, u)
                dp[u] += (dp[v] + sz[v])
                sz[u] += sz[v]
        # 换根操作
        def dfs2(u, f):
            res[u] = dp[u]
            for v in graph[u]:
                if v == f:
                    continue

                pu, pv = dp[u], dp[v]
                su, sv = sz[u], sz[v]
                dp[u] -= (dp[v] + sz[v])
                sz[u] -= sz[v]
                dp[v] += (dp[u] + sz[u])
                sz[v] += sz[u]

                dfs2(v, u)
                dp[u] = pu
                dp[v] = pv
                sz[u] = su
                sz[v] = sv

        res = [0] * n
        sz = [0] * n
        dp = [0] * n
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dfs1(0, -1)
        dfs2(0, -1)
        return res


def test_sum_of_distances_in_tree():
    solution = Solution()
    assert solution.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]) == [8, 12, 6, 10, 10, 10], 'wrong result'
    assert solution.sumOfDistancesInTree(1, []) == [0], 'wrong result'
    assert solution.sumOfDistancesInTree(2, [[1, 0]]) == [1, 1], 'wrong result'


if __name__ == '__main__':
    test_sum_of_distances_in_tree()

