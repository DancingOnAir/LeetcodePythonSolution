from collections import defaultdict
from string import ascii_lowercase


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(idx):
            if uf[idx] != idx:
                idx = find(uf[idx])
            return uf[idx]

        def unite(p, q):
            rp = find(p)
            rq = find(q)
            if rp > rq:
                uf[rp] = rq
            else:
                uf[rq] = rp

        uf = {c: c for c in ascii_lowercase}
        for i in range(len(s1)):
            unite(s1[i], s2[i])

        res = []
        for c in baseStr:
            res.append(find(c))
        return ''.join(res)


def test_smallest_equivalent_string():
    solution = Solution()
    assert solution.smallestEquivalentString("parker", "morris", "parser") == "makkek", 'wrong result'
    assert solution.smallestEquivalentString("hello", "world", "hold") == "hdld", 'wrong result'
    assert solution.smallestEquivalentString("leetcode", "programs", "sourcecode") == "aauaaaaada", 'wrong result'


if __name__ == '__main__':
    test_smallest_equivalent_string()
