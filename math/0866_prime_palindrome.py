class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_primes(x):
            return x > 1 and all(x % d for d in range(2, int(x ** 0.5) + 1))

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x //= 10
            return ans

        while True:
            if n == reverse(n) and is_primes(n):
                return n
            n += 1
            if 10 ** 7 <= n <= 10 ** 8:
                n = 10 ** 8

    # brute force, TLE
    def primePalindrome1(self, n: int) -> int:
        if n <= 2:
            return 2

        def helper():
            N = 10 ** 8 + 2
            is_prime = [True] * (N + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(N ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, N + 1, i):
                        is_prime[j] = False
            primes = [i for i in range(N + 1) if is_prime[i]]
            return primes

        primes = helper()
        palindrome_primes = []
        for p in primes:
            p = str(p)
            if p == p[::-1]:
                palindrome_primes.append(int(p))

        for x in palindrome_primes:
            if x >= n:
                return x
        return -1


def test_prime_palindrome():
    solution = Solution()
    assert solution.primePalindrome(6) == 7, 'wrong result'
    assert solution.primePalindrome(8) == 11, 'wrong result'
    assert solution.primePalindrome(13) == 101, 'wrong result'


if __name__ == '__main__':
    test_prime_palindrome()
