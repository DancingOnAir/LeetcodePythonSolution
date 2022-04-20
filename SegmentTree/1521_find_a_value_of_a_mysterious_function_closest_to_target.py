from typing import List


class Node:
    def __init__(self, l, r ,val):
        self.left_child, self.right_child = None, None
        self.left_bound, self.right_bound = l, r
        self.val = val


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

        r += 1
        l += self.n
        r += self.n
        res = self.tree[l]

        while l < r:
            if l & 1:
                res &= self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res &= self.tree[r]

            l >>= 1
            r >>= 1
        return res


class Solution:
    # bitwise operation, similiar question 898, 1061
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
