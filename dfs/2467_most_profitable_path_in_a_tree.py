from typing import List
from collections import defaultdict


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        bob_time = [n] * n

        # node:当前结点，pa：父节点，t：当前时间
        def dfs_bob(node, pa, t):
            if node == 0:
                bob_time[node] = t
                return True

            for child in graph[node]:
                if child != pa and dfs_bob(child, node, t + 1):
                    bob_time[node] = t
                    return True
            return False
        dfs_bob(bob, -1, 0)

        # 防止把根结点当成叶子结点，len(graph[node]) == 1为叶子结点
        graph[0].append(-1)
        res = -10 ** 9

        def dfs_alice(node, pa, alice_time, tot):
            if alice_time < bob_time[node]:
                tot += amount[node]
            elif alice_time == bob_time[node]:
                tot += amount[node] // 2
            # 叶子结点
            if len(graph[node]) == 1:
                nonlocal res
                res = max(res, tot)
                return
            for child in graph[node]:
                if child != pa:
                    dfs_alice(child, node, alice_time + 1, tot)
        dfs_alice(0, -1, 0, 0)
        return res


def test_most_profitable_path():
    solution = Solution()
    assert solution.mostProfitablePath([[0, 1], [1, 2], [1, 3], [3, 4]], 3, [-2, 4, 2, -4, 6]) == 6, 'wrong result'
    assert solution.mostProfitablePath([[0, 1]], 1, [-7280, 2350]) == -7280, 'wrong result'


if __name__ == '__main__':
    test_most_profitable_path()
