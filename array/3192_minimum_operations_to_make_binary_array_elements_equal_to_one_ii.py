from typing import List
from itertools import groupby


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            if x == (res & 1):
                res += 1
        return res

    def minOperations1(self, nums: List[int]) -> int:
        last = nums[0]
        res = 1 if nums[0] == 0 else 0
        for i in range(1, len(nums)):
            if last != nums[i]:
                res += 1
                last = nums[i]

        if not (nums[-1] ^ (res & 1)):
            res -= 1
        return res

    # TLE
    def minOperations1(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 0
        res = 0
        while j < n:
            if nums[i] == 0:
                res += 1
                for k in range(i, n):
                    nums[k] ^= 1
            i += 1
            j += 1

        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([0, 1, 1, 0, 1]) == 4, 'wrong result'
    assert solution.minOperations([1, 0, 0, 0]) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
