from typing import List
from bisect import bisect_left


class Solution:
    # Sieve of Eratoshenes
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # TLE
        # def primes(x):
        #     i = 2
        #     while i * i <= x:
        #         if x % i != 0:
        #             i += 1
        #         else:
        #             return False
        #     return True
        #
        # p = list()
        # for i in range(left , right + 1):
        #     if primes(i):
        #         p.append(i)
        #
        # res = [-1, -1]
        # diff = right - left + 1
        # for i in range(len(p) - 1):
        #     if p[i + 1] - p[i] < diff:
        #         res = [p[i], p[i + 1]]
        #         diff = p[i + 1] - p[i]
        # return res

        sieve = [0] + [1] * right
        primes = [2]
        for i in range(3, right + 1, 2):
            if sieve[i]:
                primes.append(i)
                j = 2
                while i * j <= right:
                    sieve[i * j] = 0
                    j += 1

        res = [-1, -1]
        start = bisect_left(primes, left)
        for i in range(start, len(primes) - 1):
            if res[0] == -1 or res[1] - res[0] > primes[i + 1] - primes[i]:
                res = [primes[i], primes[i + 1]]
        return res


def test_closest_primes():
    solution = Solution()
    assert solution.closestPrimes(1, 1000000) == [2, 3], 'wrong result'
    assert solution.closestPrimes(10, 19) == [11, 13], 'wrong result'
    assert solution.closestPrimes(4, 6) == [-1, -1], 'wrong result'


if __name__ == '__main__':
    test_closest_primes()
