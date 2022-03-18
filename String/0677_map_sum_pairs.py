from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.freq = 0


# trie which is implemented by the class TrieNode
class MapSum2:
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


# brute force
class MapSum1:
    def __init__(self):
        self.m = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.m[key] = val

    def sum(self, prefix: str) -> int:
        return sum(v for k, v in self.m.items() if k.startswith(prefix))


# trie which is implemented by defaultdict
class MapSum:
    def __init__(self):
        self.trie = defaultdict(int)
        self.v = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        delta = val - self.v[key]
        self.v[key] = val
        t = self.trie
        for ch in key:
            t = t.setdefault(ch, defaultdict(int))
            t['val'] += delta

    def sum(self, prefix: str) -> int:
        t = self.trie
        for ch in prefix:
            if ch not in t:
                return 0
            t = t[ch]
        return t['val']


def test_map_sum():
    obj = MapSum()
    obj.insert("apple", 3)
    assert obj.sum("ap") == 3, 'wrong result'
    obj.insert("app", 2)
    assert obj.sum("ap") == 5, 'wrong result'
