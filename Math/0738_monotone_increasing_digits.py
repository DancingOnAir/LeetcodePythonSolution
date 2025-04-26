class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        to_nine = len(s)
        for i in range(len(s) - 1, 0, -1):
            if s[i - 1] > s[i]:
                s[i - 1] = str(int(s[i - 1]) - 1)
                to_nine = i

        for i in range(to_nine, len(s)):
            s[i] = '9'
        return int(''.join(s))

    def monotoneIncreasingDigits1(self, n: int) -> int:
        res = []
        pre = '0'
        last = -1
        s = str(n)
        for i, c in enumerate(s):
            if c >= pre:
                res.append(c)
                if c > pre:
                    last = i
                pre = c
            else:
                return int(''.join(res[:last] + [str(int(s[last]) - 1)] + ['9' for _ in range(len(s) - last - 1)]))

        return int(''.join(res))


def test_monotone_increasing_digits():
    solution = Solution()
    assert solution.monotoneIncreasingDigits(10) == 9, 'wrong result'
    assert solution.monotoneIncreasingDigits(1234) == 1234, 'wrong result'
    assert solution.monotoneIncreasingDigits(332) == 299, 'wrong result'


if __name__ == '__main__':
    test_monotone_increasing_digits()
