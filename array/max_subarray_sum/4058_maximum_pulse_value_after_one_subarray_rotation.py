class Solution:
    def maxValue(self, nums: list[int]) -> int:
        alter_sum = 0
        for i, x in enumerate(nums):
            alter_sum += x if i % 2 == 0 else -x

        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            dp[i + 1] = max(dp[i - 1], 0) + (-diff if i % 2 == 0 else diff)
        return alter_sum + max(dp) * 2


def test_max_value():
    solution = Solution()
    assert solution.maxValue([1,5,2]) == 6, 'wrong result'
    assert solution.maxValue([6,4,3]) == 7, 'wrong result'
    assert solution.maxValue([9,7]) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_value()
