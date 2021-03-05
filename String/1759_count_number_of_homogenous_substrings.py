from itertools import groupby


class Solution:
    # https://stackoverflow.com/questions/773/how-do-i-use-itertools-groupby
    # itertools.groupby
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    def countHomogenous2(self, s: str) -> int:
        res = 0
        for c, s in groupby(s):
            n = len(list(s))
            res += n * (n + 1) // 2
        return res % (10 ** 9 + 7)

    def countHomogenous(self, s: str) -> int:
        res, cnt = 0, 0
        for i, val in enumerate(s):
            if not i or s[i - 1] == val:
                cnt += 1
            else:
                cnt = 1
            res += cnt
        return res % (10 ** 9 + 7)

    def countHomogenous1(self, s: str) -> int:
        n = 1
        res = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                n += 1
            else:
                res += (1 + n) * n // 2
                n = 1

        res += (1 + n) * n // 2
        return res % (10 ** 9 + 7)


def test_count_homogenous():
    solution = Solution()
    assert solution.countHomogenous('abbcccaa') == 13, 'wrong result'
    assert solution.countHomogenous('xy') == 2, 'wrong result'
    assert solution.countHomogenous('zzzzz') == 15, 'wrong result'


if __name__ == '__main__':
    test_count_homogenous()
