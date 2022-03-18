from collections import defaultdict


class MapSum:
    def __init__(self):
        self.m = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.m[key] = val

    def sum(self, prefix: str) -> int:
        return sum(v for k, v in self.m.items() if k.startswith(prefix))


def test_map_sum():
    obj = MapSum()
    obj.insert("apple", 3)
    assert obj.sum("ap") == 3, 'wrong result'
    obj.insert("app", 2)
    assert obj.sum("ap") == 5, 'wrong result'
