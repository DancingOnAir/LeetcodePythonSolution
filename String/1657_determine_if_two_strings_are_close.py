from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and sorted(Counter(word1).values()) == sorted(Counter(word2).values())

    def closeStrings1(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        if sorted(list(c1.keys())) != sorted(list(c2.keys())) or sorted(list(c1.values())) != sorted(list(c2.values())):
            return False
        return True


def test_close_strings():
    solution = Solution()

    assert solution.closeStrings('abc', 'bca'), 'wrong result'
    assert not solution.closeStrings('a', 'aa'), 'wrong result'
    assert solution.closeStrings('cabbba', 'abbccc'), 'wrong result'
    assert not solution.closeStrings('cabbba', 'aabbss'), 'wrong result'


if __name__ == '__main__':
    test_close_strings()
