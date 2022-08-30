from typing import List


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        pass


def test_maximum_segment_sum():
    solution = Solution()
    assert solution.maximumSegmentSum([1, 2, 5, 6, 1], [0, 3, 2, 4, 1]) == [14, 7, 2, 2, 0], 'wrong result'
    assert solution.maximumSegmentSum([3, 2, 11, 1], [3, 2, 1, 0]) == [16, 5, 3, 0], 'wrong result'


if __name__ == '__main__':
    test_maximum_segment_sum()

