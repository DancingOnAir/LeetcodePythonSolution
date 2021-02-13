from typing import List


class Solution:
    # dp 1-0 knapsack problem, equals find a target which is (sum(nums) - S) / 2
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0

        target = sum(nums) - S
        if target < 0 or (target & 1):
            return 0

        target >>= 1
        dp = [1] + [0] * target

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[target]


def test_find_target_sum_ways():
    solution = Solution()
    assert solution.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5, 'wrong result'


if __name__ == '__main__':
    test_find_target_sum_ways()
