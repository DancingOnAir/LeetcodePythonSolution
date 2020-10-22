from typing import List
from collections import OrderedDict, Counter


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0

        # nums.sort()
        # gaps = OrderedDict()

        count = Counter(nums)
        if len(count) == 1:
            return 0

        action_times = 3
        left, right = 0, len(count) - 1
        sorted_keys = sorted(count)

        while left < right:
            if count[sorted_keys[left]] > action_times and count[sorted_keys[right]] > action_times:
                return sorted_keys[right] - sorted_keys[left]
            elif count[sorted_keys[left]] > action_times:
                right -= 1
                action_times -= count[sorted_keys[right]]
            elif count[sorted_keys[right]] > action_times:
                left += 1
                action_times -= count[sorted_keys[left]]
            else:
                if sorted_keys[left + 1] - sorted_keys[left] >= sorted_keys[right] - sorted_keys[right - 1]:
                    left += 1
                    action_times -= count[sorted_keys[left]]
                else:
                    right -= 1
                    action_times -= count[sorted_keys[right]]
        return 0


def test_min_difference():
    solution = Solution()

    # nums1 = [5, 3, 2, 4]
    # print(solution.minDifference(nums1))
    #
    # nums2 = [1, 5, 0, 10, 14]
    # print(solution.minDifference(nums2))

    nums3 = [6, 6, 0, 1, 1, 4, 6]
    print(solution.minDifference(nums3))

    nums4 = [1, 5, 6, 14, 15]
    print(solution.minDifference(nums4))


if __name__ == '__main__':
    test_min_difference()
