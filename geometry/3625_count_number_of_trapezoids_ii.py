from typing import List
from collections import defaultdict, Counter


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        cnt1 = defaultdict(list)
        cnt2 = defaultdict(list)
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for x2, y2 in points[:i]:
                dx = x1 - x2
                dy = y1 - y2
                k = dy / dx if dx else float('inf')
                b = (dx * y1 - dy * x1) / dx if dx else x1
                cnt1[k].append(b)
                cnt2[(x1 + x2, y1 + y2)].append(k)

        res = 0
        for x in cnt1.values():
            if len(x) == 1:
                continue
            tot = 0
            for c in Counter(x).values():
                res += tot * c
                tot += c

        for x in cnt2.values():
            if len(x) == 1:
                continue
            tot = 0
            for c in Counter(x).values():
                res -= tot * c
                tot += c

        return res


def test_count_trapezoids():
    solution = Solution()
    assert solution.countTrapezoids([[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]) == 2, 'wrong result'
    assert solution.countTrapezoids([[0, 0], [1, 0], [0, 1], [2, 1]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_count_trapezoids()
