from typing import List


class Solution:
    # dp[i]表示以i结尾的最长非递减序列长度
    def minimumOperations(self, nums: List[int]) -> int:
        dp = [0] * 4
        for x in nums:
            dp[x] += 1
            dp[2] = max(dp[1], dp[2])
            dp[3] = max(dp[3], dp[2])
        return len(nums) - dp[3]

    def minimumOperations1(self, nums: List[int]) -> int:
        n = len(nums)

        # dfs(i, k)表示从[0 : i]的范围内，且nums[i]变成了k的最长的非递减子序列
        def dfs(i, k):
            if i < 0 or k <= 0:
                return 0
            return max(dfs(i - 1, k), dfs(i, k - 1)) + (k == nums[i])

        res = float('-inf')
        for k in range(1, 4):
            res = max(res, dfs(n - 1, k))
        return n - res


def test_minimum_operations():
    solution = Solution()
    assert solution.minimumOperations([2, 1, 3, 2, 1]) == 3, 'wrong result'
    assert solution.minimumOperations([1, 3, 2, 1, 3, 3]) == 2, 'wrong result'
    assert solution.minimumOperations([2, 2, 2, 2, 3, 3]) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_operations()
