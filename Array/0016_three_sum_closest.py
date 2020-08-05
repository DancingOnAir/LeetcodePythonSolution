from typing import List
import sys


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == target:
                    return cur_sum
                elif abs(cur_sum - target) < abs(res - target):
                    res = cur_sum

                if cur_sum < target:
                    left += 1
                else:
                    right -= 1
        return res


def test_three_sum_closest():
    solution = Solution()

    nums1 = [-1, 2, 1, -4]
    target1 = 1
    print(solution.threeSumClosest(nums1, target1))

    nums2 = [0, 1, 2]
    target2 = 3
    print(solution.threeSumClosest(nums2, target2))

    nums3 = [-100, -98, -2, -1]
    target3 = -101
    print(solution.threeSumClosest(nums3, target3))


if __name__ == '__main__':
    test_three_sum_closest()