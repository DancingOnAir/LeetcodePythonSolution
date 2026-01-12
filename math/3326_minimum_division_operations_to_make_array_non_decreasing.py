from functools import lru_cache
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        @lru_cache(None)
        def get_lpf(x):
            LPF = [0] * x
            for i in range(2, x):
                if LPF[i] == 0:
                    for j in range(i, x, i):
                        if LPF[j] == 0:
                            LPF[j] = i
            return LPF

        lpf = get_lpf(max(nums) + 1)
        res = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                nums[i] = lpf[nums[i]]
                if nums[i] > nums[i + 1]:
                    return -1
                res += 1
        return res

    # TLE
    def minOperations1(self, nums: List[int]) -> int:
        def get_primes(x):
            primes = []
            is_prime = [True] * (x + 1)
            for i in range(2, x + 1):
                if is_prime[i]:
                    primes.append(i)
                    for j in range(i * i, x + 1, i):
                        is_prime[j] = False
            return primes

        primes = get_primes(max(nums))
        res = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue

            for p in primes:
                if p > nums[i] // 2:
                    break
                if nums[i] % p == 0:
                    nums[i] = p
                    res += 1
                    break
            if nums[i] > nums[i + 1]:
                return -1
        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([105, 11]) == 1, 'wrong result'
    assert solution.minOperations([25, 7]) == 1, 'wrong result'
    assert solution.minOperations([7, 7, 6]) == -1, 'wrong result'
    assert solution.minOperations([1, 1, 1, 1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
