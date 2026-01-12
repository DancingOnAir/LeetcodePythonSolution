from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def possible(x):
            return sum(x // t for t in time) >= totalTrips

        l, r = 1, totalTrips * min(time)
        while l <= r:
            mid = l + (r - l) // 2
            if possible(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

    def minimumTime1(self, time: List[int], totalTrips: int) -> int:
        def possible(k):
            total = 0
            for t in time:
                if t > k:
                    break
                total += k // t
            return total >= totalTrips

        n = len(time)
        time.sort()
        left, right = 1, totalTrips * time[0]
        while left <= right:
            mid = left + (right - left) // 2
            if possible(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


def test_minimum_time():
    solution = Solution()
    assert solution.minimumTime([9, 3, 10, 5], 2) == 5, 'wrong result'
    assert solution.minimumTime([1, 2, 3], 5) == 3, 'wrong result'
    assert solution.minimumTime([2], 1) == 2, 'wrong result'


if __name__ == '__main__':
    test_minimum_time()
