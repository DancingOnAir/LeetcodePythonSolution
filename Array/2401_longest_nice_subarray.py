from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 1
        cur_sum = nums[0]
        left = 0
        for right in range(1, len(nums)):
            while nums[right] & cur_sum != 0:
                cur_sum -= nums[left]
                left += 1

            cur_sum += nums[right]
            res = max(res, right - left + 1)
        return res


def test_longest_nice_subarray():
    solution = Solution()
    assert solution.longestNiceSubarray([1, 3, 8, 48, 10]) == 3, 'wrong result'
    assert solution.longestNiceSubarray([3, 1, 5, 11, 13]) == 1, 'wrong result'


if __name__ == '__main__':
    test_longest_nice_subarray()
