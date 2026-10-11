from itertools import pairwise


class Solution:
    def minRotations(self, n: int, s: str) -> int:
        def dist(x: int, y: int) -> int:
            d = abs(x - y)
            return min(d, 10 - d)

        s = list(map(ord, s))
        suf = 0
        for x, y in pairwise(s):
            suf += dist(x, y)

        res = dist(ord('0'), s[-1]) + suf

        pre = dist(ord('0'), s[0])
        for x, y in pairwise(s):
            op = dist(x, y)
            suf -= op
            res = min(res, pre + dist(x, s[-1]) + suf)
            pre += op
        return res


def test_min_rotations():
    solution = Solution()
    assert solution.minRotations(4, "1502") == 9, 'wrong result'
    assert solution.minRotations(4, "2916") == 12, 'wrong result'
    assert solution.minRotations(4, "4219") == 6, 'wrong result'


if __name__ == '__main__':
    test_min_rotations()
