from typing import List
from collections import defaultdict


class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        def check(x1, y1, x2, y2):
            cnt = 0
            for i in range(n):
                if points[i][0] < x1 or points[i][0] > x2:
                    continue
                if points[i][1] < y1 or points[i][1] > y2:
                    continue
                if (points[i][0] == x1 or points[i][0] == x2) and (points[i][1] == y1 or points[i][1] == y2):
                    cnt += 1
                    continue
                return False
            return cnt == 4

        n = len(points)
        res = -1
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = min(points[i][0], points[j][0]), min(points[i][1], points[j][1])
                x2, y2 = max(points[i][0], points[j][0]), max(points[i][1], points[j][1])
                if check(x1, y1, x2, y2):
                    res = max(res, (x2 - x1) * (y2 - y1))

        return res


def test_max_rectangle_area():
    solution = Solution()
    assert solution.maxRectangleArea([[1, 1], [1, 3], [3, 1], [3, 3]]) == 4, 'wrong result'
    assert solution.maxRectangleArea([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]) == -1, 'wrong result'
    assert solution.maxRectangleArea([[1, 1], [1, 3], [3, 1], [3, 3], [1, 2], [3, 2]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_rectangle_area()
