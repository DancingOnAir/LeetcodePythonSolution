from typing import List
from itertools import accumulate


class Solution:
    # diff array
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        d = [0] * (n + 1)
        for f, l, s in bookings:
            d[f] += s
            if l < n:
                d[l + 1] -= s

        return list(accumulate(d))[1:]


def test_corp_flight_bookings():
    solution = Solution()
    assert solution.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5) == [10, 55, 45, 25, 25], 'wrong result'
    assert solution.corpFlightBookings([[1, 2, 10], [2, 2, 15]], 2) == [10, 25], 'wrong result'


if __name__ == '__main__':
    test_corp_flight_bookings()
