from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        p = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            p = p.children.setdefault(cur, TrieNode())

    def search(self, num):
        if not self.root:
            return -1
        p, res = self.root, 0
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if 1 - cur in p.children:
                res |= (1 << i)
                p = p.children[1 - cur]
            elif cur in p.children:
                p = p.children[cur]
            else:
                return -1
        return res


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        res = [-1] * len(queries)
        trie = Trie()
        j = 0
        for i, (x, m) in queries:
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1

            res[i] = trie.search(x)
        return res


def test_maximize_xor():
    solution = Solution()
    assert solution.maximizeXor([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]) == [3, 3, 7], 'wrong result'
    assert solution.maximizeXor([5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]]) == [15, -1, 5], 'wrong result'


if __name__ == '__main__':
    test_maximize_xor()

