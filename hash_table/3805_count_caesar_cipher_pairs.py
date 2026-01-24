from typing import List
from collections import defaultdict, Counter
from functools import cache


class Solution:
    def countPairs(self, words: List[str]) -> int:
        @cache
        def norm(word: str):
            c1 = ord(word[0])
            if c1 == 0x61:
                return word.encode('ascii')
            return bytes((c - c1 + 26) % 26 + 0x61 for c in word.encode('ascii'))

        cnt = Counter(norm(w) for w in words)
        return sum(v * (v - 1) for v in cnt.values()) >> 1

    def countPairs1(self, words: List[str]) -> int:
        m = defaultdict(int)
        for w in words:
            diff = ""
            for i in range(len(w) - 1):
                diff += str(ord(w[i]) - ord(w[i + 1]) - (26 if w[i] > w[i + 1] else 0))
            m[diff] += 1

        res = 0
        for v in m.values():
            if v > 1:
                res += v * (v - 1) / 2
        return res


def test_count_pairs():
    solution = Solution()
    assert solution.countPairs(["fusion", "layout"]) == 1, 'wrong result'
    assert solution.countPairs(["ab", "aa", "za", "aa"]) == 2, 'wrong result'


if __name__ == '__main__':
    test_count_pairs()
