from collections import defaultdict


# class Node:
#     def __init__(self, start, end):
#         self.left, self.right = None, None
#         self.start = start
#         self.end = end
#         self.overlap = 0
#
#
# class MyCalendarTwo:
#     def __init__(self):
#         self.root = Node(0, 0)
#
#     def book(self, start: int, end: int) -> bool:
#         return self.update(start, end)
#
#     def update(self, start, end):
#         node = self.root
#         while True:
#             if start >= node.end:
#                 node = node.right
#                 if node is None:
#                     node.right = Node(start, end)
#                     return True
#             elif end <= node.start:
#                 node = node.left
#                 if node is None:
#                     node.left = Node(start, end)
#                     return True
#             else:
#                 if node.overlap == 1:
#                     return False

class MyCalendarTwo:
    def __init__(self):
        self.calendar = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.calendar[start] += 1
        self.calendar[end] -= 1

        res = 0
        for k in sorted(self.calendar.keys()):
            res += self.calendar[k]
            if res == 3:
                self.calendar[start] -= 1
                self.calendar[end] += 1

                return False
        return True


def test_my_calendar_two():
    obj = MyCalendarTwo()
    assert obj.book(10, 20), 'wrong result'
    assert obj.book(50, 60), 'wrong result'
    assert obj.book(10, 40), 'wrong result'
    assert not obj.book(5, 15), 'wrong result'
    assert obj.book(5, 10), 'wrong result'
    assert obj.book(25, 55), 'wrong result'


if __name__ == '__main__':
    test_my_calendar_two()
