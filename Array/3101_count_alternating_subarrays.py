from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        res, left = 0, 0
        for right in range(1, len(nums)):
            if nums[right - 1] != nums[right]:
                continue
            res += (1 + (right - left)) * (right - left) // 2
            left = right

        return res + (1 + (len(nums) - left)) * (len(nums) - left) // 2


def test_count_alternating_subarrays():
    solution = Solution()
    assert solution.countAlternatingSubarrays([0, 1, 1, 1]) == 5, 'wrong result'
    assert solution.countAlternatingSubarrays([1, 0, 1, 0]) == 10, 'wrong result'


if __name__ == '__main__':
    test_count_alternating_subarrays()
