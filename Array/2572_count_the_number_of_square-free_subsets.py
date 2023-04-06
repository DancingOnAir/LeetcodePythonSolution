from typing import List
from collections import Counter


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        # 30以内的质数
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        # sf意思是square-free number, 这里sf_mask[i]表示数字i的质因数集合，使用二进制表示。
        sf_mask = [0] * 31
        for i in range(2, 31):
            for j, p in enumerate(primes):
                if i % p == 0:
                    if i % (p * p) == 0:
                        sf_mask[i] = -1
                        break
                    # 把质因数p的下标加入到集合中
                    sf_mask[i] |= 1 << j

        MOD = 10 ** 9 + 7
        M = 1 << len(primes)
        # f[i]表示恰好组成质因数集合i的方案数
        f = [0] * M
        # 质因数集合为空集的方案数为1
        f[0] = 1
        for x in nums:
            mask = sf_mask[x]
            if mask >= 0:
                for j in range(M - 1, mask - 1, -1):
                    # j是mask的子集
                    if (j | mask) == j:
                        # 不选mask和选mask
                        f[j] = (f[j] + f[j ^ mask]) % MOD
        # -1 是为了去掉nums的空集
        return (sum(f) - 1) % MOD


def test_square_free_subsets():
    solution = Solution()
    assert solution.squareFreeSubsets([3, 4, 4, 5]) == 3, 'wrong result'
    assert solution.squareFreeSubsets([1]) == 1, 'wrong result'


if __name__ == '__main__':
    test_square_free_subsets()
