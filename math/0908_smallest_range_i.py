from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mx, mi = max(nums), min(nums)
        return max((mx - k) - (mi + k), 0)

    def smallestRangeI1(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        max_diff = nums[-1] - nums[0]
        return 0 if max_diff <= 2 * k else max_diff - 2 * k


def test_smallest_range_i():
    solution = Solution()
    assert solution.smallestRangeI([1], 0) == 0, 'wrong result'
    assert solution.smallestRangeI([0, 10], 2) == 6, 'wrong result'
    assert solution.smallestRangeI([1, 3, 6], 3) == 0, 'wrong result'


if __name__ == '__main__':
    test_smallest_range_i()
