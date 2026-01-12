from typing import List
from functools import reduce


class Solution:
    # backtracking mode1
    def maxStrength(self, nums: List[int]) -> int:
        n = len(nums)
        res = -10
        path = []

        def dfs(i):
            if len(path) > 0:
                nonlocal res
                res = max(res, reduce(lambda x, y: x * y, path))

            if i >= len(nums):
                return

            dfs(i + 1)

            path.append(nums[i])
            dfs(i + 1)
            path.pop()

        dfs(0)
        return res

    # math
    def maxStrength1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            if nums[0] * nums[1] <= 0:
                return max(nums)
            return nums[0] * nums[1]

        mx_negative, pos_mx_negative, cnt_negative = -10, -1, 0
        mx = -10
        for i, x in enumerate(nums):
            if x == 0:
                nums[i] = 1

            if x < 0:
                if mx_negative < x:
                    pos_mx_negative = i
                    mx_negative = x
                cnt_negative += 1

            mx = max(mx, x)
        if mx == 0 and cnt_negative <= 1:
            return 0
        if cnt_negative & 1:
            nums[pos_mx_negative] = 1
        return reduce(lambda x, y: x * y, nums)


def test_max_strength():
    solution = Solution()
    # assert solution.maxStrength([0, -5, 0]) == 0, 'wrong result'
    # assert solution.maxStrength([0, -1]) == 0, 'wrong result'
    assert solution.maxStrength([3, -1, -5, 2, 5, -9]) == 1350, 'wrong result'
    assert solution.maxStrength([-4, -5, -4]) == 20, "wrong result"


if __name__ == '__main__':
    test_max_strength()
