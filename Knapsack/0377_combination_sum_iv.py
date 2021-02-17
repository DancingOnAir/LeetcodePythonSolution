from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i - j]

        return dp[target]


def test_combination_sum_iv():
    solution = Solution()
    assert solution.combinationSum4([1, 2, 3], 4) == 7, 'wrong result'
    assert solution.combinationSum4([], 4) == 0, 'wrong result'


if __name__ == '__main__':
    test_combination_sum_iv()
