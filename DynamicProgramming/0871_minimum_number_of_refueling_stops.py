from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pass


def test_min_refuel_stops():
    solution = Solution()
    assert solution.minRefuelStops(1, 1, []) == 0, 'wrong result'
    assert solution.minRefuelStops(100, 1, [[10, 100]]) == -1, 'wrong result'
    assert solution.minRefuelStops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_refuel_stops()
