from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        rectangles = sorted((p1, p2) for p1, p2 in zip(bottomLeft, topRight))

        res = 0
        for i in range(len(rectangles) - 1):
            for j in range(i + 1, len(rectangles)):
                w = min(rectangles[j][1][0], rectangles[i][1][0]) - max(rectangles[j][0][0], rectangles[i][0][0])
                h = min(rectangles[j][1][1], rectangles[i][1][1]) - max(rectangles[j][0][1], rectangles[i][0][1])
                side = min(w, h)
                if side > 0:
                    res = max(res, side * side)

        return res


def test_largest_square_area():
    solution = Solution()
    assert solution.largestSquareArea([[1, 1], [2, 2], [3, 1]], [[3, 3], [4, 4], [6, 6]]) == 1, 'wrong result'
    assert solution.largestSquareArea([[1, 1], [2, 2], [1, 2]], [[3, 3], [4, 4], [3, 4]]) == 1, 'wrong result'
    assert solution.largestSquareArea([[1, 1], [3, 3], [3, 1]], [[2, 2], [4, 4], [4, 2]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_largest_square_area()
