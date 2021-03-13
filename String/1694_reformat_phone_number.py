class Solution:
    def reformatNumber(self, number: str) -> str:
        def helper(digits, k):
            if len(digits) == 3:
                return digits
            return helper(digits[:-3], k - 1) + '-' + digits[-3:]

        res = ''
        for c in number:
            if c.isdigit():
                res += c
        n = len(res)
        i = n - 1
        q, r = divmod(n, 3)
        if r == 0:
            if not q:
                return res
            else:
                return helper(res[: 3 * q], q)
        elif r == 1:
            if q == 1:
                return res[-4: -2] + '-' + res[-2:]
            else:
                return helper((res[: 3 * (q - 1)]), q - 1) + '-' + res[-4: -2] + '-' + res[-2:]
        else:
            if not q:
                return res
            else:
                return helper(res[:3 * q], q) + '-' + res[-2:]

        return res


def test_reforamt_number():
    solution = Solution()
    # assert solution.reformatNumber('1-23-45 6') == '123-456', 'wrong result'
    assert solution.reformatNumber('123 4-567') == '123-45-67', 'wrong result'
    assert solution.reformatNumber('123 4-5678') == '123-456-78', 'wrong result'
    assert solution.reformatNumber('12') == '12', 'wrong result'
    assert solution.reformatNumber('--17-5 229 35-39475 ') == '175-229-353-94-75', 'wrong result'


if __name__ == '__main__':
    test_reforamt_number()

