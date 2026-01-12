from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]


def test_find_words_containing():
    solution = Solution()
    assert solution.findWordsContaining(["leet", "code"], "e") == [0, 1], 'wrong result'
    assert solution.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "a") == [0, 2], 'wrong result'
    assert solution.findWordsContaining(["abc", "bcd", "aaaa", "cbc"], "z") == [], 'wrong result'


if __name__ == '__main__':
    test_find_words_containing()
