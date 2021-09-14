from itertools import combinations


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combs = list(map(''.join, combinations(characters, combinationLength)))[::-1]

    def next(self) -> str:
        return self.combs.pop()

    def hasNext(self) -> bool:
        return bool(self.combs)


def test_combination_iterator():
    combination_iterator = CombinationIterator("abc", 2)
    assert combination_iterator.next() == 'ab', 'wrong result'
    assert combination_iterator.hasNext(), 'wrong result'
    assert combination_iterator.next() == 'ac', 'wrong result'
    assert combination_iterator.hasNext(), 'wrong result'
    assert combination_iterator.next() == 'bc', 'wrong result'
    assert not combination_iterator.hasNext(), 'wrong result'


if __name__ == '__main__':
    test_combination_iterator()
