from ast import List
from math import gcd


class Solution:
    def count_valid_splits(self, arr: list[int]) -> int:
        n = len(arr)
        suf_gcd = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf_gcd[i] = gcd(suf_gcd[i + 1], arr[i])
        pre = cnt = 0
        for i, x in enumerate(arr):
            pre = gcd(pre, x)
            if pre == suf_gcd[i + 1]:
                cnt += 1
        return cnt

    def maxValidSplits(self, nums: list[int]) -> int:
        res = self.count_valid_splits(nums)
        g = 0
        for i, x in enumerate(nums):
            if g > 0 and x % g == 0:
                continue
            g = gcd(g, x)
            res = max(res, self.count_valid_splits(nums[:i] + nums[i + 1 :]))
        return res


def test_max_valid_splits():
    solution = Solution()
    assert solution.maxValidSplits([10, 30, 15, 10]) == 2, 'wrong result'
    assert solution.maxValidSplits([2, 10, 14]) == 1, 'wrong result'
    assert solution.maxValidSplits([2, 4]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_valid_splits()
