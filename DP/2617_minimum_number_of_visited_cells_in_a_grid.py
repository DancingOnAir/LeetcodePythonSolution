from typing import List
from heapq import heappop, heappush
from math import inf


class Solution:
    # https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/solution/m-n-ge-you-xian-dui-lie-by-zerotrac2-d9rg/
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[inf] * n for _ in range(m)]
        dp[0][0] = 1
        # 优先队列
        row_heap, col_heap = [[] for _ in range(m)], [[] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                while row_heap[i] and row_heap[i][0][1] + grid[i][row_heap[i][0][1]] < j:
                    heappop(row_heap[i])
                if row_heap[i]:
                    dp[i][j] = min(dp[i][j], dp[i][row_heap[i][0][1]] + 1)

                while col_heap[j] and col_heap[j][0][1] + grid[col_heap[j][0][1]][j] < i:
                    heappop(col_heap[j])
                if col_heap[j]:
                    dp[i][j] = min(dp[i][j], dp[col_heap[j][0][1]][j] + 1)

                if dp[i][j] != inf:
                    heappush(row_heap[i], (dp[i][j], j))
                    heappush(col_heap[j], (dp[i][j], i))

        return dp[-1][-1] if dp[-1][-1] < inf else -1

    # dp but TLE
    def minimumVisitedCells1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[10 ** 6] * n for _ in range(m)]
        dp[0][0] = 1
        for r in range(1, m):
            for i in range(r):
                if grid[i][0] + i >= r:
                    dp[r][0] = min(dp[r][0], dp[i][0] + 1)

        for c in range(1, n):
            for j in range(c):
                if grid[0][j] + j >= c:
                    dp[0][c] = min(dp[0][c], dp[0][j] + 1)

        for r in range(1, m):
            for c in range(1, n):
                for i in range(r):
                    if grid[i][c] + i >= r:
                        dp[r][c] = min(dp[r][c], dp[i][c] + 1)
                for j in range(c):
                    if grid[r][j] + j >= c:
                        dp[r][c] = min(dp[r][c], dp[r][j] + 1)

        return -1 if dp[-1][-1] == 10 ** 6 else dp[-1][-1]


def test_minimum_visited_cells():
    solution = Solution()
    assert solution.minimumVisitedCells([[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]]) == 4, 'wrong result'
    assert solution.minimumVisitedCells([[3, 4, 2, 1], [4, 2, 1, 1], [2, 1, 1, 0], [3, 4, 1, 0]]) == 3, 'wrong result'
    assert solution.minimumVisitedCells([[2, 1, 0], [1, 0, 0]]) == -1, 'wrong result'


if __name__ == '__main__':
    test_minimum_visited_cells()
