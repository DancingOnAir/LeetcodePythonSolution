from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n - indexDifference):
            for j in range(i + indexDifference, n):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]


def test_find_indices():
    solution = Solution()
    assert solution.findIndices([5, 1, 4, 1], 2, 4) == [0, 3], 'wrong result'
    assert solution.findIndices([2, 1], 0, 0) == [0, 0], 'wrong result'
    assert solution.findIndices([1, 2, 3], 2, 4) == [-1, -1], 'wrong result'


if __name__ == '__main__':
    test_find_indices()
