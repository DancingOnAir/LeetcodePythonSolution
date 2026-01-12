from typing import List


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        nums.sort()
        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])


def test_minimize_sum():
    solution = Solution()
    assert solution.minimizeSum([58, 42, 8, 75, 28]) == 30, 'wrong result'
    assert solution.minimizeSum([1, 4, 3]) == 0, 'wrong result'
    assert solution.minimizeSum([1, 4, 7, 8, 5]) == 3, 'wrong result'


if __name__ == '__main__':
    test_minimize_sum()
