from typing import List
from collections import defaultdict


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_remainder = sum(nums) % p
        if not total_remainder:
            return 0

        last = {0: -1}
        cur = 0
        res = n = len(nums)
        for i, val in enumerate(nums):
            cur = (cur + val) % p
            last[cur] = i

            if (cur - total_remainder) % p in last:
                res = min(res, i - last[(cur - total_remainder) % p])

        return res if res < n else -1

    # brute force method, but TLE
    def minSubarray1(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        if not total % p:
            return 0

        pre_sum = [0]
        for num in nums:
            pre_sum.append(num + pre_sum[-1])

        for l in range(1, len(nums)):
            for i in range(len(nums) - l + 1):
                temp = total - (pre_sum[i + l] - pre_sum[i])
                if not temp % p:
                    return l

        return -1


def test_min_subarray():
    solution = Solution()

    nums1 = [3, 1, 4, 2]
    p1 = 6
    assert solution.minSubarray(nums1, p1) == 1, "wrong result"

    nums2 = [6, 3, 5, 2]
    p2 = 9
    assert solution.minSubarray(nums2, p2) == 2, "wrong result"

    nums3 = [1, 2, 3]
    p3 = 3
    assert solution.minSubarray(nums3, p3) == 0, "wrong result"

    nums4 = [1, 2, 3]
    p4 = 7
    assert solution.minSubarray(nums4, p4) == -1, "wrong result"

    nums5 = [1000000000, 1000000000, 1000000000]
    p5 = 3
    assert solution.minSubarray(nums5, p5) == 0, "wrong result"


if __name__ == '__main__':
    test_min_subarray()
