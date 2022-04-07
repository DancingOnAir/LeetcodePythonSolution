from collections import defaultdict


# segment tree
# build a segment tree, if new event range can put into the same side of the tree node, it's true, otherwise, false.
class Node:
    def __init__(self, l, r):
        self.left, self.right = None, None
        self.l = l
        self.r = r


class MyCalendar:
    def __init__(self):
        self.root = Node(0, 0)

    def book(self, start: int, end: int) -> bool:
        return self.update(start, end)

    def update(self, start, end):
        node = self.root
        while True:
            if end <= node.l:
                if node.left is None:
                    node.left = Node(start, end)
                    return True
                node = node.left
            elif start >= node.r:
                if node.right is None:
                    node.right = Node(start, end)
                    return True
                node = node.right
            else:
                return False


# brute force
class MyCalendar1:
    def __init__(self):
        self.calendar = list()

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calendar:
            if start < e and end > s:
                return False
        self.calendar.append((start, end))
        return True


def test_my_calendar():
    obj = MyCalendar()
    assert obj.book(10, 20), 'wrong result'
    assert not obj.book(15, 25), 'wrong result'
    assert obj.book(20, 30), 'wrong result'


if __name__ == '__main__':
    test_my_calendar()
