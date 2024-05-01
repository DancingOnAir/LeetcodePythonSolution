from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n, res = len(nums), float('inf')
        pre, suf = [float('inf')] * n, [float('inf')] * n

        for i in range(1, n):
            pre[i] = min(pre[i - 1], nums[i - 1])
        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], nums[i + 1])

        for i in range(1, n - 1):
            if nums[i] > pre[i] and nums[i] > suf[i]:
                res = min(res, pre[i] + nums[i] + suf[i])
        return res if res < float('inf') else -1


def test_minimum_sum():
    solution = Solution()
    assert solution.minimumSum([8, 6, 1, 5, 3]) == 9, 'wrong result'
    assert solution.minimumSum([5, 4, 8, 7, 10, 2]) == 13, 'wrong result'
    assert solution.minimumSum([6, 5, 4, 3, 4, 5]) == -1, 'wrong result'


if __name__ == '__main__':
    test_minimum_sum()
