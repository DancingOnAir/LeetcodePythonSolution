from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for x1, y1, r in queries:
            cur = 0
            for x2, y2 in points:
                cur += ((x2 - x1) ** 2 + (y2 - y1) ** 2 <= r * r)
            res.append(cur)
        return res


def test_count_points():
    solution = Solution()
    assert solution.countPoints([[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]]) == [3, 2, 2], 'wrong result'
    assert solution.countPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]) == [2, 3, 2, 4], 'wrong result'


if __name__ == '__main__':
    test_count_points()
