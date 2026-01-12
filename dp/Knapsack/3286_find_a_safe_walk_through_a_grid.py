from typing import List
from collections import deque


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        q = deque([(0, 0)])
        while q:
            i, j = q.popleft()
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n:
                    val = grid[x][y]
                    if dist[i][j] + val < dist[x][y]:
                        dist[x][y] = dist[i][j] + val
                        if val == 0:
                            q.appendleft((x, y))
                        else:
                            q.append((x, y))
        return dist[-1][-1] < health


def test_find_safe_walk():
    solution = Solution()
    assert solution.findSafeWalk([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 1), 'wrong result'
    assert not solution.findSafeWalk([[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0]],
                                     3), 'wrong result'
    assert solution.findSafeWalk([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 5), 'wrong result'


if __name__ == '__main__':
    test_find_safe_walk()
