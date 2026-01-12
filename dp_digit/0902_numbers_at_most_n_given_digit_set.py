from typing import List
from functools import lru_cache
from bisect import bisect_right, bisect_left


class Solution:
    # https://leetcode.com/problems/numbers-at-most-n-given-digit-set/discuss/559624/Python-Digit-DP-(Pattern-For-Similar-Questions)
    # Variable idx is the current position in N,
    # prefix tells if the current number is the prefix of N,
    # bigger tells if the current number will be bigger than N when we reach full length.
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        N = list(map(int, str(n)))
        D = list(map(int, digits))

        @lru_cache(None)
        def dp(idx, prefix, bigger):
            if idx == len(N):
                return not bigger
            if not prefix and not bigger:
                return 1 + len(D) * dp(idx + 1, False, False)

            return 1 + sum(dp(idx + 1, prefix and d == N[idx], bigger or (prefix and d > N[idx])) for d in D)

        return dp(0, True, False) - 1

    # math solution
    def atMostNGivenDigitSet1(self, digits: List[str], n: int) -> int:
        N = str(n)
        n = len(N)
        res = sum(len(digits) ** i for i in range(1, n))

        i = 0
        while i < n:
            # here, N is str eg. is n = 1234, N = '1234', so N[0] is the the highest digit '1'
            res += sum(c < N[i] for c in digits) * (len(digits) ** (n - i - 1))
            if N[i] not in digits:
                break
            i += 1

        return res + (i == n)


def test_at_most_n_given_digit_set():
    solution = Solution()
    assert solution.atMostNGivenDigitSet(["1", "3", "5", "7"], 100) == 20, 'wrong result'
    assert solution.atMostNGivenDigitSet(["1", "4", "9"], 1000000000) == 29523, 'wrong result'
    assert solution.atMostNGivenDigitSet(["7"], 8) == 1, 'wrong result'
    assert solution.atMostNGivenDigitSet(["8"], 8) == 1, 'wrong result'


if __name__ == '__main__':
    test_at_most_n_given_digit_set()
