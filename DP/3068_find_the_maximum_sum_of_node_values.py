from typing import List


class Solution:
    # dp
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        dp0, dp1 = 0, float('-inf')
        for x in nums:
            # 注意这里dp0和dp1是同时进行的，不能分开2行写，除非有个中间变量记录dp0的原始值
            dp0, dp1 = max(dp0 + x, dp1 + (x ^ k)), max(dp1 + x, dp0 + (x ^ k))
            # temp = dp0
            # dp0 = max(dp0 + x, dp1 + (x ^ k))
            # dp1 = max(dp1 + x, temp + (x ^ k))
        return dp0

    # trick
    def maximumValueSum1(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        res = sum(nums)
        cnt = 0
        min_change = float('inf')
        max_unchange = float('-inf')
        for x in nums:
            diff = (x ^ k) - x
            if diff > 0:
                cnt += 1
                res += diff
                min_change = min(min_change, diff)
            else:
                max_unchange = max(max_unchange, diff)

        if cnt % 2 == 0:
            return res
        return res + max(max_unchange, -min_change)


def test_maximum_value_sum():
    solution = Solution()
    assert solution.maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]]) == 6, 'wrong result'
    assert solution.maximumValueSum([2, 3], 7, [[0, 1]]) == 9, 'wrong result'
    assert solution.maximumValueSum([7, 7, 7, 7, 7, 7], 3,
                                    [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]) == 42, 'wrong result'


if __name__ == '__main__':
    test_maximum_value_sum()
