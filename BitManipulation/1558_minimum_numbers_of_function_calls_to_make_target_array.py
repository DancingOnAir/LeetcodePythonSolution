from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return sum(bin(x).count('1') for x in nums) + len(bin(max(nums))) - 3


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([1,5]) == 5, 'wrong result'
    assert solution.minOperations([2, 2]) == 3, 'wrong result'
    assert solution.minOperations([4, 2, 5]) == 6, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
