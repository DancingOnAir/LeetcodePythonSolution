from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        res, right = 0, -1
        for x, _ in sorted(points, key=lambda p: p[0]):
            if right < x:
                res += 1
                right = x + w

        return res


def test_min_rectangles_to_cover_points():
    solution = Solution()
    assert solution.minRectanglesToCoverPoints([[2, 1], [1, 0], [1, 4], [1, 8], [3, 5], [4, 6]], 1) == 2, 'wrong result'
    assert solution.minRectanglesToCoverPoints([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]],
                                               2) == 3, 'wrong result'
    assert solution.minRectanglesToCoverPoints([[2, 3], [1, 2]], 0) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_rectangles_to_cover_points()
