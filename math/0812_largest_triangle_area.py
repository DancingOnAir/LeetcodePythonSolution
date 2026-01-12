from typing import List
from itertools import combinations


class Solution:
    # https://leetcode.com/problems/largest-triangle-area/solutions/122711/cjavapython-solution-with-explanation-an-4cwg/
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(0.5 * abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - b[0] * a[1] - c[0] * b[1] - a[0] * c[1]) for a, b, c in combinations(points, 3))


def test_largest_triangle_area():
    solution = Solution()
    assert abs(solution.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]) - 2.00000) < 10 ** (
        -5), 'wrong result'
    assert abs(solution.largestTriangleArea([[1, 0], [0, 0], [0, 1]]) - 0.50000) < 10 ** (-5), 'wrong result'


if __name__ == '__main__':
    test_largest_triangle_area()
