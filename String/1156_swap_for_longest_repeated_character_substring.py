from collections import Counter, defaultdict


class Solution:
    def maxRepOpt1(self, text: str) -> int:
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
