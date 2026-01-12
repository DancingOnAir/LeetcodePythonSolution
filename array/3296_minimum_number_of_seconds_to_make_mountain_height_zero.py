from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        hp = []
        for t in workerTimes:
            heappush(hp, (t, 1, t))

        for _ in range(mountainHeight):
            time, cnt, base = heappop(hp)
            heappush(hp, (time + base * (cnt + 1),cnt + 1, base))
        return time


def test_min_number_of_seconds():
    solution = Solution()
    assert solution.minNumberOfSeconds(4, [2, 1, 1]) == 3, 'wrong result'
    assert solution.minNumberOfSeconds(10, [3, 2, 2, 4]) == 12, 'wrong result'
    assert solution.minNumberOfSeconds(5, [1]) == 15, 'wrong result'


if __name__ == '__main__':
    test_min_number_of_seconds()
