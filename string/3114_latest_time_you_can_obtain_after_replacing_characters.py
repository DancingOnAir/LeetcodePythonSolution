class Solution:
    def findLatestTime(self, s: str) -> str:
        s = list(s)
        if s[0] == '?':
            s[0] = '1' if s[1] == '?' or s[1] < '2' else '0'
        if s[1] == '?':
            s[1] = '1' if s[0] == '1' else '9'
        if s[3] == '?':
            s[3] = '5'
        if s[4] == '?':
            s[4] = '9'
        return ''.join(s)

    def findLatestTime1(self, s: str) -> str:
        res = []
        for i, c in enumerate(s):
            if i == 2 or c != '?':
                res.append(c)
            else:
                if i == 0:
                    if s[1] == '0' or s[1] == '1' or s[1] == '?':
                        res.append('1')
                    else:
                        res.append('0')
                elif i == 1:
                    if res[-1] == '1':
                        res.append('1')
                    else:
                        res.append('9')
                elif i == 3:
                    res.append('5')
                else:
                    res.append('9')
        return ''.join(res)


def test_find_latest_time():
    solution = Solution()
    assert solution.findLatestTime("??:1?") == "11:19", 'wrong result'
    assert solution.findLatestTime("1?:?4") == "11:54", 'wrong result'
    assert solution.findLatestTime("0?:5?") == "09:59", 'wrong result'


if __name__ == '__main__':
    test_find_latest_time()
