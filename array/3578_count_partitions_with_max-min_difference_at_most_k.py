from typing import List
from collections import deque


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        maxq = deque()
        minq = deque()
        dp = [1] + [0] * n
        tot = 0
        l = 0

        for r, x in enumerate(nums):
            tot += dp[r]

            while len(maxq) > 0 and nums[maxq[-1]] <= x:
                maxq.pop()
            maxq.append(r)

            while len(minq) > 0 and nums[minq[-1]] >= x:
                minq.pop()
            minq.append(r)

            while nums[maxq[0]] - nums[minq[0]] > k:
                tot -= dp[l]
                l += 1
                if minq[0] < l:
                    minq.popleft()
                if maxq[0] < l:
                    maxq.popleft()
            dp[r + 1] = tot % MOD

        return dp[n]


def test_count_partitions():
    solution = Solution()
    assert solution.countPartitions([9, 4, 1, 3, 7], k=4) == 6, 'wrong result'
    assert solution.countPartitions([3, 3, 4], k=0) == 2, 'wrong result'


if __name__ == '__main__':
    test_count_partitions()

