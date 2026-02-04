from typing import List


class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                return i + 1
        return 0


def test_minimum_prefix_length():
    solution = Solution()
    assert solution.minimumPrefixLength([1, -1, 2, 3, 3, 4, 5]) == 4, 'wrong result'
    assert solution.minimumPrefixLength([4, 3, -2, -5]) == 3, 'wrong result'
    assert solution.minimumPrefixLength([1, 2, 3, 4]) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_prefix_length()
