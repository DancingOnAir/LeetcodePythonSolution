from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                res[i][j] = max(grid[ii][jj] for ii in range(i, i + 3) for jj in range(j, j + 3))
        return res

    def largestLocal1(self, grid: List[List[int]]) -> List[List[int]]:
        tmp = list()
        for row in grid:
            tmp.append([max(row[i:i + 3]) for i in range(len(row) - 2)])

        res = list()
        for col in zip(*tmp):
            res.append([max(col[i:i + 3]) for i in range(len(col) - 2)])

        return [[*col] for col in zip(*res)]


def test_largest_local():
    solution = Solution()
    assert solution.largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]) == [[9, 9], [8, 6]], 'wrong result'
    assert solution.largestLocal([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == [[2, 2, 2], [2, 2, 2], [2, 2, 2]], 'wrong result'


if __name__ == '__main__':
    test_largest_local()
