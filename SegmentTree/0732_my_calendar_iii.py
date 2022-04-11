from collections import defaultdict


class Node:
    def __init__(self, l, r):
        self.left_child, self.right_child = None, None
        self.left_bound = l
        self.right_bound = r
        self.val = 0
        self.lazy = 0


class SegmentTree:
    def __init__(self, l, r):
        self.root = Node(l, r)

    def update(self, l, r):
        self._update(self.root, l, r)

    def _update(self, node, l, r):
        if node is None:
            return

        if r < node.left_bound or l > node.right_bound:
            return
        elif l <= node.left_bound and r >= node.right_bound:
            node.val += 1
            node.lazy += 1
        else:
            self.pushdown(node)
            self._update(node.left_child, l, r)
            self._update(node.right_child, l, r)
            self.pushup(node)

    def pushdown(self, node):
        if node is None:
            return

        mid = (node.left_bound + node.right_bound) >> 1
        if node.left_child is None:
            node.left_child = Node(node.left_bound, mid)
        if node.right_child is None:
            node.right_child = Node(mid + 1, node.right_bound)

        node.left_child.val += node.lazy
        node.left_child.lazy += node.lazy

        node.right_child.val += node.lazy
        node.right_child.lazy += node.lazy

        node.lazy = 0

    def pushup(self, node):
        node.val = max(node.left_child.val, node.right_child.val)

    def query(self, l, r):
        return self._query(self.root, l, r)

    def _query(self, node, l, r):
        if node is None:
            return 0

        if l > node.right_bound or r < node.left_bound:
            return 0
        elif l <= node.left_bound and r >= node.right_bound:
            return node.val
        else:
            self.pushdown(node)
            left_res = self._query(node.left_child, l, r)
            right_res = self._query(node.right_child, l, r)
            return max(left_res, right_res)


class MyCalendarThree1:
    def __init__(self):
        self.st = SegmentTree(0, 10 ** 9 + 2)

    def book(self, start: int, end: int) -> int:
        self.st.update(start, end - 1)
        return self.st.root.val


class MyCalendarThree:
    def __init__(self):
        self.memo = defaultdict(int)

    def book(self, start: int, end: int) -> int:
        res = cur = 0
        self.memo[start] += 1
        self.memo[end] -= 1
        for k in sorted(self.memo):
            cur += self.memo[k]
            res = max(res, cur)
        return res


def test_my_calendar_three():
    obj = MyCalendarThree()
    assert obj.book(10, 20) == 1, 'wrong result'
    assert obj.book(50, 60) == 1, 'wrong result'
    assert obj.book(10, 40) == 2, 'wrong result'
    assert obj.book(5, 15) == 3, 'wrong result'
    assert obj.book(5, 10) == 3, 'wrong result'
    assert obj.book(25, 55) == 3, 'wrong result'


if __name__ == '__main__':
    test_my_calendar_three()
