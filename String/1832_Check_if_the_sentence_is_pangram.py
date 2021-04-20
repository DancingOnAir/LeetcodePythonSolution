from collections import Counter
from operator import ior
from functools import reduce


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return reduce(ior, map(lambda c: 1 << (ord(c) - 97), sentence)) == (1 << 26) - 1

    def checkIfPangram2(self, sentence: str) -> bool:
        return len(Counter(sentence)) == 26

    def checkIfPangram1(self, sentence: str) -> bool:
        counter = [0] * 26
        for c in sentence:
            counter[ord(c) - 97] += 1

        return counter.count(0) == 0


def test_check_if_pangram():
    solution = Solution()
    assert solution.checkIfPangram('thequickbrownfoxjumpsoverthelazydog'), 'wrong result'
    assert not solution.checkIfPangram('leetcode'), 'wrong result'


if __name__ == '__main__':
    test_check_if_pangram()
