from re import match


class Solution:
    def maximumTime(self, time: str) -> str:
        for h in range(24)[::-1]:
            for m in range(60)[::-1]:
                t = f'{h:02}:{m:02}'

                if match(time.replace('?', '.'), t):
                    return t

    def maximumTime1(self, time: str) -> str:
        res = ''
        i, n = 0, len(time)

        while i < n:
            if time[i] == '?':
                if i == 0:
                    if time[1] == '?':
                        res += '23'
                        i += 1
                    elif time[1] < '4':
                        res += '2'
                    else:
                        res += '1'
                elif i == 1:
                    if res[0] < '2':
                        res += '9'
                    else:
                        res += '3'
                elif i == 3:
                    res += '5'
                else:
                    res += '9'
                pass
            else:
                res += time[i]
            i += 1

        return res


def test_maximum_time():
    solution = Solution()
    assert solution.maximumTime('2?:?0') == '23:50', 'wrong result'
    assert solution.maximumTime('0?:3?') == '09:39', 'wrong result'
    assert solution.maximumTime('1?:22') == '19:22', 'wrong result'


if __name__ == '__main__':
    test_maximum_time()
