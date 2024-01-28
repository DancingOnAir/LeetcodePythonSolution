from typing import List
from collections import defaultdict


class WordFilter1:
    def __init__(self, words: List[str]):
        self.pres = defaultdict(set)
        self.sufs = defaultdict(set)
        self.weights = defaultdict(int)

        for i, w in enumerate(words):
            pre, suf = '', ''
            for c in w:
                pre += c
                self.pres[pre].add(w)
            for c in w[::-1]:
                suf += c
                self.sufs[suf[::-1]].add(w)

            self.weights[w] = i

    def f(self, pref: str, suff: str) -> int:
        res = -1
        for w in self.pres[pref] & self.sufs[suff]:
            if self.weights[w] > res:
                res = self.weights[w]
        return res


def test_word_filter():
    obj = WordFilter(["apple"])
    assert obj.f('a', 'e') == 0, 'wrong result'


if __name__ == '__main__':
    test_word_filter()
