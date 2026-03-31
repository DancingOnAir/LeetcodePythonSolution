from typing import List
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        m = defaultdict(int)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                m[nums[i] * nums[j]] += 1
        return sum(v * (v - 1) // 2 for v in m.values()) * 8


def test_tuple_same_product():
    solution = Solution()
    assert solution.tupleSameProduct([2, 3, 4, 6]) == 8, 'wrong result'
    assert solution.tupleSameProduct([1, 2, 4, 5, 10]) == 16, 'wrong result'


if __name__ == '__main__':
    test_tuple_same_product()
