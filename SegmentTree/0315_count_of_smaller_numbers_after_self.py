from typing import List
from math import log2


# zkw segment tree
class ZkwSegmentTree:
    def __init__(self, nums):
        self.MAX = 10 ** 4 + 1
        while self.N < len(nums) + 2:
            self.N <<= 1

        self.tree = [0] * (self.N << 1)


class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (n * 4)

    def update(self, x, i, l, r):
        if l == r:
            self.tree[i] += 1
        else:
            m = (l + r) >> 1
            if x <= m:
                self.update(x, i*2, l, m)
            else:
                self.update(x, i*2+1, m+1, r)
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]

    def query(self, xl, xr, i, l, r):
        if xl > xr:
            return 0

        if xl == l and xr == r:
            return self.tree[i]

        m = (l + r) >> 1
        return self.query(xl, min(xr, m), i*2, l, m) + self.query(max(xl, m+1), xr, i*2+1, m+1, r)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # max range
        MAX = 10 ** 4 + 1
        # converting range from [-10^4, 10^4] to [0, 2*10^4]
        for i in range(len(nums)):
            nums[i] += MAX
        st = SegmentTree(MAX * 2)
        for i in range(len(nums) - 1, -1, -1):
            st.update(nums[i], 1, 0, MAX * 2)
            nums[i] = st.query(0, nums[i]-1, 1, 0, MAX * 2)
        return nums


def test_count_smaller():
    solution = Solution()
    assert solution.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0], 'wrong result'
    assert solution.countSmaller([-1]) == [0], 'wrong result'
    assert solution.countSmaller([-1, -1]) == [0, 0], 'wrong result'


if __name__ == '__main__':
    test_count_smaller()
