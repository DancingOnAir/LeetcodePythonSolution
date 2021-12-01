from typing import List
from collections import Counter


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1, c2 = Counter(words1), Counter(words2)
        return sum(c1[w] == c2[w] == 1 for w in (c1 & c2))


def test_count_words():
    solution = Solution()

    assert solution.countWords(["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"]) == 2, 'wrong result'
    assert solution.countWords(["b", "bb", "bbb"], ["a", "aa", "aaa"]) == 0, 'wrong result'
    assert solution.countWords(["a", "ab"], ["a", "a", "a", "ab"]) == 1, 'wrong result'


if __name__ == '__main__':
    test_count_words()
