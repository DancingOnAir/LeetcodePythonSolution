from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        max_idx, min_idx = 0, 0
        for i in range(indexDifference, n):
            if nums[i - indexDifference] > nums[max_idx]:
                max_idx = i - indexDifference
            if nums[i - indexDifference] < nums[min_idx]:
                min_idx = i - indexDifference
            if abs(nums[i] - nums[min_idx]) >= valueDifference:
                return [min_idx, i]
            elif abs(nums[i] - nums[max_idx]) >= valueDifference:
                return [max_idx, i]
        return [-1, -1]


def test_find_indices():
    solution = Solution()
    assert solution.findIndices([5, 1, 4, 1], 2, 4) == [0, 3], 'wrong result'
    assert solution.findIndices([2, 1], 0, 0) == [0, 0], 'wrong result'
    assert solution.findIndices([1, 2, 3], 2, 4) == [-1, -1], 'wrong result'


if __name__ == '__main__':
    test_find_indices()
