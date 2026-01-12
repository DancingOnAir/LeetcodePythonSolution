from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w.find(pref) == 0 for w in words)

    def prefixCount1(self, words: List[str], pref: str) -> int:
        return sum(w.startswith(pref) for w in words)


def test_prefix_count():
    solution = Solution()
    assert solution.prefixCount(["pay", "attention", "practice", "attend"], 'at') == 2, 'wrong result'
    assert solution.prefixCount(["leetcode", "win", "loops", "success"], 'code') == 0, 'wrong result'


if __name__ == '__main__':
    test_prefix_count()
