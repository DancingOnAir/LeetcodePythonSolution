from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        for i, val in enumerate(nums):
            if i:
                nums[i] = nums[i - 1] + val
        return nums


def test_running_sum():
    solution = Solution()

    nums1 = [1, 2, 3, 4]
    print(solution.runningSum(nums1))

    nums2 = [1, 1, 1, 1, 1]
    print(solution.runningSum(nums2))

    nums3 = [3, 1, 2, 10, 1]
    print(solution.runningSum(nums3))


if __name__ == '__main__':
    test_running_sum()
