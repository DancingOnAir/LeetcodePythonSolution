from typing import List


class Solution:
    # dp[i] represents the farthest distance when adding i-th gas
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= location:
                    dp[j + 1] = max(dp[j + 1], dp[j] + capacity)

        for i, dist in enumerate(dp):
            if dist >= target:
                return i

        return -1


def test_min_refuel_stops():
    solution = Solution()
    assert solution.minRefuelStops(1, 1, []) == 0, 'wrong result'
    assert solution.minRefuelStops(100, 1, [[10, 100]]) == -1, 'wrong result'
    assert solution.minRefuelStops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_refuel_stops()
