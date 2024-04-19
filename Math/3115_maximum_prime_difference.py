from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def helper():
            mark = [True] * 101
            primes = set()

            for i in range(2, 101):
                if mark[i]:
                    primes.add(i)

                for p in primes:
                    if i * p > 101:
                        break
                    mark[i * p] = False
                    if i % p == 0:
                        break

            return primes

        primes = helper()
        res = []
        for i, v in enumerate(nums):
            if v in primes:
                res.append(i)
        return res[-1] - res[0]

    def maximumPrimeDifference1(self, nums: List[int]) -> int:
        def helper():
            mark = [True] * 101
            primes = set()

            for i in range(2, 101):
                if mark[i]:
                    primes.add(i)

                for p in primes:
                    if i * p > 101:
                        break
                    mark[i * p] = False
                    if i % p == 0:
                        break

            return primes

        primes = helper()
        i, j = 0, len(nums) - 1
        left, right, res = -1, -1, 0
        while i <= j:
            if nums[i] in primes:
                left = i
            else:
                i += 1
            if nums[j] in primes:
                right = j
            else:
                j -= 1

            if left != -1 and right != -1:
                return right - left
        return -1


def test_maximum_prime_difference():
    solution = Solution()
    assert solution.maximumPrimeDifference([4, 2, 9, 5, 3]) == 3, 'wrong result'
    assert solution.maximumPrimeDifference([4, 8, 2, 8]) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximum_prime_difference()
