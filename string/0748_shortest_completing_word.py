from typing import List
from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        c = Counter([ch.lower() for ch in licensePlate if ch.isalpha()])
        for w in sorted(words, key=len):
            if len(c - Counter(w)) == 0:
                return w
        return ""


def test_shortest_completing_word():
    solution = Solution()
    assert solution.shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "steppe"]) == "steps", 'wrong result'
    assert solution.shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"]) == "pest", 'wrong result'


if __name__ == '__main__':
    test_shortest_completing_word()
