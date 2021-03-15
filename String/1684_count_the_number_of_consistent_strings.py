from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)

        res = len(words)
        for w in words:
            for c in w:
                if c not in s:
                    res -= 1
                    break
        return res


def test_count_consistent_strings():
    solution = Solution()
    allowed1 = "ab"
    words1 = ["ad", "bd", "aaab", "baa", "badab"]
    assert solution.countConsistentStrings(allowed1, words1) == 2, 'wrong result'

    allowed2 = "abc"
    words2 = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    assert solution.countConsistentStrings(allowed2, words2) == 7, 'wrong result'

    allowed4 = "cad"
    words4 = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    assert solution.countConsistentStrings(allowed4, words4) == 4, 'wrong result'


if __name__ == '__main__':
    test_count_consistent_strings()
