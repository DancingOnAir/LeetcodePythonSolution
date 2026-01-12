from typing import List
from functools import reduce


class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        res, tot, = 0, -1
        for x in nums:
            tot &= x
            if tot == 0:
                res += 1
                tot = -1
        return max(1, res)


def test_max_subarrays():
    solution = Solution()
    # 21: 10101
    # 22: 10110
    # 29: 11101
    assert solution.maxSubarrays([22, 21, 29, 22]) == 1, 'wrong result'
    assert solution.maxSubarrays([0, 8, 0, 0, 0, 23]) == 4, 'wrong result'
    assert solution.maxSubarrays([1, 0, 2, 0, 1, 2]) == 3, 'wrong result'
    assert solution.maxSubarrays([5, 7, 1, 3]) == 1, 'wrong result'


if __name__ == '__main__':
    test_max_subarrays()
