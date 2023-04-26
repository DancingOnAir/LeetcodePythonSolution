from typing import List
from math import gcd


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        if ones > 0:
            return len(nums) - ones

        res = float('inf')
        for i in range(len(nums)):
            g = nums[i]
            for j in range(i + 1, len(nums)):
                g = gcd(g, nums[j])
                if g == 1:
                    res = min(res, j - i)

        return -1 if res == float('inf') else res + len(nums) - 1


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([1, 1, 1]) == 0, 'wrong result'
    assert solution.minOperations([2, 6, 3, 4]) == 4, 'wrong result'
    assert solution.minOperations([2, 10, 6, 14]) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
