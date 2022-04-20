from typing import List


class TreeNode:
    def __init__(self):
        self.left = -1
        self.right = -1
        self.or_sum = 0


class Tree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.max_size = 4 * self.n
        self.tree = [TreeNode() for _ in range(self.max_size)]

    def build(self, idx, left, right):
        self.tree[idx].left = left
        self.tree[idx].right = right
        if left == right:
            self.tree[idx].or_sum = self.arr[left - 1]
        else:
            mid = (left + right) >> 1
            self.build(idx << 1, left, mid)
            self.build(idx << 1 | 1, mid + 1, right)
            self.pushup(idx)

    def pushup(self, idx):
        return self.tree[idx << 1].or_sum & self.tree[idx << 1 | 1].or_sum

    def query(self, l, r, i, xl, xr):
        if xl <= l and xr >= r:
            return self.tree[i].or_sum
        else:
            mid = (l + r) >> 1
            res = float('inf')
            if xl <= mid:
                res &= self.query(l, r, i << 1, xl, mid)
            if xr > mid:
                res &= self.query(l, r, i << 1 | 1, mid+1, xr)
        return res


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * self.n + arr

    def build(self):
        for i in reversed(range(1, self.n)):
            self.tree[i] = self.tree[i << 1] & self.tree[i << 1 | 1]

    def query(self, l, r):
        if l > r:
            return float('-inf')

        l += self.n
        r += self.n
        res = self.tree[l]

        while l <= r:
            # 左边界不属于其父节点的左孩子（左孩子下标为偶数）
            if l & 1:
                res &= self.tree[l]
                l += 1
            l >>= 1
            # 右边界不属于其父节点的右孩子
            if r & 1 == 0:
                res &= self.tree[r]
                r -= 1
            r >>= 1

        return res


class Solution:
    # bitwise operation, similar question 898, 1061
    def closestToTarget1(self, arr: List[int], target: int) -> int:
        s, res = set(), float('inf')

        for a in arr:
            s = {a & b for b in s} | {a}
            for c in s:
                res = min(res, abs(c - target))
        return res

    # segment tree
    # 注意,对于任何正整数a, b 有a & b <= a, 在进行连续的&运算后，生成的是有序数组，可以使用二分查找来提速
    # 也可以使用sliding window提速
    def closestToTarget(self, arr: List[int], target: int) -> int:
        st = SegmentTree(arr)
        st.build()

        res = float('inf')
        l = r = 0
        while r < len(arr):
            v = st.query(l, r)
            res = min(res, abs(v - target))

            if v >= target:
                r += 1
            else:
                if l < r:
                    l += 1
                else:
                    l += 1
                    r += 1
        return res


def test_closest_to_target():
    solution = Solution()
    assert solution.closestToTarget([9, 12, 3, 7, 15], 5) == 2, 'wrong result'
    assert solution.closestToTarget([1000000, 1000000, 1000000], 1) == 999999, 'wrong result'
    assert solution.closestToTarget([1, 2, 4, 8, 16], 0) == 0, 'wrong result'


if __name__ == '__main__':
    test_closest_to_target()
