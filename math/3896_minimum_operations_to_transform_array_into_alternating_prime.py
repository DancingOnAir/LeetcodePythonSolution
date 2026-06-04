from math import isqrt


MX = 100004
primes = [0, 0] + [1] * (MX - 1)
for i in range(2, isqrt(MX) + 1):
    if primes[i]:
        for j in range(i * i, MX, i):
            primes[j] = 0


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        res = 0
        for i, x in enumerate(nums):
            while primes[x] == i % 2:
                res += 1
                x += 1
        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([1, 2, 3, 4]) == 3, 'wrong result'
    assert solution.minOperations([5, 6, 7, 8]) == 0, 'wrong result'
    assert solution.minOperations([4, 4]) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
