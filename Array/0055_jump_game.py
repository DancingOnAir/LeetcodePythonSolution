from typing import List
from functools import reduce


class Solution:
    # reduce
    def canJump(self, nums: List[int]) -> bool:
        return reduce(lambda m, i_val: max(m, i_val[0] + i_val[1]) * (i_val[0] <= m), enumerate(nums, 1), 1) > 0

    # go forwarding
    def canJump1(self, nums: List[int]) -> bool:
        max_right = 0
        for i, val in enumerate(nums):
            if i > max_right:
                return False
            max_right = max(max_right, i + val)
        return True


def test_can_jump():
    solution = Solution()
    nums1 = [2, 3, 1, 1, 4]
    print(solution.canJump(nums1))

    nums2 = [3, 2, 1, 0, 4]
    print(solution.canJump(nums2))


if __name__ == '__main__':
    test_can_jump()