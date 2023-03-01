from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = j = 0
        for i in range(n // 2):
            j += 1
            j = bisect_left(nums, nums[i] * 2, j)
            if j == n:
                break
            res += 1

        return res * 2


def test_max_num_of_marked_indices():
    solution = Solution()
    assert solution.maxNumOfMarkedIndices([3, 5, 2, 4]) == 2, 'wrong result'
    assert solution.maxNumOfMarkedIndices([9, 2, 5, 4]) == 4, 'wrong result'
    assert solution.maxNumOfMarkedIndices([7, 6, 8]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_num_of_marked_indices()
