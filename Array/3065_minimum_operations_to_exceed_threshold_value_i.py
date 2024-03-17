from typing import List
from bisect import bisect_left


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return bisect_left(sorted(nums), k)


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([2, 11, 10, 1, 3], 10) == 3, 'wrong result'
    assert solution.minOperations([1, 1, 2, 4, 9], 1) == 0, 'wrong result'
    assert solution.minOperations([1, 1, 2, 4, 9], 9) == 4, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
