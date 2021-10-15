from typing import List
from collections import Counter
from itertools import combinations


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        cnt = Counter(frozenset(w) for w in words)
        res = list()
        for p in puzzles:
            cur = 0
            for k in range(7):
                for c in combinations(p[1:], k):
                    cur += cnt[frozenset(tuple(p[0]) + c)]
            res.append(cur)

        return res

    # using bfs to find all combinations
    def findNumOfValidWords2(self, words: List[str], puzzles: List[str]) -> List[int]:
        cnt = Counter(frozenset(w) for w in words)
        res = list()
        for p in puzzles:
            subs = [p[0]]
            for c in p[1:]:
                subs += [s + c for s in subs]
            res.append(sum(cnt[frozenset(s)] for s in subs))
        return res

    # brute force
    def findNumOfValidWords1(self, words: List[str], puzzles: List[str]) -> List[int]:
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
