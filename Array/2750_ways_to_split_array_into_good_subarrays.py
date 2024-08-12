from typing import List
from functools import reduce


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        left = -1
        res = 0
        for right, x in enumerate(nums):
            if x == 1:
                if res == 0:
                    res = 1
                else:
                    res *= right - left
                    res %= 10 ** 9 + 7
                left = right
        return res

    def numberOfGoodSubarraySplits1(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right and (nums[left] == 0 or nums[left] == 0):
            if nums[left] == 0:
                left += 1
            if nums[right] == 0:
                right -= 1

        nums = nums[left: right + 1]
        if not nums:
            return 0

        cnt, zeros = 0, []
        for x in nums:
            if x == 1 and cnt != 0:
                zeros.append(cnt)
                cnt = 0
            elif x == 0:
                cnt += 1

        if len(zeros) == 0:
            return 1

        res = 1
        for x in zeros:
            res *= (x + 1)
        return res % (10 ** 9 + 7)


def test_number_of_good_subarray_splits():
    solution = Solution()
    assert solution.numberOfGoodSubarraySplits([0, 1, 0, 0, 1]) == 3, 'wrong result'
    assert solution.numberOfGoodSubarraySplits([0, 1, 0]) == 1, 'wrong result'


if __name__ == '__main__':
    test_number_of_good_subarray_splits()
