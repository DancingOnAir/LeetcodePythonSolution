from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0

        total = sum(nums)
        dp = [1] + [0] * total

        for num in nums:
            for i in range(total, 0, -1):
                if i >= num:
                    dp[i] += dp[i - num]
                if i + num <= total:
                    dp[i] += dp[i + num]
        return dp[S]
        pass


def test_find_target_sum_ways():
    solution = Solution()
    assert solution.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5, 'wrong result'


if __name__ == '__main__':
    test_find_target_sum_ways()
