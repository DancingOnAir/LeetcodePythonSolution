from typing import List
from collections import defaultdict


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        m = defaultdict(list)
        for x, y in points:
            m[x].append(y)

        res = float('inf')
        last_x = dict()
        for x in sorted(m):
            y = m[x]
            y.sort()

            for j, y2 in enumerate(y):
                for i in range(j):
                    y1 = y[i]
                    if (y1, y2) in last_x:
                        res = min(res, (x - last_x[(y1, y2)]) * (y2 - y1))
                    last_x[(y1, y2)] = x
        return res if res < float('inf') else 0


def test_min_area_rect():
    solution = Solution()
    assert solution.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]) == 4, 'wrong result'
    assert solution.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_area_rect()
