from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < 2:
            return 0
        nums.sort()
        res = nums[-1] - nums[0]
        for i in range(n - 1):
            mx = max(nums[-1] - k, nums[i] + k)
            mi = min(nums[0] + k, nums[i + 1] - k)
            res = min(res, mx - mi)
        return res


def test_smallest_range_ii():
    solution = Solution()
    assert solution.smallestRangeII([1], 0) == 0, 'wrong result'
    assert solution.smallestRangeII([0, 10], 2) == 6, 'wrong result'
    assert solution.smallestRangeII([1, 3, 6], 3) == 3, 'wrong result'


if __name__ == '__main__':
    test_smallest_range_ii()
