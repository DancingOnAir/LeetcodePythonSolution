from typing import List
from collections import Counter
from functools import lru_cache


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        @lru_cache(None)
        def dp(i, L):
            if i >= len(words):
                return 0
            res = 0
            M = L
            for ch in words[i]:
                if ch not in M:
                    return dp(i + 1, L)
                M = M.replace(ch, '', 1)
                res += score[ord(ch) - 97]
            return max(dp(i + 1, L), dp(i + 1, M) + res)
        return dp(0, ''.join(letters))


def test_max_score_words():
    solution = Solution()
    assert solution.maxScoreWords(["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]) == 23, 'wrong result'
    assert solution.maxScoreWords(["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]) == 27, 'wrong result'
    assert solution.maxScoreWords(["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_score_words()
