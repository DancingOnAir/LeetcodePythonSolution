from typing import List
from heapq import heappop, heappush, heapify
from collections import deque


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = [0] * 50
        res = [0] * (len(nums) - k + 1)
        for i, val in enumerate(nums):
            if val < 0:
                cnt[val + 50] += 1
            if i - k >= 0 and nums[i - k] < 0:
                cnt[nums[i - k] + 50] -= 1
            if i - k + 1 < 0:
                continue

            tot = 0
            for j in range(50):
                tot += cnt[j]
                if tot >= x:
                    res[i - k + 1] = j - 50
                    break
        return res


def test_get_subarray_beauty():
    solution = Solution()
    assert solution.getSubarrayBeauty([1, -1, -3, -2, 3], 3, 2) == [-1, -2, -2], 'wrong result'
    assert solution.getSubarrayBeauty([-1, -2, -3, -4, -5], 2, 2) == [-1, -2, -3, -4], 'wrong result'
    assert solution.getSubarrayBeauty([-3, 1, 2, -3, 0, -3], 2, 1) == [-3, 0, -3, -3, -3], 'wrong result'


if __name__ == '__main__':
    test_get_subarray_beauty()
