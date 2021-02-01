from typing import List
from functools import lru_cache


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if 1 == n:
            return 0

        pre_sum = [0] * (n + 1)
        for i, val in enumerate(stoneValue):
            pre_sum[i + 1] = val + pre_sum[i]

        @lru_cache(None)
        def dp(left, right):
            if left == right:
                return 0

            res = 0
            for i in range(left, right):
                left_sum = pre_sum[i + 1] - pre_sum[left]
                right_sum = pre_sum[right + 1] - pre_sum[i + 1]
                if left_sum <= right_sum:
                    res = max(res, dp(left, i) + left_sum)
                elif left_sum >= right_sum:
                    res = max(res, dp(i + 1, right) + right_sum)
            return res

        return dp(0, n - 1)

    # dfs but failed
    # thoughts, how to choose the subarray,
    # eg. left sum equals right sum, both are 9
    #     [3, 3, 3] and [1, 4, 4] or [3, 3, 3] and [5, 4] or [3, 3, 3] and [2, 2, 2, 3]
    def stoneGameV1(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if 1 == n:
            return 0

        def helper(left, right, res):
            if right <= left:
                return res

            min_gap = 0x3f3f3f3f
            cur_left, cur_right, total = 0, 0, 0

            for i in range(left, right):
                left_sum = pre_sum[i] - pre_sum[left - 1]
                right_sum = pre_sum[right] - pre_sum[i]
                if min_gap > abs(left_sum - right_sum):
                    min_gap = abs(left_sum - right_sum)
                    if left_sum < right_sum:
                        total = left_sum
                        cur_left = left
                        cur_right = i
                    elif left_sum > right_sum:
                        total = right_sum
                        cur_left = i + 1
                        cur_right = right
                    else:
                        total = left_sum

            return helper(cur_left, cur_right, res + total)

        pre_sum = [0]
        for v in stoneValue:
            pre_sum.append(pre_sum[-1] + v)

        res = helper(1, n, 0)

        return res


def test_stone_game_v():
    solution = Solution()
    assert solution.stoneGameV([6, 2, 3, 4, 5, 5]) == 18, 'wrong result'
    assert solution.stoneGameV([7, 7, 7, 7, 7, 7, 7]) == 28, 'wrong result'
    assert solution.stoneGameV([4]) == 0, 'wrong result'


if __name__ == '__main__':
    test_stone_game_v()
