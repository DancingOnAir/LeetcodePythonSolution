from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # 遍历斜线
        for k in range(1, m + n):
            min_j = max(0, n - k)
            max_j = min(n - 1, m + n - k - 1)
            temp = [grid[k + j - n][j] for j in range(min_j, max_j + 1)]
            # min_j > 0时斜线处于右上方
            temp.sort(reverse=min_j == 0)
            for j, val in zip(range(min_j, max_j + 1), temp):
                grid[k + j - n][j] = val
        return grid


def test_sort_matrix():
    solution = Solution()
    assert solution.sortMatrix([[1,7,3],[9,8,2],[4,5,6]])[0][0] == 8, 'wrong result'
    assert solution.sortMatrix([[0,1],[1,2]])[0][0] == 2, 'wrong result'


if __name__ == '__main__':
    test_sort_matrix()
