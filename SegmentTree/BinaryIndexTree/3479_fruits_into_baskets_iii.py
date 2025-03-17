from typing import List


class BinaryIndexTree:
    def __init__(self, nums):
        n = len(nums)
        self.mx = [0] * (2 << (n - 1).bit_length())
        self.build(nums, 1, 0, n - 1)

    def update(self, i):
        self.mx[i] = max(self.mx[i * 2], self.mx[i * 2 + 1])

    def build(self, nums, i, l, r):
        if l == r:
            self.mx[i] = nums[l]
            return
        m = (l + r) // 2
        self.build(nums, i * 2, l, m)
        self.build(nums, i * 2 + 1, m + 1, r)
        self.update(i)

    def find(self, i, l, r, x):
        if self.mx[i] < x:
            return -1
        if l == r:
            self.mx[i] = -1
            return l
        m = (l + r) // 2
        p = self.find(i * 2, l, m, x)
        if p < 0:
            p = self.find(i * 2 + 1, m + 1, r, x)
        self.update(i)
        return p


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        tree = BinaryIndexTree(baskets)
        n = len(baskets)
        res = 0
        for x in fruits:
            if tree.find(1, 0, n - 1, x) < 0:
                res += 1
        return res


def test_num_Of_unplaced_fruits():
    solution = Solution()
    assert solution.numOfUnplacedFruits([4, 2, 5], baskets=[3, 5, 4]) == 1, 'wrong result'
    assert solution.numOfUnplacedFruits([3, 6, 1], baskets=[6, 4, 7]) == 0, 'wrong result'


if __name__ == '__main__':
    test_num_Of_unplaced_fruits()


