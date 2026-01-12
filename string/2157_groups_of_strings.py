from typing import List
from functools import lru_cache


class Solution:
    class UF(object):
        def __init__(self, n):
            self.parents = list(range(n))
            self.sz = [1] * n
            self.group = n

        def find(self, p):
            while p != self.parents[p]:
                self.parents[p] = self.parents[self.parents[p]]
                p = self.parents[p]
            return p

        def union(self, p, q):
            rp = self.find(p)
            rq = self.find(q)

            if rp == rq:
                return

            if self.sz[rp] < self.sz[rq]:
                self.parents[rp] = rq
                self.sz[rq] += self.sz[rp]
            else:
                self.parents[rq] = rp
                self.sz[rp] += self.sz[rq]

            self.group -= 1
    # bit mask + union find
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        uf = self.UF(n)
        memo = dict()
        del_memo = dict()

        for i in range(n):
            h = 0
            for ch in words[i]:
                h |= 1 << (ord(ch) - ord('a'))

            for j in range(26):
                # if h's j-th bit is 1
                if (h >> j) & 1:
                    # new h is the bitmask after deleting the j-th bit
                    del_h = h ^ (1 << j)
                    if del_h in memo:
                        uf.union(i, memo[del_h])
                    # rep h is the bitmask after replacing the j-th bit
                    if del_h in del_memo:
                        uf.union(i, del_memo[del_h])
                    else:
                        del_memo[del_h] = i
                    # for k in range(26):
                    #     rep_h = del_h | (1 << k)
                    #     if rep_h != del_h and rep_h in memo:
                    #         uf.union(i, memo[rep_h])
                else:
                    # add h is the bitmask after adding the j-th bit
                    add_h = h | (1 << j)
                    if add_h in memo:
                        uf.union(i, memo[add_h])

            memo[h] = i
        return [uf.group, max(uf.sz)]

    # set operation but TLE
    def groupStrings1(self, words: List[str]) -> List[int]:
        @lru_cache(None)
        def conntected(w1, w2):
            s1 = set(w1)
            s2 = set(w2)

            if abs(len(s1) - len(s2)) > 1:
                return False

            return len(s1 - s2) <= 1 and len(s2 - s1) <= 1

        n = len(words)
        uf = self.UF(n)
        for i in range(n):
            for j in range(i + 1, n):
                if conntected(words[i], words[j]):
                    uf.union(i, j)

        return [uf.group, max(uf.sz)]


def test_group_strings():
    solution = Solution()

    assert solution.groupStrings(["xo", "t", "uhc", "gf"]) == [4, 1], 'wong result'
    assert solution.groupStrings(["ghnv", "uip", "tenv", "hvepx", "e", "ktc", "byjdt", "ulm", "cae", "ea"]) == [8, 3], 'wong result'
    assert solution.groupStrings(["a", "b", "ab", "cde"]) == [2, 3], 'wong result'
    assert solution.groupStrings(["a", "ab", "abc"]) == [1, 3], 'wong result'


if __name__ == '__main__':
    test_group_strings()
