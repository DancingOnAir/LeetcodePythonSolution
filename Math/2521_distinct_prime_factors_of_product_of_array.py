from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def prime(x):
            factors = set()
            i = 2
            while i * i <= x:
                while x % i == 0:
                    x //= i
                    factors.add(i)
                i += 1

            if x > 1:
                factors.add(x)
            return factors

        res = set()
        for num in nums:
            res |= prime(num)
        return len(res)


def test_distinct_prime_factors():
    solution = Solution()
    assert solution.distinctPrimeFactors([2, 4, 3, 7, 10, 6]) == 4, 'wrong result'
    assert solution.distinctPrimeFactors([2, 4, 8, 16]) == 1, 'wrong result'


if __name__ == '__main__':
    test_distinct_prime_factors()
