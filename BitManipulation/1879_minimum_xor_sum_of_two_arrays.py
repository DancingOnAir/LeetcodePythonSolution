from typing import List
from functools import lru_cache


class Solution:
    # i表示用了几个nums1里的元素，j是选择nums2里的元素
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def dp(mask):
            i = bin(mask).count('1')
            if i >= n:
                return 0

            return min((nums1[i] ^ nums2[j]) + dp(mask + (1 << j)) for j in range(n) if (mask & (1 << j)) == 0)

        n = len(nums2)
        return dp(0)


def test_minimum_xor_sum():
    solution = Solution()
    assert solution.minimumXORSum([1, 2], [2, 3]) == 2, 'wrong result'
    assert solution.minimumXORSum([1, 0, 3], [5, 3, 4]) == 8, 'wrong result'


if __name__ == '__main__':
    test_minimum_xor_sum()
