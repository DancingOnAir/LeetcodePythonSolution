class MyCalendarTwo:

    def __init__(self):
        pass

    def book(self, start: int, end: int) -> bool:
        pass


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
