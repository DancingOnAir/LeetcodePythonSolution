from typing import List
from collections import defaultdict


class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        dp1 = defaultdict(int)
        dp2 = defaultdict(int)
        dp2[0] = 1
        MOD = 1_000_000_007
        ps = 0
        for i, x in enumerate(nums):
            ps ^= x
            last1 = dp2[ps ^ target1]
            last2 = dp1[ps ^ target2]
            if i == len(nums) - 1:
                return (last1 + last2) % MOD
            dp1[ps] = (dp1[ps] + last1) % MOD
            dp2[ps] = (dp2[ps] + last2) % MOD


def test_alternating_xor():
    solution = Solution()
    assert solution.alternatingXOR([2, 3, 1, 4], target1=1, target2=5) == 1, 'wrong result'
    assert solution.alternatingXOR([1, 0, 0], target1=1, target2=0) == 3, 'wrong result'
    assert solution.alternatingXOR([7], target1=1, target2=7) == 0, 'wrong result'


if __name__ == '__main__':
    test_alternating_xor()
