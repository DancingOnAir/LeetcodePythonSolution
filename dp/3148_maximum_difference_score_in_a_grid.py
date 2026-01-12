from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        res = float('-inf')
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                pre = min(grid[i - 1][j] if i > 0 else float('inf'), grid[i][j - 1] if j > 0 else float('inf'))
                res = max(res, grid[i][j] - pre)
                grid[i][j] = min(grid[i][j], pre)
        return res


def test_max_score():
    solution = Solution()
    assert solution.maxScore([[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]]) == 9, 'wrong result'
    assert solution.maxScore([[4, 3, 2], [3, 2, 1]]) == -1, 'wrong result'


if __name__ == '__main__':
    test_max_score()
