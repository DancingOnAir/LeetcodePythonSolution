from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total, cur = sum(nums), 0
        n, mi, res = len(nums), float('inf'), 0
        for i in range(n - 1):
            cur += nums[i]
            x = abs(cur // (i + 1) - (total - cur) // (n - i - 1))
            if mi > x:
                mi = x
                res = i
            if mi == 0:
                return res

        if total / n < mi:
            return n - 1
        return res

    def minimumAverageDifference1(self, nums: List[int]) -> int:
        ps = []
        for x in nums:
            if not ps:
                ps.append(x)
            else:
                ps.append(ps[-1] + x)

        n, mi, res = len(nums), float('inf'), 0
        for i, x in enumerate(nums):
            cur = abs(int(ps[i] / (i + 1)) - (int((ps[-1] - ps[i]) / (n - i - 1)) if (n - i - 1) > 0 else 0))
            if mi > cur:
                mi = cur
                res = i
        return res


def test_minimum_average_difference():
    solution = Solution()
    assert solution.minimumAverageDifference([1,2,3,4,5]) == 0, 'wrong result'
    assert solution.minimumAverageDifference([2, 5, 3, 9, 5, 3]) == 3, 'wrong result'
    assert solution.minimumAverageDifference([0]) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_average_difference()
