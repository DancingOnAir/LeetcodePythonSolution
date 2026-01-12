class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

        primes = set()
        n = len(s)
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur = cur * 10 + int(s[j])
                if is_prime(cur):
                    primes.add(cur)
        primes = sorted(primes)
        if len(primes) < 3:
            return sum(primes)
        return sum(primes[-3:])

    # TLE
    def sumOfLargestPrimes1(self, s: str) -> int:
        def get_primes(x):
            is_primes = [True] * (x)
            primes = []
            for i in range(2, x):
                if is_primes[i]:
                    primes.append(str(i))
                    for j in range(i * i, x, i):
                        is_primes[j] = False
            return primes

        p = get_primes(int(s) + 1)
        res = []
        for ss in p[::-1]:
            if ss in s:
                res.append(ss)
            if len(res) == 3:
                break
        return sum(map(int, res)) if res else 0


def test_sum_of_largest_primes():
    solution = Solution()
    assert solution.sumOfLargestPrimes("12234") == 1469, 'wrong result'
    assert solution.sumOfLargestPrimes("111") == 11, 'wrong result'


if __name__ == '__main__':
    test_sum_of_largest_primes()
