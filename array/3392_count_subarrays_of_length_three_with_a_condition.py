from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = tot = left = 0
        for right, x in enumerate(nums):
            tot += x
            if right > 1:
                if tot == (nums[left] + x) * 3:
                    res += 1
                tot -= nums[left]
                left += 1
        return res


def test_count_subarrays():
    solution = Solution()
    assert solution.countSubarrays([1, 2, 1, 4, 1]) == 1, 'wrong result'
    assert solution.countSubarrays([1, 1, 1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_subarrays()
