from collections import defaultdict
from bisect import bisect_right


class TimeMap:
    def __init__(self):
        self.memo = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.memo[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        p = bisect_right(self.memo[key], timestamp, key=lambda x: x[1] <= timestamp)
        return self.memo[key][p][0] if p != -1 else ''


def test_time_map():
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)
    assert time_map.get("foo", 1) == 'bar', 'wrong result'
    assert time_map.get("foo", 3) == 'bar', 'wrong result'

    time_map.set("foo", "bar2", 4)
    assert time_map.get("foo", 4) == 'bar2', 'wrong result'
    assert time_map.get("foo", 5) == 'bar2', 'wrong result'


if __name__ == '__main__':
    test_time_map()

