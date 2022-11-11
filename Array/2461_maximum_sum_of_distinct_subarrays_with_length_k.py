from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = cur = 0
        l = 0
        m = set()
        for r in range(len(nums)):
            while nums[r] in m:
                cur -= nums[l]
                m.remove(nums[l])
                l += 1

            m.add(nums[r])
            cur += nums[r]

            if r - l + 1 == k:
                res = max(res, cur)
                cur -= nums[l]
                m.remove(nums[l])
                l += 1
        return res


def test_maximum_subarray_sum():
    solution = Solution()
    assert solution.maximumSubarraySum([3, 2, 3, 1], 3) == 6, 'wrong result'
    assert solution.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3) == 15, 'wrong result'
    assert solution.maximumSubarraySum([4, 4, 4], 3) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximum_subarray_sum()
