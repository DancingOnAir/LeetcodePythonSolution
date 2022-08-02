from typing import List
from operator import gt, lt


class Solution:
    # improved monotone stack
    def subArrayRanges(self, nums: List[int]) -> int:
        def helper(op):
            res = 0
            stk = list()
            for i in range(len(nums) + 1):
                while stk and (i == len(nums) or op(nums[stk[-1]], nums[i])):
                    mid = stk.pop()
                    ii = stk[-1] if stk else -1
                    res += nums[mid] * (i - mid) * (mid - ii)
                stk.append(i)
            return res
        return helper(lt) - helper(gt)

    # monotone stack
    def subArrayRanges2(self, nums: List[int]) -> int:
        n = len(nums)
        min_left, max_left = [0] * n, [0] * n
        min_stack, max_stack = list(), list()
        for i, val in enumerate(nums):
            while min_stack and nums[min_stack[-1]] > val:
                min_stack.pop()
            min_left[i] = min_stack[-1] if min_stack else -1
            min_stack.append(i)

            while max_stack and nums[max_stack[-1]] < val:
                max_stack.pop()
            max_left[i] = max_stack[-1] if max_stack else -1
            max_stack.append(i)

        min_right, max_right = [0] * n, [0] * n
        min_stack, max_stack = list(), list()
        for i in range(n - 1, -1, -1):
            while min_stack and nums[min_stack[-1]] >= nums[i]:
                min_stack.pop()
            min_right[i] = min_stack[-1] if min_stack else n
            min_stack.append(i)

            while max_stack and nums[max_stack[-1]] <= nums[i]:
                max_stack.pop()
            max_right[i] = max_stack[-1] if max_stack else n
            max_stack.append(i)

        min_sum = max_sum = 0
        for i, num in enumerate(nums):
            min_sum += (min_right[i] - i) * (i - min_left[i]) * num
            max_sum += (max_right[i] - i) * (i - max_left[i]) * num
        return max_sum - min_sum

    # two loops
    def subArrayRanges1(self, nums: List[int]) -> int:
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
