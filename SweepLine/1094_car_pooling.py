from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        endpoints = list()
        for n, s, e in trips:
            endpoints.append([s, n])
            endpoints.append([e, -n])

        mx = cur = 0
        for i, diff in sorted(endpoints):
            cur += diff
            mx = max(mx, cur)
        return mx <= capacity


def test_car_pooling():
    solution = Solution()
    assert not solution.carPooling([[2, 1, 5], [3, 3, 7]], 4), 'wrong result'
    assert solution.carPooling([[2, 1, 5], [3, 3, 7]], 5), 'wrong result'


if __name__ == '__main__':
    test_car_pooling()
