from typing import List
# from collections import defaultdict


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        def bfs(u, pa, val):
            if val % signalSpeed == 0:
                nonlocal cnt
                cnt += 1

            for v in g[u]:
                if v != pa:
                    cur = weights[u][v] + val
                    bfs(v, u, cur)

        n = len(edges) + 1
        g = [[] for _ in range(n)]
        weights = [[-1] * n for _ in range(n)]
        for u, v, w in edges:
            g[u].append(v)
            g[v].append(u)

            weights[u][v] = w
            weights[v][u] = w

        res = [0] * n
        for u in range(n):
            cur, pre = 0, 0
            for v in g[u]:
                cnt = 0
                bfs(v, u, weights[u][v])
                cur += pre * cnt
                pre += cnt

            res[u] = cur
        return res


def test_count_pair_of_connectable_servers():
    solution = Solution()
    assert solution.countPairsOfConnectableServers([[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], 1) == [0,4,6,6,4,0], 'wrong result'
    assert solution.countPairsOfConnectableServers([[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]], 3) == [2,0,0,0,0,0,2], 'wrong result'


if __name__ == '__main__':
    test_count_pair_of_connectable_servers()
