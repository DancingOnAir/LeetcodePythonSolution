from typing import List
from collections import Counter
from itertools import product


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        # def sieve_of_euler(x):
        #     n = 10 ** (x + 1)
        #     prime = [True] * n
        #
        #     for i in range(2, int(n ** 0.5) + 1):
        #         if prime[i]:
        #             for j in range(i * i, n, i):
        #                 prime[j] = False
        #     return [i for i in range(2, n) if prime[i]]
        #
        # def is_prime(x):
        #     if x < 2:
        #         return False
        #
        #     for p in primes:
        #         if x % p == 0:
        #             return False
        #         if p > x ** 0.5:
        #             break
        #     return True

        def is_prime(num):
            if num < 10 or num % 2 == 0:
                return False
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

        nums = []
        m, n, d = len(mat), len(mat[0]), (-1, 0, 1)
        # primes = sieve_of_euler(max(m, n))

        for x, y, dx, dy in product(range(m), range(n), d, d):
            if dx == dy == 0:
                continue

            X, Y, val = x + dx, y + dy, mat[x][y]
            while 0 <= X < m and 0 <= Y < n:
                val = val * 10 + mat[X][Y]
                nums.append(val)
                X += dx
                Y += dy

        cnt = Counter(nums)
        return max(filter(is_prime, cnt), key=lambda x: (cnt[x], x), default=-1)


def test_most_frequent_prime():
    solution = Solution()
    assert solution.mostFrequentPrime([[1, 1], [9, 9], [1, 1]]) == 19, 'wrong result'
    assert solution.mostFrequentPrime([[7]]) == -1, 'wrong result'
    assert solution.mostFrequentPrime([[9, 7, 8], [4, 6, 5], [2, 8, 6]]) == 97, 'wrong result'


if __name__ == '__main__':
    test_most_frequent_prime()
