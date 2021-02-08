from typing import List
from itertools import accumulate


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
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
