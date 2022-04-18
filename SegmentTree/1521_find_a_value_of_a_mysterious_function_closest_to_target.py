from typing import List


class Node:
    def __init__(self, val):
        self.left_child, self.right_child = None, None
        self.val = val
#
#
# class SegmentTree:
#     def __init__(self, l, r):
#         self.root = Node(l, r)
#
#     def update(self, node, l , r):
#         if node is None:
#             return
#
#         if l > node.right_bound or r < node.left_bound:
#             return
#         elif l <= node.left_bound and r >= node.right_bound:
#
#         else:
#             self.update(node.left_child, l, r)
#             self.update(node.right_child, l, r)

class SegmentTree:
    def __init__(self, l, r, target):
        self.root = Node(0)
        self.build(self.root, l, r)
        self.target = target
        self.closest = 10 ** 6

    def build(self, node, l, r):
        if l == r:
            return node
        mid = (l + r) >> 1

        node.left_child = Node(0)
        self.build(node.left_child, l, mid)
        node.right_child = Node(0)
        self.build(node.right_child, mid + 1, r)

    def update(self, node, l, r, i, val):
        if l == r:
            node.val = val
            node.closest = abs(val - self.target)
            return

        mid = (l + r) >> 1
        if i <= mid:
            self.update(node.left_child, l, mid, i, val)
        else:
            self.update(node.right_child, mid+1, r, i, val)
        node.val &= val

    def query(self, node, l, r, lx, rx):
        if l == lx and r == rx:
            self.closest = min(self.closest, abs(node.val - self.target))
            return node.val

        mid = (l + r) >> 1
        if rx <= mid:
            res = self.query(node.left_child, l, mid, lx, rx)
        elif lx >= mid:
            res = self.query(node.right_child, mid+1, r, lx, rx)
        else:
            res = self.query(node.left_child, l, mid, lx, rx) & self.query(node.right_child, mid+1, r, lx, rx)

        self.closest = (self.closest, abs(res - self.target))
        return res


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        n = len(arr)
        st = SegmentTree(1, n, target)
        for i, val in enumerate(arr):
            st.update(st.root, 1, n, i+1, val)
        return st.query(st.root, 1, n, 1, n)


def test_closest_to_target():
    solution = Solution()
    assert solution.closestToTarget([9, 12, 3, 7, 15], 5) == 2, 'wrong result'
    assert solution.closestToTarget([1000000, 1000000, 1000000], 1) == 999999, 'wrong result'
    assert solution.closestToTarget([1, 2, 4, 8, 16], 0) == 0, 'wrong result'


if __name__ == '__main__':
    test_closest_to_target()
