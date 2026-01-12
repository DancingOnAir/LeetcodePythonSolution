from typing import List
from collections import defaultdict
from functools import reduce
from itertools import product


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        m = defaultdict(int)
        for w in words:
            mask = reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), w, 0)
            m[mask] = max(m[mask], len(w))
        return max([m[x] * m[y] for x, y in product(m, m) if x & y == 0], default=0)


def test_max_product():
    solution = Solution()
    assert solution.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]) == 16, 'wrong result'
    assert solution.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4, 'wrong result'
    assert solution.maxProduct(["a", "aa", "aaa", "aaaa"]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_product()
