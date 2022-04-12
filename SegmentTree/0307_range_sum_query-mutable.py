from typing import List
from math import log2


class NumArray:
    def __init__(self, nums: List[int]):
        self.N = 1
        while self.N < len(nums) + 2:
            self.N <<= 1
        self.tree = [0] * (self.N << 1)

        for i in range(len(nums)):
            self.tree[i + self.N + 1] = nums[i]
        for i in range(self.N - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, index: int, val: int) -> None:
        i = index + self.N + 1
        cur = self.tree[i]
        while i > 0:
            self.tree[i] += val - cur
            i >>= 1

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        left += self.N
        right += self.N + 2

        while (left ^ right ^ 1) != 0:
            # 如果左边端点是其父节点的左儿子，那么加上它的兄弟，即父节点右儿子的值
            if ~left & 1:
                res += self.tree[left ^ 1]
            # 如果右边端点是其父节点的右儿子，那么加上它的兄弟，即父节点左儿子的值
            if right ^ 1:
                res += self.tree[right ^ 1]
            left >>= 1
            right >>= 1
        return res


def test_num_array():
    obj = NumArray([1, 3, 5])
    assert obj.sumRange(0, 2) == 9, 'wrong result'
    obj.update(1, 2)
    assert obj.sumRange(0, 2) == 8, 'wrong result'


if __name__ == '__main__':
    test_num_array()
