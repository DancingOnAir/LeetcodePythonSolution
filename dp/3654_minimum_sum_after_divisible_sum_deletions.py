from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        min_dp = [float('inf')] * k
        min_dp[0] = 0
        dp = s = 0
        for x in nums:
            s = (s + x) % k
            dp = min(dp + x, min_dp[s])
            min_dp[s] = dp
        return dp


def test_min_array_sum():
    solution = Solution()
    assert solution.minArraySum([1,1,1], 2) == 1, 'wrong result'
    assert solution.minArraySum([3,1,4,1,5], 3) == 5, 'wrong result'


if __name__ == '__main__':
    test_min_array_sum()
