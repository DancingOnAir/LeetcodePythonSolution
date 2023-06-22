from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left = res = 0
        total = 1
        for right, x in enumerate(nums):
            total *= x
            while total >= k:
                total //= nums[left]
                left += 1
            res += right - left + 1
        return res


def test_num_subarray_product_less_than_k():
    solution = Solution()
    assert solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8, 'wrong result'
    assert solution.numSubarrayProductLessThanK([1, 2, 3], 0) == 0, 'wrong result'


if __name__ == '__main__':
    test_num_subarray_product_less_than_k()
