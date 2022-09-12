from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        pass


def test_most_booked():
    solution = Solution()
    assert solution.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]) == 0, 'wrong result'
    assert solution.mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_most_booked()

