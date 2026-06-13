from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.num = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        q = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            q = q.children.setdefault(cur, TrieNode())
        q.num = num

    def query(self, num):
        q = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if 1 - cur in q.children:
                q = q.children[1 - cur]
            elif cur in q.children:
                q = q.children[cur]
        return q.num ^ num


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        trie.insert(nums[0])
        res = 0
        for i in range(1, len(nums)):
            res = max(res, trie.query(nums[i]))
            trie.insert(nums[i])
        return res


def test_find_maximum_xor():
    solution = Solution()
    assert solution.findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28, 'wrong result'
    assert solution.findMaximumXOR([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]) == 127, 'wrong result'


if __name__ == '__main__':
    test_find_maximum_xor()
