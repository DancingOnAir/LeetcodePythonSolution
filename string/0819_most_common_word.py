from collections import Counter
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall('\w+', paragraph.lower())
        banned = set(banned)
        return Counter(w for w in words if w not in banned).most_common(1)[0][0]


def test_most_common_word():
    solution = Solution()
    assert solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",
                                   ["hit"]) == "ball", 'wrong result'
    assert solution.mostCommonWord("a.", []) == "a", 'wrong result'


if __name__ == '__main__':
    test_most_common_word()
