from itertools import accumulate


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ps = list(accumulate(days))

        def helper(date):
            return ps[int(date[:2]) - 1] + int(date[-2:])

        return max(0, helper(min(leaveAlice, leaveBob)) - helper(max(arriveAlice, arriveBob)) + 1)


def test_count_days_together():
    solution = Solution()
    assert solution.countDaysTogether("01-15", "01-18", "01-16", "01-19") == 3, 'wrong result'
    assert solution.countDaysTogether("08-15", "08-18", "08-16", "08-19") == 3, 'wrong result'
    assert solution.countDaysTogether("10-01", "10-31", "11-01", "12-31") == 0, 'wrong result'


if __name__ == '__main__':
    test_count_days_together()
