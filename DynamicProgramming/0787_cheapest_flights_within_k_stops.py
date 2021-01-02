from typing import List
from collections import deque


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if n < 1 or not flights or K < 0:
            return -1

        graph = [[] for _ in range(n)]
        for s, d, price in flights:
            graph[s].append((d, price))
        seen = [float('inf')] * n
        q = deque([(src, -1, 0)])
        while q:
            node, stops, cost = q.popleft()
            if node == dst or stops == K:
                continue

            for nei, price in graph[node]:
                if cost + price >= seen[nei]:
                    continue

                seen[nei] = cost + price
                q.append((nei, stops + 1, cost + price))

        return seen[dst] if seen[dst] != float('inf') else -1

    def findCheapestPrice1(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # dp[i][j] means distance to reach j using at most i edges from src
        dp = [[float('inf')] * n for _ in range(K + 2)]
        for i in range(K + 2):
            dp[i][src] = 0
        for i in range(1, K + 2):
            for f in flights:
                if dp[i - 1][f[0]] != float('inf'):
                    dp[i][f[1]] = min(dp[i][f[1]], dp[i - 1][f[0]] + f[2])

        return dp[K + 1][dst] if dp[K + 1][dst] != float('inf') else -1


def test_find_cheapest_price():
    solution = Solution()

    n1 = 3
    edges1 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src1 = 0
    dst1 = 2
    k1 = 1
    assert solution.findCheapestPrice(n1, edges1, src1, dst1, k1) == 200, 'wrong result'

    n2 = 3
    edges2 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src2 = 0
    dst2 = 2
    k2 = 0
    assert solution.findCheapestPrice(n2, edges2, src2, dst2, k2) == 500, 'wrong result'


if __name__ == '__main__':
    test_find_cheapest_price()
