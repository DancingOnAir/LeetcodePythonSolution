from typing import List


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[i + 1] - nums[i] for i in range(len(nums) - 1))


def test_find_value_of_partition():
    solution = Solution()
    assert solution.findValueOfPartition(
        [771963616, 776813785, 28603508, 639757365, 958320601, 988875230, 197812712, 27130325, 844013034,
         334036196]) == 1473183, 'wrong result'
    assert solution.findValueOfPartition([1, 3, 2, 4]) == 1, 'wrong result'
    assert solution.findValueOfPartition([100, 1, 10]) == 9, 'wrong result'


if __name__ == '__main__':
    test_find_value_of_partition()
