from bisect import bisect_right

MX = 1_000_001
is_prime = [True] * MX
primes = []
prime_sum = []
s = 0
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        s += i
        prime_sum.append(s)
        for j in range(i * i, MX, i):
            is_prime[j] = False


class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        i = bisect_right(primes, n)
        j = bisect_right(prime_sum, s, 0, i)
        return primes[:j]


def test_max_primes():
    solution = Solution()
    assert solution.maxPrimes(7, 20) == [2, 3, 5, 7], 'wrong result'
    assert solution.maxPrimes(15, 15) == [2, 3, 5], 'wrong result'
    assert solution.maxPrimes(5, 1) == [], 'wrong result'


if __name__ == '__main__':
    test_max_primes()
