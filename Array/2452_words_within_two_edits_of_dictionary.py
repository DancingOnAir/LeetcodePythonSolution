from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = list()
        for q in queries:
            for d in dictionary:
                if sum(x != y for x, y in zip(q, d)) < 3:
                    res.append(q)
                    break
        return res


def test_two_edit_words():
    solution = Solution()
    assert solution.twoEditWords(["word", "note", "ants", "wood"], ["wood", "joke", "moat"]) == ["word", "note", "wood"], 'wrong result'
    assert solution.twoEditWords(["yes"], ["not"]) == [], 'wrong result'


if __name__ == '__main__':
    test_two_edit_words()
