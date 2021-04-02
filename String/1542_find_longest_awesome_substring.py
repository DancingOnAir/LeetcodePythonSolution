from collections import Counter


class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        res = 0
        for i in range(n):
            for j in range(i+1, n+1):
                ss = s[i:j]
                c = Counter(ss)
                if sum([1 for v in c.values() if (v & 0b1) == 1]) < 2:
                    res = max(res, len(ss))
        return res


def test_longest_awesome():
    solution = Solution()
    assert solution.longestAwesome('3242415') == 5, 'wrong result'
    assert solution.longestAwesome('12345678') == 1, 'wrong result'
    assert solution.longestAwesome('213123') == 6, 'wrong result'
    assert solution.longestAwesome('00') == 2, 'wrong result'


if __name__ == '__main__':
    test_longest_awesome()
