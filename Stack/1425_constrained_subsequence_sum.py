from typing import List
from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = deque()

        for i in range(len(nums)):
            if dq:
                nums[i] += dq[0]

            while len(dq) and nums[i] > dq[-1]:
                dq.pop()

            if nums[i] > 0:
                dq.append(nums[i])

            if i >= k and dq and dq[0] == nums[i - k]:
                dq.popleft()
        return max(nums)


def test_constrained_subset_sum():
    solution = Solution()
    assert solution.constrainedSubsetSum([-5266, 4019, 7336, -3681, -5767], 2) == 11355, 'wrong result'
    assert solution.constrainedSubsetSum([10, 2, -10, 5, 20], 2) == 37, 'wrong result'
    assert solution.constrainedSubsetSum([-1, -2, -3], 1) == -1, 'wrong result'
    assert solution.constrainedSubsetSum([10, -2, -10, -5, 20], 2) == 23, 'wrong result'


if __name__ == '__main__':
    test_constrained_subset_sum()
