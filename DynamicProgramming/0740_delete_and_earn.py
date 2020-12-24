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
                    continue
            else:
                memo[nums[i]] += 1

            nxt = nums[i] + 1
            total1, total2 = 0, 0
            while nxt in memo:
                if (nxt - nums[i]) & 0b1:
                    total1 += memo[nxt] * nxt
                else:
                    total2 += memo[nxt] * nxt
                nxt += 1

            pre = nums[i] - 1
            total3, total4 = 0, 0
            while pre in memo:
                if (nums[i] - pre) & 0b1:
                    total3 += memo[pre] * pre
                else:
                    total4 += memo[pre] * pre
                pre -= 1

            if total2 + total4 + memo[nums[i]] * nums[i] <= total1 + total3:
                dp[i+1] = dp[i]
            elif total2 + total4 + (memo[nums[i]] - 1) * nums[i] < total1 + total3:
                dp[i+1] = dp[i] + total2 + total4 + memo[nums[i]] * nums[i] - total1 - total3
            else:
                dp[i+1] = dp[i] + nums[i]
        return dp[n]


def test_delete_and_earn():
    solution = Solution()

    # nums1 = [3, 4, 2]
    # assert solution.deleteAndEarn(nums1) == 6, 'wrong result'
    #
    # nums2 = [2, 2, 3, 3, 3, 4]
    # assert solution.deleteAndEarn(nums2) == 9, 'wrong result'

    nums3 = [8, 7, 3, 8, 1, 4, 10, 10, 10, 2]
    assert solution.deleteAndEarn(nums3) == 52, 'wrong result'


if __name__ == '__main__':
    test_delete_and_earn()
