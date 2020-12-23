from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        memo = dict()
        for i in range(n):
            if nums[i] not in memo:
                memo[nums[i]] = 1
                if nums[i] + 1 not in memo and nums[i] - 1 not in memo:
                    dp[i+1] = dp[i] + nums[i]
                elif nums[]
            else:
                memo[nums[i]] += 1
        return dp[n]


def test_delete_and_earn():
    solution = Solution()

    nums1 = [3, 4, 2]
    assert solution.deleteAndEarn(nums1) == 6, 'wrong result'

    nums2 = [2, 2, 3, 3, 3, 4]
    assert solution.deleteAndEarn(nums2) == 9, 'wrong result'


if __name__ == '__main__':
    test_delete_and_earn()
