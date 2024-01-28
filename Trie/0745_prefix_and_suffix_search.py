from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, idx):
        root = self.root
        root.idx = idx
        for ch in word:
            root = root.children.setdefault(ch, TrieNode())
            root.idx = idx

    def start_with(self, word):
        root = self.root
        for ch in word:
            if ch not in root.children:
                return -1
            root = root.children[ch]
        return root.idx


# https://leetcode.com/problems/prefix-and-suffix-search/solutions/1185171/python-two-solutions-trie-and-bruteforce-explained/
class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i, w in enumerate(words):
            long = w + '#' + w
            for j in range(len(w)):
                self.trie.insert(long[j:], i)

    def f(self, pref: str, suff: str) -> int:
        res = self.trie.start_with(suff + '#' + pref)
        return res


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
