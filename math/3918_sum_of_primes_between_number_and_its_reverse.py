MX = 1001
is_prime = [False, False] + [True] * (MX - 2)
for i in range(2, int(MX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MX, i):
            is_prime[j] = False

ps = [0] * MX
for i in range(1, MX):
    ps[i] = ps[i - 1] + (i if is_prime[i] else 0)


class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = 0
        x = n
        while x > 0:
            r = r * 10 + x % 10
            x //= 10
        return ps[max(n, r)] - ps[min(n, r) - 1]


def test_sum_of_primes_in_range():
    solution = Solution()
    assert solution.sumOfPrimesInRange(13) == 132, 'wrong result'
    assert solution.sumOfPrimesInRange(10) == 17, 'wrong result'
    assert solution.sumOfPrimesInRange(8) == 0, 'wrong result'


if __name__ == '__main__':
    test_sum_of_primes_in_range()
