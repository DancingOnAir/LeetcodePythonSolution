from typing import List


class Solution:
    # pre sum
    def subarraySum(self, nums: List[int]) -> int:
        pre_sum = []
        res = tot = 0
        for i, x in enumerate(nums):
            tot += x
            pre_sum.append(tot)
            res += pre_sum[i] - (pre_sum[i - nums[i] - 1] if i - nums[i] - 1 >= 0 else 0)
        return res

    # simulation
    def subarraySum1(self, nums: List[int]) -> int:
        res = 0
        for i, x in enumerate(nums):
            start = max(0, i - x)
            res += sum(nums[start: i+1])
        return res


def test_subarray_sum():
    solution = Solution()
    assert solution.subarraySum([2, 3, 1]) == 11, 'wrong result'
    assert solution.subarraySum([3, 1, 1, 2]) == 13, 'wrong result'


if __name__ == '__main__':
    test_subarray_sum()
