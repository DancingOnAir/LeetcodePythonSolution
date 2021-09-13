from datetime import date


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap_year(y):
            if 0 == y % 400:
                return True
            elif 0 == y % 100:
                return False
            elif 0 == y % 4:
                return True
            return False

        def calculate_days(y, m, d):
            res = 0
            for i in range(1970, y):
                res += 366 if is_leap_year(i) else 365
            return res + pre_sum[m - 1] + d + (1 if is_leap_year(y) and m > 2 else 0)

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        pre_sum = [0]
        for i in days:
            pre_sum.append(i + pre_sum[-1])

        return abs(calculate_days(int(date1[:4]), int(date1[5: 7]), int(date1[8:])) -
                   calculate_days(int(date2[:4]), int(date2[5: 7]), int(date2[8:])))

    def daysBetweenDates1(self, date1: str, date2: str) -> int:
        return abs(date.fromisoformat(date2) - date.fromisoformat(date1)).days


def test_days_between_dates():
    solution = Solution()

    assert solution.daysBetweenDates("2019-06-29", "2019-06-30") == 1
    assert solution.daysBetweenDates("2020-01-15", "2019-12-31") == 15
    assert solution.daysBetweenDates("2100-09-22", "1991-03-12") == 40006
    assert solution.daysBetweenDates("2009-08-18", "2080-08-08") == 25923


if __name__ == '__main__':
    test_days_between_dates()
