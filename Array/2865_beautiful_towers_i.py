from typing import List


class Solution:
    # monotone stack
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        def pre_sum(nums):
            stk, ps = [], []
            total = 0
            for x in nums:
                cnt = 1
                while stk and stk[-1][0] > x:
                    a, b = stk.pop()
                    total -= a * b
                    cnt += b

                stk.append((x, cnt))
                total += x * cnt
                ps.append(total)
            return ps

        left = [0] + pre_sum(heights)
        right = pre_sum(heights[::-1])[::-1] + [0]
        return max(l + r for l, r in zip(left, right))

    def maximumSumOfHeights1(self, heights: List[int]) -> int:
        def helper(nums):
            pre = [0] * len(nums)
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    j = i - 1
                    while j >= 0:
                        if nums[j] <= nums[i]:
                            break
                        j -= 1
                    pre[i] = pre[j + 1] + nums[i] * (i - j - 1)
                else:
                    pre[i] = pre[i - 1] + nums[i - 1]
            return pre

        left = helper(heights)
        right = helper(heights[::-1])[::-1]
        res = 0
        for i, x in enumerate(heights):
            res = max(res, left[i] + x + right[i])
        return res


def test_maximum_sum_of_heights():
    solution = Solution()
    assert solution.maximumSumOfHeights([5, 3, 4, 1, 1]) == 13, 'wrong result'
    assert solution.maximumSumOfHeights([6, 5, 3, 9, 2, 7]) == 22, 'wrong result'
    assert solution.maximumSumOfHeights([3, 2, 5, 5, 2, 3]) == 18, 'wrong result'


if __name__ == '__main__':
    test_maximum_sum_of_heights()
