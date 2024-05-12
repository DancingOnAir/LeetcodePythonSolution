from typing import List
from collections import Counter


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left, res = 0, 0
        cnt = Counter()
        for right, x in enumerate(nums):
            cnt[x] += 1
            while cnt[x] > k:
                cnt[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res


def test_max_subarray_length():
    solution = Solution()
    assert solution.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2) == 6, 'wrong result'
    assert solution.maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1) == 2, 'wrong result'
    assert solution.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4) == 4, 'wrong result'


if __name__ == '__main__':
    test_max_subarray_length()
