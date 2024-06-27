from typing import List


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        # 顺时针旋转90度
        def rotate(g):
            return list(zip(*(g[::-1])))

        return min(self.f(grid), self.f(rotate(grid)))

    def f(self, grid):
        # g是grid以行为分割的子矩阵grid[:i][:]
        def minimum_area(g, l, r):
            left, right = len(g[0]), 0
            top, bottom = len(g), 0
            for i, row in enumerate(g):
                for j, x in enumerate(row[l: r]):
                    if x == 1:
                        left = min(left, j)
                        right = max(right, j)
                        bottom = i
                        top = min(top, i)
            return (right - left + 1) * (bottom - top + 1)

        m, n = len(grid), len(grid[0])
        res = m * n

        if m > 2:
            for i in range(1, m):
                for j in range(i + 1, m):
                    cur = minimum_area(grid[:i], 0, n)
                    cur += minimum_area(grid[i: j], 0, n)
                    cur += minimum_area(grid[j:], 0, n)
                    res = min(res, cur)

        if m > 1 and n > 1:
            for i in range(1, m):
                for j in range(1, n):
                    cur = minimum_area(grid[:i], 0, n)
                    cur += minimum_area(grid[i:], 0, j)
                    cur += minimum_area(grid[i:], j, n)
                    res = min(res, cur)

                    cur = minimum_area(grid[:i], 0, j)
                    cur += minimum_area(grid[:i], j, n)
                    cur += minimum_area(grid[i:], 0, n)
                    res = min(res, cur)

        return res


def test_minimum_sum():
    solution = Solution()
    assert solution.minimumSum([[1, 0, 1], [1, 1, 1]]) == 5, 'wrong result'
    assert solution.minimumSum([[1, 0, 1, 0], [0, 1, 0, 1]]) == 5, 'wrong result'


if __name__ == '__main__':
    test_minimum_sum()
