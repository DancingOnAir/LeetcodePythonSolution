from bisect import bisect_right

MX = 1_001
is_prime = [True] * MX
primes = []
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MX, i):
            is_prime[j] = False


class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        m = bisect_right(primes, n)
        dp = [[float('inf')] * (s + 1) for _ in range(m + 1)]
        dp[m][0] = 0

        for i in range(m - 1, -1, -1):
            x = primes[i]
            for j in range(s + 1):
                if j < x:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = min(dp[i + 1][j - x] + 1, dp[i + 1][j])

        j = s
        while j > 0 and dp[0][j] == float('inf'):
            j -= 1

        res = []
        for i in range(m):
            if j == 0:
                break
            x = primes[i]
            if dp[i + 1][j - x] + 1 <= dp[i + 1][j]:
                res.append(x)
                j -= x
        return res


def test_max_primes():
    solution = Solution()
    assert solution.maxPrimeSubset(7, 20) == [2, 3, 5, 7], 'wrong result'
    assert solution.maxPrimeSubset(15, 18) == [5,13], 'wrong result'
    assert solution.maxPrimeSubset(5, 1) == [], 'wrong result'


if __name__ == '__main__':
    test_max_primes()
