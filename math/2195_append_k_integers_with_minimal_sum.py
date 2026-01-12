from typing import List


class Solution:
    # binary search
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid
        s = left + k
        return s * (s + 1) // 2 - sum(nums[:left])

    # math
    def minimalKSum1(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        pre = 0
        for x in nums:
            gap = x - pre - 1
            if k <= gap:
                return res + (pre + 1 + pre + k) * k // 2

            if gap > 0:
                res += (pre + 1 + pre + gap) * gap // 2
                k -= gap
            pre = x
        return res + (pre + 1 + pre + k) * k // 2


def test_minimal_k_sum():
    solution = Solution()
    assert solution.minimalKSum([1, 4, 25, 10, 25], k=2) == 5, 'wrong result'
    assert solution.minimalKSum([5, 6], k=6) == 25, 'wrong result'


if __name__ == '__main__':
    test_minimal_k_sum()
