from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = list()
        for num in nums:
            i = bisect_left(dp, num)
            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num
        return len(dp)

    def lengthOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


def test_length_of_lis():
    solution = Solution()

    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    assert solution.lengthOfLIS(nums1) == 4, 'wrong result'
    nums2 = [0, 1, 0, 3, 2, 3]
    assert solution.lengthOfLIS(nums2) == 4, 'wrong result'
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    assert solution.lengthOfLIS(nums3) == 1, 'wrong result'


if __name__ == '__main__':
    test_length_of_lis()
