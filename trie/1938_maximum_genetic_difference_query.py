from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num, x):
        p = self.root
        for i in range(17, -1, -1):
            bit = (num >> i) & 1
            p = p.children.setdefault(bit, TrieNode())
            p.cnt += x

    def max_xor(self, num):
        res = 0
        p = self.root

        for i in range(17, -1, -1):
            bit = (num >> i) & 1
            if (bit ^ 1) in p.children and p.children[bit ^ 1].cnt > 0:
                res |= (1 << i)
                bit ^= 1
            p = p.children[bit]
        return res


class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        Q, graph = defaultdict(list), defaultdict(list)
        for i, (node, val) in enumerate(queries):
            Q[node].append((i, val))

        for i, pa in enumerate(parents):
            graph[pa].append(i)

        res = [-1] * len(queries)
        trie = Trie()

        def dfs(node):
            trie.insert(node, 1)
            for i, val in Q[node]:
                res[i] = trie.max_xor(val)
            for neib in graph[node]:
                dfs(neib)
            trie.insert(node, -1)

        dfs(graph[-1][0])

        return res


def test_max_genetic_difference():
    solution = Solution()
    assert solution.maxGeneticDifference([-1, 0, 1, 1], [[0, 2], [3, 2], [2, 5]]) == [2, 3, 7], 'wrong result'
    assert solution.maxGeneticDifference([3, 7, -1, 2, 0, 7, 0, 2], [[4, 6], [1, 15], [0, 5]]) == [6, 14,
                                                                                                   7], 'wrong result'


if __name__ == '__main__':
    test_max_genetic_difference()
