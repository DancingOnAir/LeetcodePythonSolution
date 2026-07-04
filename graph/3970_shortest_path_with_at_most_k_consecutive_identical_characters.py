from heapq import heapify, heappush, heappop


class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))

        dist = [[float("inf")] * (k + 1) for _ in range(n)]
        # 最短路径长度, id, 最后连续相同字母长度
        hp = [(0, 0, 1)]
        while hp:
            d, u, cnt = heappop(hp)
            if u == n - 1:
                return d
            if d > dist[u][cnt]:
                dist[u][cnt] = d
            for v, w in g[u]:
                new_cnt = 1 if labels[u] != labels[v] else cnt + 1
                new_dist = d + w
                if new_cnt <= k and new_dist < dist[v][new_cnt]:
                    dist[v][new_cnt] = new_dist
                    heappush(hp, (new_dist, v, new_cnt))
        return -1


def test_shortest_path():
    solution = Solution()
    assert solution.shortestPath(3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1) == 3, 'wrong result'
    assert solution.shortestPath(3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2) == 2, 'wrong result'
    assert solution.shortestPath(3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2) == -1, 'wrong result'


if __name__ == '__main__':
    test_shortest_path()

