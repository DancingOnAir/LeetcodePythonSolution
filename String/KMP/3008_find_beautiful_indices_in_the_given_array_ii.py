from typing import List
from bisect import bisect_left


class Solution:
    # kmp + two pointers
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def get_next(txt):
            n = len(txt)
            nxt = [0] * n
            j = 0
            for i in range(1, n):
                while j > 0 and txt[i] != txt[j]:
                    j = nxt[j - 1]
                if txt[i] == txt[j]:
                    j += 1
                nxt[i] = j
            return nxt

        def kmp(txt, pattern):
            nxt = get_next(pattern)
            j = 0
            pos = []
            for i, ch in enumerate(txt):
                while j > 0 and ch != pattern[j]:
                    j = nxt[j - 1]
                if ch == pattern[j]:
                    j += 1
                if j == len(pattern):
                    pos.append(i - j + 1)
                    j = nxt[j - 1]
            return pos

        res = []
        pa = kmp(s, a)
        pb = kmp(s, b)
        j = 0
        for x in pa:
            while j < len(pb) and pb[j] < x - k:
                j += 1
            if j < len(pb) and abs(pb[j] - x) <= k:
                res.append(x)

        return res

    # kmp + binary search
    def beautifulIndices1(self, s: str, a: str, b: str, k: int) -> List[int]:
        def get_next(ss):
            nxt = [0] * len(ss)
            j = 0
            for i in range(1, len(ss)):
                while j > 0 and ss[i] != ss[j]:
                    j = nxt[j - 1]
                if ss[i] == ss[j]:
                    j += 1
                nxt[i] = j
            return nxt

        def kmp(txt, pattern):
            nxt = get_next(pattern)
            p = []
            j = 0
            for i, ch in enumerate(txt):
                while j > 0 and ch != pattern[j]:
                    j = nxt[j - 1]
                if ch == pattern[j]:
                    j += 1
                if j == len(pattern):
                    p.append(i - j + 1)
                    j = nxt[j - 1]
            return p

        pa = kmp(s, a)
        pb = kmp(s, b)

        res = []
        for x in pa:
            i = bisect_left(pb, x)
            if (i < len(pb) and pb[i] - x <= k) or (i > 0 and x - pb[i - 1] <= k):
                res.append(x)
        return res


def test_beautiful_indices():
    solution = Solution()
    assert solution.beautifulIndices("xxtxxuftxt", "tx", "x", 2) == [2, 7], 'wrong result'
    assert solution.beautifulIndices("isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15) == [16, 33], 'wrong result'
    assert solution.beautifulIndices("abcd", "a", "a", 4) == [0], 'wrong result'


if __name__ == '__main__':
    test_beautiful_indices()
