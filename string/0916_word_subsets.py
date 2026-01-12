from typing import List
from collections import Counter
from functools import lru_cache


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = Counter()
        for w in words2:
            counter |= Counter(w)

        return [w for w in words1 if not (counter - Counter(w))]

    # TLE
    def wordSubsets1(self, words1: List[str], words2: List[str]) -> List[str]:
        res = list()
        counts = [Counter(w) for w in words2]

        for w in words1:
            c1 = Counter(w)
            if all(len(c2 - c1) == 0 for c2 in counts):
                res.append(w)

        return res


def test_word_subsets():
    solution = Solution()
    assert solution.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]) == ["facebook",
                                                                                                       "google",
                                                                                                       "leetcode"], 'wrong result'
    assert solution.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]) == ["apple",
                                                                                                       "google",
                                                                                                       "leetcode"], 'wrong result'


if __name__ == '__main__':
    test_word_subsets()

