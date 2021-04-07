class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)[::-1]
        res = '.'.join(s[i: i+3] for i in range(0, len(s), 3))
        return res[::-1]

    def thousandSeparator2(self, n: int) -> str:
        n = str(n)
        q, r = divmod(len(n), 3)

        if not r:
            res = n[:3]
        else:
            res = n[:r]
        for i in range(1 if not r else 0, q):
            res += '.' + n[r + 3 * i: r + 3 * i + 3]
        return res

    def thousandSeparator1(self, n: int) -> str:
        res = list()
        for i, c in enumerate(str(n)[::-1]):
            res.append(c)
            if (i + 1) % 3 == 0 and (i + 1) != len(str(n)):
                res.append('.')
        return ''.join(res[::-1])


def test_thousand_separator():
    solution = Solution()
    assert solution.thousandSeparator(987) == "987", 'wrong result'
    assert solution.thousandSeparator(1234) == "1.234", 'wrong result'
    assert solution.thousandSeparator(123456789) == "123.456.789", 'wrong result'
    assert solution.thousandSeparator(0) == "0", 'wrong result'


if __name__ == '__main__':
    test_thousand_separator()
