from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.freq = 0


class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.m = dict()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.m.get(key, 0)
        self.m[key] = val

        node = self.root
        node.freq += delta
        for ch in key:
            node = node.children.setdefault(ch, TrieNode())
            node.freq += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.freq


class MapSum1:
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
