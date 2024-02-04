from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        # 子树的数量
        self.cnt = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        p = self.root
        # 1 <= nums[i] <= 2^20 - 1
        for i in range(19, -1, -1):
            bit = (num >> i) & 1
            p = p.children.setdefault(bit, TrieNode())
            p.cnt += 1

    def remove(self, num):
        p = self.root
        for i in range(19, -1, -1):
            bit = (num >> i) & 1
            p = p.children[bit]
            p.cnt -= 1

    def max_xor(self, num):
        p = self.root
        res = 0
        for i in range(19, -1, -1):
            bit = (num >> i) & 1
            if (bit ^ 1) in p.children and p.children[bit ^ 1].cnt:
                # bit ^ 1 和bit是相异的，所以2者异或的结果为1
                res |= (1 << i)
                bit ^= 1
            p = p.children[bit]
        return res


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res, left = 0, 0
        trie = Trie()
        nums.sort()
        for x in nums:
            trie.insert(x)
            while nums[left] * 2 < x:
                trie.remove(nums[left])
                left += 1
            res = max(res, trie.max_xor(x))
        return res


def test_maximum_strong_pair_xor():
    solution = Solution()
    assert solution.maximumStrongPairXor([1, 2, 3, 4, 5]) == 7, 'wrong result'
    assert solution.maximumStrongPairXor([10, 100]) == 0, 'wrong result'
    assert solution.maximumStrongPairXor([500, 520, 2500, 3000]) == 1020, 'wrong result'


if __name__ == '__main__':
    test_maximum_strong_pair_xor()
