from typing import List


class Solution:
    # sweep line
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n + 1)
        for i, j, x in bookings:
            res[i - 1] += x
            res[j] -= x

        for i in range(1, n):
            res[i] += res[i - 1]
        return res[:-1]


def test_corp_flight_bookings():
    solution = Solution()
    assert solution.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5) == [10, 55, 45, 25, 25], 'wrong result'
    assert solution.corpFlightBookings([[1, 2, 10], [2, 2, 15]], 2) == [10, 25], 'wrong result'


if __name__ == '__main__':
    test_corp_flight_bookings()

