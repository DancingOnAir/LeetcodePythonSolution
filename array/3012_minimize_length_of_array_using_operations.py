from typing import List
from collections import Counter


class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        mi = min(nums)
        cnt = 0
        for x in nums:
            if x % mi:
                return 1
            elif x == mi:
                cnt += 1
        return (cnt + 1) // 2


def test_minimum_array_length():
    solution = Solution()
    assert solution.minimumArrayLength([1, 4, 3, 1]) == 1, 'wrong result'
    assert solution.minimumArrayLength([5, 5, 5, 10, 5]) == 2, 'wrong result'
    assert solution.minimumArrayLength([2, 3, 4]) == 1, 'wrong result'


if __name__ == '__main__':
    test_minimum_array_length()
