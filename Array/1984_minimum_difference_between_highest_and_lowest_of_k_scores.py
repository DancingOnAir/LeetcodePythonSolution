from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        res = float('inf')
        for r in range(len(nums)):
            if r - l + 1 == k:
                res = min(res, nums[r] - nums[l])
                l += 1
        return res


def test_minimum_difference():
    solution = Solution()
    assert solution.minimumDifference([90], 1) == 0, 'wrong result'
    assert solution.minimumDifference([9, 4, 1, 7], 2) == 2, 'wrong result'


if __name__ == '__main__':
    test_minimum_difference()
