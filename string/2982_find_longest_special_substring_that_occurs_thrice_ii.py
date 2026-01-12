from collections import defaultdict
from itertools import groupby


class Solution:
    def maximumLength1(self, s: str) -> int:
        cnt = [(k, len(list(g))) for k, g in groupby(s)]

        lengths = [[] for _ in range(26)]
        for k, sz in cnt:
            i = ord(k) - ord('a')
            lengths[i].append(sz)

        res = -1
        # 26
        for l in lengths:
            if len(l) == 1:
                if l[0] > 2:
                    res = max(res, l[0] - 2)
            elif len(l) == 2:
                # nlog(n)
                l.sort()
                if l[-1] > 1:
                    res = max(res, min(l[-1] - 1, l[0]), l[-1] - 2)
            elif len(l) > 2:
                # nlog(n)
                l.sort()
                res = max(res, l[-1] - 2)
                res = max(res, min(l[-1] - 1, l[-2]))
                res = max(res, l[-3])

        return res

    # O(n)
    def maximumLength(self, s: str) -> int:
        subs = [''.join(g) for _, g in groupby(s)]

        m = defaultdict(int)
        for sub in subs:
            m[sub] += 1
            if len(sub) > 1:
                m[sub[1:]] += 2
            if len(sub) > 2:
                m[sub[2:]] += 3

        return max(map(len, filter(lambda x: m[x] > 2, m.keys())), default=-1)


def test_maximum_length():
    solution = Solution()
    assert solution.maximumLength("aaaa") == 2, 'wrong result'
    assert solution.maximumLength("abcdef") == -1, 'wrong result'
    assert solution.maximumLength("abcaba") == 1, 'wrong result'


if __name__ == '__main__':
    test_maximum_length()
