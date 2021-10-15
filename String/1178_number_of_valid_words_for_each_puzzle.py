from typing import List
from collections import Counter


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        words_count = [set(w) for w in words]
        puzzles_count = [set(p) for p in puzzles]

        res = [0] * len(puzzles)
        for i, ps in enumerate(puzzles_count):
            for ws in words_count:
                if len(ws - ps) == 0 and puzzles[i][0] in ws:
                    res[i] += 1
        return res


def test_find_num_of_valid_words():
    solution = Solution()

    assert solution.findNumOfValidWords(["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
                                        ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]) == [1, 1, 3, 2, 4, 0], 'wrong result'
    assert solution.findNumOfValidWords(["apple", "pleas", "please"],
                                        ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"]) == [0, 1, 3, 2, 0], 'wrong result'


if __name__ == '__main__':
    test_find_num_of_valid_words()
