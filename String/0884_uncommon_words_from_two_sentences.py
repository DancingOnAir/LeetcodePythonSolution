from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [c for c, v in Counter((s1 + ' ' + s2).split()).items() if v == 1]


def test_uncommon_from_sentences():
    solution = Solution()

    assert solution.uncommonFromSentences("this apple is sweet", "this apple is sour") == ["sweet", "sour"], 'wrong result'
    assert solution.uncommonFromSentences("apple apple", "banana") == ["banana"], 'wrong result'


if __name__ == '__main__':
    test_uncommon_from_sentences()
