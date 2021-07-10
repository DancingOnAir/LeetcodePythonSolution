class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        if startTime > finishTime:
            return (96 - self.numberOfRounds("00:00", startTime) - (1 if int(startTime[-2:]) % 15 else 0)) + self.numberOfRounds("00:00", finishTime)

        hours = int(finishTime[:2]) - int(startTime[:2])
        q1, r1 = divmod(int(startTime[-2:]), 15)
        q2, r2 = divmod(int(finishTime[-2:]), 15)

        if hours == 0:
            return max(q2 - q1 - (0 if r1 == 0 else 1), 0)

        return 4 - q1 - (0 if r1 == 0 else 1) + q2 + (hours - 1) * 4


def test_number_of_rounds():
    solution = Solution()

    assert solution.numberOfRounds("12:01", "12:44") == 1, 'wrong result'
    assert solution.numberOfRounds("20:00", "06:00") == 40, 'wrong result'
    assert solution.numberOfRounds("00:00", "23:59") == 95, 'wrong result'
    assert solution.numberOfRounds("00:01", "00:00") == 95, 'wrong result'
    assert solution.numberOfRounds("00:47", "00:57") == 0, 'wrong result'


if __name__ == '__main__':
    test_number_of_rounds()
