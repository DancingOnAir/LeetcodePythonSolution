from typing import List


class Node:
    def __init__(self):
        self.children = dict()
        self.isEnd = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, w):
        p = self.root
        for c in w:
            if c not in p.children:
                p.children[c] = Node()
            p = p.children[c]
        p.isEnd += 1

    def lcp(self, w):
        p = self.root
        res = 0
        for c in w:
            if c not in p.children:
                break
            p = p.children[c]
            res += 1
        return res


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for y in set(arr2):
            trie.insert(str(y))

        res = 0
        for x in set(arr1):
            res = max(res, trie.lcp(str(x)))
        return res


def test_longest_common_prefix():
    solution = Solution()
    assert solution.longestCommonPrefix([1, 10, 100], [1000]) == 3, 'wrong result'
    assert solution.longestCommonPrefix([1, 2, 3], [4, 4, 4]) == 0, 'wrong result'


if __name__ == '__main__':
    test_longest_common_prefix()
