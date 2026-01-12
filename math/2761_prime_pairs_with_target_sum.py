from typing import List


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def get_primes(x):
            primes = []
            is_primes = [True] * (x + 1)
            for i in range(2, x + 1):
                if is_primes[i]:
                    primes.append(i)
                    for j in range(i * i, x + 1, i):
                        is_primes[j] = False
            return primes, is_primes

        primes, is_primes = get_primes(n)
        if n % 2:
            return [[2, n - 2]] if n > 4 and is_primes[n - 2] else []
        res = []
        for p in primes:
            q = n - p
            if q < p:
                break
            if is_primes[q]:
                res.append([p, q])
        return res


def test_find_prime_pairs():
    solution = Solution()
    assert solution.findPrimePairs(261) == [], 'wrong result'
    assert solution.findPrimePairs(38) == [[7, 31], [19, 19]], 'wrong result'
    assert solution.findPrimePairs(10) == [[3, 7], [5, 5]], 'wrong result'
    assert solution.findPrimePairs(2) == [], 'wrong result'


if __name__ == '__main__':
    test_find_prime_pairs()
