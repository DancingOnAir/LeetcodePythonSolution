MX = 1_000_001
prime_divisors = [[] for _ in range(MX)]
for i in range(2, MX):
    # 质数
    if not prime_divisors[i]:
        for j in range(i, MX, i):
            prime_divisors[j].append(i)


class Solution:
    def maxSubarray(self, nums: list[int], k: int) -> int:
        res = float('-inf')
        f = 0
        for x in nums:
            f = max(f, 0) + (-x if x % k else x)
            res = max(res, f)
        return res

    def divisibleGame(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        all_prime_divisors = []
        for x in nums:
            all_prime_divisors.extend(prime_divisors[x])

        if not all_prime_divisors:
            return MOD - 2

        all_prime_divisors = sorted(set(all_prime_divisors))
        max_diff = 0
        best_k = 0
        for k in all_prime_divisors:
            diff = self.maxSubarray(nums, k)
            if diff > max_diff:
                max_diff = diff
                best_k = k
        return max_diff * best_k % MOD


def test_divisible_game():
    solution = Solution()
    assert solution.divisibleGame([1, 4, 6, 8]) == 36, 'wrong result'
    assert solution.divisibleGame([2, 1, 2]) == 6, 'wrong result'
    assert solution.divisibleGame([1]) == 1000000005, 'wrong result'


if __name__ == '__main__':
    test_divisible_game()
