from collections import defaultdict


class MyCalendar:
    def __init__(self):
        self.memo = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.memo[start] += 1
        self.memo[end] -= 1
        sum = 0

        for v in self.memo.values():
            sum += v
            if sum > 1:
                self.memo[start] -= 1
                self.memo[end] += 1
                return False
        return True


def test_my_calendar():
    obj = MyCalendar()
    assert obj.book(10, 20), 'wrong result'
    assert not obj.book(15, 25), 'wrong result'
    assert obj.book(20, 30), 'wrong result'


if __name__ == '__main__':
    test_my_calendar()
