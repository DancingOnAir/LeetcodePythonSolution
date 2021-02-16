from typing import List


class Solution:
    # do solution for 0-1 knapsack problem
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        n = len(nums)
        if target & 1:
            return False

        target >>= 1
        dp = [True] + [False] * target
        for x in nums:
            for i in range(target, x - 1, -1):
                dp[i] |= dp[i - x]
        return dp[-1]

    # dp
    def canPartition2(self, nums: List[int]) -> bool:
        target, n = sum(nums), len(nums)
        if target & 1:
            return False

        target >>= 1
        dp = [True] + [False] * target
        for x in nums:
            dp = [dp[i] or (i >= x and dp[i - x]) for i in range(target + 1)]
            if dp[target]:
                return True

        return False

    # brute force dict
    def canPartition1(self, nums: List[int]) -> bool:
        if sum(nums) & 1 == 0:
            mid = sum(nums) >> 1
            possible_sums = {0}
            for num in nums:
                # union set
                possible_sums |= {i + num for i in possible_sums}
                if mid in possible_sums:
                    return True

        return False


def test_can_partition():
    solution = Solution()
    assert solution.canPartition([1, 5, 11, 5]), 'wrong result'
    assert not solution.canPartition([1, 2, 3, 5]), 'wrong result'


if __name__ == '__main__':
    test_can_partition()
