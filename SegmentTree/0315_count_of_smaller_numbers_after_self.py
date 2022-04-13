from typing import List


class ZkwSegmentTree:
    def __init__(self, nums):
        self.N = 1
        while self.N < len(nums) + 2:
            self.N <<= 1

        self.tree = [0] * (self.N << 1)
        for i in range(len(nums)):
            self.tree[i + self.N + 1] = nums[i]
        for i in range(self.N - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        pass


def test_count_smaller():
    solution = Solution()
    assert solution.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0], 'wrong result'
    assert solution.countSmaller([-1]) == [0], 'wrong result'
    assert solution.countSmaller([-1, -1]) == [0, 0], 'wrong result'


if __name__ == '__main__':
    test_count_smaller()
