from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        x = sorted(c.values())

        if x[0] == 1:
            if len(set(x[1:])) == 1:
                return True
        x[-1] -= 1
        if len(set(x)) == 1:
            return True

        return False

    # my method
    def equalFrequency1(self, word: str) -> bool:
        c = Counter(word)
        c = Counter(c.values())

        if len(c) == 1:
            return list(c.keys())[0] == 1 or list(c.values())[0] == 1
        elif len(c) > 2:
            return False

        k1, k2 = sorted(c.keys(), key=lambda x: (c[x], x))
        if c[k1] == 1:
            if k1 == 1 or k1 - k2 == 1 or (c[k2] == 1 and k2 - k1 == 1):
                return True

        return False


def test_equal_frequency():
    solution = Solution()
    assert solution.equalFrequency("cccaa"), 'wrong result'
    assert solution.equalFrequency("cccd"), 'wrong result'
    assert solution.equalFrequency("bac"), 'wrong result'
    assert solution.equalFrequency("abcc"), 'wrong result'
    assert not solution.equalFrequency("aazz"), 'wrong result'


if __name__ == '__main__':
    test_equal_frequency()
