from typing import List


class Node:
    def __init__(self):
        self.children = dict()
        self.idx = -1


class Trie:
    def __init__(self, words):
        self.root = Node()
        self.words = words
        self.min_length = min(range(len(words)), key=lambda x: len(words[x]))

    def insert(self, w, idx):
        p = self.root
        for i, c in enumerate(w):
            p = p.children.setdefault(c, Node())
            if p.idx == -1:
                p.idx = idx
            else:
                if len(self.words[idx]) < len(self.words[p.idx]):
                    p.idx = idx
                elif len(self.words[idx]) == len(self.words[p.idx]) and idx < p.idx:
                    p.idx = idx

    def query(self, w):
        p = self.root
        res = self.min_length

        for c in w:
            if c in p.children:
                p = p.children[c]
                res = p.idx
            else:
                break

        return res


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie(wordsContainer)
        for i, w in enumerate(wordsContainer):
            trie.insert(w[::-1], i)

        res = []
        for w in wordsQuery:
            res.append(trie.query(w[::-1]))
        return res


def test_string_indices():
    solution = Solution()
    assert solution.stringIndices(["abcd", "bcd", "xbcd"], ["cd", "bcd", "xyz"]) == [1, 1, 1], 'wrong result'
    assert solution.stringIndices(["abcdefgh", "poiuygh", "ghghgh"], ["gh", "acbfgh", "acbfegh"]) == [2, 0,
                                                                                                      2], 'wrong result'


if __name__ == '__main__':
    test_string_indices()
