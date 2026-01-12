from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        nums.sort()

        if nums[0] > 0:
            res += 1

        if nums[-1] < n:
            res += 1

        for i in range(n - 1):
            if nums[i] < i + 1 < nums[i + 1]:
                res += 1
        return res


def test_count_ways():
    solution = Solution()
    assert solution.countWays([1, 1]) == 2, 'wrong result'
    assert solution.countWays([6, 0, 3, 3, 6, 7, 2, 7]) == 3, 'wrong result'


if __name__ == '__main__':
    test_count_ways()
