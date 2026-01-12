from itertools import zip_longest


class Solution:
    def reformat(self, s: str) -> str:
        digits = list()
        alphabets = list()

        for c in s:
            if c.isdigit():
                digits += [c]
            else:
                alphabets += [c]

        if abs(len(alphabets) - len(digits)) > 1:
            return ''

        if len(digits) < len(alphabets):
            alphabets, digits = digits, alphabets
        return ''.join(d+a for d, a in zip_longest(digits, alphabets, fillvalue=''))


def test_reformat():
    solution = Solution()
    assert solution.reformat('a0b1c2') == '0a1b2c', 'wrong result'
    assert solution.reformat('leetcode') == '', 'wrong result'
    assert solution.reformat('1229857369') == '', 'wrong result'
    assert solution.reformat('covid2019') == 'c2o0v1i9d', 'wrong result'
    assert solution.reformat('ab123') == '1a2b3', 'wrong result'


if __name__ == '__main__':
    test_reformat()
