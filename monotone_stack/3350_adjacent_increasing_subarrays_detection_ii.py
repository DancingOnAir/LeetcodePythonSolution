from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        pre_increase, increase = 0, 1
        res = 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increase += 1
            else:
                pre_increase = increase
                increase = 1

            res = max(res, min(pre_increase, increase), increase // 2)
        return res


def test_max_increasing_subarrays():
    solution = Solution()
    assert solution.maxIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1]) == 3, 'wrong result'
    assert solution.maxIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7]) == 2, 'wrong result'


if __name__ == '__main__':
    test_max_increasing_subarrays()
