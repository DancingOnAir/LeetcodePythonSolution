from typing import List
from collections import Counter


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        left = max_freq = 0
        cnt = Counter()
        for right, x in enumerate(nums):
            cnt[x] += 1
            max_freq = max(max_freq, cnt[x])
            if right - left + 1 - max_freq > k:
                cnt[nums[left]] -= 1
                left += 1

        return max_freq


def test_longest_equal_subarray():
    solution = Solution()
    assert solution.longestEqualSubarray([1, 3, 2, 3, 1, 3], 3) == 3, 'wrong result'
    assert solution.longestEqualSubarray([1, 1, 2, 2, 1, 1], 2) == 4, 'wrong result'


if __name__ == '__main__':
    test_longest_equal_subarray()
