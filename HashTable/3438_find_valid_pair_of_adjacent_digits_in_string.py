from collections import Counter
from itertools import pairwise


class Solution:
    def findValidPair(self, s: str) -> str:
        cnt = Counter(s)
        for x, y in pairwise(s):
            if x != y and cnt[x] == int(x) and cnt[y] == int(y):
                return x + y
        return ""


def test_find_valid_pair():
    solution = Solution()
    assert solution.findValidPair("2523533") == "23", 'wrong result'
    assert solution.findValidPair("221") == "21", 'wrong result'
    assert solution.findValidPair("22") == "", 'wrong result'


if __name__ == '__main__':
    test_find_valid_pair()
