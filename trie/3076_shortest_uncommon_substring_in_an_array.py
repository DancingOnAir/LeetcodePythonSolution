from typing import List


class Node:
    def __init__(self):
        self.children = dict()
        self.cnt = set()


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, w, idx):
        for i in range(len(w)):
            p = self.root
            for c in w[i:]:
                p = p.children.setdefault(c, Node())
                p.cnt.add(idx)

    def query(self, w):
        res = []

        for i in range(len(w)):
            p = self.root
            cur = ''
            for c in w[i:]:
                cur += c
                p = p.children[c]
                if len(p.cnt) == 1:
                    res.append(cur)
                    break
        return sorted(res, key=lambda x: (len(x), x))[0] if res else ''


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        trie = Trie()
        for i, w in enumerate(arr):
            trie.insert(w, i)

        res = []
        for w in arr:
            res.append(trie.query(w))
        return res


def test_shortest_substrings():
    solution = Solution()
    assert solution.shortestSubstrings(["cab", "ad", "bad", "c"]) == ["ab", "", "ba", ""], 'wrong result'
    assert solution.shortestSubstrings(["abc", "bcd", "abcd"]) == ["", "", "abcd"], 'wrong result'


if __name__ == '__main__':
    test_shortest_substrings()
