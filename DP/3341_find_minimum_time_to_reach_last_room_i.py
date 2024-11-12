from typing import List
from heapq import heappop, heappush


class Solution:
    # https://leetcode.cn/problems/find-minimum-time-to-reach-last-room-ii/solutions/2975554/dijkstra-zui-duan-lu-pythonjavacgo-by-en-alms/
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        hp = [(0, 0, 0)]
        while True:
            d, i, j = heappop(hp)
            if i == n - 1 and j == m - 1:
                return d
            if d > dist[i][j]:
                continue
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < m and 0 <= y < n:
                    new_dist = max(d, moveTime[x][y]) + 1
                    if new_dist < dist[x][y]:
                        dist[x][y] = new_dist
                        heappush(hp, (new_dist, x, y))


def test_min_time_to_reach():
    solution = Solution()
    assert solution.minTimeToReach([[0, 4], [4, 4]]) == 6, 'wrong result'
    assert solution.minTimeToReach([[0, 0, 0], [0, 0, 0]]) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_time_to_reach()
