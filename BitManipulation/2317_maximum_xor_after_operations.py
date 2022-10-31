from typing import List
from functools import reduce


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x | y, nums)


def test_maximum_xor():
    solution = Solution()
    assert solution.maximumXOR([3, 2, 4, 6]) == 7, 'wrong result'
    assert solution.maximumXOR([1, 2, 3, 9, 2]) == 11, 'wrong result'


if __name__ == '__main__':
    test_maximum_xor()
