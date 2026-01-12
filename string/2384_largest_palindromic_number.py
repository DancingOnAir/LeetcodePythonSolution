from collections import Counter


class Solution:
    # pythonic
    def largestPalindromic(self, num: str) -> str:
        c = Counter(num)
        res = ''.join(c[i] // 2 * i for i in '9876543210').lstrip('0')
        mid = max(v % 2 * k for k, v in c.items())
        return (res + mid + res[::-1]) or '0'

    # brute force
    def largestPalindromic1(self, num: str) -> str:
        res = []
        c = Counter(num)
        center = ''
        for k in sorted(c.keys(), reverse=True):
            if c[k] % 2 == 0:
                if k != '0' or res:
                    res += [k] * (c[k] // 2)
            else:
                if not center:
                    center = k

                if c[k] > 1:
                    if k != '0' or res:
                        res += [k] * (c[k] // 2)

        if not res and not center:
            return '0'
        return ''.join(res + [center] + res[::-1])


def test_largest_palindromic():
    solution = Solution()
    assert solution.largestPalindromic("0000") == "0", 'wrong result'
    assert solution.largestPalindromic("00000") == "0", 'wrong result'
    assert solution.largestPalindromic("444947137") == "7449447", 'wrong result'
    assert solution.largestPalindromic("00009") == "9", 'wrong result'


if __name__ == '__main__':
    test_largest_palindromic()
