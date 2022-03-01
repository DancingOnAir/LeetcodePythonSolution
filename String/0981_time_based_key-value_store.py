from collections import defaultdict
from bisect import bisect_right


class TimeMap:
    def __init__(self):
        self.key_timestamp = defaultdict(list)
        self.timestamp_value = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_timestamp[key].append(timestamp)
        self.timestamp_value[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        p = bisect_right(self.key_timestamp[key], timestamp)
        if p == 0:
            return ''

        return self.timestamp_value[self.key_timestamp[key][p - 1]]


def test_time_map():
    time_map = TimeMap()
    time_map.set("foo", "bar", 2)
    assert time_map.get("foo", 1) == '', 'wrong result'
    assert time_map.get("foo", 2) == 'bar', 'wrong result'
    assert time_map.get("foo", 3) == 'bar', 'wrong result'

    time_map.set("foo", "bar2", 4)
    assert time_map.get("foo", 4) == 'bar2', 'wrong result'
    assert time_map.get("foo", 5) == 'bar2', 'wrong result'


if __name__ == '__main__':
    test_time_map()

