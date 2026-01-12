from typing import List
from math import gcd


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res = 2
        left, mul = 0, 1
        for right, x in enumerate(nums):
            while gcd(mul, x) > 1:
                mul //= nums[left]
                left += 1
            res = max(res, right - left + 1)
            mul *= x
        return res


def test_max_length():
    solution = Solution()
    assert solution.maxLength([1, 2, 1, 2, 1, 1, 1]) == 5, 'wrong result'
    assert solution.maxLength([2, 3, 4, 5, 6]) == 3, 'wrong result'
    assert solution.maxLength([1, 2, 3, 1, 4, 5, 1]) == 5, 'wrong result'


if __name__ == '__main__':
    test_max_length()
