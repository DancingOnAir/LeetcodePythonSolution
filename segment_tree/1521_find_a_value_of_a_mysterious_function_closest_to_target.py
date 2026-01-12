from typing import List


class Tree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.max_size = 4 * self.n
        self.tree = [0] * self.max_size

    def build(self):
        self._build(1, 0, self.n - 1)

    def _build(self, idx, left, right):
        if left == right:
            self.tree[idx] = self.arr[left]
        else:
            mid = (left + right) >> 1
            self._build(idx << 1, left, mid)
            self._build(idx << 1 | 1, mid + 1, right)
            self.pushup(idx)

    def pushup(self, idx):
        self.tree[idx] = self.tree[idx << 1] & self.tree[idx << 1 | 1]

    def query(self, xl, xr):
        return self._query(0, self.n - 1, 1, xl, xr)

    def _query(self, l, r, i, xl, xr):
        if xl <= l and xr >= r:
            return self.tree[i]

        mid = (l + r) >> 1
        res = 1048575
        if xl <= mid:
            res &= self._query(l, mid, i << 1, xl, xr)
        if xr > mid:
            res &= self._query(mid + 1, r, i << 1 | 1, xl, xr)
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
    def closestToTarget2(self, arr: List[int], target: int) -> int:
        st = SegmentTree(arr)
        st.build()

        res = float('inf')
        l = r = 0
        while r < len(arr):
            v = st.query(l, r)
            res = min(res, abs(v - target))
            # 当v大于target的时候，希望期望的结果趋于0，那么减小v的值，这样必须添加新的元素做&操作，所以r += 1
            if v >= target:
                r += 1
            else:
                if l < r:
                    l += 1
                else:
                    l += 1
                    r += 1
        return res

    def closestToTarget(self, arr: List[int], target: int) -> int:
        # 求合适的segment tree的大小
        # n = len(arr)
        # x = math.ceil(math.log2(n))
        # max_size = 2 * pow(2, x) - 1
        # tree = [0] * max_size

        st = Tree(arr)
        st.build()

        l = r = 0
        res = float('inf')
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
