from collections import Counter
from itertools import permutations


class Solution:
    def countAnagrams(self, s: str) -> int:
        def helper(w):
            return len(set(permutations(w)))

        res = 1

        for w in s.split():
            res *= helper(w)
            res %= 10 ** 9 + 7
        return res


def test_count_anagrams():
    solution = Solution()
    assert solution.countAnagrams("too hot") == 18, 'wrong result'
    assert solution.countAnagrams("aa") == 1, 'wrong result'


if __name__ == '__main__':
    test_count_anagrams()
