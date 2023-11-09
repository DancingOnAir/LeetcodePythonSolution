class Solution:
    def countTime(self, time: str) -> int:
        res = 1
        if time[0] == '?' and time[1] == '?':
            res = 24
        elif time[0] == '?':
            res = 3 if time[1] < '4' else 2
        elif time[1] == '?':
            res = 10 if time[0] < '2' else 4

        if time[3] == '?' and time[4] == '?':
            res *= 60
        elif time[3] == '?':
            res *= 6
        elif time[4] == '?':
            res *= 10

        return res


def test_count_time():
    solution = Solution()
    assert solution.countTime("?5:00") == 2, 'wrong result'
    assert solution.countTime("0?:0?") == 100, 'wrong result'
    assert solution.countTime("??:??") == 1440, 'wrong result'


if __name__ == '__main__':
    test_count_time()
