from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.ended = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for ch in word:
            root = root.children.setdefault(ch, TrieNode())
        root.ended = True

    def search(self, word):
        root = self.root

        for ch in word:
            if root.ended:
                return True
            if ch not in root.children:
                return False
            root = root.children[ch]

        return root.ended


class StreamChecker:
    def __init__(self, words: List[str]):
        self.letters = ''
        self.trie = Trie()
        for w in words:
            self.trie.insert(w[::-1])

    def query(self, letter: str) -> bool:
        self.letters = letter + self.letters
        return self.trie.search(self.letters)


def test_stream_checker():
    streamChecker = StreamChecker(["cd", "f", "kl"])
    assert not streamChecker.query("a"), 'wrong result'
    assert not streamChecker.query("b"), 'wrong result'
    assert not streamChecker.query("c"), 'wrong result'
    assert streamChecker.query("d"), 'wrong result'
    assert not streamChecker.query("e"), 'wrong result'
    assert streamChecker.query("f"), 'wrong result'
    assert not streamChecker.query("g"), 'wrong result'
    assert not streamChecker.query("h"), 'wrong result'
    assert not streamChecker.query("i"), 'wrong result'
    assert not streamChecker.query("j"), 'wrong result'
    assert not streamChecker.query("k"), 'wrong result'
    assert streamChecker.query("l"), 'wrong result'


if __name__ == '__main__':
    test_stream_checker()
