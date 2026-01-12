from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res, local_max = float('-inf'), float('-inf')
        for num in nums:
            local_max = max(num, local_max + num)
            res = max(res, local_max)

        return res

    def maxSubArray2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

            res = max(res, nums[i])
        return res

    def maxSubArray1(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res, sub_array_sum = float('-inf'), 0
        for i, val in enumerate(nums):
            sub_array_sum += val
            res = max(res, sub_array_sum)
            sub_array_sum = max(sub_array_sum, 0)

        return res


def test_max_sub_array():
    solution = Solution()

    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums1))


if __name__ == '__main__':
    test_max_sub_array()
