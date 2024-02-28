from typing import List
from collections import defaultdict


class Node:
    def __init__(self):
        self.son = dict()
        self.cnt = 0


class Solution:

    # dict tree
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
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
