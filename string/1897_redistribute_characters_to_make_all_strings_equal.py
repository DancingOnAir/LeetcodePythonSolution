from typing import List
from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return all(v % len(words) == 0 for v in Counter(''.join(words)).values())

    def makeEqual1(self, words: List[str]) -> bool:
        n = len(words)
        if n < 2:
            return True

        cnt = Counter()
        for w in words:
            cnt += Counter(w)

        return all(v % n == 0 for v in cnt.values())


def test_make_equal():
    solution = Solution()
    assert solution.makeEqual(["abc", "aabc", "bc"]), 'wrong result'
    assert not solution.makeEqual(["ab", "a"]), 'wrong result'


if __name__ == '__main__':
    test_make_equal()
