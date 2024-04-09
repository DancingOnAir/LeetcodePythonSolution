from typing import List
from functools import reduce


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # return bin(reduce(lambda x, y: x ^ y, nums) ^ k).count('1')
        return bin(reduce(lambda x, y: x ^ y, nums, k)).count('1')


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([2, 1, 3, 4], 1) == 2, 'wrong result'
    assert solution.minOperations([2, 0, 2, 0], 0) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
