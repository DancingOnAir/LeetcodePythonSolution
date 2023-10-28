from collections import Counter
from itertools import permutations
from math import factorial


class Solution:
    def countAnagrams(self, s: str) -> int:
        def helper(w):
            fact = factorial(len(w))
            c = Counter(w)
            inv_fact = 1
            for v in c.values():
                inv_fact *= factorial(v)
            return fact // inv_fact

        res = 1
        mod = 10 ** 9 + 7
        for w in s.split():
            res *= helper(w)

        return res % mod

    # TLE
    def countAnagrams1(self, s: str) -> int:
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
