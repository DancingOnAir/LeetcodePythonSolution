from collections import defaultdict


# brute force
class MyCalendar:
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
