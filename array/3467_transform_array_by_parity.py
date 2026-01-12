from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return sorted(x & 1 for x in nums)


def test_transform_array():
    solution = Solution()
    assert solution.transformArray([4, 3, 2, 1]) == [0, 0, 1, 1], 'wrong result'
    assert solution.transformArray([1, 5, 1, 4, 2]) == [0, 0, 1, 1, 1], 'wrong result'


if __name__ == '__main__':
    test_transform_array()
