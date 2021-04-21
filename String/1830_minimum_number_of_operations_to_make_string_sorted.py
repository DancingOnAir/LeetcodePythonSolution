class Solution:
    def makeStringSorted(self, s: str) -> int:
        n = len(s)
        sorted_s = ''.join(sorted(s))

        res = 0
        while s != sorted_s:
            cur = n - 1
            while s[cur - 1] <= s[cur]:
                # if cur
                cur -= 1

            pre = cur - 1
            while cur < n - 1 and s[cur + 1] < s[pre]:
                cur += 1

            interval_str = ''
            if pre + 1 < cur:
                interval_str = s[pre + 1: cur]
            s = s[:pre] + s[cur] + (interval_str + s[pre] + s[cur + 1:])[::-1]

            res += 1
        return res % (10 ** 9 + 7)


def test_make_string_sorted():
    solution = Solution()
    assert solution.makeStringSorted('cba') == 5, 'wrong result'
    assert solution.makeStringSorted('aabaa') == 2, 'wrong result'
    assert solution.makeStringSorted('cdbea') == 63, 'wrong result'
    assert solution.makeStringSorted('leetcodeleetcodeleetcode') == 982157772, 'wrong result'


if __name__ == '__main__':
    test_make_string_sorted()
