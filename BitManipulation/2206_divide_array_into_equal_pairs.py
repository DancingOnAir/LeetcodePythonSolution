from typing import List
from collections import Counter


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(x % 2 == 0 for x in Counter(nums).values())


def test_divide_array():
    solution = Solution()
    assert solution.divideArray([3, 2, 3, 2, 2, 2]), 'wrong result'
    assert not solution.divideArray([1, 2, 3, 4]), 'wrong result'


if __name__ == '__main__':
    test_divide_array()
