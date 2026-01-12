from collections import Counter, defaultdict
from itertools import groupby


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        count = Counter(text)

        # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
        # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
        A = [[c, len(list(g))] for c, g in groupby(text)]
        # only extend 1 more
        res = max(min(count[c], k+1) for c, k in A)
        # merge 2 groups which are separated by only 1 character
        for i in range(1, len(A) - 1):
            if A[i][1] == 1 and A[i - 1][0] == A[i + 1][0]:
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i - 1][0]]))
        return res

    def maxRepOpt11(self, text: str) -> int:
        n = len(text)
        if n < 2:
            return 1

        cnt = Counter(text)
        i = 0
        d = defaultdict(int)
        unique = 0
        res = 0
        for j, c in enumerate(text):
            if c not in d:
                unique += 1

            d[c] += 1
            while i < n and (unique > 2 or (unique == 2 and min(d.values()) > 1)):
                d[text[i]] -= 1
                if d[text[i]] == 0:
                    unique -= 1
                    del d[text[i]]
                i += 1

            for k, v in d.items():
                if cnt[k] > v and unique == 2:
                    res = max(res, v + 1)
                else:
                    res = max(res, v)
        return res


def test_max_rep_opt1():
    solution = Solution()

    assert solution.maxRepOpt1('acbaaa') == 4, 'wrong result'
    assert solution.maxRepOpt1('ababa') == 3, 'wrong result'
    assert solution.maxRepOpt1('aaabaaa') == 6, 'wrong result'
    assert solution.maxRepOpt1('aaabbaaa') == 4, 'wrong result'
    assert solution.maxRepOpt1('aaaaa') == 5, 'wrong result'
    assert solution.maxRepOpt1('abcdef') == 1, 'wrong result'


if __name__ == '__main__':
    test_max_rep_opt1()
