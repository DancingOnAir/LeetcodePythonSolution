from typing import List


class Solution:
    # two loops
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            mx = mi = nums[i]
            for j in range(i, n):
                mx = max(mx, nums[j])
                mi = min(mi, nums[j])
                res += mx - mi
        return res


def test_subarray_ranges():
    solution = Solution()
    assert solution.subArrayRanges([1, 2, 3]) == 4, 'wrong result'
    assert solution.subArrayRanges([1, 3, 3]) == 4, 'wrong result'
    assert solution.subArrayRanges([4, -2, -3, 4, 1]) == 59, 'wrong result'


if __name__ == '__main__':
    test_subarray_ranges()
