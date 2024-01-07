from itertools import groupby
from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        m = defaultdict(int)
        for i, ch in enumerate(s):
            cnt = 1
            m[(ch, cnt)] += 1
            for j in range(i, len(s)):
                if j + 1 < len(s) and s[j] == s[j + 1]:
                    cnt += 1
                    m[(ch, cnt)] += 1
                else:
                    break

        res = -1
        for k, v in m.items():
            if v > 2:
                res = max(res, k[1])
        return res

    def maximumLength1(self, s: str) -> int:
        cnt = [(k, len(list(g))) for k, g in groupby(s)]

        lengths = [[] for _ in range(26)]
        for k, sz in cnt:
            i = ord(k) - ord('a')
            lengths[i].append(sz)

        res = -1
        for l in lengths:
            if len(l) == 1:
                if l[0] > 2:
                    res = max(res, l[0] - 2)
            elif len(l) == 2:
                l.sort()
                if l[-1] > 1:
                    res = max(res, min(l[-1] - 1, l[0]), l[-1] - 2)
            elif len(l) > 2:
                l.sort()
                res = max(res, l[-1] - 2)
                res = max(res, min(l[-1] - 1, l[-2]))
                res = max(res, l[-3])

        return res


def test_maximum_length():
    solution = Solution()
    assert solution.maximumLength("eccdnmcnkl") == 1, 'wrong result'
    assert solution.maximumLength("aaaa") == 2, 'wrong result'
    assert solution.maximumLength("abcdef") == -1, 'wrong result'
    assert solution.maximumLength("abcaba") == 1, 'wrong result'


if __name__ == '__main__':
    test_maximum_length()
