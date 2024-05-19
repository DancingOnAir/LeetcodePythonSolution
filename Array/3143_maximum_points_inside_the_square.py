from typing import List
from collections import defaultdict


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        min_radius = defaultdict(lambda: float('inf'))
        second_min_radius = float('inf')
        for radius, tag in zip([max(map(abs, p)) for p in points], s):
            if min_radius[tag] > radius:
                # 注意这里radius要取较大的值才能保证有2个相同的tag
                min_radius[tag], radius = radius, min_radius[tag]

            second_min_radius = min(second_min_radius, radius)
        return sum(radius < second_min_radius for radius in min_radius.values())

    def maxPointsInsideSquare1(self, points: List[List[int]], s: str) -> int:
        m = []
        for a, b in zip(points, s):
            m.append([max(map(abs, a)), b])

        res = 0
        seen = set()
        pre_radius = -1
        cnt = 0
        for a, b in sorted(m, key=lambda x: x[0]):
            if b in seen:
                if a != pre_radius:
                    res += cnt
                return res

            if a == pre_radius:
                cnt += 1
            else:
                pre_radius = a
                res += cnt
                cnt = 1
            seen.add(b)
        return res + cnt


def test_max_points_inside_square():
    solution = Solution()
    assert solution.maxPointsInsideSquare([[-1, -4], [16, -8], [13, -3], [-12, 0]], "abda") == 1, 'wrong result'
    assert solution.maxPointsInsideSquare([[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]], "abdca") == 2, 'wrong result'
    assert solution.maxPointsInsideSquare([[1, 1], [-2, -2], [-2, 2]], "abb") == 1, 'wrong result'
    assert solution.maxPointsInsideSquare([[1, 1], [-1, -1], [2, -2]], "ccd") == 0, 'wrong result'


if __name__ == '__main__':
    test_max_points_inside_square()
