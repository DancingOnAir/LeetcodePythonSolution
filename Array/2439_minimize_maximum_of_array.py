from typing import List
from math import ceil


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = total = 0
        for i, x in enumerate(nums):
            total += x
            res = max(res, total / (i + 1))
        return ceil(res)


def test_minimize_array_value():
    solution = Solution()
    assert solution.minimizeArrayValue([3, 7, 1, 6]) == 5, 'wrong result'
    assert solution.minimizeArrayValue([10, 1]) == 10, 'wrong result'


if __name__ == '__main__':
    test_minimize_array_value()

