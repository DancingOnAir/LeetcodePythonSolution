from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return sum(x & 1 == 0 for x in nums) > 1


def test_has_trailing_zeros():
    solution = Solution()
    assert solution.hasTrailingZeros([1, 2, 3, 4, 5]), 'wrong result'
    assert solution.hasTrailingZeros([2, 4, 8, 16]), 'wrong result'
    assert not solution.hasTrailingZeros([1, 3, 5, 7, 9]), 'wrong result'


if __name__ == '__main__':
    test_has_trailing_zeros()
