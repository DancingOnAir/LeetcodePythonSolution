from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        stk = list()
        for i in range(n - 1, -1, -1):
            while stk and nums[i] > nums[stk[-1]]:
                dp[i] = max(dp[i] + 1, dp[stk.pop()])
            stk.append(i)
        return max(dp)


def test_total_steps():
    solution = Solution()
    assert solution.totalSteps([10, 1, 2, 3, 4, 5, 6, 1, 2, 3]) == 6, 'wrong result'
    assert solution.totalSteps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]) == 3, 'wrong result'
    assert solution.totalSteps([4, 5, 7, 7, 13]) == 0, 'wrong result'


if __name__ == '__main__':
    test_total_steps()
