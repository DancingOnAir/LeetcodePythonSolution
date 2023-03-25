from typing import List
from bisect import bisect_left


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = 0
        for x in houses:
            i = bisect_left(heaters, x)
            if i == 0:
                cur = heaters[i] - x
            elif i == len(heaters):
                cur = x - heaters[i - 1]
            else:
                cur = min(heaters[i] - x, x - heaters[i - 1])
            res = max(res, cur)

        return res


def test_find_radius():
    solution = Solution()
    assert solution.findRadius([1, 2, 3], [2]) == 1, 'wrong result'
    assert solution.findRadius([1, 2, 3, 4], [1, 4]) == 1, 'wrong result'
    assert solution.findRadius([1, 5], [2]) == 3, 'wrong result'


if __name__ == '__main__':
    test_find_radius()
