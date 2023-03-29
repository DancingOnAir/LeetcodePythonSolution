from typing import List
from itertools import accumulate


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        pre_sum = list(accumulate([0] + nums))
        # 这里 pre_sum[i + 1] = pre_sum[i] + nums[i], left sum = pre_sum[-1] - pre_sum[i]
        return [abs(pre_sum[-1] - pre_sum[i + 1] - pre_sum[i]) for i, x in enumerate(nums)]

    def leftRigthDifference1(self, nums: List[int]) -> List[int]:
        res = list()
        total = sum(nums)
        left_sum = 0
        for x in nums:
            res.append(abs(total - x - left_sum - left_sum))
            left_sum += x
        return res


def test_left_right_difference():
    solution = Solution()
    assert solution.leftRigthDifference([10,4,8,3]) == [15,1,11,22]
    assert solution.leftRigthDifference([1]) == [0]


if __name__ == '__main__':
    test_left_right_difference()
