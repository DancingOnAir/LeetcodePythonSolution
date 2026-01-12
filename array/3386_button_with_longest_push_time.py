from typing import List
from heapq import heappush, heappop


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        hp = []
        heappush(hp, (-events[0][1], events[0][0]))
        for i in range(1, len(events)):
            heappush(hp, (-events[i][1] + events[i - 1][1], events[i][0]))
        return heappop(hp)[1]


def test_button_with_longest_time():
    solution = Solution()
    assert solution.buttonWithLongestTime([[1, 2], [2, 5], [3, 9], [1, 15]]) == 1, 'wrong result'
    assert solution.buttonWithLongestTime([[10, 5], [1, 7]]) == 10, 'wrong result'


if __name__ == '__main__':
    test_button_with_longest_time()
