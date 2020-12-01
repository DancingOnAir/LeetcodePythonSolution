from typing import List


class Solution:
    # dp
    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n+1):
            dp[i] = i
        for i in range(2, n+1):
            for j in range(2, i):
                if not i % j:
                    dp[i] = min(dp[i], dp[i // j] + j)
        return dp[n]

    # prime factorization solution
    def minSteps(self, n: int) -> int:
        for i in range(2, int(n ** 1/2) + 1):
            if not n % i:
                return self.minSteps(n // i) + i
        return 0 if n == 1 else n

    # not elegant prime factorization solution
    def minSteps1(self, n: int) -> int:
        if n < 2:
            return 0

        num = n
        factors = list()
        for i in range(2, int(num ** (1/2)) + 1):
            for j in range(2, num):
                if not num % j:
                    factors.append(j)
                    num //= j
                    break

        if not len(factors):
            return n
        else:
            return sum(factors + [num])


def test_min_steps():
    solution = Solution()

    assert solution.minSteps(3) == 3, "wrong result"
    assert solution.minSteps(5) == 5, "wrong result"
    assert solution.minSteps(15) == 8, "wrong result"
    assert solution.minSteps(24) == 9, "wrong result"


if __name__ == '__main__':
    test_min_steps()
