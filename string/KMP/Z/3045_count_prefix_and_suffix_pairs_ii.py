from typing import List
from collections import defaultdict


class Node:
    def __init__(self):
        self.son = dict()
        self.cnt = 0


class Solution:
    # z algorithm
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # z[i]的定义是后缀s[i:]与s的最长公共前缀长度
        # 如果z[i] = n - i说明前缀，后缀相等
        def cal_z(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = max(min(z[i - l], r - i + 1), 0)

                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    l, r = i, z[i] + i
                    z[i] += 1

            z[0] = n
            return z

        res = 0
        root = Node()
        for w in words:
            z = cal_z(w)
            cur = root
            for i, c in enumerate(w):
                if c not in cur.son:
                    cur.son[c] = Node()
                cur = cur.son[c]
                # s[-i - i:] == s[: i + 1]
                if z[-1 - i] == i + 1:
                    res += cur.cnt
            cur.cnt += 1
        return res

    # dict tree
    def countPrefixSuffixPairs2(self, words: List[str]) -> int:
        res = 0
        root = Node()
        for w in words:
            cur = root
            for p in zip(w, w[::-1]):
                if p not in cur.son:
                    cur.son[p] = Node()
                cur = cur.son[p]
                res += cur.cnt
            cur.cnt += 1
        return res

    # straight forward
    def countPrefixSuffixPairs1(self, words: List[str]) -> int:
        m = defaultdict(int)
        lengths = set()
        res = 0
        for w in words:
            n = len(w)
            for i in lengths:
                if i <= n and w[:i] == w[-i:]:
                    res += m[w[:i]]
            m[w] += 1
            lengths.add(n)
        return res


def test_count_prefix_suffix_paris():
    solution = Solution()
    assert solution.countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]) == 4, 'wrong result'
    assert solution.countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]) == 2, 'wrong result'
    assert solution.countPrefixSuffixPairs(["abab","ab"]) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_prefix_suffix_paris()
