from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return len(words) == len(s) and all(w[0] == c for w, c in zip(words, s))

    def isAcronym1(self, words: List[str], s: str) -> bool:
        res = []
        for w in words:
            res.append(w[0])
        return ''.join(res) == s


def test_is_acronym():
    solution = Solution()
    assert solution.isAcronym(["alice", "bob", "charlie"], "abc"), 'wrong result'
    assert not solution.isAcronym(["an", "apple"], "a"), 'wrong result'
    assert solution.isAcronym(["never", "gonna", "give", "up", "on", "you"], "ngguoy"), 'wrong result'


if __name__ == '__main__':
    test_is_acronym()
