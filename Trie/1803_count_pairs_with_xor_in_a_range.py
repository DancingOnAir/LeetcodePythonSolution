from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.ended = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 1 <= nums.length <= 2 * 104, length of bits < 15
    def insert(self, num):
        p = self.root
        for i in range(14, -1, -1):
            cur = (num >> i) & 1
            p = p.children.setdefault(cur, TrieNode())
            p.ended += 1

    def query(self, num, x):
        p = self.root
        res = 0
        for i in range(14, -1, -1):
            cur = (num >> i) & 1
            if (x >> i) & 1:
                if cur in p.children:
                    res += p.children[cur].ended
                if (cur ^ 1) not in p.children:
                    return res
                p = p.children[cur ^ 1]
            else:
                if cur not in p.children:
                    return res
                p = p.children[cur]

        res += p.ended
        return res


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        # helper()表示nums中有多少对数字亦或运算小于等于x
        def helper(nums, x):
            res = 0
            trie = Trie()
            for i in range(1, len(nums)):
                trie.insert(nums[i - 1])
                res += trie.query(nums[i], x)
            return res
        return helper(nums, high) - helper(nums, low - 1)


def test_count_pairs():
    solution = Solution()
    assert solution.countPairs([1, 4, 2, 7], 2, 6) == 6, 'wrong result'
    assert solution.countPairs([9, 8, 4, 2, 1], 5, 14) == 8, 'wrong result'


if __name__ == '__main__':
    test_count_pairs()
