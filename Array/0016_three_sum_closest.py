from typing import List
import sys


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        d = {}
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right] - target
                if temp > 0:
                    right -= 1
                elif temp < 0:
                    left += 1
                else:
                    return temp + target

                d[abs(temp)] = temp + target
        return d[min(d)]


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