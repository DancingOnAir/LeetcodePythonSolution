from typing import List
from collections import Counter


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        left = []
        cnt = set()
        for x in nums:
            cnt.add(x)
            left.append(len(cnt))

        right = []
        cnt.clear()
        for x in nums[::-1]:
            cnt.add(x)
            right.append(len(cnt))
        right.reverse()
        return [left[i] - right[i + 1] for i in range(len(nums) - 1)] + [left[-1]]


def test_distinct_difference_array():
    solution = Solution()
    assert solution.distinctDifferenceArray([1, 2, 3, 4, 5]) == [-3, -1, 1, 3, 5], 'wrong result'
    assert solution.distinctDifferenceArray([3, 2, 3, 4, 2]) == [-2, -1, 0, 2, 3], 'wrong result'


if __name__ == '__main__':
    test_distinct_difference_array()
