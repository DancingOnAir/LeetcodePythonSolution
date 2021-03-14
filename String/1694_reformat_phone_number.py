import re


class Solution:
    def reformatNumber(self, number: str) -> str:
        res = []
        number = number.replace('-', '').replace(' ', '')

        i, n = 0, len(number)
        while i < n:
            if i + 4 == n:
                res.append(number[i: i + 2])
                i += 2
            elif i + 3 <= n:
                res.append(number[i: i + 3])
                i += 3
            else:
                res.append(number[i: i + 2])
                i += 2
        if len(res) > 2:
            return '-'.join(res)

        return res[0]

    # regex
    # https://leetcode.com/problems/reformat-phone-number/discuss/979806/1-liner-Python-Java-C%2B%2B
    def reformatNumber2(self, number: str) -> str:
        return re.sub('(...?(?=..))', r'\1-', re.sub('\D', '', number))

    def reformatNumber1(self, number: str) -> str:
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

