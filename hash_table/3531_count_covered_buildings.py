from typing import List
from collections import defaultdict


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rmax = [0] * (n + 1)
        rmin = [n + 1] * (n + 1)
        cmax = [0] * (n + 1)
        cmin = [n + 1] * (n + 1)

        for x, y in buildings:
            rmax[y] = max(rmax[y], x)
            rmin[y] = min(rmin[y], x)
            cmax[x] = max(cmax[x], y)
            cmin[x] = min(cmin[x], y)

        res = 0
        for x, y in buildings:
            if rmin[y] < x < rmax[y] and cmin[x] < y < cmax[x]:
                res += 1
        return res


def test_count_covered_buildings():
    solution = Solution()
    assert solution.countCoveredBuildings(3, [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]) == 1, 'wrong result'
    assert solution.countCoveredBuildings(3, [[1, 1], [1, 2], [2, 1], [2, 2]]) == 0, 'wrong result'
    assert solution.countCoveredBuildings(5, [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_count_covered_buildings()
