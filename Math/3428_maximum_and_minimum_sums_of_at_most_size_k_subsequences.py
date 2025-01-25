from typing import List
from math import pow


MOD = 10 ** 9 + 7
MX = 100000
fac = [0] * MX
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD
inv_fac = [0] * MX
inv_fac[-1] = pow(fac[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_fac[i - 1] = inv_fac[i] * i % MOD


class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        def comb(n, m):
            return fac[n] * inv_fac[m] * inv_fac[n - m] % MOD

        nums.sort()
        res = 0
        for i, x in enumerate(nums):
            cur = sum(comb(i, j) for j in range(min(k, i + 1))) % MOD
            # 当nums[n - 1 - i]做为最小值时，子序列个数和nums[i]做为最大值的个数是一样的，可以同时计算
            res += (x + nums[-1 - i]) * cur
        return res % MOD


def test_min_max_sums():
    solution = Solution()
    assert solution.minMaxSums([1, 2, 3], 2) == 24, 'wrong result'
    assert solution.minMaxSums([5, 0, 6], 1) == 22, 'wrong result'
    assert solution.minMaxSums([1, 1, 1], 2) == 12, 'wrong result'


if __name__ == '__main__':
    test_min_max_sums()
