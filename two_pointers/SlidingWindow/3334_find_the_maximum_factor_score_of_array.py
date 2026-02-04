from typing import List
from math import gcd, lcm


class Solution:
    # gcd(x, 0) = x, lcm(x, 1) = x
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        suf_gcd = [0] * (n + 1)
        suf_lcm = [0] * n + [1]
        # 计算后缀
        for i in range(n - 1, -1, -1):
            suf_gcd[i] = gcd(nums[i], suf_gcd[i + 1])
            suf_lcm[i] = lcm(nums[i], suf_lcm[i + 1])

        res = suf_lcm[0] * suf_gcd[0]
        pre_gcd, pre_lcm = 0, 1
        for i, x in enumerate(nums):
            res = max(res, gcd(pre_gcd, suf_gcd[i + 1]) * lcm(pre_lcm, suf_lcm[i + 1]))
            # 计算前缀，漏算x
            pre_gcd = gcd(pre_gcd, x)
            pre_lcm = lcm(pre_lcm, x)
        return res


def test_max_score():
    solution = Solution()
    assert solution.maxScore([2,4,8,16]) == 64, 'wrong result'
    assert solution.maxScore([1,2,3,4,5]) == 60, 'wrong result'


if __name__ == '__main__':
    test_max_score()


