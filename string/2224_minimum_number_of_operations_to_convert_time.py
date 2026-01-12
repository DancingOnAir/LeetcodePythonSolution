class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def get_minutes(x):
            return int(x[:2]) * 60 + int(x[-2:])

        diff = get_minutes(correct) - get_minutes(current)
        res = 0
        for x in [60, 15, 5, 1]:
            res += diff // x
            diff %= x
        return res


def test_convert_time():
    solution = Solution()
    assert solution.convertTime("02:30", "04:35") == 3, 'wrong result'
    assert solution.convertTime("11:00", "11:01") == 1, 'wrong result'


if __name__ == '__main__':
    test_convert_time()
