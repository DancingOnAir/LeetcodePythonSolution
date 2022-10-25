from typing import List
from bisect import bisect_right


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        passengers.sort()
        buses.sort()
        cap = cur = 0
        for time in buses:
            cap = capacity
            while cur < len(passengers) and passengers[cur] <= time and cap > 0:
                cur += 1
                cap -= 1

        res = buses[-1] if cap > 0 else passengers[cur - 1]
        passengers = set(passengers)
        while res in passengers:
            res -= 1
        return res


def test_latest_time_catch_the_bus():
    solution = Solution()
    assert solution.latestTimeCatchTheBus([6, 8, 18, 17], [6, 8, 17], 1) == 18, 'wrong result'
    assert solution.latestTimeCatchTheBus([10, 20], [2, 17, 18, 19], 2) == 16, 'wrong result'
    assert solution.latestTimeCatchTheBus([20, 30, 10], [19, 13, 26, 4, 25, 11, 21], 2) == 20, 'wrong result'


if __name__ == '__main__':
    test_latest_time_catch_the_bus()
