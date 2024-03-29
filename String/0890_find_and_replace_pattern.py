from typing import List
from collections import defaultdict
from functools import lru_cache


class Solution:
    def findAndReplacePattern(self, words, p):
        def normalize(w):
            m = dict()
            return [m.setdefault(c, len(m)) for c in w]
        return [w for w in words if normalize(w) == normalize(p)]

    # isomorphic method
    def findAndReplacePattern2(self, words: List[str], pattern: str) -> List[str]:
        return [w for w in words if len(w) == len(pattern) and len(set(w)) == len(set(pattern)) == len(set(zip(w, pattern)))]

    def findAndReplacePattern1(self, words: List[str], pattern: str) -> List[str]:
        @lru_cache(None)
        def get_pos(word):
            m = defaultdict(list)
            for i, ch in enumerate(word):
                m[ch].append(i)
            return list(m.values())

        res = list()
        p = get_pos(pattern)
        for w in words:
            if get_pos(w) == p:
                res.append(w)
        return res


def test_find_and_replace_pattern():
    solution = Solution()

    assert solution.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb") == ["mee", "aqq"], 'wrong result'
    assert solution.findAndReplacePattern(["a", "b", "c"], "a") == ["a", "b", "c"], 'wrong result'


if __name__ == '__main__':
    test_find_and_replace_pattern()
