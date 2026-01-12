from typing import List
from collections import Counter


class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        c = Counter(ch for w in words for ch in w)
        lengths = sorted(map(len, words))
        pairs = sum(v // 2 for v in c.values())
        for i, v in enumerate(lengths):
            pairs -= v // 2
            if pairs < 0:
                return i
        return len(lengths)


def test_max_palindromes_after_operations():
    solution = Solution()
    assert solution.maxPalindromesAfterOperations(["abbb", "ba", "aa"]) == 3, 'wrong result'
    assert solution.maxPalindromesAfterOperations(["abc", "ab"]) == 2, 'wrong result'
    assert solution.maxPalindromesAfterOperations(["cd", "ef", "a"]) == 1, 'wrong result'


if __name__ == '__main__':
    test_max_palindromes_after_operations()
