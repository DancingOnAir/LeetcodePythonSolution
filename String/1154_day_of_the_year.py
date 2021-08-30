class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            months[1] = 29

        return d + sum(months[:m - 1])


def test_day_of_year():
    solution = Solution()

    assert solution.dayOfYear("2019-01-09") == 9, 'wrong result'
    assert solution.dayOfYear("2019-02-10") == 41, 'wrong result'
    assert solution.dayOfYear("2003-03-01") == 60, 'wrong result'
    assert solution.dayOfYear("2004-03-01") == 61, 'wrong result'


if __name__ == '__main__':
    test_day_of_year()
