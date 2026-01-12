from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        res, pre = 0, 0

        for r in range(n):
            for c in range(m):
                x = grid[r - 1][c] if r > 0 else 0
                y = grid[r][c - 1] if c > 0 else 0
                pre = grid[r - 1][c - 1] if r > 0 and c > 0 else 0
                cur = x + y - pre + grid[r][c]
                grid[r][c] = cur

                if cur < k:
                    res += 1
        return res


def test_count_submatrices():
    solution = Solution()
    # assert solution.countSubmatrices([[7, 6, 3], [6, 6, 1]], 18) == 4, 'wrong result'
    assert solution.countSubmatrices([[7, 2, 9], [1, 5, 0], [2, 6, 6]], 20) == 6, 'wrong result'


if __name__ == '__main__':
    test_count_submatrices()
