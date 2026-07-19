class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def getTimeInSeconds(time: str) -> int:
            h, m, s = map(int, time.split(":"))
            return h * 3600 + m * 60 + s
        return getTimeInSeconds(endTime) - getTimeInSeconds(startTime)


def test_seconds_between_times():
    solution = Solution()
    assert solution.secondsBetweenTimes("01:00:00", endTime = "01:00:25") == 25, 'wrong result'
    assert solution.secondsBetweenTimes("12:34:56", endTime = "13:00:00") == 1504, 'wrong result'


if __name__ == '__main__':
    test_seconds_between_times()
