from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = bisect_left(nums, target)
        right = left
        for i in range(left, len(nums)):
            if nums[i] == target:
                right += 1
        return list(range(left, right))

    def targetIndices1(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l = bisect_left(nums, target)
        r = bisect_right(nums, target)
        if l >= len(nums) or nums[l] != target:
            return []
        return list(range(l, r))


def test_target_indices():
    solution = Solution()
    assert solution.targetIndices([1], 2) == [], 'wrong result'
    assert solution.targetIndices([1, 2, 5, 2, 3], 2) == [1, 2], 'wrong result'
    assert solution.targetIndices([1, 2, 5, 2, 3], 3) == [3], 'wrong result'
    assert solution.targetIndices([1, 2, 5, 2, 3], 5) == [4], 'wrong result'


if __name__ == '__main__':
    test_target_indices()
