from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        # dp[i][j] means the longest good sequence ending at index i with at most j different neighbours
        dp = [[1] * (k + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(k + 1):
                for p in range(i):
                    if nums[i] == nums[p]:
                        dp[i][j] = max(dp[i][j], dp[p][j] + 1)
                    elif j > 0:
                        dp[i][j] = max(dp[i][j], dp[p][j - 1] + 1)

        return max(max(d) for d in dp)


def test_maximum_length():
    solution = Solution()
    assert solution.maximumLength([1, 2, 1, 1, 3], 2) == 4, 'wrong result'
    assert solution.maximumLength([1, 2, 3, 4, 5, 1], 0) == 2, 'wrong result'


if __name__ == '__main__':
    test_maximum_length()
