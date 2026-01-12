from typing import List


class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        max_num = max(nums)
        dp = [[0] * (max_num + 1)]

        for num in nums:
            cur = dp[-1][:]
            cur[num] += 1
            dp.append(cur)

        res = list()
        for l, r in queries:
            diff = [i for x, y, i in zip(dp[l], dp[r+1], range(max_num+1)) if x != y]
            res.append(min([y - x for x, y in zip(diff, diff[1:])] or [-1]))
        return res


def test_min_difference():
    solution = Solution()

    assert solution.minDifference([1, 3, 4, 8], [[0, 1], [1, 2], [2, 3], [0, 3]]) == [2, 1, 4, 1]
    assert solution.minDifference([4, 5, 2, 2, 7, 10], [[2, 3], [0, 2], [0, 5], [3, 5]]) == [-1, 1, 1, 3]


if __name__ == '__main__':
    test_min_difference()
