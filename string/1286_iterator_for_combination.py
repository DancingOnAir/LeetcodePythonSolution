from itertools import combinations


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.finished = False
        self.pos = [x for x in range(combinationLength)]

    def next(self) -> str:
        res = ''.join(self.s[x] for x in self.pos)
        i = -1
        for k in range(len(self.pos) - 1, -1, -1):
            if self.pos[k] != len(self.s) - len(self.pos) + k:
                i = k
                break

        if i == -1:
            self.finished = True
        else:
            self.pos[i] += 1
            for j in range(i + 1, len(self.pos)):
                self.pos[j] = self.pos[j - 1] + 1
        return res

    def hasNext(self) -> bool:
        return not self.finished


def generate_combinations(l, n):
    end = int('1' * l, 2)
    res = list()
    for i in range(end + 1):
        b = "{0:b}".format(i)
        if b.count('1') == n:
            res.append(b.zfill(l))
    return res


class CombinationIterator2:
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.n = len(characters)
        self.combs = generate_combinations(self.n, combinationLength)
        self.m = len(self.combs) - 1
        pass

    def next(self) -> str:
        res = ''
        for i in range(self.n):
            if self.combs[self.m][i] == '1':
                res += self.characters[i]
        self.m -= 1
        return res

    def hasNext(self) -> bool:
        return self.m > -1


class CombinationIterator1:
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
