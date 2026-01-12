from typing import List
from itertools import combinations
from functools import reduce


class Solution:
    """
    an efficient approach: find bitwise OR of array. ith bit contribution to to xor sum is 2**(n-1).
    The result is 2**(n-1) * bitORSum

    Explanation:

    consider ith bit for the final result. If there is no element whose ith bit is 1, then all xor subset
    sums has 0 in ith bit; if there are k (k>=1) elements whose ith bits are 1, then there are in total
    comb(k, 1) + comb(k,3) + .. = 2**(k-1) ways to select odd number our of these k elements to make the subset
    xor sum's ith bit to be 1, and there are 2**(n-k) ways to choose from the remaining elements whose ith bits
    are 0s. Therefore, we have in total 2**(k-1) * 2**(n-k) = 2**(n-1) subsets whose xor sums have 1 in their
    ith bit, which means the contribution to the final sum is 2**(n-1) * 2**i. Notice this result is irrelevant
    to k.

    So we only need to determine whether there is any element whose ith bit is 1. We use bitwise OR sum to do this.

    Time complexity: O(n), Space: O(1)
    """
    # 数学推导 https://math.stackexchange.com/questions/248245/exactly-half-of-the-elements-of-mathcalpa-are-odd-sized
    def subsetXORSum(self, nums: List[int]) -> int:
        bits = 0
        for x in nums:
            bits |= x
        return bits * (2 ** (len(nums) - 1))

    # bit mask
    def subsetXORSum2(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, 1 << len(nums)):
            total = 0
            for j in range(len(nums)):
                if i & (1 << j):
                    total ^= nums[j]
            res += total

        return res

    # brute force
    def subsetXORSum1(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums) + 1):
            for comb in combinations(nums, i):
               res += reduce(lambda x, y: x ^ y, comb)
        return res


def test_subset_xor_sum():
    solution = Solution()
    assert solution.subsetXORSum([1, 3]) == 6, 'wrong result'
    assert solution.subsetXORSum([5, 1, 6]) == 28, 'wrong result'
    assert solution.subsetXORSum([3, 4, 5, 6, 7, 8]) == 480, 'wrong result'


if __name__ == '__main__':
    test_subset_xor_sum()
