from typing import List
from math import lcm


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if k % nums[i] == 0:
                if nums[i] == k:
                    res += 1

                cur = nums[i]
                for j in range(i + 1, n):
                    cur = lcm(cur, nums[j])
                    if cur % k == 0:
                        if cur == k:
                            res += 1

        return res


def test_subarray_lcm():
    solution = Solution()
    assert solution.subarrayLCM([2, 1, 1, 5], 5) == 3, 'wrong result'
    assert solution.subarrayLCM([3, 6, 2, 7, 1], 6) == 4, 'wrong result'
    assert solution.subarrayLCM([3], 2) == 0, 'wrong result'


if __name__ == '__main__':
    test_subarray_lcm()
