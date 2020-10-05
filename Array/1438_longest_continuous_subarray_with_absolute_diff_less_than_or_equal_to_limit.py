from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()

        left, res = 0, 0
        for right, val in enumerate(nums):
            while max_deque and val > max_deque[-1]:
                max_deque.pop()
            while min_deque and val < min_deque[-1]:
                min_deque.pop()
            max_deque.append(val)
            min_deque.append(val)

            if max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1
        # return len(nums) - left; // ok, but confusing and hard to explain
        # return right - left + 1; // ok, but confusing and hard to explain
        return len(nums) - left


def test_longest_subarray():
    solution = Solution()

    # nums1 = [8, 2, 4, 7]
    # limit1 = 4
    # print(solution.longestSubarray(nums1, limit1))
    #
    # nums2 = [10, 1, 2, 4, 7, 2]
    # limit2 = 5
    # print(solution.longestSubarray(nums2, limit2))

    nums3 = [4, 2, 2, 2, 4, 4, 2, 2]
    limit3 = 0
    print(solution.longestSubarray(nums3, limit3))


if __name__ == '__main__':
    test_longest_subarray()
