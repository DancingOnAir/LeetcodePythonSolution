from typing import List
from math import lcm
from collections import defaultdict


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res = 0
        m = dict()
        for x in nums:
            cur = {x: 1}
            for y in m.keys():
                l = lcm(x, y)
                if l <= k:
                    cur[l] = cur.get(l, 0) + m[y]
            res += cur.get(k, 0)
            m = cur
        return res

    def subarrayLCM1(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            cur = nums[i]
            for j in range(i, len(nums)):
                cur = lcm(cur, nums[j])
                if cur == k:
                    res += 1
                elif cur > k:
                    break

        return res


def test_subarray_lcm():
    solution = Solution()
    assert solution.subarrayLCM([2, 1, 1, 5], 5) == 3, 'wrong result'
    assert solution.subarrayLCM([3, 6, 2, 7, 1], 6) == 4, 'wrong result'
    assert solution.subarrayLCM([3], 2) == 0, 'wrong result'


if __name__ == '__main__':
    test_subarray_lcm()
