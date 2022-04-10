class Node:
    def __init__(self, l, r):
        self.left_child, self.right_child = None, None
        self.left_bound = l
        self.right_bound = r
        self.val = 0
        self.lazy = 0


class SegmentTree:
    def __init__(self):
        pass

class MyCalendarThree:
    def __init__(self):
        pass

    def book(self, start: int, end: int) -> int:
        pass


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
